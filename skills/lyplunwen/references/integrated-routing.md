# Integrated Routing and Handoffs

Use this reference when selecting a dependent skill, resolving overlapping capabilities, or registering an artifact returned by another module.

## Routing matrix

| Need | Route | Required input | Register the output as |
|---|---|---|---|
| Project intake and state | `research-architect-intake` | idea, materials, constraints, paths | project configuration, inventories, workflow state |
| Candidate questions | `research-architect-brainstorm` | intake artifacts | question options and feasibility filter |
| Literature and gap map | `research-architect-literature` | screened corpus or search results | concept, exemplar, and gap maps |
| Source-grounded full-paper reading | `nature-reader` | selected full text, PDF, HTML, DOI, or excerpt | reader plus stable source locators |
| Deep analysis of a core paper | `nature-paper-card` | selected paper or reader artifact | evidence-grounded Paper Card |
| Study design | `research-architect-design` | user-confirmed research spine | study and analysis plans |
| Evidence and claims | `research-architect-evidence` | real research outputs | evidence bank, claim register, figure map |
| Claim-level literature support | `research-architect-citation` | claim register and verified literature | citation support bank |
| Bibliography identity and metadata | `nature-ref-verifier` | citations or bibliography | reference verification report |
| Citation-to-claim support | `/ars-citation-check` | draft plus references | citation error report |
| Full draft | `research-architect-draft` | passed spine, design, evidence, citation, and blueprint gates | versioned first draft |
| Structural and evidentiary audit | `research-architect-audit` | complete draft and upstream artifacts | audit report and revision queue |
| Adversarial peer review | `/ars-reviewer` | auditable complete draft | reviewer reports |
| Revision strategy | `/ars-revision-coach` | draft and review findings | prioritized revision roadmap |
| Substantive revision | `/ars-revision` | accepted roadmap and source-accounted materials | revised draft |
| Reviewer-response audit | `/ars-rebuttal-audit` | comments, response, and revised draft | rebuttal QA report |
| Remove unnecessary defensive prose | `anti-defensive-writing` | substantively stable draft | bounded direct-expression version |
| Chinese style cleanup | `humanizer-zh` | accepted Chinese substantive version | natural Chinese version |
| English style cleanup | `humanizer` | accepted English substantive version | natural English version |
| DOCX and PDF delivery | `documents`, then `pdf` | accepted final text and venue requirements | rendered, verified deliverables |

## Overlap rules

- `lyplunwen` owns project state, gates, and the next-action decision.
- Research Architect owns research construction and the manuscript's evidentiary architecture.
- `nature-reader` and `nature-paper-card` analyse selected sources; they do not define the project gap or research spine.
- `nature-ref-verifier` checks bibliographic identity. `/ars-citation-check` checks claim support. Do not merge their unresolved findings into one ambiguous status.
- ARS challenges and repairs an existing evidence-backed draft; it does not supply missing research results.
- `anti-defensive-writing` removes unnecessary protective framing but must preserve limits that affect validity or interpretation.
- Humanization is the last prose operation before document production. It must not silently alter claims, evidence, citations, or uncertainty.
- Apply historical source criticism through `historical-evidence.md` when the study depends on chronology, institutional change or conflicting accounts. This is a conditional research method, not a new skill entry point.
- Establish the venue profile and citation prototype early through `venue-and-delivery.md`; reserve final document QA for the accepted revision.

## Handoff protocol

After any dependent module returns:

1. Register the returned artifact ID, path, revision and parent IDs in `artifact_registry.json`; preserve the input version.
2. Check whether it satisfies the current gate; bind any check record to the inspected revision, scope and report. Do not accept completion from the module label alone.
3. Add unresolved findings to the appropriate register or revision queue.
4. Preserve the pre-handoff artifact and save the accepted result as a new version.
5. Synchronize configuration pointers and generated state/manifest blocks using `scripts/project_state.py`. Keep Chinese originals and Chinese checking translations in separate roles, each with an explicit English parent where applicable.
6. Resume from the first incomplete gate rather than restarting the workflow. See `state-and-versions.md` for migration and invalidation rules.

If a dependent skill is unavailable, perform the bounded task directly when safe, preserve the same output contract, and record the substitution.
