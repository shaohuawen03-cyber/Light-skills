# Stage 2 — Bounded academic search and novelty check / 有界文献检索与查新

Search date: 2026-08-12  
Workflow: `nature-academic-search` multi-source-search + citation-verification principles  
Scope status: **targeted scoping search, not a systematic review**

## 1. Search question

Four evidence domains were searched:

1. Human/oral microbiome smORFs and microproteins.
2. Periodontitis metagenomics, metatranscriptomics and metaproteomics.
3. Sequence-based prediction of BBB-penetrating, neurotoxic and metal-binding peptides.
4. Periodontitis–Alzheimer/dementia association and causal inference.

The purpose was to position and bound the aggregate computational study, not to estimate a pooled effect.

## 2. Sources and execution

### Planned routing

- T1: PubMed/PMC, Crossref/DOI records, journal/publisher article pages.
- T2: Nature/Cell/Frontiers/Springer/Wiley article pages and accessible full-text records.
- OpenAlex no-MCP fallback for broad discovery.
- Scopus, Web of Science and ScienceDirect APIs only if mounted and authorised.

### Actual access

- OpenAlex fallback: **UNAVAILABLE**. Four calls failed with TLS/SSL EOF before record retrieval; see `search_raw/openalex_failure_log.txt`.
- Academic-search MCP: **UNAVAILABLE** in this environment.
- Scopus/Web of Science/institutional subscriptions: **UNAVAILABLE**, not interpreted as “no records”.
- Accessible web, PubMed/PMC, DOI and publisher pages: **AVAILABLE** and used.

Four broad searches returned 40 displayed web records before deduplication. Additional title/DOI searches were used to verify priority metadata. Search-result counts are interface-limited and are not treated as a reproducible database denominator.

## 3. Query log

| ID | Query | Purpose |
| --- | --- | --- |
| Q1 | `oral microbiome small open reading frames micropeptides metagenomics metaproteomics` | smORF discovery and translation evidence |
| Q2 | `periodontitis metagenomics metatranscriptomics metaproteomics oral peptides study` | oral disease omics context |
| Q3 | `blood brain barrier penetrating peptide prediction neurotoxicity peptide predictor metal binding prediction peptide` | predictor landscape and applicability limits |
| Q4 | `periodontitis Alzheimer disease systematic review meta-analysis Mendelian randomization 2024 2025 2026` | association versus causality |
| Q5 | Exact-title/DOI queries for Durrant 2020/2021, Torres 2024, Ovsepian 2024, Yuan 2025, Davin 2026 and Hu 2024 | metadata verification |

## 4. Inclusion and exclusion logic

Included:

- Primary methods and resource papers that define smORF discovery/validation expectations.
- Human oral microbiome/periodontitis omics studies.
- Primary papers for predictors used or directly relevant to the workflow.
- Recent systematic reviews/meta-analyses and Mendelian-randomisation studies that define the AD boundary.
- Sources with verifiable DOI/PMID or official article records.

Excluded:

- Search snippets without resolvable article identity.
- Commercial pages, news summaries and ResearchGate copies when an authoritative record was available.
- Small-molecule BBB papers as direct support for peptide BBB claims.
- Reviews or animal/cell studies as evidence that the present candidates cause AD.
- The two mistakenly supplied unrelated files recorded in the dedicated exclusion audit.

## 5. Priority evidence map

