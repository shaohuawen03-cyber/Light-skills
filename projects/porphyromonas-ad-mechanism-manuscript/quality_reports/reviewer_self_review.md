# Reviewer-style self-review / 审稿人视角自审 — revision v3

## Overall assessment

The expanded manuscript is substantially closer to a credible submission-oriented computational Original Research Article than the previous aggregate-only draft. It now offers a full scientific rationale, explicit evidence tiers, twelve concrete 7–9-aa candidate sequences, a source-reported AChE docking ranking, four main tables, three figures, six supplementary tables and 53 curated references. The authors are unusually transparent about provenance and pseudoreplication.

The main editorial risk remains serious: sequence identities come from a separate author record without row-level linkage to the principal funnel, and docking summaries lack raw reproducibility artefacts. The paper is suitable for accountable-author review and a candid pre-submission enquiry. It is not yet a fully reproducible target-validation or mechanism study.

## Major strengths

1. **Expanded biological framing:** smORF, oral-omics, predictor, AChE/PAS, metal and periodontal–AD literatures are integrated rather than listed.
2. **Transparent evidence architecture:** principal screening, external sequence/score summaries, independent recomputation and literature context are not collapsed.
3. **Concrete hypothesis set:** twelve explicit sequences can now be synthesized and independently queried.
4. **Descriptive integrity:** candidate counts are not treated as independent participant-level replicates; unsupported peptide-level p values are rejected.
5. **Docking restraint:** Vina values are called source-reported scores, not affinities or binding free energies; contacts and MD are excluded.
6. **Actionable validation plan:** lineage, expression, stability, BBB, toxicology, metal chemistry and AChE/Aβ tests are ordered with stopping rules.
7. **Bilingual and technical consistency:** both languages contain all 53 in-text citations and synchronized values; deterministic and DOCX-package audits pass.

## Major concerns

1. **Screening lineage:** no stable ID links the twelve external strings to the principal source’s candidates, evidence matches, model rows, CHEL/FRS values or stricter 8-of-12 subset.
2. **Docking reproduction:** receptor/ligand preparation, protonation, exact grid centre, configurations, exhaustiveness, seeds, raw scores, logs, poses and interaction outputs are absent.
3. **Cohort inference:** no participant/sample-to-candidate matrix exists, precluding disease-enrichment statistics and taxonomic distribution analyses.
4. **Expression evidence:** heterogeneous oral resources cannot establish current-cohort translation or periodontitis-specific expression.
5. **Model applicability:** near-saturation of the short-branch antimicrobial label indicates possible domain shift or calibration limitations. Alternative predictors and composition-matched decoys are needed.
6. **No experimental validation:** BBB transport, neurotoxicity, metal binding/redox chemistry, AChE function, Aβ aggregation and disease phenotypes remain untested.
7. **Accession and handoff gaps:** one BioProject remains unresolved; 4-aa handling, long-branch evidence class and NTxPred2→mebipred handoff remain unclear.

## Minor concerns

- The abstract is approximately 344 words and may exceed some journal limits.
- A 5,120-word Introduction-through-Conclusion body plus 53 references may require journal-specific shortening.
- The score SDs lack a defined computational denominator and should not be used for formal comparison.
- The exact external PDF should remain a provenance artefact unless reuse rights and journal need are confirmed.
- The machine-generated DOCX requires visual inspection for page breaks, table wrapping, fonts and figure legibility.
- Author, ethics, funding, conflict, CRediT and target-journal fields remain incomplete.

## Recommendation

**Major revision before formal submission; proceed with accountable-author review and pre-submission enquiry.** If row-level screening lineage and raw docking artefacts can be recovered, the study could become a defensible preliminary computational prioritization article. Without them, editors may judge the package insufficiently reproducible despite its improved depth and transparency.
