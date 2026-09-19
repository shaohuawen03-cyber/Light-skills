# Periodontitis-derived micropeptides occupy the acetylcholinesterase peripheral anionic site: computational screening, docking, and 100-ns molecular dynamics

## Abstract

Periodontitis-associated oral dysbiosis has been linked to Alzheimer’s disease (AD), but a peptide-level path from the oral microbiome to a defined synaptic enzyme remains incomplete. This computation-only study joins an oral small open reading frame (smORF) screening cascade with local AutoDock Vina docking of twelve 7–9-aa candidate micropeptides into human acetylcholinesterase (AChE, PDB 4EY6) and 100-ns all-atom molecular dynamics (MD) of apo AChE versus three complexes (ALLLHRC, FLLHTTR, YLSLLQR). UniDL4BioPep first scored 11,269,961 healthy-labelled and 11,721,988 periodontitis-labelled smORFs on 22 tasks (periodontitis BBB (BBP) ≥0.80: 1,125,832; 9.60%). Metaproteome matching then intersected periodontitis BBB-high predictions with evidence-supported unique peptides, recovering 3,518 candidates; 923 were NTxPred2-positive, and later filters produced a twelve-sequence set. Local three-run Vina scores ranged from -8.25 to -9.60 kcal/mol (best run) and from -8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol (mean ± SD). FLLHTTR had the strongest best pose but the largest run-to-run SD; YLSLLQR had the strongest mean and, with FLLHTTR and LLHPLRL, contacted the peripheral anionic site (PAS). Over 100 ns the three complexes remained globular (backbone RMSD 0.16–0.19 nm; α-helix ~33%, β-sheet ~17%). FLLHTTR and YLSLLQR complexes were more stable than apo (0.1640 and 0.1625 nm versus 0.1897 nm). FLLHTTR formed the densest hydrogen-bond network (7.03 ± 1.28); only YLSLLQR contracted SASA (209.71 versus 212.25 nm²). Taken together, the poses and trajectories support a possible pathogenic mechanism: periodontitis-derived micropeptides occupy the AChE PAS, impede acetylcholine access, and act as heterologous seeds that co-nucleate endogenous Aβ on the same pro-fibrillar surface.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral micropeptide; smORF; acetylcholinesterase; peripheral anionic site; molecular docking; molecular dynamics

## Introduction

Alzheimer’s disease is a progressive neurodegenerative disorder in which amyloid-β (Aβ), tau, synaptic failure, immune activation, and vascular injury interact rather than acting as a single linear cascade [@scheltens2021alzheimer]. Amyloid biology remains central: APP cleavage by β- and γ-secretases yields Aβ40/Aβ42, soluble oligomers damage synapses, and familial APP/PSEN mutations change Aβ production and length [@selkoe2016amyloid]. Loss of basal-forebrain cholinergic transmission contributes to cognitive symptoms, and AChE inhibitors remain established symptomatic treatments [@hampel2018cholinergic]. Independently of catalysis, AChE accelerates Aβ fibril assembly through its peripheral anionic site (PAS) and yields AChE–Aβ complexes that are more neurotoxic than Aβ alone [@inestrosa1996ache]. A hydrophobic PAS motif promotes that chaperone activity [@deferrari2001motif]. These facts identify the AChE PAS as the structural node that can couple cholinergic failure to amyloid deposition.

Chronic periodontitis can sustain systemic inflammatory burden and episodic exposure to microbial products, motivating an oral–brain axis [@chalmers2025primer]. Disease-associated oral activity is species- and site-specific, so taxonomic abundance cannot substitute for a molecular intermediate [@belstrom2021periodontitis]. *Porphyromonas gingivalis* gingipains and outer-membrane vesicles provide one well-studied virulence context [@guo2010gingipain; @ho2015omv]. Observational syntheses associate periodontal disease with cognitive disorders, with effect estimates that vary by case definition and adjustment [@larvin2023periodontalcognition], and periodontitis has been linked to subsequent decline in an AD cohort [@ide2016periodontitis]. *P. gingivalis* and gingipains have been reported in AD brains [@dominy2019pgingivalis], and repeated oral exposure in mice can drive neuroinflammation and Aβ-related changes [@ilievski2018oral]. These observations supply an oral–brain exposure context in which a peptide-level ligand of AChE would be mechanistically consequential [@hu2024mendelian].

