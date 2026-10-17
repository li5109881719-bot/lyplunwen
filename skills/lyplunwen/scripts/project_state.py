#!/usr/bin/env python3
"""Maintain artifact lineage and derived state views; does not judge research validity."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BEGIN = '<!-- lyplunwen:registry:start -->'
END = '<!-- lyplunwen:registry:end -->'
CONFIG_KEYS = {
    'venue_profile': 'venue_profile',
    'english_source': 'current_english_source',
    'anonymous_word': 'anonymous_word', 'anonymous_pdf': 'anonymous_pdf',
    'chinese_source': 'current_chinese_source',
    'chinese_word': 'current_chinese_word', 'chinese_pdf': 'current_chinese_pdf',
    'chinese_review_source': 'current_chinese_review_source',
    'chinese_review_word': 'current_chinese_review_word',
    'chinese_review_pdf': 'current_chinese_review_pdf',
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.lyp-tmp')
    tmp.write_text(value, encoding='utf-8')
    tmp.replace(path)


def save_json(path, value):
    save(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def local(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Artifact/report path must be inside the project: ' + value)
    if not path.is_file():
        raise ValueError('File not found: ' + str(path))
    return path


def ancestry(data, artifact_id):
    seen, pending = set(), [artifact_id]
    while pending:
        item = pending.pop()
        if item in seen:
            continue
        seen.add(item)
        pending.extend(data['artifacts'].get(item, {}).get('parents', []))
    return seen


def view(data):
    rows = [BEGIN, '## 当前文件登记（自动生成）', '',
            '版本与来源以 `artifact_registry.json` 为准；本表不代表质量关卡通过。', '',
            '| 角色 | 版本 | 文件 | 来源ID |', '|---|---|---|---|']
    for role, item_id in sorted(data['current'].items()):
        item = data['artifacts'][item_id]
        values = [role, item['version'], item['path'], ', '.join(item['parents']) or '—']
        rows.append('| ' + ' | '.join(v.replace('|', '\\|') for v in values) + ' |')
    rows.extend(['', '- 阶段：' + data['context'].get('stage', '未登记'),
                 '- 下一步：' + data['context'].get('next_action', '未登记'), END])
    return '\n'.join(rows)


def insert_view(text, generated):
    if BEGIN in text or END in text:
        if text.count(BEGIN) != 1 or text.count(END) != 1:
            raise ValueError('Incomplete/duplicate generated block; inspect before writing')
        start, end = text.index(BEGIN), text.index(END) + len(END)
        if end < start:
            raise ValueError('Reversed generated block')
        return text[:start] + generated + text[end:]
    split = text.find('\n')
    if text.startswith('# ') and split != -1:
        return text[:split+1] + '\n' + generated + '\n' + text[split+1:]
    return generated + '\n\n' + text


def audit(root, output, data, require_sync=False):
    errors, warnings, gates = [], [], []
    current_ids = set().union(*(ancestry(data, item_id) for item_id in data['current'].values()))
    for item_id, item in data['artifacts'].items():
        try:
            path = local(root, item['path'])
            if sha(path) != item['sha256']:
                raise ValueError('Registered file changed: ' + item_id)
        except ValueError as exc:
            (errors if item_id in current_ids else warnings).append(str(exc))
        for parent in item['parents']:
            if parent not in data['artifacts']:
                errors.append('Unknown parent: ' + parent)
    for role, item_id in data['current'].items():
        if item_id not in data['artifacts']:
            errors.append('Unknown current artifact: ' + role)
    # A current deliverable must derive from the current manuscript, even if filenames exist.
    for role in ['anonymous_word', 'anonymous_pdf']:
        if role in data['current'] and 'english_source' in data['current']:
            if data['current']['english_source'] not in ancestry(data, data['current'][role]):
                errors.append(role + ' does not derive from current english_source')
    for child_role, parent_role in [('anonymous_pdf', 'anonymous_word'),
                                    ('chinese_word', 'chinese_source'),
                                    ('chinese_pdf', 'chinese_word'),
                                    ('chinese_review_word', 'chinese_review_source'),
                                    ('chinese_review_pdf', 'chinese_review_word')]:
        if child_role in data['current'] and parent_role in data['current']:
            if data['current'][parent_role] not in ancestry(data, data['current'][child_role]):
                errors.append(child_role + ' does not derive from current ' + parent_role)
    for role in ['chinese_review_source', 'chinese_review_word', 'chinese_review_pdf']:
        if role in data['current'] and 'english_source' in data['current']:
            if data['current']['english_source'] not in ancestry(data, data['current'][role]):
                warnings.append(role + ' reflects an earlier English revision; do not label it synchronized')
    for gate in data['gate_runs']:
        invalid = []
        for snapshot in gate['snapshots']:
            try:
                if sha(local(root, snapshot['path'])) != snapshot['sha256']:
                    invalid.append(snapshot['path'])
            except ValueError:
                invalid.append(snapshot['path'])
        state = 'invalidated' if invalid else 'valid_for_recorded_artifacts'
        if not invalid and gate['subject_role'] and data['current'].get(gate['subject_role']) != gate['artifact']:
            state = 'superseded'
        gates.append({'id': gate['id'], 'artifact': gate['artifact'], 'status': gate['status'],
                      'validity': state, 'changed_or_missing': invalid})
        if invalid:
            warnings.append('Gate evidence changed; recheck ' + gate['id'])
    config_path = output / 'project_config.json'
    config = json.loads(config_path.read_text()) if config_path.exists() else {}
    for role, key in CONFIG_KEYS.items():
        if role in data['current']:
            expected = data['artifacts'][data['current'][role]]['path']
            if config.get(key) != expected:
                (errors if require_sync else warnings).append('Configuration pointer differs: ' + key)
    if require_sync:
        generated = view(data)
        for name in ['workflow_state.md', 'final_artifact_manifest.md']:
            path = output / name
            if not path.exists() or generated not in path.read_text():
                errors.append('Generated view differs: ' + name)
    return {'errors': errors, 'warnings': warnings, 'gate_runs': gates,
            'scope': 'File identity, lineage and state consistency only; no source-truth or visual-QA certification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--output-dir', default='paper_output')
    subs = parser.add_subparsers(dest='command', required=True)
    subs.add_parser('init')
    reg = subs.add_parser('register')
    reg.add_argument('--id', required=True)
    reg.add_argument('--path', required=True, help='Path relative to the project root')
    reg.add_argument('--version', required=True)
    reg.add_argument('--role')
    reg.add_argument('--parent', action='append', default=[])
    context = subs.add_parser('context')
    context.add_argument('--stage', required=True)
    context.add_argument('--next-action', required=True)
    gate = subs.add_parser('record-gate')
    gate.add_argument('--id', required=True)
    gate.add_argument('--artifact', required=True)
    gate.add_argument('--status', choices=['pass', 'pass_with_issues', 'fail', 'not_applicable'], required=True)
    gate.add_argument('--scope', required=True)
    gate.add_argument('--report', action='append', default=[])
    gate.add_argument('--issue', action='append', default=[])
    gate.add_argument('--blocker', action='append', default=[])
    gate.add_argument('--reason', default='')
    subs.add_parser('sync')
    verify = subs.add_parser('verify')
    verify.add_argument('--require-sync', action='store_true')
    args = parser.parse_args()
    root = args.project.resolve()
    output = (root / args.output_dir).resolve()
    if not output.is_relative_to(root):
        raise ValueError('Output directory must be inside the project')
    registry = output / 'artifact_registry.json'
    if args.command == 'init':
        if registry.exists():
            raise ValueError('Registry already exists; inspect it instead of reinitializing')
        save_json(registry, {'schema_version': 1, 'artifacts': {}, 'current': {},
                             'context': {}, 'gate_runs': [], 'updated_at': now()})
        print('Registry initialized; no artifacts or quality passes inferred.')
        return
    data = json.loads(registry.read_text())
    if data.get('schema_version') != 1:
        raise ValueError('Unsupported registry schema')
    if args.command == 'register':
        path = local(root, args.path)
        for parent in args.parent:
            if parent not in data['artifacts'] or parent == args.id:
                raise ValueError('Parent must be an existing different artifact: ' + parent)
        item = {'path': str(path.relative_to(root)), 'version': args.version,
                'parents': args.parent, 'sha256': sha(path)}
        old = data['artifacts'].get(args.id)
        if old and any(old[key] != item[key] for key in item):
            raise ValueError('Artifact IDs are immutable; register a new revision ID')
        data['artifacts'][args.id] = old or dict(item, registered_at=now())
        if args.role:
            data['current'][args.role] = args.id
    elif args.command == 'context':
        data['context'] = {'stage': args.stage, 'next_action': args.next_action}
    elif args.command == 'record-gate':
        if args.artifact not in data['artifacts']:
            raise ValueError('Unknown gate artifact')
        if args.status != 'not_applicable' and not args.report:
            raise ValueError('A check report is required; file existence is not a pass')
        if args.status == 'not_applicable' and not args.reason:
            raise ValueError('A reason is required for not_applicable')
        if args.status == 'pass_with_issues' and not args.issue:
            raise ValueError('State the remaining nonblocking issues')
        if args.status == 'pass' and (args.issue or args.blocker):
            raise ValueError('Use pass_with_issues or fail for remaining findings')
        if args.status != 'fail' and args.blocker:
            raise ValueError('Blocking findings cannot be passed')
        item = data['artifacts'][args.artifact]
        if sha(local(root, item['path'])) != item['sha256']:
            raise ValueError('Gate subject changed; register its new revision first')
        paths = [item['path']] + args.report
        snapshots = [{'path': str(local(root, x).relative_to(root)), 'sha256': sha(local(root, x))} for x in paths]
        roles = [role for role, item_id in data['current'].items() if item_id == args.artifact]
        data['gate_runs'].append({'id': args.id, 'artifact': args.artifact,
            'subject_role': roles[0] if roles else None, 'status': args.status, 'scope': args.scope,
            'reports': args.report, 'issues': args.issue, 'blockers': args.blocker,
            'reason': args.reason, 'snapshots': snapshots, 'recorded_at': now()})
    elif args.command == 'sync':
        result = audit(root, output, data)
        if result['errors']:
            raise ValueError('Fix registry integrity/lineage before sync: ' + '; '.join(result['errors']))
        generated = view(data)
        # Prepare all text before writing; malformed blocks never cause partial view edits.
        prepared = {}
        for name in ['workflow_state.md', 'final_artifact_manifest.md']:
            path = output / name
            text = path.read_text() if path.exists() else '# ' + name.removesuffix('.md') + '\n'
            prepared[path] = insert_view(text, generated)
        path = output / 'project_config.json'
        config = json.loads(path.read_text()) if path.exists() else {}
        for role, key in CONFIG_KEYS.items():
            if role in data['current']:
                config[key] = data['artifacts'][data['current'][role]]['path']
        config['artifact_registry'] = str(registry.relative_to(root))
        save_json(path, config)
        for path, text in prepared.items():
            save(path, text)
        print('Current pointers and generated views synchronized; historical prose preserved.')
        return
    elif args.command == 'verify':
        result = audit(root, output, data, args.require_sync)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(1 if result['errors'] else 0)
    data['updated_at'] = now()
    save_json(registry, data)
    print('Registry updated: ' + args.command)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc))