| Domain | Verified priority record | What it supports | What it does not support |
| --- | --- | --- | --- |
| Human microbiome smORFs | Sberro et al. *Cell* 2019. DOI `10.1016/j.cell.2019.07.016` | Human microbiomes contain many previously overlooked small-protein families; computational discovery is biologically motivated. | Function of the present candidates. |
| smORF annotation | Durrant & Bhatt. *Cell Host Microbe* 2021;29:121–131.e4. DOI `10.1016/j.chom.2020.11.002` | smORF annotation benefits from complementary models and translation-signal enrichment; false ORFs remain a core problem. | That serial downstream bioactivity predictors validate translation. |
| Experimental standard | Torres et al. *Cell* 2024;187:5453–5467.e15. DOI `10.1016/j.cell.2024.07.027` | High-impact microbiome peptide discovery progressed from computational screening to synthesis, in-vitro activity and in-vivo testing. | Neuroactivity or AD relevance of oral candidates. |
| Current multi-omics standard | Davin et al. *Nature Communications* 2026. DOI `10.1038/s41467-026-72762-5` | Modern SEP discovery integrates smORF prediction, metatranscriptomics and deep metaproteomic detection; >25,000 SEPs were detected in that gut study. | Validation of the present oral candidates. |
| Oral metaproteomics | Yuan et al. *npj Biofilms and Microbiomes* 2025;11:63. DOI `10.1038/s41522-025-00692-z` | Host depletion, microbial enrichment, reproducible LC–MS/MS and taxon/function integration are current oral-metaproteome standards. | That a database sequence match equals cohort expression. |
| Periodontitis omics | Belstrøm et al. *npj Biofilms and Microbiomes* 2021;7:76. DOI `10.1038/s41522-021-00247-y` | Periodontitis associates with compartment- and species-specific oral microbial activity. | Micropeptide-level causation or attribution of the present candidates. |
| Periodontitis meta-analysis | Ovsepian et al. *Frontiers in Microbiology* 2024;15:1383404. DOI `10.3389/fmicb.2024.1383404` | Subject/sample-level data and cross-study normalisation can identify active periodontitis signatures. | Inference from aggregate peptide counts without sample mapping. |
| BBB predictor limitations | Gu et al. *BMC Biology* 2024;22:86. DOI `10.1186/s12915-024-01883-4` | BBB-peptide models face small, imbalanced training sets and generalisability concerns. | Actual BBB transport of a predicted candidate. |
| Current BBB predictor comparison | Liu et al. *Frontiers in Molecular Biosciences* 2026. DOI `10.3389/fmolb.2026.1858506` | Predictor outputs can differ substantially in sensitivity/specificity; independent external and prospective validation remain important. | Retrospective validation of the model used in the supplied source. |
| Neurotoxicity predictor | Rathore et al. *Protein Science* 2025;34:e70200. DOI `10.1002/pro.70200` | NTxPred2 is a sequence-based predictor with defined input/application scope. | Measured neurotoxicity of the 923 predicted positives. |
| Metal-binding predictor | Aptekmann et al. *Bioinformatics* 2022;38:3532–3540. DOI `10.1093/bioinformatics/btac358` | mebipred estimates sequence-level metal-binding potential. | Affinity, stoichiometry, metal identity at a specific site or redox effect. |
| CHEL/FRS predictor | Olsen et al. *Scientific Reports* 2020;10:21471. DOI `10.1038/s41598-020-78319-w` | AnOxPePred predicts chelation and free-radical-scavenging features. | “Pro-oxidant” behaviour from high CHEL/low FRS alone. |
| Observational AD association | Kim & Han. *Journal of Evidence-Based Dental Practice* 2025;25:102094. DOI `10.1016/j.jebdp.2025.102094` | Observational studies report associations, particularly for severe periodontitis. | Causation. |
| Genetic causal test | Hu et al. *Brain and Behavior* 2024;14:e3486. DOI `10.1002/brb3.3486` | Two-sample MR found no evidence of genetic causality between periodontal disease and AD in the analysed datasets. | Proof that every non-genetic pathway is absent. |
| Updated MR synthesis | Zhao et al. *BMC Oral Health* 2026;26:383. DOI `10.1186/s12903-026-07725-9` | Systematic review/meta-analysis of MR studies found no substantial causal association with AD. | Refutation of all observational or experimental biological plausibility. |

## 6. Novelty/collision assessment

### Nearest established work patterns

1. **Large-scale smORF discovery plus evidence filters** is established (Sberro; Durrant & Bhatt; Davin).
2. **Computational peptide mining plus serial prioritisation** is established; stronger papers commonly add synthesis and functional validation (Torres).
3. **Multiple BBB-peptide predictors and model comparisons** are established (Gu; Liu).
4. **Periodontitis omics signatures** are established at subject/sample level (Belstrøm; Ovsepian).
5. **Periodontitis–AD association and mechanism reviews** are numerous; recent causal analyses remain non-supportive or mixed (Hu; Zhao).

### Search-bounded verdict

- A claim of “first multi-model peptide screen” is **not defensible**.
- A claim of a new AD mechanism is **not defensible**.
- A claim of periodontitis specificity or *P. gingivalis* origin is **not defensible**.
- The defensible contribution is narrower: a **transparent, aggregate-level, hypothesis-generating prioritisation record that integrates reported sequence-evidence filtering with several established predictors and explicitly exposes denominator loss, threshold sensitivity and validation gaps**.
- This is an incremental contribution. It may support a realistic exploratory computational article only if the journal accepts the data-availability limitation.

## 7. Mandatory manuscript consequences

1. Remove AD from the primary title claim; retain it as a bounded motivation and future-test context.
2. Add the 2024–2026 literature above to show current standards and conflicting causal evidence.
3. Explicitly contrast prediction with translation, exposure, toxicity, metal chemistry and disease causality.
4. Describe the study as aggregate-level and hypothesis-generating in title, abstract, last Introduction paragraph and first Discussion paragraph.
5. Do not calculate subject-level p values or use millions of sORFs as independent biological replicates.
6. Make data/code unavailability a front-facing limitation and Data Availability statement, not a buried caveat.

## 8. Coverage boundary

This search is current to 2026-08-12 but not exhaustive. It could miss paywalled, unindexed, Chinese-language, newly corrected/retracted or database-only records. Formal systematic-review claims, citation-count claims and “no prior work exists” claims are prohibited. Retraction/correction status must be rechecked immediately before submission.