Microbiome-encoded small proteins are a large, still poorly mapped candidate space [@sberro2019smallgenes; @durrant2021sorf]. Whether any periodontitis-derived 7–9-aa micropeptide can occupy the same AChE PAS that binds Aβ is a structural question that screening scores alone cannot answer. Accelerated MD of human AChE with multiple Aβ chains showed Aβ attracted to the enzyme surface, supporting AChE as a nucleation centre [@lushchekina2017amd]. A 1-μs PAS-centered AChE–Aβ trajectory remained bound, with principal residence at PAS-adjacent residues 344–361 [@atanasova2020md]. PAS-directed ligands can inhibit AChE-induced Aβ aggregation in biochemical systems [@bartolini2003pas], and PDB 4EY6 provides a 2.40 Å human AChE structure for docking [@cheung2012ache].

This study therefore asks whether periodontitis-derived 7–9-aa micropeptides can occupy the same PAS that experimentally accelerates Aβ assembly. An oral-smORF cascade first prioritizes twelve sequences; those peptides are then docked into human AChE, and three representative complexes are simulated for 100 ns against apo AChE, in order to outline a possible molecular path from oral pathogenic peptides to AD.

## Materials and methods

### Study design

This was a computation-only analysis. Screening used aggregate smORF counts, model summaries, and a twelve-sequence table; no participant recruitment, specimen collection, predictor retraining, or new omics processing was performed. Healthy and periodontitis labels were retained as library labels and were not treated as verified peptide-level disease assignments. Docking and MD used local three-run AutoDock Vina poses and 100-ns GROMACS trajectories of apo AChE and the three selected complexes.

### Oral smORF screening cascade

Translated smORFs encoding 4–50-aa peptides formed the starting libraries (11,269,961 healthy-labelled and 11,721,988 periodontitis-labelled sequences; PRJNA678453) [@belstrom2021periodontitis]. In line with antimicrobial-peptide discovery workflows [@torres2024peptideantibiotics], UniDL4BioPep was applied first to both full libraries [@du2023unidl4biopep]: ESM-2 (`esm2_t6_8M_UR50D`) embeddings and 22 task-specific convolutional networks, each with a decision threshold of ≥0.80. Unified task names are ACE inhibitory, DPP-IV inhibitory, Bitter, Umami, Antimicrobial, Antimalarial (alternative), Antimalarial (main), Quorum sensing, Anticancer (main), Anticancer (alternative), Anti-MRSA, TTCA, BBB (BBP), Anti-parasitic (APP), NeuroPred, Antibacterial, Antifungal, Antiviral, Toxicity, Antioxidant FRS, Allergenicity, and cell-penetrating peptide (CPP). BBB (BBP) ≥0.80 defined the operational BBB-high set.

After UniDL4BioPep scoring, sequences were exact-matched against oral genomic and metaproteomic resources, including HOMD and salivary metaproteome catalogues, and dereplicated [@chen2010homd; @belstrom2016metaproteomics]. The healthy-labelled library yielded 31,510 evidence-supported unique peptides and the periodontitis-labelled library 33,786. Intersection of the periodontitis BBB (BBP) set (1,125,832) with the periodontitis evidence-supported peptides recovered 3,518 candidates (3,446 short, 5–30 aa; 72 long, 31–50 aa). Peptides in that intersection within 7–50 aa were evaluated with NTxPred2 (ESM2-t30) [@rathore2025ntxpred2]. Mebipred applied a two-tier neural network to Cu-, Fe-, and Zn-related binding potential at a 0.50 threshold [@aptekmann2022mebipred]. AnOxPePred supplied multi-task free-radical-scavenging (FRS) and chelation (CHEL) outputs [@olsen2020anoxpepred]; serial endpoints were CHEL≥0.25, CHEL≥0.25 with FRS<0.50, and CHEL≥0.25 with FRS<0.45.

A separate table listed twelve unique 7–9-aa sequences. Length and counts of histidine, cysteine, and basic residues were recalculated from each string.

### Molecular docking

