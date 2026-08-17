## Abstract

Periodontitis-associated oral dysbiosis may contribute to Alzheimer’s disease (AD)-relevant inflammation, but a defined molecular connection has not been established. Microbiome small open reading frames (smORFs) provide a large candidate peptide space for computational prioritization. We therefore sought to reconstruct an aggregate oral-smORF screening cascade and define a tractable peptide set for mechanistic follow-up. This computation-only secondary analysis integrated sequence/proteomic filtering, ESM-2 embeddings with task-specific convolutional networks, an ESM2-t30 neurotoxicity model, a two-tier neural-network metal-binding predictor, a multi-task antioxidant convolutional network, sequence-composition analysis, and a separate acetylcholinesterase (AChE) docking summary. Filtering retained 31,510 and 33,786 candidates from libraries of 11,269,961 and 11,721,988 smORFs. In the periodontitis-labelled branch, 3,518 candidates were BBB-high; NTxPred2 evaluated 3,299 and classified 923 as model-positive. Later filters retained 111, 15, 12, and 8 candidates. A separate table contained twelve unique 7–9-aa sequences with AChE Vina means from −9.60 to −8.25 kcal/mol. Sequence composition and score ordering were reproducible, but row-level linkage and docking execution remained unresolved.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral micropeptide; smORF; deep learning; acetylcholinesterase; molecular dynamics

## Introduction

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder characterized by interacting amyloid-β (Aβ), tau, synaptic, immune, vascular, and metabolic abnormalities [@scheltens2021alzheimer]. Amyloid remains central to disease biology, but amyloid burden alone does not explain the temporal and clinical heterogeneity of AD [@selkoe2016amyloid]. Peripheral inflammatory conditions may therefore act as modifiers within a multilevel disease process rather than as single sufficient causes.

Periodontitis is a chronic inflammatory disease driven by a dysbiotic polymicrobial biofilm and a susceptible host response. It can create a sustained inflammatory burden and episodic systemic exposure to microbial products, motivating investigation of an oral–brain axis [@chalmers2025primer]. Within this ecosystem, *Porphyromonas gingivalis* is a well-studied Gram-negative anaerobic pathobiont. Gingipains, immune modulation, tissue degradation, nutrient acquisition, and community cooperation allow the organism to influence the periodontal niche even when it is not numerically dominant [@guo2010gingipain]. These properties provide mechanistic context but do not justify assigning an untraced community peptide to *P. gingivalis*.

Several observations support continued investigation while also illustrating the evidentiary gap. *P. gingivalis*-related DNA or protein signals have been reported in AD-associated post-mortem material, but detection in diseased tissue cannot establish the direction, timing, or causal role of exposure [@dominy2019pgingivalis]. Repeated oral exposure in mice has produced neuroinflammatory, neurodegenerative, and Aβ-related changes, supporting model-specific plausibility rather than direct human inference [@ilievski2018oral]. Outer-membrane vesicles provide a possible vehicle for concentrated bacterial cargo and host-cell signaling, although their natural biodistribution and effective dose in humans remain uncertain [@nara2021omv]. Conversely, Mendelian-randomization analysis has not established a genetic causal effect of periodontal disease on AD [@hu2024mendelian]. Together, these studies motivate molecular investigation but do not define a settled causal pathway.

Microbiome-encoded small proteins and peptides are plausible but underexplored molecular intermediates. Large-scale human microbiome analyses have identified many conserved small-gene families, often without known domains or functions [@sberro2019smallgenes]. Dedicated smORF annotation improves sensitivity by combining coding features and other evidence rather than relying on conventional protein-length thresholds [@durrant2021sorf]. Nevertheless, a predicted smORF is not necessarily transcribed or translated, and a detected peptide is not necessarily released from a biofilm, stable in blood, transported across the blood–brain barrier (BBB), or active in neural tissue.

The relevant molecular mechanism therefore remains unclear. This study was designed as an early-stage computational prioritization rather than a mechanistic test. We reconstructed the aggregate candidate funnel, described the actual model architectures used at each stage, characterized a supplied twelve-sequence set, and bounded the interpretation of an available AChE docking-score table. The aims were to reduce the candidate space without overstating model outputs and to establish a scientifically ordered path toward sequence traceability, independent computation, molecular dynamics (MD), and experimental validation.

## Materials and methods

### Study design and data sources

