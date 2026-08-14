# Aggregate Prioritization of Periodontitis-Cohort Oral Micropeptides and a Source-Reported Acetylcholinesterase Docking Follow-up

**Article type:** Interim Original Research Draft  
**Purpose:** Short stage-deliverable for supervisor review; the complete manuscript remains the versioned v3.0.0 package.

## Abstract

**Background:** Small open reading frames (smORFs) represent a poorly characterized component of the oral microbiome. Computational models can prioritize candidate peptides, but their outputs do not establish translation, blood–brain barrier (BBB) transport, toxicity, target binding, or disease causality.

**Methods:** We reconstructed aggregate counts from a periodontitis-cohort oral-smORF screening record. The workflow included evidence filtering, UniDL4BioPep BBB scoring, NTxPred2, mebipred, and AnOxPePred CHEL/FRS thresholds. Percentages were independently recalculated. A separately maintained external v0.4 report supplied twelve peptide sequences and mean±SD AutoDock Vina scores against human acetylcholinesterase (AChE; PDB 4EY6). Sequence composition and score ordering were audited, but docking was not rerun because raw inputs, configurations, logs, and poses were unavailable.

**Results:** Evidence filtering retained 31,510/11,269,961 healthy-branch and 33,786/11,721,988 periodontitis-branch smORFs. The periodontitis branch contained 3,518 BBB-high candidates; NTxPred2 evaluated 3,299 and classified 923 as positive. The source subsequently reported 111 metal-binding-positive candidates, 15 with CHEL≥0.25, 12 with CHEL≥0.25 and FRS<0.50, and 8 with FRS<0.45. The external record listed twelve unique 7–9-aa sequences. Eleven contained histidine, six contained cysteine, and all contained Arg or Lys. Reported Vina means ranged from −9.60 to −8.25 kcal/mol.

**Conclusion:** The combined evidence defines a short, testable candidate set but does not demonstrate periodontitis specificity, brain exposure, neurotoxicity, AChE binding, or an Alzheimer’s disease mechanism. Row-level screening lineage, reproducible docking artefacts, and experimental validation are required.

**Keywords:** oral microbiome; smORF; micropeptide; periodontitis; acetylcholinesterase; molecular docking; computational prioritization

## 1. Introduction

Microbiome smORFs encode a large and incompletely annotated peptide space. Large-scale analyses have identified thousands of conserved small genes, while dedicated prediction systems improve detection of short coding sequences [1,2]. Nevertheless, a predicted smORF is not necessarily translated, and a translated peptide is not necessarily stable or biologically active.

Periodontitis is associated with changes in oral microbial composition and gene expression [3,4]. However, disease-related interpretation requires participant-level mapping, appropriate normalization, and control of repeated or homologous sequences. Exact matching to oral databases or heterogeneous proteomic datasets can support sequence existence, but it cannot independently prove current-cohort expression or periodontitis specificity.

Peptide predictors offer a practical filtering strategy. UniDL4BioPep predicts multiple peptide-activity labels [5]; BBB models estimate sequence patterns associated with penetration [6]; NTxPred2 predicts neurotoxic-peptide labels [7]; mebipred estimates metal-binding potential [8]; and AnOxPePred predicts chelating and free-radical-scavenging features [9]. These outputs are prioritization labels rather than experimental observations. Strong peptide-discovery studies therefore proceed to chemical synthesis and functional assays [10].

An AChE-focused follow-up is biologically interesting because cholinergic dysfunction remains relevant to Alzheimer’s disease (AD) [11], and AChE can accelerate amyloid-β assembly through regions involving the peripheral anionic site (PAS) [12]. Human AChE structure 4EY6 provides a target for structural hypothesis generation [13]. Metal dyshomeostasis is also implicated in AD-related aggregation and oxidative biology [14]. These observations motivate experiments, but they do not establish that oral peptides reach the brain or modify AChE/Aβ biology.

This interim study asks a limited question: what candidate set is supported by the available aggregate screening record and the separately reported sequence/docking summary? The objective is to present the numerical funnel, list the available sequences, and define the next validation steps without overstating mechanism.

## 2. Materials and Methods

### 2.1 Study design and evidence sources

The principal source was an aggregate computational record derived from healthy and periodontitis oral-metagenome branches. It supplied screening counts, thresholds, and workflow descriptions but not candidate-level rows, sample mappings, or executable pipeline code. A user-designated external v0.4 repository separately supplied twelve sequence strings and Vina mean±SD values. The external information was treated as an author-reported summary, not as independently reproduced analysis.

