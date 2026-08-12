# Stage 3 — Critical literature review and evidence synthesis / 批判性文献综述与证据综合

Workflow: K-Dense `literature-review` at pinned commit recorded in `SKILL_PROVENANCE.md`  
Input handoff: `01_topic_brainstorming.md` + `02_literature_search_and_novelty.md`  
Review type: targeted narrative synthesis with explicit evidence boundaries; not PRISMA/systematic.

## 1. Executive synthesis / 执行摘要

The literature supports four statements:

1. Human microbiomes contain a large, incompletely annotated smORF/microprotein space.
2. Credible smORF discovery normally combines gene-calling/evolutionary evidence with translation or proteomic evidence; downstream bioactivity predictions do not establish translation.
3. Sequence-based peptide predictors can reduce screening burden but are task-specific, sensitive to training-set composition and not equivalent to measured BBB transport, neurotoxicity or metal chemistry.
4. Periodontitis is observationally associated with dementia/AD in some syntheses, while recent Mendelian-randomisation studies and their synthesis do not establish a substantial causal relationship.

The present study can therefore justify **candidate prioritisation**, but not periodontitis specificity, oral expression in the analysed cohort, brain exposure, neurotoxicity, metal-dependent oxidative injury or AD causality.

## 2. Thematic synthesis / 主题综合

### Theme A — smORFs are plausible but technically easy to overcall

**Consensus.** Sberro et al. revealed thousands of previously overlooked small-protein families in human-associated microbiomes. Durrant and Bhatt subsequently combined family pHMMs and deep learning in SmORFinder and tested whether predictions were enriched for Ribo-seq/MetaRibo-seq signals. Current deep multi-omics work by Davin et al. further couples prediction with metatranscriptomic and metaproteomic evidence.

**Implication for this manuscript.** Exact sequence matching and deduplication are reasonable search-space reduction steps. However, a large raw sORF denominator is not a biological sample size, and a predicted ORF is not automatically translated. The present 31,510/33,786 retained counts should be labelled evidence-filtered candidates, not confirmed micropeptides.

**Gap exposed.** Candidate DNA/amino-acid sequences, genomic coordinates, spectra, peptide-spectrum matches, false-discovery controls and translation evidence were not supplied. The study cannot independently establish that its final candidates are expressed in the analysed cohort.

### Theme B — current oral-omics standards are subject/sample resolved

**Consensus.** Belstrøm et al. demonstrated compartment- and species-specific microbial activity using paired metagenomics/metatranscriptomics. Ovsepian et al. pooled 54 subgingival plaque samples (27 healthy, 27 periodontitis), explicitly normalised and analysed subject/sample-level activity. Yuan et al. showed that salivary metaproteomics benefits from host depletion, microbial enrichment, FDR-controlled peptide/protein identification, taxonomic assignment and deposited raw data.

**Implication for this manuscript.** The healthy and periodontitis aggregate counts can describe two pipeline branches. They cannot support differential abundance, prevalence, association or enrichment because sample-level mapping is absent.

**Gap exposed.** The source reports 24 healthy and 26 periodontitis participants but supplies no participant-level outcomes. Treating millions of sORFs or tens of thousands of candidates as biological replicates would be pseudoreplication.

### Theme C — serial predictors rank candidates but do not create orthogonal biological evidence

**Consensus.** UniDL4BioPep, NTxPred2, mebipred and AnOxPePred address different labels and were developed with different datasets. The BBB-prediction literature itself documents limited positive examples, class imbalance, threshold dependence and performance differences between models. Sequence-derived models can share compositional signals, so agreement need not be independent confirmation.

**Implication for this manuscript.** The funnel is useful as an operational filter only. “Convergence” should mean satisfying several computational rules, not biological triangulation. Thresholds (0.80, 0.50, CHEL 0.25, FRS 0.50/0.45) must be reported as source-prespecified operational cutoffs, not validated clinical probabilities.

**Gap exposed.** No scores, calibration curves, domain-of-applicability checks, alternative predictors, threshold-sensitivity reanalysis or external candidate validation are available. NTxPred2 structurally excludes 219 short candidates; they are missing, not negative.

### Theme D — computational discovery is most persuasive when followed by synthesis and assays

**Consensus.** Torres et al. computationally prioritised microbiome-derived peptides but then synthesised 78 candidates, tested antimicrobial activity in vitro and advanced leads into animal models. The exact assays differ from the present neuro/metal hypothesis, but the evidentiary sequence is instructive: prediction → identity → phenotype → mechanism.

**Implication for this manuscript.** The present study stops at prediction. Its appropriate endpoint is a hypothesis-generating shortlist, not a validated neuroactive peptide set. The absence of sequences prevents even the first follow-up step in the current package.

### Theme E — periodontitis–AD evidence is associational and causally unsettled

**Consensus.** Observational meta-analyses report associations between severe periodontitis and dementia/AD, but estimates vary with disease definition, severity and adjustment. Oral-bacteria/AD findings are inconsistent. Mechanistic work involving *P. gingivalis* supplies biological plausibility, not attribution of unclassified peptides.

**Counter-evidence.** Hu et al. found no evidence of a genetic causal relationship between periodontal disease and AD in two AD datasets. Zhao et al.’s 2026 systematic review/meta-analysis of Mendelian-randomisation experiments likewise reported no substantial causal association with AD.

