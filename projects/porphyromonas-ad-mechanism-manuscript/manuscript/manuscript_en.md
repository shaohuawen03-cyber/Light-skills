# Evidence-Bounded Multi-Model Prioritization of Periodontitis-Cohort Oral Micropeptides with Predicted Blood–Brain Barrier Penetration, Neurotoxicity, and Metal-Interaction Features: An Aggregate-Level In Silico Study

**Article type:** Original Research Article  
**Draft status:** Submission-oriented scientific-content draft for accountable-author review. Author names, affiliations, correspondence details, journal-specific formatting, and author-approved declarations were not supplied and are not inferred.

## Abstract

**Background:** Microbiome small open reading frames (smORFs) are incompletely characterized. Serial sequence predictors can reduce large candidate spaces, but cannot establish translation, exposure, toxicity, mechanism, or disease causality. We reconstructed and audited an aggregate workflow that prioritized oral smORF-derived candidates from a periodontitis cohort branch.

**Methods:** The principal source supplied aggregate counts, thresholds, and workflow descriptions for 4–50-amino-acid sORFs. UniDL4BioPep output ≥0.80 defined a blood–brain barrier (BBB)-high set, followed by NTxPred2, mebipred (threshold 0.50), and AnOxPePred chelating (CHEL)/free-radical-scavenging (FRS) outputs. Analyses were descriptive. Sequences, subject/sample mappings, row-level scores, and original code were unavailable; the primary pipeline was not rerun.

**Results:** The source reported 11,269,961 healthy-branch and 11,721,988 periodontitis-branch sORFs, reduced to 31,510 and 33,786 evidence-filtered candidates. BBB-high outputs were 3,359/30,557 (10.99%) and 3,446/32,754 (10.52%) in healthy and periodontitis short branches, and 40/953 (4.20%) and 72/1,032 (6.98%) in long branches. The 3,518-candidate periodontitis set was 97.95% short. NTxPred2 evaluated 3,299 candidates; 219 were outside its length range and 923/3,299 (27.98%) evaluated candidates were positive. The source next reported 111 metal-binding-positive candidates: 15 (13.51%) met CHEL≥0.25, 12 (10.81%) also met FRS<0.50, and 8 (7.21%) met FRS<0.45.

**Conclusions:** The workflow provides an auditable aggregate reduction record and source-reported 12-candidate main set with an 8-candidate stricter subset. It establishes neither disease specificity nor experimental activity. Candidate identities and row-level provenance must be released before synthesis, validation, or neurodegenerative interpretation.

**Keywords:** oral microbiome; small open reading frame; micropeptide; periodontitis; blood–brain barrier; neurotoxicity prediction; metal-binding prediction; aggregate analysis; hypothesis generation

## 1. Introduction

Small open reading frames are frequently missed or misannotated because short coding sequences are difficult to distinguish from chance ORFs and are poorly represented in conventional annotation pipelines. Large-scale human-microbiome analyses nevertheless indicate that smORFs encode a substantial and incompletely characterized small-protein space [1]. Methodological work has since combined profile hidden Markov models, deep learning, evolutionary information, and ribosome-profiling evidence to improve annotation [2]. More recently, high-resolution multi-omics has integrated smORF prediction with metatranscriptomics and deep metaproteomic detection [3]. Together, these studies support smORFs as a legitimate discovery space while making clear that a predicted ORF is not automatically a translated or functional peptide.

Periodontitis is accompanied by ecological and functional changes in the oral microbiome. Paired metagenomic and metatranscriptomic studies have identified compartment- and species-specific activity associated with periodontitis [4], and a cross-study metatranscriptome analysis has demonstrated the value of subject/sample-resolved data, normalization, and false-discovery control [5]. Sequence resources such as HOMD/eHOMD provide curated oral microbial references [6,7], whereas metaproteomic datasets provide context-dependent evidence of peptide detection [8,9]. Dedicated oral metaproteomic workflows now emphasize host depletion, microbial enrichment, peptide- and protein-level false-discovery control, taxonomic assignment, and raw-data deposition [10]. Exact matching to these resources can narrow a search space, but a match from another cohort or disease context does not establish expression or disease specificity in the cohort under analysis.

