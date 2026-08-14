# Deep-Learning-Guided Multi-Model Prioritization of Oral Micropeptides at the Periodontitis–Alzheimer’s Disease Interface

## Abstract

**Background:** Alzheimer’s disease (AD) is defined by interacting amyloid, tau, neuroimmune and vascular abnormalities. Periodontal infection—particularly infection involving *Porphyromonas gingivalis*—has been proposed as one contributor to this multifactorial process, but the human causal and molecular links remain unresolved.

**Objective:** To prioritize oral micropeptide candidates for mechanistic follow-up within a *P. gingivalis*–motivated, but not organism-assigned, AD hypothesis.

**Methods:** Supplied aggregate records from health- and periodontitis-labeled oral metagenomic candidate sets were evaluated through a deep-learning-guided cascade integrating protein-language-model embeddings, task-specific convolutional neural networks, a hierarchical neural-network metal-binding predictor and multi-task antioxidant prediction. Public accession records were checked to distinguish the PRJNA678453 source cohort from its derived EBI-EMG/MGnify Third Party Annotation (TPA) assembly project, PRJEB65451. Source-reported acetylcholinesterase (AChE) docking was summarized separately, and only descriptive calculations were performed.

**Results:** The supplied funnel began with 11,269,961 health-labeled and 11,721,988 periodontitis-labeled smORFs and retained 31,510 and 33,786 nonredundant proteomically supported candidates, respectively. The downstream aggregate record contained 3,518 BBB-high candidates; NTxPred2 covered 3,299, of which 923 were classified as neurotoxic. Metal-binding and antioxidant filters retained 111, 15, 12 and finally 8 candidates. A separate external record listed 12 sequences from FLLHTTR to HVLLLRQCA and source-reported Vina means of −9.60 to −8.25 kcal/mol against AChE.

**Conclusions:** The analysis defines a compact computational validation set, not a demonstrated periodontal–AD mechanism. Sequence provenance, organism assignment, independent docking reproduction and experimental validation remain necessary.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral micropeptides; metagenomics; machine learning; acetylcholinesterase

## Introduction

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder and the leading cause of dementia, with a pathological continuum that develops years before overt cognitive impairment [1]. Contemporary models place amyloid-β accumulation within an interacting network of tau pathology, synaptic dysfunction, innate immune activation and neurovascular injury rather than attributing disease progression to a single pathway [2].

Periodontitis is a chronic, dysbiosis-associated inflammatory disease whose potential neurological consequences have motivated investigation of an oral–brain axis [3]. Within dysbiotic periodontal biofilms, *Porphyromonas gingivalis* is a Gram-negative anaerobic pathobiont with extensive immune-modulatory and tissue-destructive capacity [4]. The ulcerated periodontal interface may permit episodic systemic exposure to bacterial cells, inflammatory mediators and virulence products, providing a biologically plausible route by which a localized oral infection could influence distant tissues.

Several non-exclusive mechanisms connect *P. gingivalis* exposure with AD-related molecular processes. A post-mortem study reported *P. gingivalis* DNA and gingipain immunoreactivity in AD brain tissue, although those observations remain insufficient to establish directionality or causation [5]. Repeated oral infection in wild-type mice produced neuroinflammatory and amyloid-related changes, supporting experimental plausibility rather than direct human inference [6]. In a separate mouse model, *P. gingivalis* outer-membrane vesicles reached brain tissue and were associated with inflammasome activation, tau phosphorylation and memory dysfunction [7]. Conversely, a two-sample Mendelian-randomization analysis found no genetic evidence that periodontal disease causes AD, underscoring the unresolved status of the human causal relationship [8].

The molecular bridge between periodontal dysbiosis and neurodegeneration therefore remains incomplete. One mechanistic gap concerns microbially encoded peptides. Small open reading frames are widespread in human-associated microbiomes and encode a large, incompletely characterized peptide repertoire [9]. Computational annotation can recover candidate small proteins that conventional gene-calling pipelines frequently miss [10]. Whether peptides represented in periodontitis-labeled oral metagenomic candidate sets are expressed, released from biofilms, systemically exposed, capable of crossing the blood–brain barrier (BBB), or able to influence neuronal, metal/redox or cholinergic processes is unknown. We therefore performed a deep-learning-guided, multi-model prioritization to define a tractable candidate set for provenance reconstruction and experimental validation. The analysis was explicitly exploratory and did not assign the candidates to *P. gingivalis* or treat model scores as evidence of an AD mechanism.

## Materials and methods

### Study design and accession provenance

This study was a structured descriptive secondary analysis of supplied aggregate screening records. The records contained health- and periodontitis-labeled candidate counts but did not include participant-level mappings, accession-to-group tables or row-level model outputs.

