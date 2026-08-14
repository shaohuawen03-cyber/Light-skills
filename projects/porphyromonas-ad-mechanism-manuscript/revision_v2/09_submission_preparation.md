# Stage 9 — Submission preparation / 投稿准备

Inputs: polished bilingual manuscript, statistical audit, figure audit, verified bibliography  
Outputs: `submission/` package, rebuilt DOCX files, final quality reports.

## 1. Submission strategy

A target journal was not silently chosen on the authors’ behalf. Current scope/indexing checks support discussing **BMC Oral Health** first, with **Scientific Reports** as a broad secondary enquiry and **Journal of Oral Microbiology** as a stronger-topic but higher-evidence target. No target removes the central reproducibility limitation.

The recommended next external action is a candid pre-submission enquiry, not immediate portal submission. The enquiry explicitly asks whether an aggregate original article without candidate identities or original code will receive editorial consideration.

## 2. Prepared components

- `submission/journal_targeting_bilingual.md`
- `submission/presubmission_enquiry_bilingual.md`
- `submission/cover_letter_bilingual_template.md`
- `submission/title_page_bilingual_template.md`
- `submission/highlights_bilingual.md`
- `submission/submission_readiness_checklist.md`
- `manuscript/manuscript_bilingual.docx`
- `manuscript/supplementary_tables_bilingual.docx`
- editable and raster figures in `manuscript/figures/`

## 3. Technical versus scientific readiness

### Technically prepared and checked

- English–Chinese section-parallel manuscript rebuilt from the current language files.
- 25-reference shared bibliography with DOI-set parity across English, Chinese, verification record, and BibTeX.
- Two main tables, two figures, and three supplementary tables.
- Deterministic aggregate audit and 4/4 source checksum verification.
- Current manuscript-consistency and language-structure audits: PASS.
- Final-mode draft lint: no FAIL-level issue in either language.
- Generated OOXML manuscript (345 paragraphs, four tables, four drawings, two embedded images) and supplement (271 paragraphs, three tables); CRC, XML parsing, internal relationships, expected content, and media checks: PASS.
- Editable SVG and raster PNG figure assets.
- Templates for title page, letter, highlights, and declarations.

### Not complete and not fabricated

- Authors/affiliations/correspondence/ORCIDs.
- Institutional ethics determination.
- Funding, conflicts, CRediT roles, and author approval.
- Candidate sequences and row-level outputs.
- Original analysis code/environment.
- Final journal format and submission portal metadata.
- Word/LibreOffice visual rendering and PDF export.
- Final Crossmark/retraction check.

## 4. Final editorial risk statement

The manuscript is more honest, current, and internally auditable than the first draft, but the absence of candidate identities and original analytical artefacts remains a probable desk-rejection reason. This cannot be repaired by further prose editing. The package is suitable for accountable-author review and a pre-submission enquiry; it is not represented as guaranteed acceptable or fully reproducible.

## 5. Final technical outcomes

The bilingual Markdown was regenerated after the last abstract edits. Current arithmetic, manuscript-consistency, language-structure, citation-inventory, source-checksum, and OOXML package audits pass. A repository search found the excluded-source identity only in the dedicated exclusion record. The environment still cannot render DOCX pages or produce a validated PDF, so visual inspection remains explicitly unresolved.

## 6. Stage verdict

**Nine-stage reconstruction and available package-level tests are complete.** The package is ready for accountable-author review and an author-approved pre-submission enquiry. It is **not ready for immediate formal portal submission** until the administrative and file-level checklist is completed and editorial tolerance for the scientific reproducibility gap is known.
