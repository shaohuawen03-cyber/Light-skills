# Final quality summary / 最终质量汇总

Date / 日期: 2026-08-12

## Overall status / 总体状态

- **Bilingual scientific-content package / 中英文科学内容包:** PASS for accountable-author review / 可交责任作者审阅。
- **Author-approved pre-submission enquiry / 经作者批准的预投稿询问:** READY after completion of the correspondent fields / 补齐通讯作者字段后可用。
- **Immediate formal SCI submission / 立即正式 SCI 投稿:** NOT READY / 尚未就绪。
- **Main unresolved scientific limitation / 核心科学局限:** candidate sequences, identities, row-level scores, sample mappings, and original pipeline code are unavailable.
- **Rendered visual review / 渲染视觉审查:** UNAVAILABLE in this environment; no claim of page-by-page Word/PDF validation is made.

## Current deterministic checks / 当前确定性检查

| Check | Current result | Interpretation |
| --- | --- | --- |
| Corrected source corpus | PASS | Four in-scope source files verified against `SHA256SUMS.txt`; the unrelated files are excluded and documented only in the dedicated exclusion record. |
| Excluded-source identity scan | PASS | The excluded identity occurs only in `evidence/excluded_source_record.md`; it is absent from active evidence, manuscript, references, submission files, scripts, and quality claims. |
| Aggregate statistics | PASS | `revision_v2/statistics_audit.json` reports `all_checks_pass=true`; calculations are deterministic transcriptions/recomputations from aggregate counts, not row-level reanalysis. |
| Bilingual manuscript consistency | PASS | All locked counts/percentages are present; prohibited positive mechanism/specificity claims and placeholders are absent; references 1–25 are sequential in both language files. |
| Language structure | PASS | Both files contain eight matching top-level sections, cite references 1–25 before the reference list, and contain no TODO/TBD gap markers. |
| Citation inventory | PASS | The same 25 DOI strings occur in English, Chinese, `verified_references.md`, and `references.bib`. This is inventory parity, not a final Crossmark/retraction certificate. |
| Final-mode draft lint | PASS | Neither language produced a FAIL-level finding. The Chinese `Funding` warning reflects English-heading detection; the `经费` section is present. |
| Mechanical checker | REVIEWED | English: 74 heuristic findings (50 passive voice, 10 paragraph passive-density, 13 punctuation, one `novel` hit in an official article title). Chinese: 670 findings, of which 669 are expected CJK-punctuation false positives and one is the same title hit. No automatic style finding was treated as scientific evidence. |
| DOCX package audit | PASS | Main DOCX: 345 paragraphs, four tables, four drawings, two media files. Supplement: 271 paragraphs, three tables. ZIP CRC, XML parsing, internal relationships, expected tokens, and media counts passed. |
| Word-count estimate | INFORMATIONAL | Journal-neutral tokenizer: abstract excluding keywords 244; Introduction through Conclusions 3,204; main text including declarations and excluding references 3,550. Recount in Word and the target portal. |

## Scientific-integrity boundaries / 科学诚信边界

The final wording preserves all of the following distinctions:

1. BBB model output is not measured BBB transport or brain exposure.
2. NTxPred2 positivity is not experimental neurotoxicity.
3. Mebipred positivity is not affinity, stoichiometry, binding-site, ion-specific, or coordination evidence.
4. CHEL-high/FRS-lower output is not demonstrated pro-oxidant activity.
5. A periodontitis analysis branch is not a periodontitis-specific sequence set.
6. An oral candidate is not a taxonomically assigned *Porphyromonas gingivalis* candidate.
7. Candidate counts are computational accounting units, not independent biological replicates.
8. The reported 111/923 handoff is not presented as an audited transition rate.
9. Observational periodontitis–cognition/AD associations are not evidence of causation.
10. Aggregate computational prioritization is not candidate validation or an established disease mechanism.

## Remaining blockers / 剩余阻断项

### Scientific/reproducibility

- Candidate sequences, stable IDs, taxonomy, spectra, row-level scores, and subject/sample mapping are absent.
- Original discovery/prediction code, versions, database snapshots, environment, seeds, and run logs are absent.
- One BioProject identity remains unresolved; the long-branch evidence class and the mebipred handoff require clarification.
- No cohort-matched translation/expression, BBB transport, toxicology, metal-dependent biochemistry, or disease-mechanism experiment is available.

### Authorial/administrative

- Target journal and article type require final author selection and official-rule recheck.
- Authors, affiliations, correspondence, ORCIDs, CRediT, funding, conflicts, ethics/consent language, originality, and final approval require named human authors.
- Data/Code Availability and generative-AI disclosure require accountable-author approval and journal-policy adaptation.
- All 25 references require final correction/Crossmark/retraction screening immediately before submission.

### File-level

- Open both DOCX files in Microsoft Word or LibreOffice and inspect every page, table, image, symbol, hyperlink, and Chinese font.
- Apply the selected journal format, recount words, validate figure specifications, accept/reject tracked changes, remove comments/hidden metadata, and export a compliant PDF if required.

## Final recommendation / 最终建议

Use `manuscript/manuscript_bilingual.docx` for bilingual author review and `submission/presubmission_enquiry_bilingual.md` as the next external-action draft. Discuss BMC Oral Health first; treat Scientific Reports only as a broad secondary enquiry. Do not submit through a journal portal or claim full reproducibility/experimental validation until the blocking checklist is resolved or an editor explicitly confirms willingness to consider the disclosed aggregate-only package.
