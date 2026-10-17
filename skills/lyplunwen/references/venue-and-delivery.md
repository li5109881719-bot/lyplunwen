# Venue requirements, citations, and delivery

Read when a venue is named, before citation/Word conversion, and before final delivery. Apply only requirements relevant to the user's intended output.

## Dated venue profile

Maintain `paper_output/venue_profile.json` or an equivalent existing record containing venue, article type, official guidance URL, date actually checked, archived evidence/locator, manuscript and abstract limits with counting scope, submission language, reference style, anonymity, requested declarations, and current verification status. Record unknown/provisional fields rather than guessing. Add advisor-supplied exemplars with their role.

For each requirement, preserve its authority and whether it is explicit or inferred. Current journal-specific instructions govern submission; an accepted article shows published practice; a publisher's general template supplies compatible styles. Published layout is not a requirement to reproduce publisher typography. If sources conflict, inspect them and register the conflict. Recheck potentially changed requirements when moving to submission; do not impose a universal expiry interval or an unrelated journal's rules.

Set working word budgets only after deciding article type and counting scope. Final counting must include notes/tables/captions if required; record the application, actual scope, revision, and count. A status-bar number without confirmed counting options is not definitive compliance. Retain modest room for necessary late edits according to the actual limit.

## Canonical citation data and early technical prototype

Keep one canonical source record; citation instances contain claim IDs, source IDs, locators and intended note placement. Use a consistent term/translation table for names, institutions and titles across languages. Distinguish a book title, an article title, its translated title, and its journal/newspaper carrier.

Repeated citation of one source can be legitimate, especially for different pages or claims. Merge redundant supporting instances only when the surviving note still supports all nearby claims. A multiple-source note is valid when the style permits it and each source's role is clear. Do not reduce note counts as a quality target or substitute a convenient source solely to make two notes look different.

Before the first full Word build, create and inspect a small prototype covering applicable first/repeat citations, non-English titles, multiple-source notes, and navigation. Use native endnotes/footnotes or reference fields when suitable; use actual journal requirements instead of assuming APA or numeric bibliography style. Do not require native notes universally when the journal uses another system. If Word is requested, verify in Word when feasible; structural XML checks alone do not prove visible navigation.

## Bilingual and prose handoff

Record original-language draft, accepted submission-language source, and checking translation as distinct roles. Preserve stable paragraph and claim IDs. After substantive changes, update corresponding translations/notes or mark their exact older source revision. Purely stylistic edits need meaning comparison before deciding whether a translation update is necessary.

After substantive review, apply `anti-defensive-writing`, then language-specific Humanizer, then meaning regression. Compare dates, names, quantities, institutional/legal status, source attribution, uncertainty, and cited claim scope against the accepted draft. Respect requested formal register, acronym handling, LaTeX commands, and existing emphasis. Fix newly found source problems upstream before finalizing language.

## Final delivery checks

Bind checks to the exact source and output snapshots:

1. **Content and citations:** source/export text agreement; expected references and notes; no missing IDs; first/repeat source identity and locators; test applicable navigation. Check a whole defect class when a user identifies one example.
2. **Format and rendering:** current requested font/color/styles, word-count scope, exported PDF and visual pages. Rebuild and inspect affected output after changes; do not reuse an earlier draft's render as final proof.
3. **Anonymous files, when required:** inspect visible text, headers/footers, comments, tracked revisions, core/custom properties, and relevant author-bearing parts; then inspect exported PDF metadata. Clean identifiers after final saving/export and verify the delivered bytes, because applications may repopulate them. Inspect author data securely rather than echoing it into logs.
4. **Provenance and state:** register outputs with source parents, synchronize current-file views and configuration, run the registry verifier, and record actual check reports for the delivered revisions. Preserve originals.

Changes invalidate affected checks: factual/citation edits require support and identity review; translation changes require meaning/alignment review; rebuilt Word/PDF require relevant structural/render and metadata checks. Metadata-only cleaning requires integrity/metadata recheck without automatically repeating unrelated linguistic review.

If a renderer omits glyphs but the native application displays them, use the native exported PDF for visual QA and keep both observations. If only structural QA is available, state that limited result; do not label visual QA passed. A reading PDF independently typeset from the same source is not proof of Word layout.

Manuscript readiness, verified file delivery, author decisions, and actual external submission are separate statuses. Submission confirmation requires actual system evidence and the user's authorization for that action. Do not infer submission from completed documents.
