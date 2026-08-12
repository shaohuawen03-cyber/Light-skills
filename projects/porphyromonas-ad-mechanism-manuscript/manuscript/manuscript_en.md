# Computational Prioritization of Periodontitis-Cohort Oral Micropeptides with Predicted Blood–Brain Barrier Permeability, Neurotoxicity, and Metal-Interaction Features Relevant to Alzheimer’s Disease: A Multi-Model In Silico Study

**Article type:** Original Research Article
**Draft status:** Scientific-content draft for author review. Author names, affiliations, correspondence details, and author-approved declarations were not supplied and are intentionally not invented.

## Abstract

**Background:** Periodontitis is associated with cognitive disorders in observational and preclinical literature, but the molecular mediators of this relationship remain uncertain. Small proteins encoded by oral microbial short open reading frames are under-characterized and may provide experimentally tractable candidates. This study aimed to prioritize periodontitis-cohort oral peptides with convergent sequence-based predictions relevant to blood–brain barrier (BBB) permeability, neurotoxicity, and metal interaction.

**Methods:** Aggregate inputs and outputs were obtained from the supplied primary analysis record. That record described 4–50-amino-acid sORFs from an oral metagenomic cohort, exact sequence matching against oral proteomic/reference resources, removal of duplicates, and division into 5–30-amino-acid and 31–50-amino-acid branches. UniDL4BioPep outputs at a model-score threshold of 0.80 were used to identify BBB-high candidates. The periodontitis branch was then evaluated with NTxPred2 for sequences of at least 7 amino acids, mebipred at a threshold of 0.50 for Cu/Fe/Zn-binding potential, and AnOxPePred for chelating (CHEL) and free-radical-scavenging (FRS) scores. Analyses were descriptive; percentages were recomputed from reported aggregate counts.

**Results:** The supplied workflow reported 11,269,961 healthy-branch and 11,721,988 periodontitis-branch sORFs, yielding 31,510 and 33,786 nonredundant evidence-filtered candidates, respectively. BBB-high predictions included 3,359 of 30,557 healthy short peptides (10.99%), 3,446 of 32,754 periodontitis short peptides (10.52%), 40 of 953 healthy long peptides (4.20%), and 72 of 1,032 periodontitis long peptides (6.98%). Downstream periodontitis prioritization therefore comprised 3,518 candidates, of which 3,446 (97.95%) were 5–30 amino acids. NTxPred2 covered 3,299 candidates after 219 sequences shorter than 7 amino acids were excluded; 923 of 3,299 (27.98%) were predicted neurotoxic. The supplied record next reported 111 Cu/Fe/Zn-binding-positive candidates. Of these, 15 had CHEL≥0.25, 12 additionally met FRS<0.50, and 8 met the stricter FRS<0.45 criterion.

**Conclusions:** Sequential model convergence reduced a large periodontitis-cohort sORF space to a 12-candidate operational set and an 8-candidate stricter subset for experimental follow-up. These outputs are prioritization signals, not evidence of brain exposure, neurotoxicity, metal-dependent pro-oxidant activity, taxonomic origin, or Alzheimer’s disease causation. Sequence-level outputs, model provenance, and experimental validation are required before mechanistic claims can be evaluated.

**Keywords:** periodontitis; oral microbiome; micropeptide; short open reading frame; blood–brain barrier; neurotoxicity; metal binding; Alzheimer’s disease; computational prioritization

## 1. Introduction

Small proteins encoded by short open reading frames are routinely under-detected because sequence length complicates both gene calling and experimental annotation. Large-scale analyses of human-associated metagenomes have nevertheless identified thousands of conserved small-protein families, many lacking known domains, and have provided transcriptional or translational evidence for subsets [1]. Oral metagenomic and metatranscriptomic studies further show that periodontitis is associated with altered species-level activity in a complex microbial community [2]. These observations motivate systematic analysis of small coding sequences in periodontal microbiomes, while also emphasizing that a predicted sORF is not automatically a translated or functional peptide.