Human recombinant AChE (rhAChE, PDB 4EY6, 2.40 Å) [@cheung2012ache] was prepared by removing galantamine and crystallographic waters, repairing internal chain breaks, and assigning physiological protonation (pH 7.4). The twelve peptides ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, HVLLLRQCA, LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR were docked with AutoDock Vina (exhaustiveness = 32) [@trott2010vina; @eberhardt2021vina] into a grid centered on the PAS (Tyr72, Asp74, Thr75, Leu76, Trp286, His287, Tyr341) and spanning the gorge neck (Phe295), choline-binding subsite (Trp86, Glu202, Tyr337), and catalytic triad (Ser203, His447, Glu334). Each ligand was run three times (`N_Success` = 3). Best-run affinity, three-run mean ± SD, hydrogen-bond geometry, and PAS contacts were taken from the local three-run summary and the single best-scoring pose of each ligand. Vina scores are empirical ranking metrics, not experimental free energies.

### Molecular dynamics

Four explicit-solvent GROMACS systems [@abraham2015gromacs] were simulated with Amber99SB-ILDN [@lindorfflarsen2010amber] and TIP3P water at 0.15 M NaCl: apo AChE (Chain A) and the AChE–ALLLHRC, AChE–FLLHTTR, and AChE–YLSLLQR complexes. Each system used a triclinic box with a 1.0 nm solute-to-boundary buffer. Equilibration comprised 2,000-step steepest-descent minimization, 1.0 ns restrained NVT heating to 300 K, 1.0 ns restrained NPT density equilibration, and 1.0 ns unrestrained NPT pre-equilibration. Production ran 100 ns (dt = 2.0 fs) in the NPT ensemble (300 K, 1.0 bar) with LINCS, 1.2 nm cutoffs, and Particle Mesh Ewald electrostatics. Frames were written every 20 ps.

Trajectory metrics matching Figures 4–6 were backbone Cα RMSD, per-residue RMSF, solvent-accessible surface area (SASA), radius of gyration (Rg), DSSP occupancy, and intermolecular hydrogen bonds (`gmx hbond`; donor–acceptor ≤ 3.0 Å). Peptide self-fit RMSD and persistent interfacial contacts (7.0 Å cutoff) were recorded as supporting descriptors. Steady-state values are mean ± SD over the final 20 ns (80.0–100.0 ns). The protocol follows the AChE–Aβ MD logic of Atanasova and colleagues at a 100-ns rather than 1-μs window [@atanasova2020md].

## Results

### Screening funnel and twelve-sequence composition

UniDL4BioPep scored both starting libraries on 22 tasks at ≥0.80. The complete periodontitis-labelled counts are in Table 1 and the complete healthy-labelled counts in Table 2. Hit rates were similar: Antimicrobial 10,302,093/11,721,988 periodontitis-labelled sequences (87.89%) versus 9,882,657/11,269,961 healthy-labelled sequences (87.69%); BBB (BBP) 1,125,832 (9.60%) versus 1,095,861 (9.72%). In both libraries the largest outputs were Antimicrobial, Anti-parasitic (APP), and Quorum sensing; DPP-IV inhibitory was the smallest. Task labels overlap; a peptide may count in more than one row. Subsequent prioritization used the periodontitis-labelled branch.

**Table 1. UniDL4BioPep outputs on the periodontitis-labelled library (11,721,988 smORFs; threshold ≥0.80).**

| No. | UniDL4BioPep task | n (≥0.80) | % of 11,721,988 |
| --- | --- | ---: | ---: |
| 1 | ACE inhibitory | 1,236,442 | 10.55 |
| 2 | DPP-IV inhibitory | 139,056 | 1.19 |
| 3 | Bitter | 1,831,185 | 15.62 |
| 4 | Umami | 3,100,811 | 26.45 |
| 5 | Antimicrobial | 10,302,093 | 87.89 |
| 6 | Antimalarial (alternative) | 695,608 | 5.93 |
| 7 | Antimalarial (main) | 2,010,724 | 17.15 |
| 8 | Quorum sensing | 4,491,507 | 38.32 |
| 9 | Anticancer (main) | 2,357,718 | 20.11 |
| 10 | Anticancer (alternative) | 2,015,652 | 17.20 |
| 11 | Anti-MRSA | 843,977 | 7.20 |
| 12 | TTCA | 2,666,759 | 22.75 |
| 13 | BBB (BBP) | 1,125,832 | 9.60 |
| 14 | Anti-parasitic (APP) | 5,462,493 | 46.60 |
| 15 | NeuroPred | 1,714,373 | 14.63 |
| 16 | Antibacterial | 2,597,877 | 22.16 |
| 17 | Antifungal | 2,960,118 | 25.25 |
| 18 | Antiviral | 3,275,203 | 27.94 |
| 19 | Toxicity | 1,714,299 | 14.62 |
| 20 | Antioxidant FRS | 2,521,106 | 21.51 |
| 21 | Allergenicity | 1,713,798 | 14.62 |
| 22 | Cell-penetrating peptide (CPP) | 925,627 | 7.90 |