This was a computation-only secondary analysis of aggregate screening counts, model summaries, a twelve-sequence table, and a corresponding AChE docking-score table. No participant recruitment, specimen collection, wet-laboratory experiment, new omics processing, predictor retraining, or docking rerun was performed. MD trajectory analysis is ongoing as a predefined extension. The supplied healthy and periodontitis labels were retained as branch labels and were not treated as verified candidate-level disease assignments.

The public-accession context was examined to distinguish the source project from derived assemblies. PRJNA678453 is the project associated with paired oral metagenomic and metatranscriptomic measurements [@belstrom2021periodontitis]. PRJEB65451 is an EBI-EMG/MGnify-brokered Third Party Annotation metagenomic assembly project derived from PRJNA678453 with metaSPAdes v3.15.3, not an independent clinical cohort. Specific participant, specimen, assembly-analysis, and metagenome-assembled-genome totals were omitted because the available material lacked a consistent accession-to-group table, sample-to-assembly mapping, and bin-level manifest.

The available data did not include candidate nucleotide rows, complete peptide rows for the full funnel, genomic coordinates, sample mappings, taxonomic assignments, peptide-spectrum matches, complete predictor outputs, or the original discovery pipeline. These limitations precluded participant-level prevalence estimates, taxonomic attribution, disease-enrichment tests, and reconstruction of the exact candidate handoff between all model stages.

### smORF candidate definition and sequence-evidence filtering

Translated smORFs encoding 4–50-aa peptides were retained in the supplied analysis. Initial healthy-labelled and periodontitis-labelled libraries contained 11,269,961 and 11,721,988 candidates, respectively. Candidate sequences were exact-matched against named oral sequence and proteomic resources and then dereplicated, retaining 31,510 healthy-labelled and 33,786 periodontitis-labelled candidates. Exact matches were interpreted as support for sequence existence or prior observation within the relevant resource, not proof of expression in the analyzed disease-labelled branch.

The filtered libraries were divided into short (5–30 aa) and long (31–50 aa) branches. The healthy-labelled branch comprised 30,557 short and 953 long candidates; the periodontitis-labelled branch comprised 32,754 short and 1,032 long candidates. Although the initial definition included 4-aa peptides, the downstream bins began at 5 aa; the disposition of 4-aa sequences could not be determined from the supplied aggregate tables.

### Deep-learning-guided multi-model prioritization

UniDL4BioPep provided the first functional-prioritization layer. The documented architecture uses the pretrained ESM-2 model `esm2_t6_8M_UR50D` to encode each peptide as a 320-dimensional contextual representation, followed by a six-layer task-specific convolutional neural network for binary peptide-bioactivity classification [@du2023unidl4biopep]. An output threshold of ≥0.80 was applied, including for BBB prioritization. The output was termed “BBB-high” rather than BBB-permeable because model calibration and experimental transport were not available for this very-short microbiome-peptide domain.

The principal source also retained high-confidence counts for 22 UniDL4BioPep functional outputs separately in the short and long branches. These covered ACE inhibition, TTCA, BBB, anti-parasitic, NeuroPred, antibacterial, antifungal, antiviral, toxicity, antioxidant FRS, allergenicity, DPP-IV inhibition, cell penetration, bitter and umami taste, broad antimicrobial activity, two antimalarial outputs, quorum sensing, two anticancer outputs, and Anti-MRSA activity. Every task used the supplied ≥0.80 threshold. Counts and percentages were transcribed against the branch-specific backgrounds (long: 953 healthy-labelled and 1,032 periodontitis-labelled; short: 30,557 and 32,754); outputs were overlapping task labels and were not used as independent biological replicates or as evidence of between-group enrichment.

The periodontitis-labelled BBB-high set then entered the peptide mode of NTxPred2. This model fine-tunes the ESM2-t30 protein language model on neurotoxic-peptide sequences [@rathore2025ntxpred2]. Only peptides within the documented 7–50-aa input range were considered evaluated; shorter candidates were classified as outside model coverage rather than negative.

Mebipred evaluated Cu-, Fe-, and Zn-related binding potential. Unlike the ESM-based stages, mebipred combines amino-acid composition, physicochemical descriptors, and metal-binding 5-mer frequencies in a two-tier artificial-neural-network framework: a general metal-binding network is followed by ion-specific classifiers [@aptekmann2022mebipred]. A decision threshold of 0.50 was applied.