A second challenge is to prioritize a tractable validation set without converting model outputs into biological claims. UniDL4BioPep provides a common deep-learning architecture for multiple peptide-bioactivity labels [11]. The BBB-peptide prediction literature illustrates both the utility and the limitations of this approach: available positive sets are modest, class imbalance is common, and different models can trade sensitivity against specificity [12,13]. NTxPred2, mebipred, and AnOxPePred respectively estimate sequence-based neurotoxicity, metal-binding potential, and antioxidant-related chelating/free-radical-scavenging features [14–16]. Because these models use overlapping sequence-derived information, serial agreement is useful for operational ranking but does not constitute independent biological confirmation. Stronger microbiome-peptide discovery studies have followed computational prioritization with synthesis and functional assays [17].

Neurodegenerative disease provides one possible downstream context for BBB-, toxicity-, and metal-related hypotheses, but the causal evidence must be represented accurately. Observational syntheses have reported associations between periodontitis and cognitive disorders, with effect estimates varying by disease definition, severity, population, and study design [18,19,22]. Clinical oral-bacteria findings are also heterogeneous [20]. Experimental work involving *Porphyromonas gingivalis* supports biological plausibility for selected pathogen-derived products [21], but cannot be transferred to taxonomically unassigned peptides. Recent Mendelian-randomization analyses found no convincing genetic causal relationship between periodontal disease and Alzheimer’s disease (AD) [23], and a 2026 synthesis of Mendelian-randomization studies likewise found no substantial causal association with AD [24]. Current reviews therefore retain biological plausibility while recognizing that direct human causality remains unproven [25].

Against this background, the present study asks a bounded question: how does the source-reported combination of sequence-evidence filters and established peptide predictors reduce an aggregate periodontitis-cohort oral sORF candidate space, which candidate-feature combinations remain at each threshold, and which interpretations remain untested? The contribution is a transparent descriptive reconstruction and statistical/claim audit. It is not a new predictor, a healthy-versus-periodontitis association test, or a validated disease mechanism.

## 2. Materials and Methods

### 2.1 Study design, principal source, and scope

This study is an aggregate-level descriptive reconstruction of a source-reported computational analysis. The sole source of study methods, thresholds, and results was `材料与方法及结果_机制研究版.docx` (SHA-256: `f4132a02cb9955c808739c3cbf15edd947f6203d577e8586490933a5d2daa4b5`). The corresponding PDF was retained as an original file but was not independently parsed page by page in the drafting environment. Contextual documents did not supply study results.

The principal record named PRJNA678453 and PRJEB65451 and stated that 296 high-quality metagenome-assembled genomes represented 24 healthy participants and 26 participants with periodontitis. PRJNA678453 could be linked to a published oral metagenomic/metatranscriptomic study [4]. PRJEB65451 could not be independently resolved during drafting and is retained as an unresolved provenance element rather than represented as verified metadata.

No new participant recruitment, specimen collection, wet-laboratory experiment, docking, molecular dynamics, or clinical analysis was performed. Only aggregate counts, thresholds, and narrative workflow descriptions were available. Candidate nucleotide/amino-acid sequences, genomic coordinates, sample-to-sequence mappings, taxonomic assignments, peptide-spectrum matches, row-level model scores, run logs, random seeds, database snapshots, and original executable code were not supplied. Accordingly, the present analysis audits aggregate arithmetic and reporting boundaries; it does not independently reproduce the primary bioinformatics workflow.

### 2.2 Source-reported sORF construction and sequence-evidence filtering

According to the principal record, sample-specific mapping was used to construct healthy and periodontitis sORF libraries, after which translated sequences 4–50 amino acids long were retained. The raw healthy and periodontitis libraries contained 11,269,961 and 11,721,988 sORFs, respectively.

