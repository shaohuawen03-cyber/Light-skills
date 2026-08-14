# Stage 7 — Evidence-first manuscript rebuilding / 证据优先的稿件重写

Workflow: Nature `nature-writing` + ARS academic-paper drafting sequence  
Outputs: `manuscript/manuscript_en.md`, `manuscript/manuscript_zh.md`, and rebuilt bilingual Markdown.

## 1. Writing decision

The manuscript was rebuilt around one defensible claim:

> A source-reported serial predictor workflow can be reconstructed as an internally consistent aggregate candidate-reduction record, but it does not provide participant-level inference or validation beyond computational prioritization.

The title, Abstract, Introduction objective, first Discussion paragraph, Conclusions, Data Availability, and Code Availability now state this boundary consistently.

## 2. Argument architecture

### Introduction

1. smORFs are a legitimate but difficult discovery space.
2. Current standards add translation/proteomic evidence and sample resolution.
3. Serial peptide predictors are useful for triage but remain model outputs.
4. Periodontitis–AD observational evidence is counterbalanced by current Mendelian-randomization evidence.
5. The study asks an aggregate workflow question, not a mechanism question.

### Methods

1. Defines the principal source and aggregate reconstruction.
2. Separates sequence-resource matching from expression evidence.
3. Reports every threshold with its semantic boundary.
4. States that the primary pipeline was not rerun.
5. Defines candidate sequences as computational accounting units, not biological replicates.
6. Links the deterministic Stage-5 audit.

### Results

1. Candidate-space reduction.
2. Descriptive BBB/multi-activity output distributions.
3. NTxPred2 eligibility and positivity.
4. Source-reported metal/CHEL/FRS chain and threshold sensitivity.
5. Two tables and the revised funnel figure.

### Discussion

1. Bounded contribution and weak novelty are explicit.
2. Current smORF/oral-omics validation standards provide the comparator.
3. A dedicated subsection explains pseudoreplication.
4. Predictor stacking, non-coverage, domain shift and metal-output semantics are separated.
5. Observational AD context is balanced with 2024–2026 causal counter-evidence.
6. The evidence ladder orders future work from identity to disease mechanism.
7. Limitations determine, rather than merely qualify, the conclusion.

## 3. Major scientific changes from revision 1

- Removed AD from the primary title claim.
- Replaced “AD-relevant candidates” with testable downstream context.
- Added explicit statement that the final candidate identities cannot be listed or synthesized from the supplied package.
- Added recent comparator literature: Durrant & Bhatt, Davin, Ovsepian, Yuan, Gu/Augur, Liu/B3BPFN, Torres, Hu, and Zhao.
- Added a dedicated aggregate-statistics boundary.
- Changed the mebipred transition to a source-reported, visually dashed handoff.
- Added threshold sensitivity (8/12 retained at stricter FRS).
- Rebuilt Data/Code Availability to distinguish present repository utilities from the missing original pipeline.
- Removed future structural-simulation detail that was not necessary for the bounded research question.

## 4. Parallel-language control

English and Chinese files have matched top-level sections and corresponding scientific content:

- Abstract / 摘要
- Introduction / 引言
- Materials and Methods / 材料与方法
- Results / 结果
- Discussion / 讨论
- Conclusions / 结论
- Declarations / 声明
- Shared 25-reference list

The bilingual builder inserts each complete English section followed by its Chinese counterpart. Quantitative and reference-sequence audits run independently on both language files.

## 5. Citation control

All 25 cited records have DOI-backed entries in `references/verified_references.md`, with a permitted use and support boundary. Recent dynamic facts were checked against official publisher and/or PubMed/PMC records on 2026-08-12. The manuscript does not use citation count or “first” claims.

## 6. Writing-stage verdict

**PASS for evidence-first IMRaD rebuilding.** The text is materially re-argued rather than surface edited. Scientific readiness remains constrained by missing original sequences, row-level data/code, authorship details, declarations, and journal choice.