Antioxidant-related properties were evaluated with AnOxPePred, a multi-task deep convolutional neural network. One-hot-encoded peptide sequences pass through one-dimensional convolution, average pooling, and a 256-unit fully connected layer before separate free-radical-scavenging (FRS) and chelation (CHEL) outputs are generated [@olsen2020anoxpepred]. Three operational endpoints were retained: CHEL≥0.25; CHEL≥0.25 with FRS<0.50; and CHEL≥0.25 with FRS<0.45. Serial model agreement was treated as computational triage, not independent biological confirmation, because several models reuse sequence composition and were trained for heterogeneous endpoints.

### Sequence characterization and docking-score analysis

A separate table contained twelve peptide sequences described as the main CHEL/FRS candidate set. Their correspondence to the aggregate endpoint could not be established because stable identifiers and sequence-level CHEL/FRS outputs were unavailable. Length and counts of histidine, cysteine, basic residues (Arg+Lys), and aromatic residues (Phe+Tyr+Trp) were recalculated directly from each string. Uniqueness and use of standard amino acids were also checked.

AChE was selected as a structural context because its peripheral region has been linked to accelerated Aβ assembly [@inestrosa1996ache]. PDB 4EY6 provides an experimentally determined human AChE structure with ligand-bound information [@cheung2012ache]. The available docking table described AutoDock Vina 1.2.5 scores for twelve peptides. Vina is suitable for initial screening, but its scores depend on receptor preparation, ligand protonation, initial conformers, search-space placement, exhaustiveness, and stochastic sampling [@trott2010vina]. Later Vina implementations expand the available methods without eliminating these dependencies [@eberhardt2021vina]. Means and standard deviations were therefore analyzed descriptively and were not converted into affinities or free energies. Prepared structures, exact grid-center coordinates, run definitions, raw scores, logs, poses, and interaction tables were unavailable.

### Ongoing molecular-dynamics extension

A prespecified 100-ns MD extension covers apo human AChE and AChE complexes labelled for ALLLHRC, FLLHTTR, and YLSLLQR. Planned simulations use GROMACS [@abraham2015gromacs] with the Amber99SB-ILDN force field [@lindorfflarsen2010amber], TIP3P water, a triclinic periodic box with a 1.0-nm solute-to-boundary distance, neutralization, and 0.15 mol/L NaCl. Energy minimization comprises 2,000 steepest-descent steps with heavy-atom positional restraints. Equilibration comprises 1.0 ns restrained NVT heating from 10 to 300 K, 1.0 ns restrained NPT equilibration, and 1.0 ns unrestrained NPT equilibration at 300 K and 1 bar.

The production stage is specified as 100 ns with a 2-fs time step, LINCS constraints on hydrogen-containing bonds, particle-mesh Ewald electrostatics, velocity-rescale temperature coupling, and Berendsen pressure coupling. Coordinates are scheduled every 20 ps, yielding 5,000 planned frames per trajectory. Prespecified outputs include complex-, AChE-, and peptide-level RMSD/RMSF, radius of gyration, solvent-accessible surface area, secondary structure, radial distribution functions, hydrogen bonds, residue contacts, and bridging-water analyses. Trajectory processing and quality control are ongoing; the resulting stability, convergence, and contact measurements will be incorporated after the prespecified analysis is complete.

## Results

### Sequence-evidence filtering and BBB-high outputs

Sequence-evidence filtering retained 31,510/11,269,961 healthy-labelled candidates (0.2796%) and 33,786/11,721,988 periodontitis-labelled candidates (0.2882%). In the healthy-labelled branch, 3,359/30,557 short candidates (10.99%) and 40/953 long candidates (4.20%) were BBB-high. In the periodontitis-labelled branch, 3,446/32,754 short candidates (10.52%) and 72/1,032 long candidates (6.98%) were BBB-high, yielding 3,518 candidates in total. Short peptides represented 97.95% of this BBB-high set.

The supplied periodontitis-labelled length summary contained 547 candidates at 5–7 aa, 2,893 at 8–15 aa, 6 at 16–30 aa, and 72 at 31–50 aa. Thus, the prioritized set was dominated by short sequences. Missing row identities prevented assessment of sequence overlap, taxonomic distribution, or participant-level prevalence.