Sequence databases and mass-spectrometry repositories offer complementary evidence. HOMD/eHOMD provides curated oral microbial taxonomic and genomic references [3,4], whereas salivary metaproteomic studies can establish that a peptide sequence has been observed in an oral mass-spectrometry context [5,6]. Such cross-resource matching can reduce an initial search space, but its meaning depends on the source dataset. In particular, prior detection in an oral dataset from another disease or experimental system does not establish expression in the metagenomic cohort being analyzed, nor does it establish periodontitis specificity.

A second challenge is to convert a large candidate set into a tractable validation panel without overstating model outputs. UniDL4BioPep applies pretrained biological-language-model representations within a common deep-learning architecture for peptide bioactivity classification [7]. NTxPred2, mebipred, and AnOxPePred respectively estimate neurotoxicity, sequence-level metal-binding potential, and antioxidant-related chelating/free-radical-scavenging features [8–10]. Convergence across these tools may be useful for ranking, but the tools were trained for different tasks and do not jointly demonstrate a biological mechanism.

Periodontal disease has been associated with cognitive decline, dementia, and Alzheimer’s disease (AD) in observational syntheses, although estimates vary by disease definition, severity, sex, population, and study design [11,12,17]. Oral-bacteria/AD findings are also heterogeneous [13]. Mechanistic studies involving *Porphyromonas gingivalis* and gingipains provide a rationale for investigating oral microbial products [14], but they cannot be transferred to unclassified peptides. Accordingly, this study asked a deliberately narrower question: among periodontitis-branch oral sORF candidates in the supplied analysis, which peptides survive a transparent sequence of BBB, neurotoxicity, metal-binding, CHEL, and FRS prediction filters? The objective was computational prioritization rather than causal or mechanistic validation.

## 2. Materials and Methods

### 2.1 Study design and evidence provenance

This was a secondary computational analysis of public-data-derived sORF candidates, reported at aggregate level in the supplied primary record `材料与方法及结果_机制研究版.docx` (SHA-256: `f4132a02cb9955c808739c3cbf15edd947f6203d577e8586490933a5d2daa4b5`). No new participants, specimens, wet-laboratory experiments, docking, molecular dynamics, or quantum calculations were included in the present study.

The source record identified PRJNA678453 and PRJEB65451 and stated that 296 high-quality metagenome-assembled genomes represented 24 healthy controls and 26 individuals with periodontitis. PRJNA678453 could be linked to a published oral metagenomic/metatranscriptomic study [2]. PRJEB65451 could not be independently resolved during manuscript preparation; its role therefore remains a provenance uncertainty rather than a verified accession claim.

Only aggregate counts, thresholds, and workflow descriptions were available for drafting. Candidate sequences, sample-to-sequence mappings, taxonomic assignments, per-row prediction scores, model-run logs, executable code, and software/database version snapshots were not provided. The analyses reported below reproduce the supplied aggregate record and deterministic percentage calculations, not an independent rerun of the underlying bioinformatics pipeline.

### 2.2 sORF construction and sequence-evidence filtering

According to the supplied record, sample-specific mapping was used to construct healthy and periodontitis sORF libraries, followed by retention of translated sequences 4–50 amino acids long. The raw libraries contained 11,269,961 healthy-branch and 11,721,988 periodontitis-branch sORFs.

The workflow used hash-indexed exact sequence matching against oral sequence/proteomic resources and then removed duplicate sequences. The short-peptide resource set named PXD003151, PXD004319, and PXD026727. PXD004319 contains saliva from participants with periodontitis, dental caries, and oral health [5]. PXD026727 derives from a lung-cancer salivary metaproteomics study [6], and PXD003151 has been described in the oral-dysbiosis/caries-risk context. These heterogeneous datasets can support prior observation in an oral mass-spectrometry context but cannot, by themselves, establish periodontitis-specific expression. The supplied record labeled the 31–50-amino-acid branch as HOMD-derived [3,4]; because HOMD is a sequence/taxonomy resource rather than a mass-spectrometry repository, the exact expression-evidence status of this branch requires clarification.

After filtering and deduplication, the reported healthy and periodontitis candidate sets contained 31,510 and 33,786 sequences. Candidates were analyzed as a short branch (5–30 amino acids; healthy, 30,557; periodontitis, 32,754) and a long branch (31–50 amino acids; healthy, 953; periodontitis, 1,032). Although the initial length filter included 4-amino-acid sequences, the reported downstream branch counts begin at 5 amino acids; the fate of 4-amino-acid sequences was not documented.