The workflow then used hash-indexed exact sequence matching against named oral sequence/proteomic resources and removed duplicate sequences. The short-candidate resource set included PXD003151, PXD004319, and PXD026727. PXD004319 contains salivary samples from individuals with periodontitis, dental caries, and oral health [8]. PXD026727 is a lung-cancer oral metaproteomics dataset [9]. PXD003151 has been used in an oral dysbiosis/caries-risk context. These resources may support prior observation of an exact sequence in a named oral dataset, but they cannot by themselves establish expression in the metagenomic cohort or periodontitis specificity. The source labelled the 31–50-amino-acid branch as HOMD-derived [6,7]. Because HOMD/eHOMD are sequence/taxonomy resources rather than mass-spectrometry repositories, the expression-evidence status of this branch remains ambiguous.

After source-reported evidence filtering and deduplication, 31,510 healthy candidates and 33,786 periodontitis candidates remained. These totals were divided into short (5–30 amino acids: healthy, 30,557; periodontitis, 32,754) and long (31–50 amino acids: healthy, 953; periodontitis, 1,032) branches. Although the initial rule included 4-amino-acid sequences, downstream branches began at 5 amino acids; the disposition of 4-amino-acid sequences was not documented.

### 2.3 Multi-activity and BBB-related prediction

The source reported use of UniDL4BioPep [11] with ESM2-derived sequence representations (`esm2_t6_8M_UR50D`) to score more than 20 peptide-bioactivity classes. An output of at least 0.80 was used as a common operational high-score threshold. No calibration or external validation specific to the present sequence domain was available. We therefore use "model-positive" or "high-output", not "confirmed activity" or "probability".

The BBB-related output defined the downstream candidate set. Counts from healthy and periodontitis branches were retained for descriptive orientation, but no between-group hypothesis was tested. Restricting later steps to the periodontitis branch creates a periodontitis-cohort prioritization set, not a demonstrated periodontitis-specific set.

### 2.4 Neurotoxicity, metal-binding, and CHEL/FRS prioritization

The periodontitis BBB-high set was next evaluated with NTxPred2 [14]. The source described an accepted sequence range of 7–50 amino acids. Candidates below this range were classified as not evaluated, not as negative. NTxPred2 outputs were summarized as predicted positive or negative among eligible candidates.

The source narrative subsequently described mebipred analysis at an output threshold of 0.50 for Cu-, Fe-, or Zn-binding potential [15]. Mebipred predicts sequence-level metal-binding potential; it does not provide a binding constant, ion-specific stoichiometry, residue-level site, oxidation-state preference, or coordination geometry. Although the narrative places this step after the NTxPred2-positive set, no row-level handoff file was available. The count of 111 is therefore reported as a source-reported downstream result, and 111/923 is not treated as an independently audited transition rate.

Mebipred-positive candidates were evaluated with AnOxPePred [16]. According to the source, chelating (CHEL) and free-radical-scavenging (FRS) files were joined by sequence identifier. Three operational outputs were retained: CHEL≥0.25; CHEL≥0.25 with FRS<0.50 (main set); and CHEL≥0.25 with FRS<0.45 (stricter subset). These cutoffs were source-prespecified ranking rules, not experimentally calibrated clinical or mechanistic thresholds. In particular, high predicted CHEL with lower predicted FRS does not establish pro-oxidant activity.

### 2.5 Descriptive statistics and reproducibility audit

Counts were transcribed from the principal record. Percentages were deterministically recomputed as 100×n/N with the denominator stated for each quantity. Candidate sequences were units of computational accounting, not independent biological replicates. Because sample-to-candidate mappings and row-level participant outcomes were unavailable, no p value, confidence interval, effect estimate, power analysis, receiver-operating-characteristic analysis, or multiple-testing correction was calculated for healthy-versus-periodontitis comparisons.

Arithmetic and monotonicity checks were implemented in Python standard-library code (`scripts/stage5_statistics_audit.py`). Prespecified checks required branch counts to sum to their evidence-filtered totals, model-positive counts not to exceed their denominators, NTxPred2 evaluated and non-evaluated counts to sum to the BBB-high total, and downstream threshold counts to be nested. The stricter FRS threshold was treated as the only reconstructable threshold-sensitivity contrast.

