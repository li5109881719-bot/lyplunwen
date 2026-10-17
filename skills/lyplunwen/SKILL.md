---
name: lyplunwen
description: Chinese-first academic paper workflow with source criticism, evidence-linked claims, version tracking, substantive review, and verified Word/PDF delivery. Use when the user invokes $lyplunwen or starts or resumes a paper project from ideas, literature, or real research materials.
---

# LYP 论文 0→1

Build a transparent trail from idea to claim to evidence to manuscript. Treat the target “1” as an auditable full draft ready for submission-stage revision, not a guaranteed publishable paper.

## Start or resume

For a new project:

1. Identify the project root from the user’s folder or create no files until the location is clear.
2. Use `paper_output/` as the workflow output directory.
3. Route first to `research-architect-intake`; initialize the artifact registry once real artifacts exist.
4. Ask only for missing information that materially blocks the current stage.
5. Finish and report the current stage before advancing.

For an existing project:

1. Inspect `paper_output/artifact_registry.json` when present, plus project configuration, workflow state, inventories, and current sources. Follow [references/state-and-versions.md](references/state-and-versions.md) for registration, migration, and synchronization.
2. Verify current paths, file identity, parent revisions, bilingual synchronization, and the version/scope of gate records before choosing the next stage. Do not infer the current manuscript from the largest suffix or newest timestamp.
3. Reuse valid artifacts; do not regenerate or overwrite them without cause.
4. Report completed stages, unresolved blockers, and the recommended next action.

Read [references/artifacts-and-gates.md](references/artifacts-and-gates.md) before a full run, a resume operation, or a completion claim.

## Single-orchestrator rule

`lyplunwen` is the only project-level controller. The user should not have to choose among sibling workflows or manually chain skills.

- Use Research Architect as the research-construction engine.
- Use Nature skills only as bounded literature and bibliography modules.
- Use ARS only after the relevant evidence, draft, or reviewer material exists.
- Use language-editing skills only after substantive claims and structure stabilize.
- Do not restart the project when a downstream skill returns an artifact; register its identity and parent revisions, synchronize state views, and resume at the next failed gate.

Read [references/integrated-routing.md](references/integrated-routing.md) when choosing a dependent skill, resolving overlap, or handing an artifact from one module to the next.

## Non-negotiable rules

- Preserve originals and save meaningful stages as separate versions.
- Never fabricate data, results, interviews, metrics, quotations, citations, figures, or methods.
- If required evidence does not exist, produce an executable collection or analysis plan and pause before drafting results.
- Confirm the research spine with the user before study design and drafting.
- Link every central claim to evidence IDs, citation IDs, or explicit limitation language.
- Use exemplar papers only to learn structure and evidence expectations; never copy their wording, claims, figures, or citation choices.
- Repair logic, design, and evidence before polishing prose.
- Keep source IDs, claim IDs, and paragraph IDs stable across revisions; rendered note numbers are positions, not source identities.
- Separate full-text access, reading-card structural checks, bibliographic verification, claim support, source independence, and visual QA. A pass in one does not certify the others.
- State verification limits honestly; do not claim visual QA when only structural checks ran.
- Communicate in concise, direct Chinese unless the user requests another language.

## Workflow

### 0. Intake and source inventory

Use `research-architect-intake`.

Capture the raw idea, discipline, target output, current assets, constraints, reference mode, paths, and tentative venue. Create the project configuration, source map, inventory, and workflow state.

If a target venue is known, read [references/venue-and-delivery.md](references/venue-and-delivery.md) and create a dated venue profile before setting firm word budgets or formatting citations. If the venue is undecided, record requirements as provisional rather than blocking research.

Do not write manuscript prose at this stage.

### 1. Candidate questions and feasibility

Use `research-architect-brainstorm`.

Produce 3–5 candidate questions and compare novelty, theoretical value, evidence access, method fit, time cost, ethical constraints, and venue fit. Reject topics that are merely under-studied locations without a knowledge or explanation gap.

### 2. Literature, gap, and exemplar map

Use `research-architect-literature`.

Separate concept definitions, explanations, methods, baselines or comparison logic, evidence standards, contradictions, and genuine gaps. Keep citation support separate from exemplar learning. Verify current or precise sources when web research is authorized or required.

For each search round, record the evidence question, queries, coverage, priority sources, access/read level, and stop condition. Continue for material uncertainties; move optional background leads to the backlog. Respect a request to read every item while keeping abstract-only and full-text findings distinct.

For historical/documentary research, read [references/historical-evidence.md](references/historical-evidence.md) for provenance, source dependence, actor attribution, competing explanations, and historical reading-card fields.

After initial screening:

- Use `nature-reader` for papers that require full-text, figure-aware, equation-aware, or Chinese-English source-grounded reading. Do not create a full reader for every search result.
- Use `nature-paper-card` for core papers whose evidence-to-claim chain or transferable logic needs deep analysis, or for every paper when explicitly requested. Adapt nonapplicable experimental fields to the study; never invent experiments or results to fill a template.
- Store or index these artifacts under `paper_output/reference_materials/` and retain their source anchors.
- Feed only verified findings into the literature map; a generated reader or card is an analysis artifact, not an independent source.

### 3. Confirm the research spine

Present 2–5 alternatives using:

```text
problem -> motivation -> gap -> approach -> evidence -> bounded claim -> scope
```

Explain the feasibility and tradeoff of each. Confirm the substantive choice with the user unless their existing instructions already establish it. Record the confirmation with its conversation locator; do not ask again for the same accepted choice. A generic “continue” authorizes the established next step, but does not establish an unpresented new research spine.

### 4. Study design

Use `research-architect-design`.

Convert the confirmed spine into research questions, material or data needs, sampling or case logic, method, comparison or control logic, evaluation criteria, robustness or triangulation checks, alternative explanations, failure cases, ethics, and interpretation boundaries.