### 2.3 Multi-activity prediction with UniDL4BioPep

The supplied workflow used UniDL4BioPep [7] with ESM2-derived sequence representations (`esm2_t6_8M_UR50D`) to score more than 20 peptide-bioactivity classes. A model output of at least 0.80 was treated as an operational high-score threshold for every class. Because model calibration and external validation in the present candidate domain were not available, “high-score” is used here instead of “confirmed high-confidence activity.”

The present article focuses on BBB-related predictions because these defined the input to the downstream prioritization pipeline. The complete reported activity-class counts are retained in Supplementary Tables S1 and S2. Healthy and periodontitis results are descriptive; no hypothesis test, confidence interval, or multiple-testing procedure was reconstructable from the aggregate outputs.

### 2.4 BBB-based periodontitis-branch selection

Candidates with a UniDL4BioPep BBB output of at least 0.80 were retained. The downstream study set was restricted to the periodontitis branch and combined 5–30-amino-acid and 31–50-amino-acid candidates. This restriction creates a disease-branch prioritization set, not a demonstrated disease-specific set, because sequence-level exclusivity and matched differential-abundance analyses were unavailable.

### 2.5 NTxPred2 neurotoxicity prediction

NTxPred2 was used to evaluate candidate neurotoxicity [8]. Per the supplied workflow, this step accepted sequences 7–50 amino acids long. Sequences of 5–6 amino acids were therefore not classified by NTxPred2 and were retained as “not evaluated,” not as neurotoxicity-negative. The reported model output was dichotomized as neurotoxic or non-neurotoxic.

### 2.6 Metal-binding and antioxidant-feature prediction

The workflow next used mebipred with a threshold of 0.50 to prioritize sequences with predicted Cu-, Fe-, or Zn-binding potential [9]. A positive result was interpreted only as sequence-level metal-binding potential; it supplied no binding constant, stoichiometry, residue-level site, oxidation-state preference, or coordination geometry. The supplied narrative positions this step after the NTxPred2-positive set, but no row-level handoff file was available to independently audit the precise mebipred input denominator.

Mebipred-positive candidates were evaluated with AnOxPePred [10]. Chelating score (CHEL) and free-radical-scavenging score (FRS) files were merged by sequence identifier according to the supplied workflow. Three prespecified operational outputs were summarized: CHEL≥0.25; CHEL≥0.25 plus FRS<0.50 (main set); and CHEL≥0.25 plus FRS<0.45 (stricter subset). These thresholds were prioritization rules in the supplied analysis and were not experimentally calibrated in the current cohort. In particular, high CHEL with lower predicted FRS does not establish metal-dependent pro-oxidant activity.

### 2.7 Descriptive analysis

Counts were transcribed from the primary aggregate record. Percentages were recomputed as 100×n/N using Python standard-library arithmetic and rounded to two decimal places in narrative text. No row-level uncertainty estimate, group-comparison test, effect size, receiver-operating-characteristic analysis, or correction for correlated model outputs could be performed.

## 3. Results

### 3.1 Candidate reduction before functional prediction

The healthy and periodontitis branches began with 11,269,961 and 11,721,988 sORFs, respectively. Evidence filtering and deduplication yielded 31,510 healthy candidates (0.2796% of the raw healthy library) and 33,786 periodontitis candidates (0.2882% of the raw periodontitis library). These proportions describe pipeline retention and were not compared inferentially.

**Table 1. Candidate libraries and BBB-high model outputs**

| Branch | Raw sORFs | Evidence-filtered candidates | Short background (5–30 aa) | BBB-high short, n (%) | Long background (31–50 aa) | BBB-high long, n (%) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 30,557 | 3,359 (10.99) | 953 | 40 (4.20) |
| Periodontitis | 11,721,988 | 33,786 | 32,754 | 3,446 (10.52) | 1,032 | 72 (6.98) |

### 3.2 Descriptive multi-activity profiles