## 3. Results

### 3.1 Candidate-space reduction and branch accounting

The source-reported healthy and periodontitis branches began with 11,269,961 and 11,721,988 sORFs. Evidence filtering and deduplication retained 31,510 healthy candidates (0.2796% of the raw healthy library) and 33,786 periodontitis candidates (0.2882% of the raw periodontitis library). The short and long branch counts summed exactly to their respective evidence-filtered totals. These values describe computational retention; they are not participant-level rates.

**Table 1. Aggregate candidate libraries and BBB-high outputs**

| Branch | Raw sORFs | Evidence-filtered candidates | Short background (5–30 aa) | BBB-high short, n (%) | Long background (31–50 aa) | BBB-high long, n (%) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 30,557 | 3,359 (10.99) | 953 | 40 (4.20) |
| Periodontitis | 11,721,988 | 33,786 | 32,754 | 3,446 (10.52) | 1,032 | 72 (6.98) |

### 3.2 Descriptive BBB and multi-activity outputs

BBB-high outputs comprised 3,359/30,557 healthy short candidates (10.99%) and 3,446/32,754 periodontitis short candidates (10.52%). In the long branches, the corresponding counts were 40/953 (4.20%) and 72/1,032 (6.98%). These side-by-side percentages were not tested inferentially.

The supplementary activity tables preserve all source-reported UniDL4BioPep class counts. One notable output-distribution feature was the antimicrobial label in the short branches: 30,537/30,557 healthy candidates (99.93%) and 32,721/32,754 periodontitis candidates (99.90%) were model-positive at the common 0.80 threshold. The near-universal output is not interpreted as measured biological prevalence; instead, it highlights the need for task- and domain-specific calibration before using model-positive proportions biologically.

### 3.3 Periodontitis-branch downstream prioritization

Combining 3,446 short and 72 long BBB-high outputs yielded 3,518 periodontitis-branch candidates. The short branch contributed 97.95% (3,446/3,518). Within the source-reported short-candidate length summary, 547 were 5–7 amino acids, 2,893 were 8–15 amino acids, and 6 were 16–30 amino acids; all 72 long candidates were 31–50 amino acids.

NTxPred2 evaluated 3,299/3,518 candidates (93.77%). The remaining 219 candidates (6.23%) were below the stated accepted length range and were not evaluated. Among evaluated candidates, 923/3,299 (27.98%) were predicted positive. The source stated that all 923 were no longer than 30 amino acids.

The source next reported 111 candidates positive for Cu/Fe/Zn-binding potential at the mebipred threshold. Within that source-reported set, 15/111 (13.51%) had CHEL≥0.25. Twelve of 111 (10.81%) additionally met FRS<0.50, and 8/111 (7.21%) met the stricter FRS<0.45 rule. Tightening FRS from <0.50 to <0.45 retained 8/12 (66.67%) of the main set and removed four candidates. Candidate identities could not be listed because the corresponding sequences were absent.

**Table 2. Aggregate periodontitis-branch prioritization record**

| Stage | Operational rule | Reported count | Denominator/evidence note |
| --- | --- | ---: | --- |
| BBB-high short | UniDL4BioPep BBB output ≥0.80; 5–30 aa | 3,446 | 32,754 short candidates |
| BBB-high long | UniDL4BioPep BBB output ≥0.80; 31–50 aa | 72 | 1,032 long candidates |
| BBB-high combined | Union of length branches | 3,518 | Periodontitis downstream set |
| NTxPred2 evaluated | Accepted range 7–50 aa | 3,299 | 219 not evaluated |
| NTxPred2 predicted positive | Model-positive | 923 | 3,299 evaluated |
| Metal-binding positive | mebipred output ≥0.50 | 111 | Source-reported downstream count; row-level handoff unavailable |
| CHEL-prioritized | CHEL≥0.25 | 15 | 111 source-reported metal-positive candidates |
| Main operational set | CHEL≥0.25 and FRS<0.50 | 12 | 111 source-reported metal-positive candidates |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | 111 source-reported metal-positive candidates |

