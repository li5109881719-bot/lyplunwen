# Artifact Contract and Quality Gates

Read this file for full runs, resume operations, and completion audits.

## Required project state

Store generated workflow artifacts under `paper_output/`. Preserve user source materials outside this directory unless the user explicitly requests a copy.

Minimum state files:

```text
paper_output/
├── project_config.json
├── artifact_registry.json         # authoritative identities, parents and scoped gate records
├── venue_profile.json             # dated requirements; provisional if venue unknown
├── workflow_state.md
├── source_map.md
├── source_inventory.md
├── problem_landscape.md
├── idea_candidate_matrix.md
├── research_question_options.md
├── feasibility_filter.md
├── reference_materials/
│   ├── source_index.md
│   ├── paper_readers/              # optional; selected nature-reader outputs
│   └── paper_cards/                # optional; selected nature-paper-card outputs
├── concept_dossier.md
├── corpus_inventory.md
├── exemplar_method_map.md
├── sota_gap_map.md
├── motivation_options_after_literature.md
├── confirmed_research_spine.md
├── study_design_brief.md
├── analysis_plan.md
├── evaluation_plan.md
├── experiment_registry.md
├── threats_to_validity.md
├── evidence_bank.md
├── claim_register.md
├── figure_asset_map.md
├── claim_strength_calibration.md
├── citation_support_bank.md
├── reference_verification_report.md
├── citation_check_report.md
├── section_blueprints.md
├── writing_rationale_matrix.md
├── first_draft/
│   └── main.md
├── audit_report.md
├── revision_queue.md
├── language_cleanup_log.md
└── final_artifact_manifest.md
```

Create only artifacts applicable to the actual study. Record “not applicable” with a reason instead of creating misleading empty files.

Reuse equivalent existing files and record their paths; do not rename an established project merely to match this tree. Historical studies can use an event/evidence register instead of an experiment registry. Read `historical-evidence.md` for source criticism and `venue-and-delivery.md` for venue and document checks.

Nature reader and Paper Card artifacts are derivative reading aids. Their source locators must remain traceable to the supplied paper, and they must not be treated as new independent evidence. `reference_verification_report.md` concerns bibliographic identity and metadata; `citation_check_report.md` concerns claim support and placement.

## Workflow state schema

Keep `workflow_state.md` concise and update it after each accepted stage:

Use `artifact_registry.json` for current artifact identities and parent revisions. The state and final manifest are human-readable views; their generated blocks are synchronized by `scripts/project_state.py`. Preserve historical narrative outside those blocks. See `state-and-versions.md` for commands and migration.

```markdown
# Workflow State

- Current stage:
- Last passed gate:
- Confirmed research spine: yes/no
- Real results available: yes/no/partial
- Completed artifacts:
- Unresolved blockers:
- User decisions required:
- Recommended next action:
- Last updated:
```

## Quality gates

Bind each check to the artifact ID, revision, inspected scope, report, remaining issues and date. Distinguish bibliography identity, claim support, source independence, language meaning, document structure and visual rendering. A pass for one scope does not pass another. Use `pass`, `pass_with_issues` (nonblocking findings stated), `fail`, or `not_applicable` with a reason. File existence and module completion are not passes.

When the manuscript or check evidence changes, recheck the affected scope. A later revision inherits unchanged research decisions, but does not inherit unverified claims that it has been rendered or checked. Keep manuscript readiness, file readiness and submission status separate.

### Gate 1 — Intake completeness

Pass when the project goal, current assets, constraints, desired output, and source locations are known well enough to plan the next stage.

Capture dated venue requirements early when a venue is known, including word-count scope, citation system and anonymity. A provisional venue does not block research construction.

### Gate 2 — Spine clarity

Pass only when the user has confirmed a spine containing problem, motivation, gap, approach, evidence, bounded claim, and scope.

### Gate 3 — Feasibility

Pass only when the evidence required for the intended claim is available or executable within the stated constraints.

### Gate 4 — Literature grounding

Pass only when the map distinguishes concepts, explanations, methods, comparison logic, evidence standards, contradictions, and gaps.

Record access and reading depth separately for each source. Abstract screening, full-text reading and a source-grounded Paper Card are different states. Cover the requested corpus and prioritize core sources for argument development.

### Gate 5 — Study design validity

Pass only when the design includes comparison or control logic, evaluation criteria, robustness or triangulation checks, alternative explanations, and interpretation boundaries appropriate to the evidence mode.

For historical research, specify source independence, conflicting accounts, event chronology, proposal-to-implementation distinctions and counterexamples that could change the interpretation.

### Gate 6 — Real evidence boundary

Pass to drafting results only when real research outputs exist. Otherwise stop with an execution plan.

### Gate 7 — Evidence traceability

Pass only when every central claim links to evidence IDs, citation IDs, or explicit limitation language.

### Gate 8 — Figure logic

Pass only when each planned figure or table has an argumentative function and a real evidence source.

### Gate 9 — Citation integrity and non-copying

Pass only when bibliography metadata has been verified where practicable, citations are real and relevant, nearby claims are actually supported, and exemplar use remains structural rather than textual. Keep metadata problems separate from claim-support problems.

Use one canonical identity per source with verified title and translation fields, plus separate citation instances with precise locators. Repeated citations can be legitimate; merge only when placement and evidentiary function permit it. Multiple publications drawing on the same original account are not independent corroboration. A defect found in one note triggers a scan of the same defect class throughout the manuscript.

### Gate 10 — Draft completeness and overclaim control

Pass only when the manuscript includes all sections needed to evaluate the research, states limitations, and properly bounds causal, mechanistic, generalization, performance, and practical-impact claims.

Language cleanup must not weaken or inflate these boundaries. After anti-defensive editing and humanization, compare the edited manuscript with the accepted substantive revision and recheck limitations, uncertainty, negative results, numbers, names, dates, and citation relationships.

### Gate 11 — Delivery integrity

Pass only when final files open correctly, required visual or structural checks are recorded, DOCX and PDF content agree, and originals remain preserved.

Test the venue citation format on a short prototype before producing the full document. For the final revision, verify native note/reference structures where required, navigation, all-black text if requested, rendering, total word count under the venue definition and anonymous metadata. Check metadata again after final save/export. Pair the PDF with its actual parent Word revision and record the rendering route. Do not report an earlier render as visual QA for the edited file.

## Default version naming

Use the project’s preferred language and retain the base title:

```text
论文名-00原始材料
论文名-01研究设计
论文名-02结构初稿
论文名-03完整初稿
论文名-04审稿修订版
论文名-05去防御性修订版
论文名-06语言润色版
论文名-07投稿版.docx
论文名-07投稿版.pdf
```

Never overwrite an accepted milestone unless the user explicitly requests it.

## Resume protocol

1. Inspect the registry, project configuration, workflow state, inventory and registered current artifacts.
2. Run the state consistency check; validate parent revisions, bilingual alignment and scoped check records rather than trusting a stage label, version suffix or modification time.
3. Identify the first failed or incomplete gate.
4. Report what is complete, what remains uncertain, and the smallest next action.
5. Continue from that point without recreating valid work.

## Writing rationale matrix

Before drafting, use this schema:

| Row ID | Manuscript Unit | Planned Function | Research-Spine Link | Literature/Exemplar Pattern Learned | Evidence or Citation Anchor | Planned Text Move | Claim Boundary | Final Check |
|---|---|---|---|---|---|---|---|---|

The first row must justify the whole-work throughline. Later rows should represent the smallest useful argument-bearing units. If most rows say only “write background” or “improve clarity,” return to the spine, literature map, or study design.
