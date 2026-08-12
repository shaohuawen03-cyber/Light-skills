# Revision v3 — Stage 5: statistical review / 统计审查

Date: 2026-08-12

## Retained analysis

All principal-source percentages are descriptive and use explicit denominators. Deterministic checks cover branch sums, bounds, NTxPred2 evaluated/not-evaluated partition, downstream monotonicity and the 8/12 threshold sensitivity.

## Rejected analysis

Peptide-level Fisher or chi-square tests from the external draft were not retained. Candidates are nested within participants, assemblies, homologous groups and evidence resources. Without row-level cluster membership, treating millions of candidates as independent would be pseudoreplication.

No p value, confidence interval, participant-level effect, power estimate, ROC, multiple-testing result or disease-enrichment estimate is reported.

## External sequence/score audit

`audit_external_docking_summary.py` checks:

- exactly twelve unique standard-amino-acid strings;
- lengths of 7–9 aa;
- 11/12 containing histidine, 6/12 containing cysteine, and 12/12 containing Arg/Lys;
- means spanning −9.60 to −8.25 kcal/mol;
- SDs spanning 0.04 to 0.12;
- nondecreasing order from more-negative to less-negative means.

This is a transcription/composition audit, not a statistical validation or docking reproduction. SD lacks an auditable denominator.

## Required future model

A valid group comparison requires participant/sample-level rows and a prespecified unit, clustering strategy, covariates, duplicate/homology handling, and sensitivity analyses.