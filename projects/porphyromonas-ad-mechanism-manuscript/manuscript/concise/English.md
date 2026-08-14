# Aggregate Prioritization of Oral Micropeptides at the Periodontitis–Alzheimer’s Disease Interface

## Abstract

**Background:** Alzheimer’s disease (AD) is defined by interacting amyloid, tau, neuroimmune and vascular abnormalities. Periodontal infection—particularly infection involving *Porphyromonas gingivalis*—has been proposed as one contributor to this multifactorial process, but the human causal and molecular links remain unresolved.

**Objective:** To prioritize oral micropeptide candidates for mechanistic follow-up within a *P. gingivalis*–motivated, but not organism-assigned, AD hypothesis.

**Methods:** Supplied aggregate records from health- and periodontitis-labeled oral metagenomic candidate sets were filtered by proteomic support, sequence-based blood–brain barrier (BBB), neurotoxicity, metal-binding and antioxidant predictions, and source-reported acetylcholinesterase (AChE) docking. Public accession records were checked to distinguish the PRJNA678453 source cohort from its derived EBI-EMG/MGnify Third Party Annotation (TPA) assembly project, PRJEB65451. Only descriptive calculations were performed.

**Results:** The supplied funnel began with 11,269,961 health-labeled and 11,721,988 periodontitis-labeled smORFs and retained 31,510 and 33,786 nonredundant proteomically supported candidates, respectively. The downstream aggregate record contained 3,518 BBB-high candidates; NTxPred2 covered 3,299, of which 923 were classified as neurotoxic. Metal-binding and antioxidant filters retained 111, 15, 12 and finally 8 candidates. A separate external record listed 12 sequences from FLLHTTR to HVLLLRQCA and source-reported Vina means of −9.60 to −8.25 kcal/mol against AChE.

**Conclusions:** The analysis defines a compact computational validation set, not a demonstrated periodontal–AD mechanism. Sequence provenance, organism assignment, independent docking reproduction and experimental validation remain necessary.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral micropeptides; metagenomics; machine learning; acetylcholinesterase

## Introduction

Alzheimer’s disease is a progressive neurodegenerative disorder in which amyloid-β accumulation, tau pathology, synaptic failure, neuroinflammation and vascular dysfunction interact over a prolonged preclinical interval [1,2]. These processes are heterogeneous and cannot be reduced to a single infectious, inflammatory or protein-aggregation pathway.

*Porphyromonas gingivalis* is a Gram-negative anaerobic pathobiont associated with dysbiotic periodontal biofilms. Periodontitis can create repeated opportunities for systemic exposure to oral microorganisms, inflammatory mediators and microbial products. Experimental and post-mortem studies have therefore examined several routes linking *P. gingivalis* to AD-related pathology: circulating inflammation may influence blood–brain barrier integrity and microglial activation; lipopolysaccharide and gingipains may perturb host signaling and proteostasis; and outer-membrane vesicles may disseminate virulence cargo beyond the periodontal niche [3–7]. These findings establish biologically plausible hypotheses, but they do not establish that *P. gingivalis* causes AD in humans. The evidence is heterogeneous, and a two-sample Mendelian-randomization study found no genetic evidence that periodontal disease causes AD [8].

A further mechanistic gap concerns small proteins and peptides encoded by oral microbial communities. Microbiome studies show that small open reading frames are widespread and can encode previously unrecognized bioactive molecules [9,10]. It remains unknown whether oral microbial peptides represented in periodontitis-labeled candidate sets enter the circulation, cross the BBB, affect neuronal or glial biology, disturb metal/redox homeostasis, or modulate AChE. It is also unknown whether any candidate considered here originates from *P. gingivalis*. We therefore performed an exploratory, aggregate-level prioritization to identify a small set for traceable reconstruction and experimental testing, without treating computational labels as biological validation.

## Materials and methods

### Study design and verified data provenance

