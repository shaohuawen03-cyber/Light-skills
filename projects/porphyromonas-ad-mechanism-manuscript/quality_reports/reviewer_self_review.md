# Reviewer-style self-review / 审稿人视角自审

## Overall assessment

The manuscript presents a coherent computational funnel and reports its boundaries unusually explicitly. Its novelty is the integrated prioritization of periodontitis-branch oral sORF candidates across BBB, neurotoxicity, metal-binding, CHEL and FRS models. The present package is suitable for author review, but it would face major reproducibility objections if submitted without row-level sequences, code and model provenance.

## Major strengths

1. **Clear question:** the article asks which candidates survive a prespecified computational funnel rather than claiming to prove a periodontal–AD mechanism.
2. **Transparent denominators:** NTxPred2 eligibility (3,299) is separated from positivity (923), and the 219 out-of-range sequences remain “not evaluated.”
3. **Conservative interpretation:** BBB score is not called brain exposure; NTxPred2 is not called experimental toxicity; CHEL-high/FRS-low is not called pro-oxidant activity.
4. **Taxonomic restraint:** the paper does not assign candidates to *P. gingivalis* without sequence-level evidence.
5. **Descriptive integrity:** no unsupported inferential p-values, confidence intervals or enrichment claims were added.
6. **Bilingual consistency:** core numbers, references and scientific boundaries are mirrored in English and Chinese.

## Major concerns requiring resolution before submission

1. **Reproducibility:** no peptide sequences, SeqIDs, per-model scores, code, model versions, database snapshots or execution logs are available. This is the strongest potential desk-reject/reviewer objection.
2. **Accession provenance:** PRJEB65451 remains unresolved. The relationship among PRJNA678453, the reported 296 MAGs and the 24/26 participants needs a traceable source.
3. **Long-branch evidence:** the source labels this branch HOMD-derived but calls the combined candidates proteomics-supported. HOMD is not an MS repository. The evidence class must be clarified.
4. **Heterogeneous proteomic resources:** PXD003151 and PXD026727 are not periodontitis cohorts. Exact sequence matching may support oral detection, but it does not support disease specificity or same-cohort expression.
5. **Mebipred denominator:** the count 111 is usable, but its precise input list and denominator cannot be independently audited.
6. **Applicability domain and calibration:** the exceptionally high antimicrobial-positive fraction in short peptides suggests potential domain shift or threshold/calibration issues. Model confidence should be assessed with negatives, decoys or external test data.
7. **No experimental validation:** the final 12/8 candidates are not yet linked to BBB transport, neurotoxicity, metal binding, oxidative injury, AChE/BChE function, Aβ aggregation or AD phenotypes.

## Minor concerns

- The initial filter states 4–50 aa but downstream bins begin at 5 aa; the handling of 4-aa sequences should be documented.
- Candidate overlap among multiple UniDL4BioPep activity classes cannot be assessed from aggregate counts.
- Chemical synthesis and assay conditions will differ for 8–15-aa versus 31–50-aa candidates.
- Author line, CRediT, funding, conflicts, institutional ethics wording and target-journal formatting remain to be completed.
- The title uses “periodontitis-cohort” rather than “periodontitis-specific,” which is scientifically safer but should be confirmed by the analysis authors.

## Suggested validation package

1. Public TSV/CSV with sequence, stable ID, branch, source match, sample mapping, taxonomy, each model score and each threshold decision.
2. Spectrum-level evidence with FDR controls and peptide uniqueness.
3. Executable workflow with locked versions and checksums.
4. Model calibration/applicability-domain analysis, including composition-matched decoys.
5. BBB transport and neuronal toxicity assays.
6. Cu/Fe/Zn binding plus metal-dependent ROS/lipid-peroxidation tests with controls.
7. Aβ aggregation and AChE/BChE assays before target-specific docking/MD.

## Recommendation

**Major revision before submission; suitable for internal author review now.** The narrative is appropriately bounded, but candidate-level evidence and reproducibility materials are essential for a publishable original research article.