### 2.2 Aggregate screening workflow

According to the principal record, translated 4–50-aa smORFs were evidence-filtered and dereplicated. The resulting healthy and periodontitis libraries were divided into short (5–30 aa) and long (31–50 aa) branches. UniDL4BioPep BBB output≥0.80 defined “BBB-high” [5]. The periodontitis BBB-high set was screened with NTxPred2 over its stated 7–50-aa range [7], followed by mebipred at 0.50 [8] and AnOxPePred CHEL/FRS thresholds [9]. The main endpoint required CHEL≥0.25 and FRS<0.50; a stricter endpoint used FRS<0.45.

The source did not provide the row-level NTxPred2-to-mebipred handoff. Therefore, 111 was retained as a source-reported downstream count, but 111/923 was not interpreted as an audited transition rate.

### 2.3 External sequence and docking summary

The twelve external sequences were checked for uniqueness, standard amino-acid characters, length, histidine, cysteine, basic residues (Arg+Lys), and aromatic residues. The external report stated that AutoDock Vina 1.2.5 was used against human AChE PDB 4EY6 with a 40×40×40 Å³ PAS-centred box [13,18,19]. Reported means and SDs were transcribed and checked for ordering and range.

Docking was not rerun because receptor/ligand preparation files, exact grid centre, protonation and charge settings, configurations, exhaustiveness, seeds, raw runs, logs, and poses were absent. Vina scores were not interpreted as binding affinities or free energies [18,19].

### 2.4 Statistical approach

All analyses were descriptive. Percentages were recalculated as 100×n/N. Peptide candidates were not treated as independent biological replicates because subject/sample mappings and clustering information were unavailable. Consequently, no healthy-versus-periodontitis p value or confidence interval was calculated.

## 3. Results

### 3.1 Aggregate prioritization funnel

Evidence filtering retained 31,510 of 11,269,961 healthy-branch smORFs (0.2796%) and 33,786 of 11,721,988 periodontitis-branch smORFs (0.2882%). BBB-high outputs were 3,359/30,557 (10.99%) and 3,446/32,754 (10.52%) in the short branches, and 40/953 (4.20%) and 72/1,032 (6.98%) in the long branches.

The periodontitis branch contained 3,518 BBB-high candidates. NTxPred2 evaluated 3,299 (93.77%); 219 were below its stated input range. Of the evaluated candidates, 923/3,299 (27.98%) were model-positive. The downstream record reported 111 mebipred-positive candidates, followed by 15 CHEL-priority candidates, a 12-candidate main set, and an 8-candidate stricter subset (Table 1).

**Table 1. Short aggregate screening summary**

| Stage | Rule/status | Periodontitis branch, n | Interpretation |
| --- | --- | ---: | --- |
| Evidence-filtered | Exact-match filtering and dereplication | 33,786 | Computational retention |
| BBB-high | UniDL4BioPep output≥0.80 | 3,518 | Predicted label, not measured BBB transport |
| NTxPred2 evaluated | Stated range 7–50 aa | 3,299 | 219 not evaluated |
| NTxPred2-positive | Model-positive | 923 | Not experimental neurotoxicity |
| Metal-binding-positive | mebipred≥0.50 | 111 | Source-reported downstream count |
| CHEL-priority | CHEL≥0.25 | 15 | Operational filter |
| Main set | CHEL≥0.25; FRS<0.50 | 12 | Candidate count |
| Stricter set | CHEL≥0.25; FRS<0.45 | 8 | Membership unavailable |

### 3.2 Twelve externally reported sequences

The external record listed twelve unique sequences of 7–9 aa (Table 2). Eleven contained histidine, six contained cysteine, and all contained at least one Arg or Lys. The set was short, cationic, and leucine-rich, but composition alone cannot establish metal binding, membrane transport, toxicity, or taxonomy.

**Table 2. External sequence list and source-reported Vina summary**