The primary sequence source was BioProject PRJNA678453. The published cohort comprised 22 participants—11 orally healthy controls and 11 patients with periodontitis—and generated 66 oral specimens: 22 subgingival-plaque samples, 22 tongue scrapings and 22 stimulated-saliva samples, with paired metagenomic and metatranscriptomic measurements [11]. PRJEB65451 was verified as an EBI-EMG/MGnify-brokered Third Party Annotation metagenomic assembly project derived from PRJNA678453 using metaSPAdes v3.15.3, rather than an independent clinical cohort. The ENA record currently enumerates 118 sequence-assembly analyses under PRJEB65451; these assembly records were not interpreted as participants, specimens or metagenome-assembled genomes. Because the accession chain and cohort publication did not support an alternative composition of 24 controls, 26 patients and 296 high-quality metagenome-assembled genomes, those quantities were not used. The verified clinical composition was retained only as provenance and not as a denominator for candidate-level inference.

### Candidate definition and proteomic-evidence filter

According to the archived aggregate workflow, putative small open reading frames encoding 4–50-aa peptides were partitioned by the supplied health-status labels. Candidate sequences were matched exactly against oral proteomic resources represented in the source records, including PXD003151, PXD004319, PXD026727 and HOMD-related protein sequences. Exact matches were deduplicated to generate the nonredundant proteomically supported candidate sets. Because the sequence-level input and match table were unavailable, this stage was treated as a source-reported filter and was not independently rerun.

### Deep-learning-guided multi-model prioritization

A sequential architecture was used to integrate contextual sequence representation, task-specific deep classification, hierarchical metal-binding prediction and multi-task antioxidant scoring. Each stage answered a distinct biological-prioritization question; downstream retention therefore represented a serial decision rule rather than independent experimental confirmation.

First, UniDL4BioPep used the pretrained ESM-2 model `esm2_t6_8M_UR50D` to transform each peptide into a 320-dimensional context-sensitive embedding. The embedding was processed by a six-layer deep convolutional neural network trained separately for each peptide-bioactivity task [12]. A predicted probability ≥0.8 defined a high-confidence model output, and only candidates with BBB probability ≥0.8 entered the subsequent cascade.

Second, neurotoxicity was evaluated using the peptide-specific NTxPred2 architecture. This model applies transfer learning by fine-tuning the ESM2-t30 protein language model on neurotoxic-peptide sequences [13]. Analysis was restricted to the documented 7–50-aa input range; sequences shorter than 7 aa were recorded as outside model coverage rather than as negative predictions.

Third, Cu-, Fe- and Zn-related binding potential was evaluated with mebipred. The method combines amino-acid composition, physicochemical descriptors and metal-binding 5-mer frequencies in a two-tier artificial-neural-network framework: a general metal-binding network is followed by ion-specific neural classifiers [14]. The source-recorded decision threshold was 0.5.

Fourth, antioxidant-related properties were evaluated with AnOxPePred, a multi-task deep convolutional neural network. One-hot-encoded peptide sequences pass through a one-dimensional convolutional layer, average pooling and a 256-unit fully connected layer before separate free-radical-scavenging (FRS) and chelation (CHEL) outputs are generated [15]. CHEL ≥0.25 was applied first, followed by the source-recorded combined CHEL/FRS criterion.

No model was retrained or fine-tuned in the present secondary analysis. Exact historical web-server builds, model hashes, random seeds, submitted input files and row-level outputs were not preserved. The architecture descriptions therefore document the cited implementations and relevant peptide modes, whereas the thresholds and retained counts remain source-reported aggregate records.

### External sequence characterization and docking evidence

The external twelve-sequence record was analyzed as a separate evidence layer and was not merged row by row with the aggregate screening funnel. Sequence length, molecular mass, nominal charge, hydrophobic-residue fraction and amino-acid composition were recalculated directly from the strings with version-controlled code.

AChE was selected as a structure-based contextual target because the enzyme has been reported to accelerate amyloid-β fibril assembly through its peripheral region [16]. The external record designated human AChE structure PDB 4EY6, for which ligand-bound structural information is available [17]. Vina means and standard deviations were transcribed exactly as source-reported values. Raw receptor and ligand files, protonation states, grid definitions, poses, logs and run-level scores were unavailable; consequently, docking was not rerun and no contact, affinity or functional claim was inferred. The twelve external sequences could not be mapped to the stricter aggregate endpoint of eight candidates.

### Statistical analysis and evidence interpretation

All analyses were descriptive. Retention percentages used the immediately preceding documented stage as the denominator. Candidate sequences were computational accounting units rather than independent participants or biological replicates, so no health-versus-periodontitis hypothesis test, confidence interval or peptide-level inferential model was applied. No missing row-level values were imputed.

Vina scores were used only for within-record ranking and were not interpreted as experimental affinities or binding free energies [18]. Current Vina implementations improve search and force-field options but do not eliminate dependence on receptor preparation, search-space definition and sampling [19]. Because protein–peptide recognition can involve distributed interface hot segments, a single rigid-receptor docking rank was not converted into a mechanistic conclusion [20].

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
