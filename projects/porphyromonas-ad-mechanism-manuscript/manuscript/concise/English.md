## Abstract

Periodontitis-associated oral dysbiosis has been proposed as a contributor to Alzheimer’s disease (AD)-related inflammation, but the molecular link remains uncertain. We conducted a computation-only secondary analysis of aggregate oral small open reading frame (smORF) data to prioritize micropeptides for validation. The cascade combined ESM-2 embeddings and task-specific convolutional networks, an ESM2-t30 neurotoxicity model, a two-tier neural-network metal-binding predictor, and a multi-task antioxidant convolutional network. Sequence-evidence filtering retained 31,510 and 33,786 candidates from initial libraries of 11,269,961 and 11,721,988 smORFs. In the periodontitis-labelled branch, 3,518 candidates were BBB-high; NTxPred2 evaluated 3,299 and classified 923 as positive. Subsequent filters retained 111, 15, 12, and 8 candidates. A separate table contained twelve 7–9-aa sequences and AChE Vina means from −9.60 to −8.25 kcal/mol. Sequence composition and score ordering were verifiable, whereas the connection between the twelve sequences and the aggregate endpoint, docking execution, and molecular-dynamics results were unavailable. The output is a computational shortlist for independent reproduction and experimental testing, not evidence of *Porphyromonas gingivalis* origin, brain exposure, AChE binding, or an AD mechanism.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral micropeptides; smORF; deep learning; acetylcholinesterase

## Introduction

Alzheimer’s disease (AD) develops through interacting amyloid, tau, synaptic, immune, and vascular processes rather than a single molecular pathway [@scheltens2021alzheimer]. Amyloid remains biologically important, but its relationship with disease progression must be interpreted within this broader network [@selkoe2016amyloid].

Periodontitis is a dysbiosis-associated inflammatory disease that may add to systemic inflammatory burden and has motivated oral–brain-axis research [@chalmers2025primer]. Within periodontal biofilms, *Porphyromonas gingivalis* is a pathobiont capable of proteolysis, immune modulation, tissue disruption, and community remodeling [@guo2010gingipain]. Post-mortem studies have reported *P. gingivalis*-related signals in AD brain tissue, although such observations do not establish direction or causality [@dominy2019pgingivalis]. Repeated oral exposure in mice produced neuroinflammatory and amyloid-related changes, supporting experimental plausibility but not direct human inference [@ilievski2018oral]. Vesicles have also been proposed as vehicles for concentrated microbial cargo, but their relevance to natural human brain exposure remains unresolved [@nara2021omv]. A Mendelian-randomization analysis did not establish a genetic causal effect of periodontal disease on AD, providing an important limit on strong causal claims [@hu2024mendelian].

A possible but underexplored molecular class is the microbiome-encoded micropeptide. Human-associated microbiomes contain many conserved small genes [@sberro2019smallgenes], and dedicated annotation methods improve detection of smORFs that conventional pipelines can miss [@durrant2021sorf]. However, a predicted sequence is not necessarily translated, released from a biofilm, stable in circulation, able to cross the blood–brain barrier (BBB), or active in neural tissue.

The relevant mechanism is therefore unclear. This study was conducted to reduce an aggregate oral-smORF candidate space with modern sequence models, characterize an available twelve-peptide set, and define what would be required to test AChE, metal/redox, BBB, and neurotoxicity hypotheses. The analysis remained exploratory and did not assign any candidate to *P. gingivalis* or treat model scores as biological confirmation.

## Materials and Methods

### Study design and data scope

This was a computation-only secondary analysis of aggregate screening counts, a twelve-sequence table, and an AChE docking-score table. No participant recruitment, specimen collection, wet-laboratory work, new omics processing, predictor retraining, docking rerun, or completed MD analysis was performed. Row-level sequences for the full funnel, subject/sample mappings, accession-to-group assignments, taxonomic data, peptide-spectrum matches, complete model outputs, and docking inputs were unavailable.

PRJNA678453 was treated as the source project for paired oral metagenomic and metatranscriptomic data [@belstrom2021periodontitis]. PRJEB65451 is a derived EBI-EMG/MGnify Third Party Annotation metagenomic assembly project generated from PRJNA678453 with metaSPAdes v3.15.3, not an independent clinical cohort. Specific participant, specimen, assembly-analysis, and metagenome-assembled-genome totals were omitted because consistent mapping and bin-level manifests were unavailable.

### Candidate construction and model cascade