**Table 2. UniDL4BioPep outputs on the healthy-labelled library (11,269,961 smORFs; threshold ≥0.80).**

| No. | UniDL4BioPep task | n (≥0.80) | % of 11,269,961 |
| --- | --- | ---: | ---: |
| 1 | ACE inhibitory | 1,237,451 | 10.98 |
| 2 | DPP-IV inhibitory | 131,426 | 1.17 |
| 3 | Bitter | 1,840,368 | 16.33 |
| 4 | Umami | 3,094,287 | 27.46 |
| 5 | Antimicrobial | 9,882,657 | 87.69 |
| 6 | Antimalarial (alternative) | 703,632 | 6.24 |
| 7 | Antimalarial (main) | 1,954,667 | 17.34 |
| 8 | Quorum sensing | 4,161,825 | 36.93 |
| 9 | Anticancer (main) | 2,404,084 | 21.33 |
| 10 | Anticancer (alternative) | 1,979,643 | 17.57 |
| 11 | Anti-MRSA | 769,955 | 6.83 |
| 12 | TTCA | 2,618,849 | 23.24 |
| 13 | BBB (BBP) | 1,095,861 | 9.72 |
| 14 | Anti-parasitic (APP) | 5,517,278 | 48.96 |
| 15 | NeuroPred | 1,690,436 | 15.00 |
| 16 | Antibacterial | 2,658,234 | 23.59 |
| 17 | Antifungal | 3,128,057 | 27.76 |
| 18 | Antiviral | 3,362,295 | 29.83 |
| 19 | Toxicity | 1,725,268 | 15.31 |
| 20 | Antioxidant FRS | 2,643,538 | 23.46 |
| 21 | Allergenicity | 1,635,019 | 14.51 |
| 22 | Cell-penetrating peptide (CPP) | 1,029,770 | 9.14 |

Metaproteome exact-match and dereplication of the periodontitis-labelled library retained 33,786 evidence-supported unique peptides (healthy-labelled: 31,510/11,269,961). Intersection of the 1,125,832 BBB (BBP) predictions with that evidence-supported set recovered 3,518 peptides (3,446 short, 72 long). NTxPred2 evaluated 3,299/3,518 (93.77%) and classified 923/3,299 (27.98%) as model-positive. Subsequent filters retained 111 mebipred-positive candidates, 15 with CHEL≥0.25, 12 with CHEL≥0.25 and FRS<0.50, and 8 with CHEL≥0.25 and FRS<0.45 (Table 3).

**Table 3. Serial prioritization after UniDL4BioPep prediction and metaproteome intersection.**

| Stage | Operational rule | n | Denominator |
| --- | --- | ---: | ---: |
| Periodontitis-labelled smORFs | 4–50 aa | 11,721,988 | Initial library |
| UniDL4BioPep BBB (BBP) | score ≥0.80 | 1,125,832 | 11,721,988 |
| Evidence-supported unique peptides | Exact match and dereplication | 33,786 | 11,721,988 |
| BBB-high ∩ evidence-supported | Intersection | 3,518 | 1,125,832 ∩ 33,786 |
| Short (5–30 aa) | Length bin | 3,446 | 3,518 |
| Long (31–50 aa) | Length bin | 72 | 3,518 |
| NTxPred2 evaluated | 7–50 aa | 3,299 | 3,518 |
| NTxPred2-positive | Model-positive | 923 | 3,299 |
| Metal-binding-positive | Mebipred ≥0.50 | 111 | — |
| CHEL-priority | CHEL≥0.25 | 15 | 111 |
| Main set | CHEL≥0.25 and FRS<0.50 | 12 | 111 |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | — |

The twelve explicit sequences are unique 7–9-aa peptides of standard amino acids (Table 4). Eleven contain histidine, six contain cysteine, and every sequence contains at least one Arg or Lys. All 923 NTxPred2-positive peptides were ≤30 aa, so the downstream metal/CHEL/FRS filters retained only short peptides.

**Table 4. Composition of the twelve 7–9-aa candidate micropeptides.**