This was a descriptive secondary analysis of supplied aggregate counts. The source materials attributed the health- and periodontitis-labeled candidate sets to BioProject PRJNA678453 and to PRJEB65451. Accession verification showed that PRJEB65451 is not an independent clinical cohort: it is an EBI-EMG/MGnify-brokered TPA metagenomic assembly project derived from PRJNA678453 and assembled with metaSPAdes v3.15.3. The published source cohort comprised 22 participants—11 orally healthy controls and 11 patients with periodontitis—with three oral specimens per participant, giving 66 specimens: 22 subgingival-plaque samples, 22 tongue scrapings and 22 stimulated-saliva samples. Paired metagenomic and metatranscriptomic measurements were generated [11]. The ENA project page currently enumerates 118 sequence-assembly analyses under PRJEB65451; these are assembly records, not participant or specimen counts.

The supplied aggregate data did not include participant-level mappings, accession-to-group assignments or row-level sequence outputs. Consequently, the verified 11-versus-11 cohort composition is reported as source provenance and was not used as a denominator for candidate-level inference. The source statement of 24 controls, 26 patients and 296 high-quality metagenome-assembled genomes was not retained because those numbers could not be substantiated from PRJNA678453, PRJEB65451 or the cohort publication.

### Aggregate screening and prediction algorithms

The supplied workflow started from 4–50-aa smORFs labeled by health status. Exact sequence matching to oral proteomic resources and deduplication produced the supported candidate sets. UniDL4BioPep probabilities of at least 0.8 defined high-confidence functional predictions. Candidates with BBB probability ≥0.8 entered downstream screening. NTxPred2 was applied only within its recorded 7–50-aa input range; mebipred used a 0.5 threshold for Cu/Fe/Zn-related metal-binding potential; and AnOxPePred outputs were screened at CHEL ≥0.25 and then by the recorded FRS criterion.

The websites do not implement one uniform “deep-learning” method. UniDL4BioPep represents a peptide with the pretrained ESM-2 `esm2_t6_8M_UR50D` model as a 320-dimensional embedding and passes it to a six-layer convolutional neural network for task-specific binary classification [12]. NTxPred2 fine-tunes ESM2-t30 for peptide neurotoxicity, whereas its protein and combined modes use Extra Trees classifiers on ESM-2-derived embeddings [13]. mebipred is an alignment-free, feed-forward neural-network method: amino-acid composition, physicochemical descriptors and metal-binding 5-mer counts feed a general metal-binding classifier and ion-specific second-tier models [14]. AnOxPePred one-hot encodes peptide sequences and uses a one-dimensional convolution, average pooling and a fully connected layer with separate free-radical-scavenging and chelation outputs [15]. Thus, this is a mixture of protein-language-model, convolutional-neural-network, conventional ensemble and engineered-feature neural-network approaches. The exact historical server snapshots, submitted input files and row-level outputs were unavailable; these descriptions document the cited implementations rather than a rerun.

### External sequence set and docking evidence

A separate external record contained 12 unique 7–9-aa sequences with AChE docking summaries. Sequence length, molecular mass, charge, hydrophobic-residue fraction and residue composition were recalculated directly from the strings. Docking values were transcribed as source-reported Vina means and standard deviations against human AChE (PDB 4EY6). AChE is biologically relevant to cholinergic signaling and can interact with amyloid-β through its peripheral region [16,17], but docking alone cannot establish affinity or function. Raw receptor and ligand files, protonation settings, search boxes, poses, logs and run-level scores were absent; docking was therefore not rerun. The twelve external sequences could not be linked row by row to the aggregate funnel or to the stricter set of eight.

### Statistical analysis

Counts and percentages were descriptive. Candidate sequences were computational accounting units, not independent participants or biological replicates; no peptide-level health-versus-periodontitis significance test was performed. The limitations of docking scores as endpoint surrogates were interpreted according to established docking practice [18–20].

## Results

### Aggregate prioritization funnel