At the 0.80 output threshold, the short branches contained large predicted-positive fractions for several activity classes. For example, the antimicrobial-activity model labeled 30,537 of 30,557 healthy short candidates (99.93%) and 32,721 of 32,754 periodontitis short candidates (99.90%). The corresponding BBB counts were 3,359 (10.99%) and 3,446 (10.52%); NeuroPred counts were 3,876 (12.68%) and 4,019 (12.27%). Such high prevalences, particularly for antimicrobial activity, should be interpreted as model-output distributions in this sequence domain rather than measured biological prevalence.

In the long branch, BBB-high predictions comprised 40 of 953 healthy candidates (4.20%) and 72 of 1,032 periodontitis candidates (6.98%). NeuroPred outputs were positive for 82 healthy candidates (8.60%) and 77 periodontitis candidates (7.46%), whereas antimicrobial outputs were positive for 206 (21.62%) and 238 (23.06%). Full class-by-class counts are provided in the supplementary tables. No claim of enrichment or between-group difference was made because row-level predictions and inferential analyses were unavailable.

### 3.3 Composition of the periodontitis BBB-high set

Combining the two length branches produced 3,518 periodontitis BBB-high candidates: 3,446 short peptides (97.95%) and 72 long peptides (2.05%). Among the short candidates, 547 (15.87%) were 5–7 amino acids long, 2,893 (83.95%) were 8–15 amino acids long, and 6 (0.17%) were 16–30 amino acids long. All 72 long candidates were 31–50 amino acids long. Thus, the downstream set was dominated numerically by 8–15-amino-acid sequences.

### 3.4 Sequential neurotoxicity, metal-binding, CHEL, and FRS prioritization

NTxPred2 covered 3,299 of the 3,518 BBB-high candidates. The remaining 219 (6.23%) were shorter than 7 amino acids and were not evaluated in that model step. Of the covered candidates, 923 of 3,299 (27.98%) were classified as neurotoxic; the source record stated that all 923 were 30 amino acids or shorter.

The supplied record next reported 111 candidates positive for Cu/Fe/Zn-binding potential at the mebipred threshold. Because the row-level handoff was absent, a percentage relative to the preceding 923 candidates is intentionally not reported. Within the 111 reported metal-binding-positive candidates, 15 (13.51%) had CHEL≥0.25. Twelve of 111 (10.81%) also met FRS<0.50 and constituted the operational main set; 8 of 111 (7.21%) met the stricter FRS<0.45 criterion.

**Table 2. Periodontitis-branch prioritization funnel**

| Stage | Operational rule | Reported count | Denominator note |
| --- | --- | ---: | --- |
| BBB-high short peptides | UniDL4BioPep BBB output ≥0.80; 5–30 aa | 3,446 | 32,754 short candidates |
| BBB-high long peptides | UniDL4BioPep BBB output ≥0.80; 31–50 aa | 72 | 1,032 long candidates |
| BBB-high combined set | Union of the two length branches | 3,518 | Downstream periodontitis set |
| NTxPred2 evaluated | Stated input range 7–50 aa | 3,299 | 219 sequences <7 aa not evaluated |
| Predicted neurotoxic | NTxPred2 positive | 923 | 3,299 evaluated |
| Reported Cu/Fe/Zn-binding positive | mebipred output ≥0.50 | 111 | Exact handoff denominator not independently auditable |
| CHEL-prioritized | CHEL≥0.25 | 15 | 111 metal-binding-positive candidates |
| Main operational set | CHEL≥0.25 and FRS<0.50 | 12 | 111 metal-binding-positive candidates |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | 111 metal-binding-positive candidates |

![Figure 1. Aggregate computational prioritization funnel.](figures/prioritization_funnel.png)

**Figure 1.** Aggregate computational prioritization funnel. The figure summarizes reported counts and operational thresholds; it does not imply experimental confirmation or a validated causal mechanism.

## 4. Discussion

### 4.1 Principal findings

This multi-model workflow reduced more than 11.7 million periodontitis-branch sORFs to 33,786 nonredundant evidence-filtered candidates, 3,518 BBB-high predictions, 923 NTxPred2-positive candidates among 3,299 eligible sequences, 111 reported Cu/Fe/Zn-binding-positive candidates, a 12-candidate main set, and an 8-candidate stricter subset. The practical contribution is not a demonstrated AD mechanism; it is a transparent candidate-reduction scheme that can be challenged experimentally.