The supplied analysis retained smORFs encoding 4–50-aa peptides. Initial healthy-labelled and periodontitis-labelled libraries contained 11,269,961 and 11,721,988 candidates. Exact matching against named oral sequence and proteomic resources followed by dereplication retained 31,510 and 33,786 candidates. Resource matches were interpreted as sequence-supporting evidence, not proof of expression in the analyzed clinical groups.

UniDL4BioPep encoded each peptide with the pretrained ESM-2 model `esm2_t6_8M_UR50D`, producing a 320-dimensional contextual embedding that was passed to a six-layer task-specific convolutional neural network [@du2023unidl4biopep]. The applied threshold was ≥0.80, including for BBB prioritization. NTxPred2 then evaluated peptides within its documented 7–50-aa range by fine-tuning the ESM2-t30 protein language model for neurotoxic-peptide classification [@rathore2025ntxpred2]. Sequences below 7 aa were treated as outside model coverage rather than negative.

Mebipred combined amino-acid composition, physicochemical descriptors, and metal-binding 5-mer frequencies in a two-tier artificial-neural-network framework with general and ion-specific classifiers [@aptekmann2022mebipred]. The applied threshold was 0.50. AnOxPePred used a multi-task deep convolutional neural network with one-dimensional convolution, average pooling, and a 256-unit fully connected layer to produce free-radical-scavenging (FRS) and chelation (CHEL) scores [@olsen2020anoxpepred]. Endpoints were CHEL≥0.25, CHEL≥0.25 with FRS<0.50, and CHEL≥0.25 with FRS<0.45. No model was retrained, and serial model agreement was not considered independent validation.

### Sequence, docking, and prospective MD analysis

For the separate twelve-sequence table, length and counts of histidine, cysteine, Arg+Lys, and Phe+Tyr+Trp were recalculated directly from the strings. The available docking summary described AutoDock Vina 1.2.5 scores for human AChE PDB 4EY6. Means and standard deviations were analyzed descriptively. Docking was not rerun because prepared structures, PDBQT inputs, protonation and charge settings, exact search coordinates, run definitions, raw scores, logs, poses, and interaction tables were unavailable. Vina scores were not interpreted as affinities or free energies.

A prospective 100-ns protocol was specified for apo AChE and complexes labelled for ALLLHRC, FLLHTTR, and YLSLLQR. Planned simulations used GROMACS [@abraham2015gromacs], Amber99SB-ILDN [@lindorfflarsen2010amber], TIP3P water, 0.15 mol/L NaCl, sequential restrained NVT and NPT equilibration, unrestrained NPT equilibration, and a 100-ns production stage at 300 K and 1 bar with a 2-fs time step. Planned analyses included RMSD/RMSF, radius of gyration, solvent-accessible surface area, hydrogen bonds, residue contacts, secondary structure, radial distribution functions, and bridging water. Starting complexes and complete trajectories were unavailable; no MD result was analyzed.

### Statistical analysis

All analyses were descriptive. Retention percentages used the preceding documented stage as denominator. Candidate sequences are computational units nested within samples, assemblies, genomes, and homologous groups, not independent biological replicates. Consequently, aggregate healthy-versus-periodontitis hypothesis tests, confidence intervals, and effect estimates were not calculated.

## Results

### Aggregate prioritization funnel

Sequence-evidence filtering retained 31,510/11,269,961 healthy-labelled candidates (0.2796%) and 33,786/11,721,988 periodontitis-labelled candidates (0.2882%). The periodontitis-labelled branch contained 3,518 BBB-high outputs. NTxPred2 evaluated 3,299, of which 923 were model-positive; 219 candidates were below its stated length range. Later filters yielded 111 metal-binding-positive candidates, 15 candidates with CHEL≥0.25, 12 with CHEL≥0.25 and FRS<0.50, and 8 with CHEL≥0.25 and FRS<0.45 (Table 1). Because the NTxPred2-to-mebipred row-level handoff was unavailable, 111/923 was not treated as a verified transition rate.

**Table 1. Aggregate computational prioritization results.**