The source supplied 11,269,961 health-labeled and 11,721,988 periodontitis-labeled smORFs. Proteomic matching and deduplication retained 31,510 and 33,786 candidates, corresponding to 0.2796% and 0.2882% of their respective starting pools. The subsequent record contained 3,518 BBB-high candidates. NTxPred2 returned predictions for 3,299 sequences after 219 sequences shorter than 7 aa were outside its recorded input range; 923 were labeled neurotoxic. Cu/Fe/Zn-oriented mebipred filtering retained 111 candidates. AnOxPePred yielded 15 candidates at CHEL ≥0.25, 12 after the recorded combined screen and 8 after final prioritization.

**Table 1. Aggregate computational funnel. Counts are descriptive accounting units.**

| Stage | Retained count | Evidence status |
| --- | ---: | --- |
| Health-labeled smORFs | 11,269,961 | Supplied aggregate count |
| Periodontitis-labeled smORFs | 11,721,988 | Supplied aggregate count |
| Proteomically supported, health-labeled | 31,510 | Supplied aggregate count |
| Proteomically supported, periodontitis-labeled | 33,786 | Supplied aggregate count |
| BBB probability ≥0.8 | 3,518 | Supplied model summary |
| NTxPred2 outputs | 3,299 | Supplied model summary |
| Neurotoxic label | 923 | Supplied model summary |
| Cu/Fe/Zn metal-binding positive | 111 | Supplied model summary |
| CHEL ≥0.25 | 15 | Supplied model summary |
| Combined screen | 12 | Supplied model summary |
| Final stricter set | 8 | Membership unavailable |

![Aggregate computational prioritization funnel](../figures/prioritization_funnel.png)

**Figure 1.** Aggregate computational prioritization funnel. The diagram summarizes supplied counts; it does not represent participant flow or independent biological replication.

### External twelve-sequence record

The external record listed 12 unique peptides. Source-reported mean Vina scores against AChE ranged from −9.60 to −8.25 kcal/mol. FLLHTTR ranked first and HVLLLRQCA ranked last within this record. Composition was independently recomputed, whereas docking poses and scores were not independently reproduced.

**Table 2. External sequence record and source-reported AChE docking summary.**

| Rank | Sequence | Length (aa) | Source-reported mean (kcal/mol) | Source-reported SD |
| ---: | --- | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | −9.60 | 0.08 |
| 2 | KNGIYHLK | 8 | −9.42 | 0.06 |
| 3 | KNAIRLQ | 7 | −9.31 | 0.05 |
| 4 | NRPPHPPY | 8 | −9.18 | 0.09 |
| 5 | QMMKQAQK | 8 | −9.05 | 0.07 |
| 6 | WNMSKYYK | 8 | −8.94 | 0.04 |
| 7 | YPWINHPQ | 8 | −8.83 | 0.10 |
| 8 | WVAHKNY | 7 | −8.71 | 0.06 |
| 9 | YPIVIHPN | 8 | −8.58 | 0.11 |
| 10 | YDRNWNNK | 8 | −8.46 | 0.08 |
| 11 | RKQIKRYL | 8 | −8.34 | 0.05 |
| 12 | HVLLLRQCA | 9 | −8.25 | 0.12 |

## Discussion

This analysis reduced very large supplied candidate pools to two bounded follow-up objects: an eight-candidate aggregate endpoint whose membership is unavailable and a separate twelve-sequence external record. Its value is prioritization and discrepancy localization, not discovery of a validated AD mechanism.

The biological rationale begins with the periodontal–AD interface. *P. gingivalis* infection can plausibly contribute to systemic inflammatory signaling, exposure to LPS and gingipains, vesicle-mediated cargo transport, BBB perturbation and microglial activation [3–7]. The candidate workflow then asks whether oral microbial peptides might constitute an additional, largely unexplored molecular class with predicted BBB, neurotoxicity, metal/redox or AChE-related properties. However, none of the present results demonstrates peptide expression in the source participants, release from oral biofilms, systemic exposure, BBB transport, neuronal activity or AD specificity. In particular, the aggregate source does not establish that any candidate was encoded by *P. gingivalis*; the organism is a mechanistic motivation, not an assigned sequence origin.