The length distribution is notable for validation planning. More than four fifths of the BBB-high short branch was 8–15 amino acids long, a range amenable to chemical synthesis and systematic sequence perturbation. Conversely, the 31–50-amino-acid branch was small and may have different structural behavior. These branches should not automatically share the same experimental assay conditions or structural-modeling assumptions.

### 4.2 What cross-model convergence does—and does not—mean

Cross-model agreement can improve operational tractability by requiring candidates to satisfy several independently defined criteria. It does not convert correlated sequence-derived features into orthogonal biological evidence. UniDL4BioPep, NTxPred2, mebipred, and AnOxPePred differ in training data, labels, applicability domains, and output semantics [7–10]. Short, compositionally unusual oral peptides may be outside one or more training domains. The near-universal antimicrobial prediction in the short branches further suggests that calibration and domain-shift checks are needed before interpreting model-positive prevalence biologically.

NTxPred2 non-coverage also creates a structural missingness problem: 219 BBB-high candidates were not tested because of length. They cannot be assumed non-neurotoxic, and the final pipeline preferentially represents sequences accepted by the model. A future analysis should either validate an alternative method for 5–6-amino-acid peptides or keep a parallel unclassified track through experimental screening.

### 4.3 Periodontitis and AD relevance

Meta-analyses support an observational association between periodontal disease and cognitive outcomes, but pooled estimates vary with disease severity, classification, demographic composition, and study design [11,12,17]. A clinical synthesis of oral bacteria and AD also found inconsistent microbiome-wide patterns [13]. Therefore, “AD-relevant” in this study denotes a follow-up rationale based on predicted BBB, neurotoxicity, and metal-interaction features; it does not denote an AD biomarker, risk factor, or causal agent.

Work on *P. gingivalis* and gingipains has sharpened interest in oral microbial products and neurodegeneration [14]. However, the present candidates lacked species-level assignments. They must not be described as *P. gingivalis*-derived. Current reviews also emphasize that direct human causality remains unproven and that mechanistic or therapeutic signals from preclinical studies have not yet produced a definitive clinical pathway [15]. Taxonomic assignment, cohort-level abundance, and direct functional assays are prerequisites for connecting any candidate to a periodontal organism or AD phenotype.

### 4.4 Interpreting metal-binding, CHEL, and FRS outputs

Metal dyshomeostasis and oxidative stress are biologically relevant to AD, which makes Cu/Fe/Zn-related prioritization reasonable. Nonetheless, mebipred predicts metal-binding potential from sequence and does not identify affinity, oxidation-state preference, or coordination chemistry [9]. AnOxPePred was developed to estimate antioxidative properties, including chelating and free-radical-scavenging features [10]. Consequently, the combination CHEL≥0.25 and FRS<0.50 should be read only as an operational pattern: predicted chelating potential without a comparably high predicted scavenging score.

A pro-oxidant interpretation requires direct evidence. At minimum, synthesized candidates should be tested for Cu/Fe/Zn binding using orthogonal biophysical assays; metal-dependent ROS generation; lipid peroxidation; redox cycling; and neuronal-cell injury, with peptide-only, metal-only, scrambled-sequence, positive, and negative controls. Demonstrating binding without oxidative injury would not establish the proposed mechanism; demonstrating oxidative injury without metal dependence would support a different mechanism.

### 4.5 Future structural and functional studies

The AChE–Aβ literature provides one possible structural follow-up path. A published microsecond-scale AChE–Aβ simulation reported persistent Aβ residence near AChE residues 344–361 [16]. This result can guide a future region-of-interest analysis but does not predict that the present peptides bind AChE, Aβ, or that interface. Candidate-specific docking should follow multi-conformer peptide generation, use controls and ensemble receptor states, and be validated by molecular dynamics and experiment rather than presented as a stand-alone mechanism.

A staged validation program is preferable: (1) sequence and spectrum-level confirmation; (2) taxonomic assignment and cohort-resolved abundance; (3) BBB transport or permeability assays; (4) neuronal toxicity and metal-dependent oxidative assays; (5) Aβ aggregation and AChE/BChE functional assays; and only then (6) target-specific structural studies. This sequence separates candidate identity, exposure, phenotype, mechanism, and structural explanation.