For qualitative or case research, emphasize case selection, process tracing, source triangulation, negative evidence, success-case bias, and transfer boundaries. For quantitative or experimental work, emphasize identification, variables, baselines, controls, evaluation, power where applicable, and robustness.

### 5. Execute the research

Collect, clean, code, or analyze real materials. Support the user with protocols, interview guides, coding schemes, scripts, registries, and analysis plans as appropriate.

If results do not yet exist, stop here after producing an execution plan. Never cross this boundary by inventing a plausible result.

### 6. Evidence and citation system

Use `research-architect-evidence`, then `research-architect-citation`.

Create an evidence bank, claim register, figure asset map, claim-strength calibration, and claim-level citation support bank. Distinguish fact, description, interpretation, mechanism, causality, generalization, and recommendation.

Maintain one canonical record per source for author, title, original-language title, translated title, dates, and locators. Preserve multiple legitimate citation instances of one source. Track reprints, shared documents, and borrowed interviews before counting independent corroboration. Test central interpretations against competing explanations and contrary cases.

Run the two citation checks for different purposes:

- Use `nature-ref-verifier` to verify bibliography identity and metadata such as author order, title, year, venue, volume, pages, and DOI.
- Use `/ars-citation-check` to test whether each citation actually supports the nearby claim and whether attribution, scope, and placement are sound.

Neither check substitutes for the other. Record unresolved metadata and claim-support problems separately.

### 7. Manuscript blueprint

Create `section_blueprints.md` and `writing_rationale_matrix.md` before drafting. Each argument-bearing unit must state its function, research-spine link, evidence or citation anchor, planned move, and claim boundary.

A provisional outline may develop during evidence collection once the period, questions, locatable key materials, and remaining gaps are clear. Full drafting still requires the applicable spine/evidence gates; do not make complete acquisition of every lead a prerequisite for outlining.

Prefer the drafting order:

```text
methods -> results/analysis -> discussion -> framework -> introduction -> conclusion -> abstract/title
```

Adapt the order when the field or venue requires it.

### 8. Full first draft

Use `research-architect-draft`.

Draft only from the confirmed spine, study design, evidence bank, claim register, citation bank, and rationale matrix. Preserve uncertainty and limitations. Do not fill gaps with fluent speculation.

### 9. Adversarial review and substantive revision

Use `research-architect-audit`, then `/ars-reviewer`, `/ars-revision-coach`, and `/ars-revision` when available.

Separate:

1. fatal or blocking defects;
2. structural problems;
3. method and evidence problems;
4. citation problems;
5. repairable expression problems.

Revise in that order. For a reviewer response, use `/ars-rebuttal-audit` after drafting the response.

When a user finds one defect, inspect the manuscript for the same defect class before reporting it fixed. For multilingual work, record which accepted source revision each translation reflects; update bilingual alignment after substantive changes or explicitly mark it outdated.

### 10. Style and delivery

Only after the relevant version passes substantive review without blocking findings:

1. Use `anti-defensive-writing` to remove unnecessary caveats, disclaimers, apology-like framing, and self-weakening sentences while preserving methodological, evidentiary, ethical, legal, and scope limits that affect validity.
2. Use `humanizer-zh` for Chinese manuscripts or `humanizer` for English manuscripts to remove formulaic phrasing while preserving facts, terminology, citations, uncertainty, and the author’s voice.
3. Run a final regression check against the claim register, evidence bank, limitations, negative results, numbers, names, dates, and citations. Restore any meaning or necessary boundary lost during style editing.

Before the first full Word build, verify a small citation prototype containing the applicable first/repeat citation, non-English title, multisource note, and note navigation. This is a technical check, not an additional author approval.

Use `documents` for DOCX creation or editing and render-based QA. Use `pdf` for PDF verification. Follow [references/venue-and-delivery.md](references/venue-and-delivery.md) for claim regression, native references, final word counts, source/export correspondence, and anonymity checks after export. Register the exact final files and their check reports; preserve accepted milestones.

## Stage-control behavior

- Use user confirmation for substantive research choices; execute routine reversible steps within existing authorization. Step-by-step reporting does not require a new approval after each paragraph or technical correction.
- At the research-execution boundary, pause until real outputs exist.
- After evidence exists, batch adjacent stages only when the user requests an end-to-end run.
- Invoke dependent skills only when their stated entry condition is satisfied; do not run every installed skill on every project.
- When blocked, state the exact missing input and provide the smallest executable next action.
- When the user says “继续”, verify the registry and recorded decisions, then resume from the first incomplete applicable gate rather than restarting.
- When the user says “不要直接写全文”, remain at the current planning or evidence stage.

## Completion standard

Bind every completion statement to artifact revisions and the checks actually performed. Require all applicable blocking gates to pass; carry forward nonblocking evidence opportunities without declaring them resolved. Keep manuscript completion, file delivery, and external submission as separate statuses. The generated manifest identifies:

- source materials;
- confirmed research spine;
- design and analysis artifacts;
- evidence and citation records;
- selected-paper readers or Paper Cards when used;
- bibliography-metadata and citation-support verification results;
- draft and audit versions;
- substantive revision and language-cleanup versions;
- final DOCX/PDF deliverables and their verification status.

If a dependent skill or ARS command is unavailable, preserve the same artifact contract and quality gates, perform the step directly where safe, and state the substitution.

## Invocation examples

- “使用 `$lyplunwen` 启动这个论文项目，先盘点材料，不要直接写全文。”
- “使用 `$lyplunwen` 继续当前项目，读取 `paper_output` 并告诉我下一步。”
- “使用 `$lyplunwen` 从现有数据开始建立证据库并生成论文蓝图。”
