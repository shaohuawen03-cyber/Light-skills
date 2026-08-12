# Stage 5 — Statistical review / 统计学审查

Workflow: `nature-statistics` at the pinned Nature Skills commit  
Executable audit: `scripts/stage5_statistics_audit.py`  
Machine-readable result: `statistics_audit.json` (`all_checks_pass=true`)

## 1. Statistical question and estimand

The current data do not support a population-level healthy-versus-periodontitis estimand. The only valid estimands are deterministic pipeline quantities:

- source-reported counts at each filter;
- percentages within explicitly reported candidate-set denominators;
- deterministic retention from the main threshold to the stricter threshold.

The biological experimental unit would be a participant or sample. Subject/sample-level candidate outcomes are unavailable. Unique sequence counts are useful computational units but are **not independent biological replicates**.

## 2. Analysis classification

- Analysis type: descriptive aggregate audit.
- Confirmatory hypothesis: none.
- Inferential tests: none.
- Confidence intervals: none; candidate-level binomial intervals would misleadingly imply independent sampling.
- Multiple-testing correction: not applicable to this reconstruction; the source’s >20 model-class screen cannot be reanalysed without row-level scores.
- Missing-data imputation: none.
- Outlier handling: not possible from aggregates.
- Software for audit: Python standard library; no statistical package dependency.

## 3. Denominator audit

| Quantity | Numerator / denominator | Audited result | Interpretation |
| --- | --- | ---: | --- |
| Healthy evidence-filter retention | 31,510 / 11,269,961 | 0.2796% | Pipeline retention only |
| Periodontitis evidence-filter retention | 33,786 / 11,721,988 | 0.2882% | Pipeline retention only |
| Healthy short BBB-high | 3,359 / 30,557 | 10.99% | Model-output prevalence in candidate branch |
| Periodontitis short BBB-high | 3,446 / 32,754 | 10.52% | Model-output prevalence in candidate branch |
| Healthy long BBB-high | 40 / 953 | 4.20% | Model-output prevalence in candidate branch |
| Periodontitis long BBB-high | 72 / 1,032 | 6.98% | Model-output prevalence in candidate branch |
| Short share of periodontitis BBB-high | 3,446 / 3,518 | 97.95% | Composition of downstream set |
| NTxPred2 coverage | 3,299 / 3,518 | 93.77% | 219 candidates not evaluated |
| NTxPred2 positive among evaluated | 923 / 3,299 | 27.98% | Conditional on model eligibility |
| CHEL≥0.25 among reported metal-positive | 15 / 111 | 13.51% | Source-reported downstream set |
| Main rule among reported metal-positive | 12 / 111 | 10.81% | Source-reported downstream set |
| Strict rule among reported metal-positive | 8 / 111 | 7.21% | Source-reported downstream set |
| Strict retained from main | 8 / 12 | 66.67% | Threshold sensitivity; tightening FRS removes 4/12 |

## 4. Internal consistency checks

All programmed checks passed:

- 30,557 + 953 = 31,510 healthy evidence-filtered candidates.
- 32,754 + 1,032 = 33,786 periodontitis evidence-filtered candidates.
- BBB-positive counts do not exceed branch denominators.
- 3,446 + 72 = 3,518 periodontitis BBB-high candidates.
- 3,299 evaluated + 219 not evaluated = 3,518.
- 923 ≤ 3,299.
- 8 ≤ 12 ≤ 15 ≤ 111.

These checks demonstrate arithmetic consistency, not validity of the original pipeline.

## 5. Missingness and selection

NTxPred2 non-evaluation is structurally dependent on sequence length. The 219 sequences shorter than the model’s accepted range are not missing at random and must not be pooled with negatives. The downstream pipeline therefore selects both for target predictions and for model compatibility.

The source narrative places 111 metal-binding positives after 923 NTxPred2 positives. Without the row-level handoff, `111/923` is not presented as an audited transition rate. The count order is plausible but not independently reproducible.

## 6. Healthy/periodontitis comparison decision

The four BBB proportions may be presented side by side for descriptive orientation. The manuscript must not use:

- “significantly higher/lower”;
- p values based on peptide counts;
- odds ratios treating candidates as independent;
- participant-level prevalence language;
- causal, predictive-performance or biomarker claims.

A valid group comparison would require participant/sample mapping, preprocessing/exposure denominators, a prespecified unit-level outcome, covariates, and a model accounting for clustering and repeated sequences.

## 7. Threshold sensitivity

Only one source-reported sensitivity contrast is reconstructable:

- FRS<0.50 with CHEL≥0.25: 12 candidates.
- FRS<0.45 with CHEL≥0.25: 8 candidates.
- Tightening FRS retains 66.67% of the main set and removes four candidates.

Because sequences and scores are absent, a full threshold curve, rank stability, calibration, resampling or alternative-model sensitivity analysis cannot be performed.

## 8. Statistical wording approved for the manuscript

> Counts and percentages were transcribed or deterministically recomputed from the aggregate source record. Candidate sequences were treated as units of computational accounting, not as independent biological replicates. No subject-level hypothesis test, confidence interval or effect estimate was calculated because sample-to-candidate mappings and row-level outcomes were unavailable.

## 9. Verdict

**PASS for descriptive arithmetic; FAIL for inferential healthy-versus-periodontitis statistics.** The manuscript is statistically defensible only if it preserves the aggregate, exploratory framing and makes the absent experimental unit explicit.