![Figure 1. Evidence-bounded aggregate computational prioritization.](figures/prioritization_funnel.png)

**Figure 1.** Evidence-bounded aggregate computational prioritization. Counts and operational thresholds were transcribed from the principal source record. Healthy-branch values are descriptive context only. The dashed transition indicates that the row-level handoff to mebipred was unavailable; 111/923 is therefore not presented as an audited transition rate. The 12-candidate main set and 8-candidate stricter subset are source-reported predictions, not experimentally validated peptides.

## 4. Discussion

### 4.1 Principal finding and bounded contribution

This study reconstructs a source-reported funnel from more than 11.7 million periodontitis-branch sORFs to 33,786 evidence-filtered candidates, 3,518 BBB-high outputs, 923 NTxPred2-positive outputs among 3,299 eligible candidates, 111 source-reported metal-binding-positive candidates, a 12-candidate main set, and an 8-candidate stricter subset. The arithmetic is internally consistent, and the funnel makes eligibility, positivity, non-evaluation, threshold sensitivity, and a missing row-level handoff explicit.

The contribution is nevertheless narrow. Serial use of established tools is not methodological innovation equivalent to a new predictor, and the aggregate record cannot support participant-level association. Most importantly, “12 candidates” is currently a count, not an actionable candidate table: the source package does not contain their sequences or scores. The present endpoint is therefore a transparent hypothesis-generation record rather than a validated discovery claim.

### 4.2 Position relative to current smORF and oral-omics standards

Contemporary smORF studies combine complementary computational evidence with direct translation or proteomic measurements [1–3]. Durrant and Bhatt assessed enrichment for Ribo-seq/MetaRibo-seq signals rather than relying only on classifier agreement [2]. Davin et al. integrated smORF prediction with sample-resolved metatranscriptomics and deep metaproteomics [3]. In oral metaproteomics, Yuan et al. used microbial enrichment, explicit false-discovery control, taxonomic assignment, and deposited raw mass-spectrometry data [10]. Torres et al. illustrate a different but equally important principle: computationally prioritized microbiome peptides were synthesized and functionally tested before biological activity was claimed [17].

The present record does not meet those validation standards because it lacks sequence-level evidence, spectra, subject/sample mapping, and experiments. Exact matching to heterogeneous oral datasets remains useful as a search-space filter, but prior detection in a caries-risk, mixed oral-status, or lung-cancer dataset is not evidence of expression in the present periodontitis cohort. Likewise, a HOMD match is sequence/taxonomic evidence, not mass-spectrometric confirmation. These distinctions should guide both peer-review interpretation and any future reconstruction of the pipeline.

### 4.3 Why aggregate group counts are not comparative statistics

The healthy and periodontitis candidate percentages are deterministic summaries of two computational branches. Peptides within a participant, homologous sequences across participants, and candidates produced by the same assembly are likely correlated. The millions of raw sORFs and tens of thousands of filtered candidates therefore cannot be treated as independent biological replicates. A nominal test using candidate counts would create pseudoreplication and an artificially large effective sample size.

A valid healthy-versus-periodontitis analysis would require participant/sample identifiers, a prespecified unit-level outcome, common processing denominators, candidate clustering/deduplication rules, and a statistical model that accounts for repeated sequences and participant-level covariates. None of these data were supplied. The descriptive differences in Table 1 consequently support no claim of enrichment, depletion, prevalence, risk, or disease specificity.

### 4.4 Interpretation of serial predictor outputs

Cross-model filtering can improve operational tractability, but it does not turn correlated sequence descriptors into orthogonal evidence. UniDL4BioPep, NTxPred2, mebipred, and AnOxPePred were trained for different labels and have different applicability domains [11,14–16]. BBB-prediction studies themselves report challenges arising from small positive sets, class imbalance, threshold choices, and external-validation performance [12,13]. Short or compositionally unusual microbial candidates may differ from training distributions. The near-universal short-branch antimicrobial output further cautions against interpreting a common threshold as uniformly calibrated across tasks.