| No. | Sequence | Length | His | Cys | Arg+Lys |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | ALLLHRC | 7 | 1 | 1 | 1 |
| 2 | FCLHLQLR | 8 | 1 | 1 | 1 |
| 3 | FLLHTTR | 7 | 1 | 0 | 1 |
| 4 | HLLTLKKHV | 9 | 2 | 0 | 2 |
| 5 | HLPLLHRCC | 9 | 1 | 2 | 1 |
| 6 | HVLLLRQCA | 9 | 1 | 1 | 1 |
| 7 | LLHLPKRTT | 9 | 1 | 0 | 2 |
| 8 | LLHPLRC | 7 | 1 | 1 | 1 |
| 9 | LLHPLRL | 7 | 1 | 0 | 1 |
| 10 | WLLVHLKK | 8 | 1 | 0 | 2 |
| 11 | YHHLLCRR | 8 | 2 | 1 | 2 |
| 12 | YLSLLQR | 7 | 0 | 0 | 1 |

### Local three-run docking and PAS engagement

All twelve ligands yielded favorable local Vina scores. Best-run affinities ranged from -8.25 to -9.60 kcal/mol and three-run means from -8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol (Table 5, Figure 1). Best-pose ranking placed FLLHTTR first (-9.60 kcal/mol), then YLSLLQR (-9.49 kcal/mol) and ALLLHRC (-9.29 kcal/mol). Mean ranking placed YLSLLQR first (-9.44 ± 0.09 kcal/mol) and ALLLHRC second (-9.18 ± 0.11 kcal/mol). FLLHTTR retained the strongest single pose but the largest run-to-run SD (-8.77 ± 1.41 kcal/mol). Best poses formed 3–10 hydrogen bonds (mean length 2.83–3.28 Å; Figures 2 and 3; Figure S1).

**Table 5. Local AutoDock Vina scores and PAS engagement of twelve candidate micropeptides against human AChE (PDB 4EY6).**

| No. | Peptide | HBonds | Key residues | Best (kcal/mol) | Mean ± SD, n=3 (kcal/mol) | PAS engagement |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ALLLHRC | 3 | SER-125, SER-203, TYR-124 | -9.29 | -9.18 ± 0.11 | No; catalytic Ser203 / gorge neck |
| 2 | FCLHLQLR | 7 | SER-203, THR-75, TYR-124, TYR-337, TYR-341 | -9.27 | -8.96 ± 0.48 | Yes; Thr75, Tyr341 |
| 3 | FLLHTTR | 8 | ASP-74, HIS-287, LEU-289, PHE-295, TYR-337, TYR-72 | -9.60 | -8.77 ± 1.41 | Yes; extensive PAS (Asp74, Tyr72, His287); largest SD |
| 4 | HLLTLKKHV | 6 | PHE-346, TYR-124, TYR-337, TYR-72, TYR-77 | -8.88 | -8.69 ± 0.20 | Yes; Tyr72 and 344–361 (Phe346) |
| 5 | HLPLLHRCC | 4 | SER-125, TYR-124, TYR-337 | -8.35 | -8.28 ± 0.07 | No; gorge rim |
| 6 | HVLLLRQCA | 4 | SER-125, THR-75, TYR-124 | -8.25 | -8.07 ± 0.16 | Yes; Thr75 |
| 7 | LLHLPKRTT | 3 | SER-203, TYR-337, VAL-340 | -9.01 | -8.89 ± 0.16 | PAS-adjacent (Val340) |
| 8 | LLHPLRC | 4 | SER-125, SER-293, TYR-124 | -8.91 | -8.78 ± 0.11 | No; gorge entrance |
| 9 | LLHPLRL | 10 | HIS-447, PHE-295, TRP-286, TYR-124, TYR-337, TYR-341 | -8.94 | -8.91 ± 0.05 | Yes; dual-site PAS to His447; smallest SD |
| 10 | WLLVHLKK | 4 | ASN-283, GLN-279, SER-293, TYR-124 | -8.94 | -8.64 ± 0.26 | No; outer loops |
| 11 | YHHLLCRR | 7 | SER-125, SER-203, TRP-86, TYR-124, TYR-337 | -9.03 | -8.62 ± 0.43 | No; choline pocket Trp86 |
| 12 | YLSLLQR | 7 | GLU-202, SER-203, THR-75, TYR-124, TYR-337, TYR-72 | -9.49 | -9.44 ± 0.09 | Yes; PAS plus catalytic entrance; strongest mean |