| Sequence | Length | His | Cys | Reported Vina mean±SD (kcal/mol) |
| --- | ---: | ---: | ---: | ---: |
| FLLHTTR | 7 | 1 | 0 | −9.60±0.08 |
| YLSLLQR | 7 | 0 | 0 | −9.49±0.05 |
| ALLLHRC | 7 | 1 | 1 | −9.29±0.11 |
| FCLHLQLR | 8 | 1 | 1 | −9.27±0.09 |
| YHHLLCRR | 8 | 2 | 1 | −9.03±0.07 |
| LLHLPKRTT | 9 | 1 | 0 | −9.01±0.06 |
| LLHPLRL | 7 | 1 | 0 | −8.94±0.10 |
| WLLVHLKK | 8 | 1 | 0 | −8.94±0.04 |
| LLHPLRC | 7 | 1 | 1 | −8.91±0.08 |
| HLLTLKKHV | 9 | 2 | 0 | −8.88±0.05 |
| HLPLLHRCC | 9 | 2 | 2 | −8.35±0.12 |
| HVLLLRQCA | 9 | 1 | 1 | −8.25±0.09 |

![Figure 1. Source-reported docking-score summary](../figures/fig5_docking_scores.png)

**Figure 1.** Source-reported AutoDock Vina means±SD against human AChE PDB 4EY6. The values were not independently reproduced; the run definition and poses were unavailable.

### 3.3 Current evidence boundary

The external sequence list makes synthesis planning possible, but it does not show which principal-source rows correspond to the twelve strings or which eight belong to the stricter subset. Likewise, the docking summary provides only a reported within-set ordering. Translation, BBB transport, toxicity, metal-dependent effects, AChE function, and disease relevance remain untested.

## 4. Discussion

This interim reconstruction identifies a concrete twelve-sequence hypothesis set while preserving the limits of the source material. The aggregate funnel is internally consistent and shows how serial models narrowed millions of smORFs. However, the near-complete absence of row-level provenance prevents subject-level group analysis and independent reproduction of candidate selection.

The reported docking ranking adds a structural question rather than a binding result. Vina is useful for rapid pose and score generation [18,19], but short flexible peptides have many conformations, and their rankings can depend on termini, protonation, starting conformers, receptor flexibility, box placement, and search settings. Flexible peptide refinement methods may be useful after complete inputs and poses are released [20]. Before that, residue contacts, PAS selectivity, and score differences should not be interpreted mechanistically.

The biological hypothesis also remains preliminary. Periodontitis and cognitive disorders have been associated in observational studies, but results depend on case definitions and study design [15]. Mendelian-randomization evidence does not currently support a strong causal periodontal effect on AD [16], and recent reviews continue to emphasize uncertainty [17]. Therefore, these candidates should be described as originating from a periodontitis-cohort analysis branch rather than as disease-specific mediators.

The next stage should first recover the sequence-to-sample and sequence-to-model lineage. The twelve peptides can then be synthesized and examined for purity, stability, nonspecific membrane disruption, BBB transport, neuronal toxicity, and Cu/Fe/Zn binding. AChE activity and amyloid-β aggregation assays should follow only for candidates with reproducible biochemical and exposure evidence. Scrambled peptides, composition-matched controls, peptide-only controls, and metal-only controls are essential.

The main limitations are missing candidate rows, unresolved strict-subset membership, absent predictor execution records, and unavailable docking inputs and poses. No experimental validation was performed. These limitations mean that the study is currently a computational prioritization report, not a mechanism study.

## 5. Conclusions

The available records support an aggregate screening funnel and a source-reported twelve-sequence shortlist with an AChE docking-score ordering. They do not establish target binding, biological activity, disease specificity, or causality. The main value of this interim analysis is to define a manageable candidate set and a transparent plan for reproducible computational and experimental follow-up.

## References

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178:1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29:121–131.e4. doi:10.1016/j.chom.2020.11.002.
3. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
4. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
5. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24:bbad135. doi:10.1093/bib/bbad135.
6. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
7. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34:e70200. doi:10.1002/pro.70200.
8. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38:3532–3540. doi:10.1093/bioinformatics/btac358.
9. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
10. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187:5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
11. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397:1577–1590. doi:10.1016/S0140-6736(20)32205-4.
12. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16:881–891. doi:10.1016/s0896-6273(00)80108-7.
13. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55:10282–10286. doi:10.1021/jm300871x.
14. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
15. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52:afad015. doi:10.1093/ageing/afad015.
16. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14:e3486. doi:10.1002/brb3.3486.
17. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98:220–227. doi:10.1111/prd.12631.
18. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31:455–461. doi:10.1002/jcc.21334.
19. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61:3891–3898. doi:10.1021/acs.jcim.1c00203.
20. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