A broad antimicrobial output was nearly saturated: 30,537/30,557 healthy-labelled short candidates (99.93%) and 32,721/32,754 periodontitis-labelled short candidates (99.90%) exceeded the common 0.80 threshold. Such near-universal positivity is unlikely to represent the prevalence of experimentally active oral antibiotics and instead indicates possible domain shift, calibration limitations, or an unsuitable common threshold for that label.

### Long- and short-peptide multidimensional functional prediction results

The multidimensional summaries from the principal source were retained in compact form (Table 1). Long-branch percentages used 953 healthy-labelled and 1,032 periodontitis-labelled candidates; short-branch percentages used 30,557 and 32,754. Long-peptide outputs were led by Bitter (66.63%; 62.11%), Anti-parasitic (30.22%; 27.13%), and Antimicrobial (21.62%; 23.06%). Short-peptide Antimicrobial_activity was nearly saturated (99.93%; 99.90%), with large APP_Anti-parasitic, Quorum_sensing, and ACP_Anticancer_main outputs. The periodontitis-labelled short branch contained 3,446 BBB, 4,019 NeuroPred, and 4,728 Anti-MRSA high-confidence outputs. The source used slightly different model-label suffixes in the two branch summaries; Table 1 pairs the corresponding functional categories without treating them as calibrated or experimentally equivalent measurements.

**Table 1. Long- and short-peptide multidimensional functional outputs at UniDL4BioPep score ≥0.80.**

| Functional output | Long healthy n (%) | Long periodontitis n (%) | Short healthy n (%) | Short periodontitis n (%) |
| --- | ---: | ---: | ---: | ---: |
| Anticancer (alternative) | 91 (9.55%) | 121 (11.72%) | 7,878 (25.78%) | 8,380 (25.58%) |
| BBB | 40 (4.20%) | 72 (6.98%) | 3,359 (10.99%) | 3,446 (10.52%) |
| Quorum sensing | 173 (18.15%) | 190 (18.41%) | 11,834 (38.73%) | 12,674 (38.69%) |
| Antimicrobial | 206 (21.62%) | 238 (23.06%) | 30,537 (99.93%) | 32,721 (99.90%) |
| Antibacterial | 111 (11.65%) | 153 (14.83%) | 9,269 (30.33%) | 9,273 (28.31%) |
| Anti-MRSA | 47 (4.93%) | 62 (6.01%) | 4,315 (14.12%) | 4,728 (14.43%) |
| Cell-penetrating peptide | 15 (1.57%) | 29 (2.81%) | 4,435 (14.51%) | 4,133 (12.62%) |
| Antifungal | 73 (7.66%) | 96 (9.30%) | 8,732 (28.58%) | 8,475 (25.87%) |
| Toxicity | 13 (1.36%) | 18 (1.74%) | 2,770 (9.07%) | 2,751 (8.40%) |
| Umami | 17 (1.78%) | 15 (1.45%) | 6,095 (19.95%) | 6,094 (18.61%) |
| Antimalarial (alternative) | 12 (1.26%) | 14 (1.36%) | 1,724 (5.64%) | 1,695 (5.17%) |
| TTCA | 1 (0.10%) | 1 (0.10%) | 9,123 (29.86%) | 9,161 (27.97%) |
| Antioxidant FRS | 43 (4.51%) | 41 (3.97%) | 4,171 (13.65%) | 4,093 (12.50%) |
| DPP-IV inhibitory | 0 (0.00%) | 0 (0.00%) | 207 (0.68%) | 266 (0.81%) |
| Antimalarial (main) | 0 (0.00%) | 0 (0.00%) | 6,496 (21.26%) | 6,586 (20.11%) |
| Anti-parasitic | 288 (30.22%) | 280 (27.13%) | 21,185 (69.33%) | 22,010 (67.20%) |
| NeuroPred | 82 (8.60%) | 77 (7.46%) | 3,876 (12.68%) | 4,019 (12.27%) |
| Anticancer (main) | 37 (3.88%) | 31 (3.00%) | 11,370 (37.21%) | 12,023 (36.71%) |
| ACE inhibitory | 20 (2.10%) | 14 (1.36%) | 2,781 (9.10%) | 2,856 (8.72%) |
| Allergenicity | 16 (1.68%) | 11 (1.07%) | 8,599 (28.14%) | 9,422 (28.77%) |
| Antiviral | 55 (5.77%) | 52 (5.04%) | 7,501 (24.55%) | 7,221 (22.05%) |
| Bitter | 635 (66.63%) | 641 (62.11%) | 5,037 (16.48%) | 4,986 (15.22%) |