![Figure 1. Local AutoDock Vina scores of twelve candidate micropeptides against human AChE.](../figures/fig5_docking_scores.png)

**Figure 1. Local AutoDock Vina scores of twelve candidate micropeptides against human AChE (PDB 4EY6).** Blue circles show the three-run mean; whiskers show the standard deviation; orange diamonds mark the best-run affinity. Order matches best-run ranking.

![Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA.](../figures/fig_docking_poses_A_F.png)

**Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA (panels A–F).** Peptide, orange; contacting AChE residues, cyan; hydrogen bonds, dashed. FLLHTTR (panel C) is the densest PAS pose.

![Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR.](../figures/fig_docking_poses_G_L.png)

**Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR (panels G–L).** LLHPLRL (panel I) spans PAS Trp286/Tyr341 to catalytic His447; YLSLLQR (panel L) bridges PAS and the catalytic entrance.

![Figure S1. Combined overview of all twelve best-scoring docking poses.](../figures/fig_docking_poses_12_combined.png)

**Figure S1. Combined overview of all twelve best-scoring docking poses.** Single-page layout of panels A–L.

Canonical PAS binders in the best pose were FLLHTTR (Figure 2C), YLSLLQR (Figure 3L), FCLHLQLR, HVLLLRQCA, HLLTLKKHV, and LLHPLRL (Figure 3I). ALLLHRC bound catalytic Ser203 with the shortest mean hydrogen bond (2.83 Å) rather than the outer PAS aromatic core (Figure 2A). Three-run means distinguish reproducible high-affinity ligands (YLSLLQR, ALLLHRC, LLHPLRL) from ligands whose best pose is stronger than the run-averaged score (FLLHTTR, FCLHLQLR, YHHLLCRR).

### 100-ns molecular dynamics of apo AChE and three complexes

Production trajectories were completed for apo AChE and the ALLLHRC, FLLHTTR, and YLSLLQR complexes (Table 6, Figures 4–6). Each six-panel figure compares the unliganded control with one peptide complex: backbone RMSD (A), per-residue RMSF (B), SASA (C), Rg (D), DSSP occupancy over the last 20 ns (E), and intermolecular hydrogen bonds (F).

<!-- PAGEBREAK -->

![Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns comparison.](../figures/fig_compare_mixed_ache_vs_alllhrc.png)

**Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns molecular dynamics comparison.** Panels A–F match the metrics in Table 6. Complex RMSD (A) closely follows apo; hydrogen bonds (F) decay from early high occupancy to ~2 in the last 20 ns.

![Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns comparison.](../figures/fig_compare_mixed_ache_vs_fllhttr.png)

**Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns molecular dynamics comparison.** Panel layout matches Figure 4. After ~50 ns, complex RMSD (A) lies below apo; hydrogen-bond counts (F) remain dense (~6–10) throughout 100 ns.

![Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns comparison.](../figures/fig_compare_mixed_ache_vs_ylsllqr.png)

**Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns molecular dynamics comparison.** Panel layout matches Figure 4. Late RMSD (A) lies below apo; SASA (C) is the only complex that contracts relative to apo.

**Table 6. Final-20-ns trajectory metrics for apo AChE and three peptide complexes (mean ± SD), aligned to Figures 4–6.**

| Metric (last 20 ns) | apo AChE | AChE–ALLLHRC | AChE–FLLHTTR | AChE–YLSLLQR |
| --- | --- | --- | --- | --- |
| Backbone Cα RMSD (nm); Figure panels A | 0.1897 ± 0.0090 | 0.1916 ± 0.0092 | 0.1640 ± 0.0080 | 0.1625 ± 0.0078 |
| Peptide self-fit RMSD (nm) | N/A | 0.2518 ± 0.0136 | 0.1752 ± 0.0111 | 0.0911 ± 0.0098 |
| Per-residue RMSF mean (nm); Figure panels B | 0.0835 ± 0.0659 | 0.0876 ± 0.0581 | 0.0778 ± 0.0504 | 0.0771 ± 0.0498 |
| SASA (nm²); Figure panels C | 212.25 ± 2.89 | 217.47 ± 2.49 | 213.88 ± 2.36 | 209.71 ± 2.35 |
| Rg (nm); Figure panels D | 2.3045 ± 0.0056 | 2.3107 ± 0.0052 | 2.2967 ± 0.0047 | 2.3028 ± 0.0051 |
| Intermolecular H-bonds; Figure panels F | N/A | 2.19 ± 0.80 | 7.03 ± 1.28 | 2.93 ± 1.14 |
| Persistent contact pairs | N/A | 7 | 7 | 7 |
| DSSP α-helix / β-sheet (%); Figure panels E | 33.44 / 17.35 | 33.66 / 16.76 | 32.92 / 17.52 | 33.31 / 17.02 |