Model compatibility also structures the final set. The 219 BBB-high candidates outside the NTxPred2 length range are not negative; they are unclassified by that step. Downstream candidates are thus selected not only for predicted properties but also for acceptance by each model. Without row-level scores, alternative predictors, calibration data, or threshold curves, rank stability and domain shift cannot be quantified.

Metal-related outputs require similarly restrained language. Mebipred estimates binding potential rather than affinity or coordination chemistry [15]. AnOxPePred estimates antioxidant-related CHEL and FRS features [16]. CHEL≥0.25 with FRS<0.50 therefore denotes only a source-defined computational pattern. It does not demonstrate metal-dependent reactive-oxygen-species generation or a pro-oxidant mechanism.

### 4.5 Neurodegenerative context without causal overreach

The study did not measure cognition, dementia, AD biomarkers, brain exposure, or an AD-relevant molecular target. Observational meta-analyses can motivate inquiry, particularly where severe periodontitis is associated with dementia outcomes [18,19,22], but heterogeneity and residual confounding limit causal interpretation. Oral-bacteria findings in AD remain inconsistent [20]. Mechanistic results involving *P. gingivalis* cannot establish that unassigned candidates originate from that species [21].

The causal boundary has become more important as genetic analyses have matured. Hu et al. reported no convincing genetic causal relationship between periodontal disease and AD in two-sample Mendelian-randomization analyses [23]. Zhao et al. reached a similar overall conclusion for AD in a 2026 systematic review and meta-analysis of Mendelian-randomization studies [24]. These findings do not exclude every non-genetic biological pathway, but they rule out presenting the present computational pattern as support for established periodontitis-to-AD causation. Here, BBB, toxicity, and metal-interaction labels define possible follow-up questions only.

### 4.6 Evidence ladder and future validation

The most immediate requirement is not a complex disease experiment; it is recovery and release of candidate identities, row-level scores, and provenance. Sequence identity is needed to inspect duplicates, assign taxonomy, assess model applicability, reproduce predictions, and synthesize candidates. Translation/expression should then be tested with cohort-matched metatranscriptomics, ribosome profiling, or false-discovery-controlled targeted metaproteomics. Only expression-confirmed candidates should advance to BBB transport/permeability assays and neuronal toxicity tests.

Metal-related hypotheses require orthogonal binding measurements, ion-specific competition, stoichiometry/affinity estimation, metal-dependent reactive-oxygen-species assays, and appropriate peptide-only, metal-only, scrambled-sequence, positive, and negative controls. Disease-related experiments should be considered only after identity, exposure, phenotype, and biochemical mechanism are established. This ordering prevents later-stage plausibility from being used to compensate for missing earlier-stage evidence.

![Figure 2. Evidence ladder for interpretation.](figures/evidence_ladder.png)

**Figure 2.** Evidence ladder for interpretation. The current source package reaches aggregate computational prioritization only. Candidate identities and row-level scores are unavailable, and translation/expression, BBB transport, cellular toxicity, metal-dependent biochemical effects, and disease association/causality were not tested.

### 4.7 Strengths and limitations

The study’s strengths are transparency and restraint. It provides explicit denominators, distinguishes non-evaluation from negativity, preserves a stricter threshold subset, makes the unauditable handoff visible, and separates prediction from mechanism. All displayed arithmetic can be reproduced with dependency-free code.

The limitations determine the allowable conclusion. First, absent sequences and row-level scores preclude independent reproduction, overlap analysis, calibration, taxonomic attribution, and candidate synthesis. Second, absent participant/sample mapping precludes biological inference and permits no uncertainty estimate for group contrasts. Third, original code, model versions, access dates, database snapshots, and random seeds were not supplied. Fourth, one named BioProject remains unresolved. Fifth, the short-branch evidence resources are heterogeneous, and the long-branch expression-evidence class is ambiguous. Sixth, the mebipred handoff denominator cannot be audited row by row. Seventh, threshold performance and predictor dependence cannot be assessed. Finally, no translational, proteomic, BBB, toxicological, metal-binding, oxidative, animal, or clinical endpoint was measured. These limitations cannot be corrected by statistical or linguistic refinement alone.