| Stage | Operational rule | n | Denominator or limitation |
| --- | --- | ---: | --- |
| Healthy-labelled smORFs | 4–50 aa | 11,269,961 | Initial library |
| Periodontitis-labelled smORFs | 4–50 aa | 11,721,988 | Initial library |
| Evidence-filtered healthy-labelled | Exact match and dereplication | 31,510 | 11,269,961 |
| Evidence-filtered periodontitis-labelled | Exact match and dereplication | 33,786 | 11,721,988 |
| BBB-high | UniDL4BioPep output≥0.80 | 3,518 | Periodontitis-labelled branch |
| NTxPred2 evaluated | 7–50 aa | 3,299 | 3,518 |
| NTxPred2-positive | Model-positive label | 923 | 3,299 |
| Metal-binding-positive | Mebipred output≥0.50 | 111 | Row-level handoff unavailable |
| CHEL-priority | CHEL≥0.25 | 15 | 111 |
| Main set | CHEL≥0.25 and FRS<0.50 | 12 | 111 |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | Members unavailable |

### Twelve-sequence table and docking scores

The separate table contained twelve unique 7–9-aa peptides. Eleven contained histidine, six contained cysteine, and every sequence contained Arg or Lys. The Vina means ranged from −9.60 to −8.25 kcal/mol (Table 2). FLLHTTR ranked first and HVLLLRQCA last within the available scoring table. The sequence composition could be recalculated, but docking execution and the relationship between these sequences and the aggregate set of 12 or 8 could not be established.

**Table 2. Twelve-sequence set and available AChE docking scores.**

| Rank | Sequence | Length (aa) | Mean score (kcal/mol) | SD |
| ---: | --- | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | −9.60 | 0.08 |
| 2 | YLSLLQR | 7 | −9.49 | 0.05 |
| 3 | ALLLHRC | 7 | −9.29 | 0.11 |
| 4 | FCLHLQLR | 8 | −9.27 | 0.09 |
| 5 | YHHLLCRR | 8 | −9.03 | 0.07 |
| 6 | LLHLPKRTT | 9 | −9.01 | 0.06 |
| 7 | LLHPLRL | 7 | −8.94 | 0.10 |
| 8 | WLLVHLKK | 8 | −8.94 | 0.04 |
| 9 | LLHPLRC | 7 | −8.91 | 0.08 |
| 10 | HLLTLKKHV | 9 | −8.88 | 0.05 |
| 11 | HLPLLHRCC | 9 | −8.35 | 0.12 |
| 12 | HVLLLRQCA | 9 | −8.25 | 0.09 |

## Discussion

The analysis defines a compact validation set while preserving the distinction between prediction and mechanism. Deep-learning and neural-network models make the search space tractable, but outputs trained on heterogeneous datasets may be poorly calibrated for very short microbiome-derived peptides. The nearly complete antimicrobial positivity observed in the broader full analysis further cautions against equating multiple model-positive labels with biological replication.

AChE provides a plausible structural context because its peripheral region can influence Aβ assembly [@inestrosa1996ache], and PDB 4EY6 provides an experimentally determined human structure [@cheung2012ache]. Nevertheless, Vina is a screening method whose rankings depend on receptor and ligand preparation, search-space definition, and sampling [@trott2010vina]. Later Vina implementations do not eliminate these requirements [@eberhardt2021vina], and flexible peptide docking may require peptide-specific refinement [@london2011flexpepdock]. Without poses and run definitions, the score range does not establish AChE binding, site preference, inhibition, selectivity, or Aβ modulation.

The periodontal context is similarly bounded. Existing studies motivate investigation of inflammatory, gingipain, infection-related, and vesicle-associated routes, but they cannot assign community-derived peptides to *P. gingivalis*. A candidate-level chain from sequence to assembly, sample, clinical label, taxonomy, expression, circulation, BBB transport, and target engagement is required before disease claims can be tested.

The immediate priorities are to recover row-level funnel membership, identify the stricter 8-of-12 subset, rerun fixed predictor and docking versions, and verify peptide identity and stability after synthesis. Subsequent assays should evaluate BBB transport, cytotoxicity, Cu/Fe/Zn interaction, metal-dependent redox effects, AChE/BChE function, direct binding, and Aβ phenotypes with appropriate controls. The absent row mappings, raw docking materials, complete MD inputs, and experimental measurements are decisive limitations.

## Conclusion

The aggregate data support a transparent computational funnel ending in 12 main and 8 stricter candidate counts. A separate twelve-peptide table provides composition and AChE score ordering but cannot be linked row by row to those endpoints, and neither docking nor MD results were independently produced. The shortlist is appropriate for staged validation, but it does not establish *P. gingivalis* origin, disease specificity, brain exposure, target binding, biological activity, or causality.

## References

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
4. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
5. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
6. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
7. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
8. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
9. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
10. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
11. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
12. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
13. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
14. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
15. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
16. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
17. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
18. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
19. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
20. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
21. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
22. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
