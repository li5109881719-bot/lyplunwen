# State, versions, and migration

Read on project initialization, resume, artifact handoff, or final delivery.

## One authoritative current-file registry

`paper_output/artifact_registry.json` owns current artifact pointers and immutable artifact identities. `project_config.json` retains project parameters. Managed blocks in `workflow_state.md` and `final_artifact_manifest.md` are generated views; history and research discussion outside those blocks remain intact.

Use `scripts/project_state.py` with Python 3.9 or later; it needs only the standard library. Paths passed to `--path` and `--report` are relative to the project root, not to `paper_output/`.

```bash
python3 /path/to/lyplunwen/scripts/project_state.py --project /path/to/project init
python3 /path/to/lyplunwen/scripts/project_state.py --project /path/to/project register \
  --id en-r3 --path paper_output/english_draft/main_en_r3.md --version r3 --role english_source
python3 /path/to/lyplunwen/scripts/project_state.py --project /path/to/project register \
  --id word-r3 --path paper_output/submission_package/paper_r3.docx --version r3 \
  --role anonymous_word --parent en-r3
python3 /path/to/lyplunwen/scripts/project_state.py --project /path/to/project sync
python3 /path/to/lyplunwen/scripts/project_state.py --project /path/to/project verify --require-sync
```

Use project-specific paths and IDs. An ID identifies one immutable file snapshot: path, version, SHA-256, and parent IDs. Reassigning a role to a newly registered revision is allowed; rewriting the old ID to disguise a changed file is not. Generated files should have recorded parents. A hash proves file identity, not meaning preservation.

Roles are extensible. Common roles are `english_source`, `anonymous_word`, `anonymous_pdf`, `chinese_source`, `chinese_word`, `chinese_pdf`, and `chinese_review_source/word/pdf`. Distinguish the Chinese original from a Chinese translation for checking the current English draft. A final English file need not imply that a requested Chinese review translation has already been updated.

For outputs, record actual derivation: PDF → Word → accepted source. The verifier checks that anonymous English Word/PDF derive from the current English source and warns when the Chinese review chain reflects an earlier English revision. It does not compare all document text or render it; those are separate checks.

Update stage context with `context --stage '...' --next-action '...'`, then run `sync`. Generated views are updated automatically; never hand-edit their managed blocks. Existing configuration fields outside registered current-file pointers are preserved. Review obsolete free-text summaries separately; do not keep a second manually maintained list of current paths.

## Migrate an existing project without selecting by filename

1. Read the latest user decisions, accepted artifacts, change logs, and actual contents. Dates and suffixes are clues, not acceptance.
2. Preserve configuration/state files before migration. Initialize only if no registry exists.
3. Register the verified current source, outputs, and their parents. Register older files that are parents of still-used artifacts as archival identities, without assigning a current role.
4. Keep original-language and checking-translation roles separate. If the review translation is old, preserve its true parent and warn; do not invent synchronization or silently rewrite the paper as a side effect of workflow maintenance.
5. Synchronize views and compatible configuration pointers. Run `verify --require-sync`; inspect every error and warning. Fix inconsistent provenance instead of bypassing it.
6. Preserve legacy audit reports as historical records. Do not convert their broad “pass” labels into new version-bound passes without doing the missing checks.

Equivalent project artifacts can satisfy a contract under their existing filenames. Register the mapping in configuration or the source index; do not generate empty duplicate documents to satisfy a directory diagram.

## Record quality checks for a specific artifact

```bash
python3 /path/to/lyplunwen/scripts/project_state.py --project /path/to/project record-gate \
  --id citation-support --artifact en-r3 --status pass_with_issues \
  --scope 'Claim support for the accepted English revision' \
  --report paper_output/review/claim_check_r3.md \
  --issue 'Noncentral archive lead remains unavailable; corresponding wording is bounded'
```

Allowed statuses: `pass`, `pass_with_issues`, `fail`, `not_applicable`. A pass requires a real report describing the work performed; `not_applicable` requires a reason. Blocking findings require `fail`; nonblocking findings must be explicit. The script snapshots the subject and report hashes, and detects later changes or superseded role assignments. It records the evaluator's result; it does not validate the report's scientific judgment.

Review gate records by their exact artifact ID and scope. An archived pass is not a pass for the current manuscript. If content changes, register a new artifact ID and recheck affected scopes; unchanged files retain their own recorded checks.

## Scope of automated checks

`verify` checks file existence, registered hashes, parent relationships, current-file pointers, and generated-view consistency. It reports stale check evidence and old bilingual alignment. It cannot confirm source authenticity, independent corroboration, grammar correctness, visual layout, current journal rules, or external submission. Never describe a clean registry audit as a fully verified paper.