**Implication for this manuscript.** AD may appear as cautious motivation: periodontitis–neurodegeneration is a contested context in which BBB/neurotoxicity/metal-interaction predictions generate testable questions. AD must not be in the principal result claim and should not dominate the title.

## 3. Claim–evidence matrix / 主张—证据矩阵

| Proposed manuscript statement | Best available support | Evidence level | Allowed wording | Prohibited wording |
| --- | --- | --- | --- | --- |
| Microbiome smORFs are underexplored | Sberro 2019; Durrant & Bhatt 2021; Davin 2026 | Primary computational + translation/proteomics evidence in other cohorts | “underexplored candidate space” | “all predicted sORFs are translated” |
| Periodontitis alters oral microbial activity | Belstrøm 2021; Ovsepian 2024 | Human subject/sample-level omics | “associated with altered activity” | “the present peptides drive periodontitis” |
| Exact matching can support prior observation | Belstrøm 2016; oral metaproteomics methods | Dataset-context sequence evidence | “matched to named oral resources according to source” | “confirmed expression in this periodontitis cohort” |
| BBB prediction can prioritise peptides | UniDL4BioPep + BBB-predictor literature | Model prediction | “BBB-high model output” | “crosses the BBB” |
| NTxPred2 can classify eligible sequences | Rathore 2025 | Model prediction | “predicted neurotoxic among evaluated sequences” | “neurotoxic” without qualifier |
| mebipred estimates metal-binding potential | Aptekmann 2022 | Model prediction | “predicted metal-binding potential” | affinity/ion stoichiometry/redox mechanism |
| CHEL/FRS can prioritise antioxidant-related patterns | Olsen 2020 | Model prediction | “operational CHEL/FRS pattern” | “pro-oxidant peptide” |
| Periodontitis and dementia may be associated | observational syntheses | Secondary observational evidence | “reported association” | causal risk reduction/intervention effect |
| Periodontitis causes AD | recent MR does not support; human causality unresolved | Conflicting/insufficient | “causality remains unestablished” | “causes AD” |
| Final 12/8 candidates merit follow-up | supplied aggregate record only | Internal descriptive output | “source-reported shortlist for follow-up” | “validated therapeutic/toxic candidates” |

## 4. Critical appraisal of the present study / 本研究的批判性评价

### Strengths that remain valid

- Preserves a clearly described count funnel.
- Separates model eligibility (3,299) from positivity (923).
- Distinguishes main (FRS<0.50) from stricter (FRS<0.45) rule.
- Recomputable aggregate percentages can be audited.
- Can be reframed without inventing new data.

### Major limitations affecting publishability

1. **Non-reproducible candidate identity:** no sequences or row-level output.
2. **No biological replication:** no sample/subject mapping for inference.
3. **Unverified provenance components:** PRJEB65451 unresolved; long-branch evidence status ambiguous.
4. **Heterogeneous matching resources:** caries-risk and lung-cancer oral datasets cannot confer periodontitis specificity.
5. **Model stacking:** correlated sequence features may amplify bias rather than independent evidence.
6. **No validation:** no translation, BBB, toxicology, metal-binding, ROS or disease assay.
7. **Weak novelty:** serial use of established models is incremental.

### Risk-of-bias judgement

- Selection bias: high/unclear because row-level attrition cannot be inspected.
- Measurement/model bias: high/unclear because calibration and applicability-domain information are absent.
- Confounding: not assessable at aggregate peptide level.
- Reporting bias: possible because only summary thresholds/positives are available.
- Reproducibility: partial for arithmetic; absent for primary pipeline.

## 5. Evidence-derived narrative architecture / 证据驱动的叙事结构

1. **Problem:** microbiome smORFs are under-annotated and large candidate spaces require triage.
2. **Method gap:** direct multi-omics and experimental confirmation are ideal but unavailable for this source record.
3. **Study action:** transcribe and audit a serial aggregate computational prioritisation funnel.
4. **Result:** 11.72 million periodontitis-branch sORFs → 33,786 evidence-filtered candidates → 3,518 BBB-high → 923 NTxPred2-positive among eligible → 111 source-reported metal-binding positive → 12 main / 8 strict.
5. **Meaning:** this is a transparent shortlist and threshold record.
6. **Non-meaning:** no group-level inference, mechanism or AD causality.
7. **Next test:** release sequences/provenance, confirm expression, then test transport, toxicity and metal-dependent effects.

## 6. Manuscript change directives / 稿件修改指令

- Adopt the Stage-1 locked title.
- Replace “secondary computational analysis” with “aggregate-level audit and descriptive reconstruction of a source-reported computational analysis” wherever needed to avoid implying a rerun.
- Add Durrant & Bhatt, Torres, Ovsepian, Yuan, Gu/Augur, Hu and Zhao.
- In the Abstract, state “no row-level sequences or subject mapping were available.”
- Start Discussion with the evidentiary endpoint, not the mechanistic aspiration.
- Add a dedicated section: “Why aggregate group counts are not comparative statistics.”
- Remove any suggestion that the 12 candidates can currently be synthesised; their sequences are unavailable in the package.
- Frame experimental validation as required future work, not planned or ongoing work.
- Retain a bilingual, meaning-matched structure.

## 7. Synthesis boundary / 综合边界

The review uses authoritative records accessible on 2026-08-12, but it is not exhaustive and does not provide a formal certainty-of-evidence grade. It does not rescue missing primary data. All claims remain subject to author verification and pre-submission correction/retraction checks.