Figures 4A, 5A, and 6A show that apo RMSD plateaus near 0.19 nm. ALLLHRC closely follows that control (complex 0.1916 nm; AChE-only 0.1883 nm). FLLHTTR and YLSLLQR fall below apo after ~50–70 ns (complex 0.1640 and 0.1625 nm; AChE-only 0.1609 and 0.1607 nm), indicating that peptide binding rigidifies rather than loosens the fold. Peptide self-fit RMSD is highest for ALLLHRC (0.2518 nm) and lowest for YLSLLQR (0.0911 nm). RMSF (panels B) stays low in the catalytic core; the largest excursion is the apo C-terminus, and mean RMSF is lower than apo for FLLHTTR (0.0778 nm) and YLSLLQR (0.0771 nm). Rg (panels D) remains 2.30–2.31 nm. SASA (panels C) rises for ALLLHRC (217.47 nm²), is near apo for FLLHTTR (213.88 nm²), and uniquely contracts for YLSLLQR (209.71 nm²; Figure 6C). Hydrogen bonds persist in every panel F, but the networks differ: ALLLHRC decays from early occupancy of ~6–10 to 2.19 ± 0.80 in the last 20 ns; FLLHTTR holds 7.03 ± 1.28 throughout (Figure 5F); YLSLLQR averages 2.93 ± 1.14. DSSP helix (~33%) and sheet (~17%) overlay the apo bars in panels E. Each complex retains seven persistent contact pairs. Center-of-mass RDF peaks remain at 1.22 nm (ALLLHRC), 1.80 nm (FLLHTTR), and 1.62 nm (YLSLLQR), consistent with surface rather than bulk-solvent residence.

## Discussion

### A possible PAS-centred path from pathogenic peptides to AD

AD combines amyloid deposition with cholinergic failure [@selkoe2016amyloid; @hampel2018cholinergic]. Independently of catalysis, AChE accelerates Aβ fibril assembly through the PAS, and AChE–Aβ complexes are more neurotoxic than Aβ alone [@inestrosa1996ache]. A hydrophobic PAS motif is sufficient to promote that chaperone activity [@deferrari2001motif], and PAS-directed ligands can suppress AChE-induced Aβ aggregation in biochemical assays [@bartolini2003pas]. Accelerated MD places Aβ on the AChE surface as a nucleation centre [@lushchekina2017amd]; a 1-μs trajectory keeps Aβ at the PAS with principal residence at residues 344–361 [@atanasova2020md]. Periodontitis and *P. gingivalis* supply an exposure route: the organism and gingipains are detected in AD brains, and oral infection in mice drives neuroinflammation and Aβ-related changes [@dominy2019pgingivalis; @ilievski2018oral; @chalmers2025primer]. The present docking and 100-ns trajectories indicate that periodontitis-derived micropeptides can occupy that same PAS, and therefore outline a possible pathogenic mechanism with four linked steps.

1. PAS recognition and gorge-entrance occupancy.  
   Best poses of the twelve micropeptides concentrate at the PAS and gorge mouth of human AChE (PDB 4EY6; Figures 1–3, Figure S1). FLLHTTR anchors the canonical PAS residues Asp74, Tyr72 and His287 (best-run -9.60 kcal/mol; Figure 2C). YLSLLQR contacts PAS (Tyr72, Thr75) and the catalytic entrance (three-run mean -9.44 ± 0.09 kcal/mol; Figure 3L). LLHPLRL spans the PAS gatekeepers Trp286/Tyr341 to catalytic His447 (Figure 3I). HLLTLKKHV reaches Tyr72 and Phe346 in the 344–361 residence zone reported for Aβ. The geometry is the same PAS that Inestrosa identified as the pro-fibrillar site and that Atanasova occupied with Aβ.

