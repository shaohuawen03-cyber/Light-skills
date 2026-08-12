# Final quality summary / 最终质量汇总

Date / 日期: 2026-08-12

## Deliverable status / 交付状态

- **Scientific-content draft / 科学内容草案：PASS for author review / 可交作者审阅。**
- **Submission-ready package / 投稿就绪包：NOT READY / 尚未就绪。**
- **Primary DOCX structural integrity / 主 DOCX 结构完整性：PASS。**
- **Rendered-page visual review / 逐页渲染审阅：UNAVAILABLE** because no Office/LibreOffice/PDF rendering tool is installed.
- **Canonical online citation/retraction gate / 权威在线引文与撤稿门：UNRESOLVED** because the automated resolver was unavailable; manual metadata and inventory checks are preserved separately.

## Deterministic checks / 确定性检查

| Check | Result | Interpretation |
| --- | --- | --- |
| Source checksums | PASS, 6/6 | All original DOCX/PDF files match `SHA256SUMS.txt`; BOM handling was fixed in the verifier without editing sources. |
| Bilingual core-number audit | PASS | All predefined funnel counts and percentages appear in both language manuscripts. |
| Prohibited-claim audit | PASS | No positive claim of periodontitis specificity, *P. gingivalis* origin, candidate mechanism proof, or causal proof was detected. |
| Placeholder audit | PASS | No TODO/TBD/MATERIAL GAP/RESULT GAP token remains. Transparent “not supplied” declarations are intentional and scientifically necessary. |
| Reference sequence | PASS | References 1–17 are consecutive in both English and Chinese manuscripts. |
| DOI inventory parity | PASS | The same 17 DOIs occur in English, Chinese, verified-reference record, and BibTeX. |
| Draft lint | PASS | No FAIL-level draft issue; 17 DOI items remain listed for continuing online verification. |
| Contribution consistency heuristic | PASS | No abstract/introduction/conclusion drift detected; human review remains authoritative. |
| NHST expression scan | NONE_FOUND | No t/F/r/χ²/Z-p expression was found, consistent with descriptive aggregate reporting; misses are possible. |
| Tortured-phrase scan | 0 hits | No dictionary signal; not proof of originality or absence of plagiarism. |
| DOCX package audit | PASS | ZIP CRC, all XML parts, core manuscript tokens, tables and embedded media passed structural checks. |

## Mechanical-writing findings / 机械写作发现

`mechanical_check.json` reported 78 heuristic findings:

- 50 passive-voice instances and 9 paragraph-level passive-overuse flags, mainly in Methods and provenance statements where passive construction is often acceptable;
- 18 punctuation flags caused by typographic apostrophes in names such as “Alzheimer’s,” not Chinese punctuation contamination;
- 1 overclaim flag for the word “novel” inside the immutable title of Sberro et al. (2019), not an author claim about this study.

These findings do not require scientific-content changes, but the target journal’s copyediting style may prefer ASCII apostrophes or more active Methods prose.

## Scientific integrity conclusions / 科学诚信结论

The manuscript correctly keeps the following distinctions:

1. BBB model output ≠ demonstrated BBB transport or brain exposure.
2. NTxPred2 positivity ≠ experimental neurotoxicity.
3. mebipred positivity ≠ binding affinity, site or coordination geometry.
4. CHEL-high/FRS-lower ≠ pro-oxidant activity.
5. Periodontitis branch ≠ periodontitis-specific sequence.
6. Oral candidate ≠ *P. gingivalis*-derived candidate.
7. Literature-motivated AChE/Aβ analysis ≠ completed docking or MD.
8. Periodontitis–AD association ≠ causation.

## Submission blockers / 投稿阻断项

1. Candidate sequences, stable IDs, row-level model scores, sample mapping, taxonomy and spectra are absent.
2. Original pipeline code, model/database versions, environment and run logs are absent.
3. PRJEB65451 remains unresolved.
4. The long-branch evidence class and the mebipred handoff denominator require clarification.
5. Institutional ethics wording, human author line, CRediT, funding and competing interests require accountable-author approval.
6. Retraction/correction status must be rechecked online immediately before submission.
7. The DOCX must be opened and visually reviewed page by page in Word/LibreOffice; target-journal formatting has not been applied because no journal was specified.

## Final recommendation / 最终建议

Use `manuscript/manuscript_bilingual.docx` for bilingual author review and `manuscript_en.md` as the starting point for a future English journal submission. Do not remove the major limitations unless the missing data and provenance are supplied. After author corrections, rebuild the DOCX from the tracked Markdown, rerun all audits, render the file, and perform a final human scientific/citation/ethics check.