### Serial model prioritization

NTxPred2 evaluated 3,299/3,518 periodontitis-labelled BBB-high candidates (93.77%); 219/3,518 (6.23%) were outside the stated length range. Among evaluated candidates, 923/3,299 (27.98%) were model-positive. Subsequent aggregate filters retained 111 mebipred-positive candidates, 15 candidates with CHEL≥0.25, 12 candidates with CHEL≥0.25 and FRS<0.50, and 8 candidates with CHEL≥0.25 and FRS<0.45 (Table 2). Tightening the FRS threshold retained 8/12 (66.67%) of the main count. Because candidate-level handoff data were unavailable, 111/923 was not interpreted as a verified transition rate.

All 923 NTxPred2-positive candidates were reported to be ≤30 aa. Consequently, none of the 72 periodontitis-labelled, metaproteome-supported and dereplicated 31–50-aa BBB-high long peptides remained in the neurotoxicity-positive set that fed the downstream mebipred and AnOxPePred metal/CHEL/FRS filters. The aggregate 12-candidate endpoint therefore contained only short peptides. Row-level outputs were unavailable, so the exclusion reason for each long peptide could not be reconstructed.

**Table 2. Aggregate computational prioritization results.**

| Stage | Operational rule | n | Denominator or limitation |
| --- | --- | ---: | --- |
| Healthy-labelled smORFs | 4–50 aa | 11,269,961 | Initial library |
| Periodontitis-labelled smORFs | 4–50 aa | 11,721,988 | Initial library |
| Evidence-filtered healthy-labelled | Exact match and dereplication | 31,510 | 11,269,961 |
| Evidence-filtered periodontitis-labelled | Exact match and dereplication | 33,786 | 11,721,988 |
| BBB-high short | UniDL4BioPep output≥0.80; 5–30 aa | 3,446 | 32,754 |
| BBB-high long | UniDL4BioPep output≥0.80; 31–50 aa | 72 | 1,032 |
| BBB-high total | Short + long | 3,518 | Arithmetic sum |
| NTxPred2 evaluated | 7–50 aa | 3,299 | 3,518 |
| NTxPred2-positive | Model-positive label | 923 | 3,299 |
| Metal-binding-positive | Mebipred output≥0.50 | 111 | Row-level handoff unavailable |
| CHEL-priority | CHEL≥0.25 | 15 | 111 |
| Main set | CHEL≥0.25 and FRS<0.50 | 12 | 111 |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | Sequence membership unavailable |

### Twelve-sequence set and docking-score ordering

The separate table contained twelve unique peptides composed of standard amino acids and ranging from 7 to 9 residues. Eleven contained histidine, six contained cysteine, and every sequence contained at least one Arg or Lys. These properties provide plausible synthesis and coordination hypotheses but do not establish metal binding, BBB transport, toxicity, taxonomy, or correspondence to the aggregate endpoint.

Vina means ranged from −9.60 to −8.25 kcal/mol, with standard deviations from 0.04 to 0.12 (Table 3). FLLHTTR, YLSLLQR, and ALLLHRC had the three lowest means; HLPLLHRCC and HVLLLRQCA had the two highest. The 1.35-kcal/mol span describes only this scoring table. The run-level denominator for the standard deviations was unavailable, and no residue-level interaction could be evaluated without poses.

**Table 3. Twelve-sequence set and available AChE docking scores.**

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

### Principal findings

This analysis reconstructs a computational funnel that reduces a multimillion-candidate smORF space to an aggregate main set of 12 and a stricter count of 8. It also characterizes a separate twelve-sequence set and preserves the ordering of an available AChE docking table. The main scientific contribution is not validation of a periodontal–AD mechanism; it is the definition of a bounded candidate set, explicit model-applicability limits, and an ordered strategy for recovering the missing sequence-level and experimental evidence.

### Interpretation of the model cascade

The cascade integrates modern neural architectures but should not be viewed as repeated independent confirmation. UniDL4BioPep and NTxPred2 both rely on protein-language-model representations, whereas mebipred and AnOxPePred incorporate composition-derived information. Correlated sequence features can therefore propagate through successive filters. Training datasets also differ in endpoint definition, sequence length, redundancy reduction, class balance, and negative-set construction. These issues are especially important for leucine-rich, cationic, 7–9-aa microbiome peptides that may lie outside the training distribution.