The verified accession history also changes how the inputs should be described. PRJNA678453 is the primary 11-health/11-periodontitis, 66-specimen cohort, whereas PRJEB65451 is a derived TPA assembly resource. Participants, specimens, paired DNA/RNA measurements and assembly analyses are different units and must not be conflated. Because participant-to-sequence mappings are absent, the near-equal aggregate retention percentages cannot support a disease-enrichment claim.

Several limitations are decisive. First, row-level model outputs and exact server versions are unavailable, so thresholds and counts can be audited only at aggregate level. Second, the eight-versus-twelve membership discrepancy is unresolved. Third, the docking record lacks the material needed to reproduce or inspect poses. Fourth, predictors trained on heterogeneous datasets may be poorly calibrated for very short microbiome-derived peptides; agreement between predictors does not create experimental independence. A defensible next step is to recover candidate lineage, rerun version-pinned predictors and docking, and then test synthesis quality, stability, cytotoxicity, BBB transport, metal interaction, AChE activity and neuronal or glial phenotypes before making disease-mechanism claims.

## Conclusion

Aggregate evidence supports a transparent shortlist for validation, but not a causal chain from periodontitis or *P. gingivalis* to AD. The corrected provenance is PRJNA678453 as the 22-participant, 66-specimen source cohort and PRJEB65451 as its derived EBI-EMG/MGnify TPA assembly project. The 12 external sequences and source-reported AChE scores remain separate from the unresolved final set of 8. Restoring row-level provenance and performing independent computational and experimental validation are prerequisites for mechanistic interpretation.

## References

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397:1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ. Treatments for Alzheimer’s disease emerge. *Nature*. 2023;616:33–34. doi:10.1038/s41586-023-05769-3.
3. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98:220–227. doi:10.1111/prd.12631.
4. Liu S, Butler CA, Ayton S, Reynolds EC, Dashper SG. *Porphyromonas gingivalis* and the pathogenesis of Alzheimer’s disease. *Crit Rev Microbiol*. 2024;50:127–137. doi:10.1080/1040841X.2022.2163613.
5. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains: evidence for disease causation and treatment with small-molecule inhibitors. *Sci Adv*. 2019;5:eaau3333. doi:10.1126/sciadv.aau3333.
6. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13:e0204941. doi:10.1371/journal.pone.0204941.
7. Gong T, Chen Q, Mao H, et al. Outer membrane vesicles of *Porphyromonas gingivalis* trigger NLRP3 inflammasome and induce neuroinflammation, tau phosphorylation, and memory dysfunction in mice. *Front Cell Infect Microbiol*. 2022;12:925435. doi:10.3389/fcimb.2022.925435.
8. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14:e3486. doi:10.1002/brb3.3486.
9. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178:1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
10. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Nat Microbiol*. 2021;6:564–574. doi:10.1038/s41564-021-00891-0.
11. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *NPJ Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
12. Du Z, Ding X, Xu Y, Li W. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24:bbad135. doi:10.1093/bib/bbad135.
13. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34:e70200. doi:10.1002/pro.70200.
14. Valasatava Y, Rosato A, Banci L, Andreini C. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38:3532–3540. doi:10.1093/bioinformatics/btac358.
15. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
16. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16:881–891. doi:10.1016/S0896-6273(00)80108-7.
17. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55:10282–10286. doi:10.1021/jm300871x.
18. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking. *J Comput Chem*. 2010;31:455–461. doi:10.1002/jcc.21334.
19. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61:3891–3898. doi:10.1021/acs.jcim.1c00203.
20. London N, Raveh B, Schueler-Furman O. Druggable protein–protein interactions—from hot spots to hot segments. *Curr Opin Chem Biol*. 2013;17:952–959. doi:10.1016/j.cbpa.2013.10.011.