### 4.6 Strengths and limitations

The principal strength is an explicit, auditable count-based funnel that separates model eligibility from model positivity and preserves a stricter sensitivity subset. The study also avoids treating lower FRS as direct evidence of pro-oxidant activity and separates completed predictions from future docking or experimental work.

The limitations are substantial. First, no candidate sequences or row-level scores were available, preventing independent reproduction, overlap analysis, calibration, taxonomic attribution, spectrum review, or assessment of duplicate leakage across datasets. Second, model versions, access dates, code, random seeds, and database snapshots were absent. Third, PRJEB65451 could not be independently verified. Fourth, the short-peptide evidence resources include caries-risk and lung-cancer oral datasets; exact matching to those resources is not disease-specific expression evidence. Fifth, the long branch is described as HOMD-derived even though the combined set is called proteomics-supported, leaving its evidence class ambiguous. Sixth, the exact denominator entering mebipred could not be reconstructed. Seventh, only aggregate descriptive counts were available, so no inferential group comparison or uncertainty estimate was possible. Finally, every endpoint was computational; no BBB, toxicology, metal-binding, oxidative, enzymatic, aggregation, animal, or clinical validation was supplied.

## 5. Conclusions

A sequential sequence-based workflow prioritized 12 periodontitis-branch oral peptide candidates and an 8-candidate stricter subset from a large reported sORF search space. The result is a testable shortlist, not a validated pathway linking periodontitis to AD. Releasing the row-level sequence and score matrix, resolving data provenance, and performing staged biochemical and cellular validation are necessary before claims about brain exposure, neurotoxicity, metal-mediated oxidative injury, microbial origin, target binding, or AD relevance can be strengthened.

## Declarations

### Ethics statement

The present work used aggregate descriptions of secondary public-data-derived computational analyses and involved no new recruitment, intervention, specimen collection, or access to identifiable participant data in the materials available for drafting. Whether formal ethics review or an exemption statement is required must be confirmed by the accountable authors and their institution before submission; no approval number is inferred here.

### Consent for publication

No individual-level or identifiable participant material is included in this draft.

### Data availability

The supplied workflow names PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727, and HOMD/eHOMD. PRJNA678453, PXD004319, PXD026727, and HOMD/eHOMD were linked to public records during drafting; PRJEB65451 remains unresolved. The sequence-level inputs and outputs, sample-to-sequence map, spectra, taxonomic assignments, per-model scores, and final candidate sequences were not present in the supplied package. Full independent reproduction is therefore not possible from this draft package alone. These artifacts should be deposited in a persistent repository before submission.

### Code availability

No executable analysis code for the original sORF discovery, sequence matching, deduplication, or model runs was supplied. The repository contains only scripts used to extract the source documents, recompute aggregate percentages, verify file checksums, generate the figure, and build the DOCX draft. The original analysis code and environment lockfile should be archived before submission.

### Funding

Funding information was not provided to the drafting workflow. The accountable authors must supply and verify the final funding statement.

### Competing interests

A competing-interests declaration was not provided. Each accountable author must submit an author-approved declaration before journal submission.

### Author contributions

Author identities and contributions were not supplied. CRediT roles and final approval must be completed by the named human authors; no authorship is inferred from file provenance.

### Use of generative AI

A generative-AI assistant was used to organize the supplied materials, draft bilingual scientific text, perform deterministic arithmetic checks, and support language editing. The assistant was not treated as an author. Human authors remain responsible for verifying every datum, citation, interpretation, translation, declaration, and journal-policy requirement, and should adapt this disclosure to the target journal’s current policy.

## References

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
3. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
4. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database (eHOMD): a resource for the microbiome of the human aerodigestive tract. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
5. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
6. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
7. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
8. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
9. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
10. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
11. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders: systematic review and meta-analysis. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
12. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis—a systematic review and meta-analysis of evidence from observational studies. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
13. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease: a systematic review and meta-analysis. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
14. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains: evidence for disease causation and treatment with small-molecule inhibitors. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
15. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
16. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
17. Kim J, Han DH. Periodontitis as a risk factor for dementia: a systematic review and meta-analysis. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