The near-saturated antimicrobial output provides an internal warning about calibration. It does not invalidate all rankings, but it shows that a common probability threshold can have very different meanings across tasks. Accordingly, “BBB-high,” “neurotoxicity-positive,” “metal-binding-positive,” CHEL, and FRS are operational model labels. They do not equal transport, neuronal injury, binding constants, coordination geometry, or redox activity.

### AChE, metal, and peptide-structure hypotheses

AChE is biologically relevant because its peripheral region can influence Aβ assembly, but this context does not convert a docking score into target engagement. Flexible peptides have many accessible conformers, and docking ranks can change with protonation, terminal state, receptor flexibility, initial structure, and search settings. Independent reproduction should include prepared receptor and ligand files, multiple starting conformers, explicit random seeds, all raw scores and poses, and peptide-specific flexible refinement such as FlexPepDock [@london2011flexpepdock]. The ongoing MD extension can then assess contact persistence and conformational behavior from documented starting complexes rather than substitute for uncertain docking preparation.

Histidine and cysteine enrichment provides plausible metal-coordination groups. However, sequence composition cannot determine affinity, stoichiometry, ion selectivity, coordination geometry, oxidation state, or redox consequence. Direct measurements should compare Cu(II), Fe(II/III), and Zn(II) under controlled pH and stoichiometry and should include spectroscopy, thermodynamic measurements, reactive-oxygen-species assays, and lipid-peroxidation endpoints. Peptide-only, metal-only, scrambled-sequence, composition-matched, and established positive and negative controls are required.

### Periodontal and AD interpretation

The periodontal context remains hypothesis-generating. Human associations are vulnerable to age, smoking, diabetes, medication, frailty, socioeconomic conditions, oral-care access, and reverse causation. Experimental *P. gingivalis* systems demonstrate selected possibilities at defined doses and exposure routes, but these findings cannot be assigned to untraced community peptides. The current labels do not show that any sequence is periodontitis-specific, *P. gingivalis*-encoded, expressed in the source oral community, present in circulation, or delivered to the brain.

A credible molecular chain requires sequence-to-contig or assembly mapping, sample and clinical-group assignment, taxonomic resolution, cohort-matched transcription or translation evidence, systemic exposure, BBB transport, and a reproducible target or cellular phenotype. Each step answers a distinct question and cannot be replaced by accumulating additional in silico scores.

### Validation priorities and limitations

The first priority is to recover a candidate-level table linking sequence, stable identifier, genomic coordinates, assembly, sample, group, taxonomy, peptide-spectrum evidence, every predictor score and applicability flag, CHEL/FRS values, main/strict membership, and docking ligand identity. This would resolve whether the twelve explicit sequences are the same twelve candidates represented by the aggregate endpoint and identify the stricter subset of eight.

After fixed-version computational reproduction, synthesized peptides should undergo identity, purity, solubility, aggregation, and serum/protease-stability testing. BBB transport and cytotoxicity should be evaluated separately using concentration–response designs and non-neuronal controls. Metal chemistry, AChE/BChE activity, direct binding, and Aβ aggregation should then be tested under prespecified conditions. The ongoing MD extension will contribute trajectory-derived stability and contact measurements after quality control, but disease models should be considered only after molecular identity, exposure, reproducible biochemical activity, and biologically replicated phenotypes have been established.

A further pipeline limitation is the length-dependent attrition introduced after BBB prioritization. Although 72 metaproteome-supported and dereplicated long peptides were BBB-high in the periodontitis-labelled branch, all 923 NTxPred2-positive sequences were ≤30 aa; the downstream web-predictor cascade for metal binding and CHEL/FRS therefore retained no long peptide, and the final aggregate set of 12 consisted only of short peptides. This pattern does not show that long peptides biologically lack neurotoxicity or metal-related activity. It may reflect the serial thresholds, model applicability or calibration, and web-predictor implementation; without candidate-level scores, these explanations cannot be separated.

The decisive limitations are the absence of row-level funnel data, unresolved membership of the aggregate 12 and 8 endpoints, lack of raw docking inputs and poses, ongoing MD trajectory analysis, and absence of biological measurements. The similar aggregate retention rates in the healthy-labelled and periodontitis-labelled libraries cannot support disease enrichment because the participant or sample is the appropriate inferential unit. These constraints limit the present work to computational prioritization and validation planning.

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
16. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
17. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
18. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
19. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
20. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
21. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
22. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
