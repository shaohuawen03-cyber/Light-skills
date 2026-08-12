# Final quality summary / 最终质量汇总 — revision v3

Date / 日期: 2026-08-12

## Overall status / 总体状态

- **Bilingual scientific-content package / 中英文科学内容包:** PASS for accountable-author review / 可交责任作者审阅。
- **Pre-submission enquiry / 预投稿询问:** READY after human completion and approval / 补齐并经作者批准后可用。
- **Immediate formal SCI submission / 立即正式投稿:** NOT READY / 尚未就绪。
- **Scientific ceiling / 科学上限:** provenance-aware, hypothesis-generating computational prioritization; not reproduced target binding or a validated disease mechanism / 保留来源边界的假设生成型计算优选；不是经复现的靶标结合或经验证疾病机制。
- **Rendered review / 渲染审查:** unavailable in this environment; OOXML package audit is not page-level Word/PDF validation / 当前环境不可用，文档包审计不能替代逐页审阅。

## Current deterministic checks / 当前确定性检查

| Check | Result | Interpretation |
| --- | --- | --- |
| Principal-source checksum | PASS | Four in-scope source files match `SHA256SUMS.txt`; source files were not overwritten. |
| Excluded-source scope | PASS at final repository scan | The excluded identity is confined to its dedicated audit record and is absent from active scientific/submission content. |
| Aggregate statistics | PASS | `revision_v2/statistics_audit.json`: `all_checks_pass=true`; calculations are descriptive recomputations, not row-level reanalysis. |
| External sequence/docking summary | PASS | `revision_v3/external_docking_audit.json`: twelve unique 7–9-aa strings, composition, ordering and reported ranges pass; docking was not rerun. |
| Bilingual manuscript consistency | PASS | All locked funnel and external-summary values are present; prohibited positive claims/placeholders are absent; references 1–53 are sequential. |
| Language structure | PASS | English and Chinese each have eight parallel H2 sections and cite references 1–53 before their lists. |
| Citation inventory | PASS | The same 53 DOI strings occur in English, Chinese, `verified_references.md` and the 53-entry BibTeX file. This is inventory parity, not final Crossmark screening. |
| Mechanical and claim lint | PASS | Active manuscripts contain required provenance boundaries, no configured prohibited assertions, no broken image links, no malformed tables and no gap markers. |
| DOCX package audit | PASS | Main: 799 paragraphs, 8 tables, 6 drawings and 3 media files. Supplement: 468 paragraphs and 6 tables. CRC, XML, relationships, media and expected tokens pass. |
| Word-count estimate | INFORMATIONAL | Structured abstract≈344 words; Introduction through Conclusions≈5,120; main text with declarations excluding references≈5,450. Recount under target-journal rules. |

## Scientific-integrity boundaries / 科学诚信边界

1. Principal-source screening counts and externally reported sequence/score summaries are separate evidence tiers.
2. The twelve strings are not proven to correspond row by row to the principal source’s twelve main rows or stricter eight.
3. BBB-high is not measured transport or brain exposure.
4. NTxPred2-positive is not experimental neurotoxicity.
5. Mebipred/CHEL/FRS labels are not affinity, metal selectivity, redox chemistry or pro-oxidant activity.
6. Source-reported Vina scores are not reproduced docking, binding affinities or free energies.
7. PAS/gorge residue contacts and molecular-dynamics outcomes are not audited results.
8. Candidate counts are computational accounting units, not independent biological replicates.
9. A periodontitis-cohort branch is not a periodontitis-specific or taxonomically assigned peptide set.
10. Periodontitis–AD literature motivates questions but does not establish causality.

## Remaining blockers / 剩余阻断项

### Scientific and reproducibility

- Link each external sequence to principal-source candidate, sample, assembly, evidence match and predictor rows; identify the strict eight.
- Recover original screening code, versions, databases, environment and run logs.
- Recover prepared docking inputs, exact configuration/grid, seeds, raw runs, logs, poses and interaction outputs; reproduce the ranking.
- Resolve the outstanding BioProject, 4-aa handling, long-branch evidence class and NTxPred2→mebipred handoff.
- Add cohort-matched expression, BBB, toxicology, metal and AChE/Aβ experiments.

### Authorial and administrative

- Select the target journal and recheck current scope, article type, indexing, fees, word limits, figure rules and AI policy.
- Complete authors, affiliations, correspondence, ORCIDs, CRediT, funding, conflicts, ethics/consent, originality and final approval.
- Approve Data/Code Availability and AI disclosure.
- Perform final DOI, Crossmark, correction and retraction checks for all 53 references.

### File-level

- Open both DOCX files in Word/LibreOffice and inspect every page, table, image, symbol, hyperlink and Chinese font.
- Apply journal formatting, recount words, verify figure dimensions/resolution and export a compliant PDF if required.

## Recommendation / 建议

Use `manuscript/manuscript_bilingual.docx` for bilingual author review and `submission/presubmission_enquiry_bilingual.md` for a candid editorial enquiry. Do not claim full reproducibility, target validation, experimental validation or disease causality. Formal submission should proceed only after authors complete administrative requirements and accept the disclosed scientific risk, preferably after editorial guidance or recovery of the missing lineage/docking artefacts.