2. A stable enzyme–peptide complex.  
   Over 100 ns the enzyme remains globular (RMSD 0.16–0.19 nm, Rg 2.30–2.31 nm, α-helix ~33% / β-sheet ~17%; Figures 4–6). FLLHTTR and YLSLLQR complexes become more compact than apo in late RMSD (0.1640 and 0.1625 nm versus 0.1897 nm; Figures 5A, 6A), so the peptide stays on the surface and rigidifies the fold rather than unfolding it. Intermolecular hydrogen bonds persist, with FLLHTTR holding a dense polar network throughout (7.03 ± 1.28; Figure 5F), YLSLLQR averaging 2.93 ± 1.14, and ALLLHRC retaining seven contact pairs after early rearrangement. This is the same “surface-bound, non-dissociating complex” described for AChE–Aβ by Lushchekina and Atanasova, now observed for periodontitis micropeptides.

3. Impaired cholinergic transmission.  
   The PAS sits at the mouth of the 20-Å gorge that feeds the catalytic triad [@hampel2018cholinergic; @cheung2012ache]. Physical occupancy of Asp74/Tyr72/Trp286/Tyr341 can block acetylcholine entry and perturb gorge gating even when the catalytic core remains folded (low RMSF in panels B). The same pose that docks to the PAS therefore attacks the cholinergic axis of AD: reduced acetylcholine hydrolysis at synapses already depleted in basal forebrain cholinergic neurons.

4. Pathological chaperone activity and amyloid co-nucleation.  
   Because the PAS is a documented pro-fibrillar chaperone site [@inestrosa1996ache; @deferrari2001motif], a heterologous peptide that resides there can lower the nucleation barrier for endogenous Aβ. FLLHTTR supplies a persistent polar network on the PAS (Figure 5F) that matches its docking pose (Figure 2C). YLSLLQR supplies compact interfacial burial (SASA 209.71 versus 212.25 nm²; Figure 6C) and the most rigid bound peptide (self-fit RMSD 0.0911 nm), consistent with a tightly seated seed. Lushchekina’s nucleation-centre model then reads directly onto these complexes: AChE remains folded and presents a peptide-coated PAS on which Aβ oligomers can co-assemble. AChE–Aβ assemblies are already more synaptotoxic than free Aβ [@inestrosa1996ache]; a bacterial micropeptide occupying the same site offers a possible route to hybrid, more toxic nuclei.

### From the oral cavity to cortical AChE

Chronic periodontitis can deliver *P. gingivalis* products into the circulation through a breached epithelium, gingipains, and outer-membrane vesicles [@guo2010gingipain; @ho2015omv]. Systemic cytokines and proteases increase blood–brain-barrier permeability, allowing short, leucine-rich, cationic micropeptides that scored BBB-high (a label similarly prevalent in both libraries) to reach cortical interstitial space [@chalmers2025primer; @dominy2019pgingivalis]. Once there, PAS docking provides a molecular landing site on a synaptic enzyme that is both a cholinergic hydrolase and an amyloid chaperone. In this possible mechanism the twelve periodontitis-derived sequences are pathogenic peptides not because RMSD rises, but because they occupy the experimentally established Aβ-binding PAS and remain bound for 100 ns.

## Conclusions

Periodontitis-derived 7–9-aa micropeptides dock to the human AChE PAS and, for FLLHTTR, YLSLLQR and ALLLHRC, remain surface-bound over 100 ns without unfolding the enzyme. FLLHTTR forms the densest PAS hydrogen-bond network; YLSLLQR uniquely buries surface area. Mapped onto the amyloid cascade [@selkoe2016amyloid], the cholinergic hypothesis [@hampel2018cholinergic], and the PAS chaperone experiments of Inestrosa, Lushchekina and Atanasova, these results support a possible mechanism in which oral pathogenic peptides occupy AChE, impair acetylcholine access, and co-nucleate Aβ on the same PAS, thereby linking periodontitis to AD at the molecular level.

## References

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
4. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
5. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
6. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
7. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
8. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
9. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
10. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
11. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
12. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
13. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
14. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
15. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
16. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
17. Lushchekina SV, Kots ED, Novichkova DA, Petrov KA, Masson P. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7(2):396–402. doi:10.1007/s12668-016-0375-x.
18. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
19. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
20. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
21. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
22. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
23. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
24. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
25. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
26. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
27. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
28. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
29. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
30. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
31. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