## 5. Conclusions

A source-reported serial prediction workflow reduced an aggregate periodontitis-cohort oral sORF space to a 12-candidate main count and an 8-candidate stricter count. The defensible result is an auditable, hypothesis-generating prioritization record—not a disease-specific peptide atlas or validated neurodegenerative mechanism. Release of sequence-level identities, scores, sample mappings, and original code is the minimum next step. Experimental claims should await cohort-matched expression evidence and staged transport, toxicity, and metal-dependent functional validation.

## Declarations

### Ethics statement

The available materials described aggregate secondary computational analyses of public-data-derived sequences and contained no identifiable participant data. No new recruitment, intervention, or specimen collection was conducted for this reconstruction. The accountable authors and their institution must confirm whether the original data use and the proposed submission require ethics approval or an exemption; no approval number is inferred.

### Consent for publication

No identifiable individual material is included in this draft. Any journal-required consent statement must be confirmed by the accountable authors.

### Data availability

The principal record names PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727, and HOMD/eHOMD. PRJNA678453, PXD004319, PXD026727, and HOMD/eHOMD were linked to public records during drafting; PRJEB65451 remains unresolved. Candidate sequences, sample mappings, peptide-spectrum matches, taxonomic assignments, row-level model outputs, and final candidate identities were not included in the supplied package. Consequently, the primary analysis and final shortlist cannot be independently reproduced from this manuscript package. These artifacts should be recovered and deposited in a persistent repository before submission whenever possible.

### Code availability

No executable code for the original sORF discovery, exact matching, deduplication, or predictor runs was supplied. Repository code reproduces document extraction, checksum verification, deterministic aggregate arithmetic, programmatic figures, bilingual assembly, and DOCX packaging only. It must not be represented as the original analysis pipeline.

### Funding

Funding information was not supplied. The accountable authors must provide and verify the final funding statement.

### Competing interests

An author-approved competing-interests statement was not supplied. Each accountable author must complete the journal’s declaration before submission.

### Author contributions

Author identities and contributions were not supplied. CRediT roles, accountability, and final manuscript approval must be completed by the named human authors; authorship is not inferred from file provenance.

### Use of generative AI

A generative-AI assistant supported source organization, bilingual drafting, deterministic arithmetic review, figure scripting, and language editing. It was not used to generate scientific data or to replace accountable author review and is not an author. Human authors must verify every datum, citation, translation, interpretation, and declaration and adapt this disclosure to the target journal’s policy.

## References

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
3. Davin ME, Ortís Sunyer J, Delgado LF, et al. High-resolution multi-omics enhances prediction and detection of smORF-encoded proteins in the human gut microbiome. *Nat Commun*. 2026. doi:10.1038/s41467-026-72762-5.
4. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
5. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
6. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
7. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database (eHOMD): a resource for the microbiome of the human aerodigestive tract. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
8. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
9. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
10. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
11. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
12. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
13. Liu X, Zhao Z, Guan J, et al. Prediction of blood-brain barrier-penetrating peptides using B3BPFN. *Front Mol Biosci*. 2026;13:1858506. doi:10.3389/fmolb.2026.1858506.
14. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
15. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
16. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
17. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
18. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders: systematic review and meta-analysis. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
19. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis—a systematic review and meta-analysis of evidence from observational studies. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
20. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease: a systematic review and meta-analysis. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
21. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains: evidence for disease causation and treatment with small-molecule inhibitors. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
22. Kim J, Han DH. Periodontitis as a risk factor for dementia: a systematic review and meta-analysis. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
23. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
24. Zhao Y, Zhang C, Chang X, et al. Causal association between periodontitis and systemic diseases: a systematic review and meta-analysis of Mendelian randomization studies. *BMC Oral Health*. 2026;26:383. doi:10.1186/s12903-026-07725-9.
25. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
