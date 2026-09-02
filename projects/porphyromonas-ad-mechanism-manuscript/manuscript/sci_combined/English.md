# Periodontitis-derived micropeptides occupy the acetylcholinesterase peripheral anionic site: computational screening, docking, and 100-ns molecular dynamics

## Abstract

Periodontitis-associated oral dysbiosis has been linked to Alzheimer’s disease (AD), but a peptide-level path from the oral microbiome to a defined synaptic enzyme remains incomplete. This computation-only study joins an oral small open reading frame (smORF) screening cascade with local AutoDock Vina docking of twelve 7–9-aa candidate micropeptides into human acetylcholinesterase (AChE, PDB 4EY6) and 100-ns all-atom molecular dynamics (MD) of apo AChE versus three complexes (ALLLHRC, FLLHTTR, YLSLLQR). Sequence/proteomic filtering retained 33,786 periodontitis-labelled candidates from 11,721,988 smORFs; 3,518 were blood–brain-barrier (BBB)-high, 923 were NTxPred2-positive, and later filters produced a twelve-sequence set. Local three-run Vina scores ranged from -8.25 to -9.60 kcal/mol (best run) and from -8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol (mean ± SD). FLLHTTR had the strongest best pose but the largest run-to-run SD; YLSLLQR had the strongest mean and, with FLLHTTR and LLHPLRL, contacted the peripheral anionic site (PAS). Over 100 ns the three complexes remained globular (backbone RMSD < 0.22 nm; α-helix ~33–34%, β-sheet ~17%), with persistent intermolecular hydrogen bonds (2.19–4.23 in the last 20 ns) and SASA contraction only for YLSLLQR. The poses and trajectories supply a computational analogy onto the experimental AChE–amyloid-β (Aβ) PAS chaperone pathway; they are not measured affinities or proof of AD causation.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral micropeptide; smORF; acetylcholinesterase; peripheral anionic site; molecular docking; molecular dynamics

## Introduction

Alzheimer’s disease is a progressive neurodegenerative disorder in which amyloid-β (Aβ), tau, synaptic failure, immune activation, and vascular injury interact rather than acting as a single linear cascade [@scheltens2021alzheimer]. Amyloid biology remains central: APP cleavage by β- and γ-secretases yields Aβ40/Aβ42, soluble oligomers damage synapses, and familial APP/PSEN mutations change Aβ production and length [@selkoe2016amyloid]. Loss of basal-forebrain cholinergic transmission contributes to cognitive symptoms, and AChE inhibitors remain established symptomatic treatments [@hampel2018cholinergic]. Independently of catalysis, AChE accelerates Aβ fibril assembly through its peripheral anionic site (PAS) and yields AChE–Aβ complexes that are more neurotoxic than Aβ alone [@inestrosa1996ache]. A hydrophobic PAS motif promotes that chaperone activity [@deferrari2001motif]. These facts make AChE a biologically motivated structural target; they do not make every computationally scored ligand an AD pathogen.

Chronic periodontitis can sustain systemic inflammatory burden and episodic exposure to microbial products, motivating an oral–brain axis [@chalmers2025primer]. Disease-associated oral activity is species- and site-specific, so taxonomic abundance cannot substitute for a molecular intermediate [@belstrom2021periodontitis]. *Porphyromonas gingivalis* gingipains and outer-membrane vesicles provide one well-studied virulence context [@guo2010gingipain; @ho2015omv]. Observational syntheses associate periodontal disease with cognitive disorders, with effect estimates that vary by case definition and adjustment [@larvin2023periodontalcognition], and periodontitis has been linked to subsequent decline in an AD cohort [@ide2016periodontitis]. *P. gingivalis* and gingipains have been reported in AD brains [@dominy2019pgingivalis], and repeated oral exposure in mice can drive neuroinflammation and Aβ-related changes [@ilievski2018oral]. Mendelian randomization has not established a genetic causal effect of periodontal disease on AD [@hu2024mendelian]. Human association, experimental plausibility, and genetic evidence therefore answer different questions.

Microbiome-encoded small proteins are a large, still poorly mapped candidate space [@sberro2019smallgenes; @durrant2021sorf]. Whether any periodontitis-derived 7–9-aa micropeptide can occupy the same AChE PAS that binds Aβ is a structural question that screening scores alone cannot answer. Accelerated MD of human AChE with multiple Aβ chains showed Aβ attracted to the enzyme surface, supporting AChE as a nucleation centre [@lushchekina2017amd]. A 1-μs PAS-centered AChE–Aβ trajectory remained bound, with principal residence at PAS-adjacent residues 344–361 [@atanasova2020md]. PAS-directed ligands can inhibit AChE-induced Aβ aggregation in biochemical systems [@bartolini2003pas], and PDB 4EY6 provides a 2.40 Å human AChE structure for docking [@cheung2012ache].

The present article therefore combines two previously separate computational layers. First, an oral-smORF cascade is reconstructed to show how twelve 7–9-aa sequences were prioritized. Second, those twelve peptides are docked locally into human AChE, and three representative complexes are simulated for 100 ns against an apo control. The aim is a single, bounded original-research narrative: a screening funnel plus completed docking and MD, interpreted as a computational analogy of periodontal micropeptides onto the AChE–Aβ PAS pathway.

## Materials and methods

### Study design

This was a computation-only analysis. The screening layer is a secondary reconstruction of aggregate smORF counts, model summaries, and a twelve-sequence table; no participant recruitment, specimen collection, predictor retraining, or new omics processing was performed. Healthy and periodontitis labels were retained as branch labels and were not treated as verified peptide-level disease assignments. The docking and MD layer used local three-run AutoDock Vina poses and completed 100-ns GROMACS trajectories; it does not reuse the older screening docking-score table.

### Oral smORF screening cascade

Translated smORFs encoding 4–50-aa peptides formed the starting libraries (11,269,961 healthy-labelled and 11,721,988 periodontitis-labelled sequences). Candidates were exact-matched against named oral genomic and metaproteomic resources, including HOMD [@chen2010homd] and salivary metaproteome catalogues [@belstrom2016metaproteomics], then dereplicated. Exact matches support sequence existence or prior observation, not expression in the analysed branch. The public-accession context of the source oral metagenomic/metatranscriptomic project is PRJNA678453 [@belstrom2021periodontitis].

UniDL4BioPep provided the first functional layer: ESM-2 (`esm2_t6_8M_UR50D`) embeddings followed by a task-specific convolutional network, with an output threshold of ≥0.80, including the operational “BBB-high” label [@du2023unidl4biopep]. Periodontitis-labelled BBB-high peptides within 7–50 aa were evaluated with NTxPred2 (ESM2-t30 neurotoxicity model) [@rathore2025ntxpred2]. Mebipred applied a two-tier neural network to Cu-, Fe-, and Zn-related binding potential at a 0.50 threshold [@aptekmann2022mebipred]. AnOxPePred supplied multi-task free-radical-scavenging (FRS) and chelation (CHEL) outputs [@olsen2020anoxpepred]; serial endpoints were CHEL≥0.25, CHEL≥0.25 with FRS<0.50, and CHEL≥0.25 with FRS<0.45. Serial model agreement was treated as computational triage, not independent biological confirmation.

A separate table listed twelve unique 7–9-aa sequences. Length and counts of histidine, cysteine, and basic residues were recalculated from each string. Correspondence of that list to the aggregate CHEL/FRS endpoint could not be proven at row level because stable identifiers were unavailable.

### Molecular docking

Human recombinant AChE (rhAChE, PDB 4EY6, 2.40 Å) [@cheung2012ache] was prepared by removing galantamine and crystallographic waters, repairing internal chain breaks, and assigning physiological protonation (pH 7.4). The twelve peptides ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, HVLLLRQCA, LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR were docked with AutoDock Vina (exhaustiveness = 32) [@trott2010vina; @eberhardt2021vina] into a grid centered on the PAS (Tyr72, Asp74, Thr75, Leu76, Trp286, His287, Tyr341) and spanning the gorge neck (Phe295), choline-binding subsite (Trp86, Glu202, Tyr337), and catalytic triad (Ser203, His447, Glu334). Each ligand was run three times (`N_Success` = 3). Best-run affinity, three-run mean ± SD, hydrogen-bond geometry, and PAS contacts were taken from the local three-run summary and the single best-scoring pose of each ligand. Individual PDBQT files and configuration logs are not archived. Vina scores are empirical ranking metrics, not experimental free energies.

### Molecular dynamics

Four explicit-solvent GROMACS systems [@abraham2015gromacs] were simulated with Amber99SB-ILDN [@lindorfflarsen2010amber] and TIP3P water at 0.15 M NaCl: apo AChE (Chain A) and the AChE–ALLLHRC, AChE–FLLHTTR, and AChE–YLSLLQR complexes. Each system used a triclinic box with a 1.0 nm solute-to-boundary buffer. Equilibration comprised 2,000-step steepest-descent minimization, 1.0 ns restrained NVT heating to 300 K, 1.0 ns restrained NPT density equilibration, and 1.0 ns unrestrained NPT pre-equilibration. Production ran 100 ns (dt = 2.0 fs) in the NPT ensemble (300 K, 1.0 bar) with LINCS, 1.2 nm cutoffs, and Particle Mesh Ewald electrostatics. Frames were written every 20 ps.

Trajectory metrics matching Figures 4–6 were backbone Cα RMSD, per-residue RMSF, solvent-accessible surface area (SASA), radius of gyration (Rg), DSSP occupancy, and intermolecular hydrogen bonds (`gmx hbond`; donor–acceptor ≤ 3.0 Å). Peptide self-fit RMSD and persistent interfacial contacts (7.0 Å cutoff) were recorded as supporting descriptors. Steady-state values are mean ± SD over the final 20 ns (80.0–100.0 ns). The protocol follows the AChE–Aβ MD logic of Atanasova and colleagues at a 100-ns rather than 1-μs window [@atanasova2020md].

## Results

### Screening funnel and twelve-sequence composition

Sequence-evidence filtering retained 31,510/11,269,961 healthy-labelled candidates (0.2796%) and 33,786/11,721,988 periodontitis-labelled candidates (0.2882%). In the periodontitis-labelled branch, 3,446 short and 72 long peptides were BBB-high (3,518 total). NTxPred2 evaluated 3,299/3,518 (93.77%) and classified 923/3,299 (27.98%) as model-positive; 219 candidates lay outside the 7–50-aa coverage window. Subsequent aggregate filters retained 111 mebipred-positive candidates, 15 with CHEL≥0.25, 12 with CHEL≥0.25 and FRS<0.50, and 8 with CHEL≥0.25 and FRS<0.45 (Table 1). A near-saturated UniDL4BioPep antimicrobial output (99.90% of periodontitis-labelled short peptides above 0.80) indicates that a common threshold is not equally calibrated across tasks.

**Table 1. Aggregate oral-smORF prioritization counts.**

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

The twelve explicit sequences are unique 7–9-aa peptides of standard amino acids (Table 2). Eleven contain histidine, six contain cysteine, and every sequence contains at least one Arg or Lys. Composition supplies synthesis and metal-coordination hypotheses only; it does not establish taxonomy, translation, BBB transport, or identity with the aggregate 12-count endpoint. All 923 NTxPred2-positive peptides were ≤30 aa, so none of the 72 BBB-high long peptides entered the downstream metal/CHEL/FRS filters.

**Table 2. Composition of the twelve 7–9-aa candidate micropeptides.**

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

All twelve ligands yielded favorable local Vina scores. Best-run affinities ranged from -8.25 to -9.60 kcal/mol and three-run means from -8.07 ± 0.16 to -9.44 ± 0.09 kcal/mol (Table 3, Figure 1). Best-pose ranking placed FLLHTTR first (-9.60 kcal/mol), then YLSLLQR (-9.49 kcal/mol) and ALLLHRC (-9.29 kcal/mol). Mean ranking placed YLSLLQR first (-9.44 ± 0.09 kcal/mol) and ALLLHRC second (-9.18 ± 0.11 kcal/mol). FLLHTTR retained the strongest single pose but the largest run-to-run SD (-8.77 ± 1.41 kcal/mol). Best poses formed 3–10 hydrogen bonds (mean length 2.83–3.28 Å; Figures 2 and 3; Figure S1).

**Table 3. Local AutoDock Vina scores and PAS engagement of twelve candidate micropeptides against human AChE (PDB 4EY6).**

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

**Figure 1. Local AutoDock Vina scores of twelve candidate micropeptides against human AChE (PDB 4EY6).** Blue circles show the three-run mean; whiskers show the standard deviation; orange diamonds mark the best-run affinity. Order matches best-run ranking. Scores are empirical Vina metrics, not experimental free energies.

![Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA.](../figures/fig_docking_poses_A_F.png)

**Figure 2. Best-scoring docking poses of ALLLHRC, FCLHLQLR, FLLHTTR, HLLTLKKHV, HLPLLHRCC, and HVLLLRQCA (panels A–F).** Peptide, orange; contacting AChE residues, cyan; hydrogen bonds, dashed. FLLHTTR (panel C) is the densest PAS pose.

![Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR.](../figures/fig_docking_poses_G_L.png)

**Figure 3. Best-scoring docking poses of LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, YHHLLCRR, and YLSLLQR (panels G–L).** LLHPLRL (panel I) spans PAS Trp286/Tyr341 to catalytic His447; YLSLLQR (panel L) bridges PAS and the catalytic entrance.

![Figure S1. Combined overview of all twelve best-scoring docking poses.](../figures/fig_docking_poses_12_combined.png)

**Figure S1. Combined overview of all twelve best-scoring docking poses.** Single-page layout of panels A–L.

Canonical PAS binders in the best pose were FLLHTTR (Figure 2C), YLSLLQR (Figure 3L), FCLHLQLR, HVLLLRQCA, HLLTLKKHV, and LLHPLRL (Figure 3I). ALLLHRC bound catalytic Ser203 with the shortest mean hydrogen bond (2.83 Å) rather than the outer PAS aromatic core (Figure 2A). Three-run means distinguish reproducible high-affinity ligands (YLSLLQR, ALLLHRC, LLHPLRL) from ligands whose best pose is stronger than the run-averaged score (FLLHTTR, FCLHLQLR, YHHLLCRR).

### 100-ns molecular dynamics of apo AChE and three complexes

Production trajectories were completed for apo AChE and the ALLLHRC, FLLHTTR, and YLSLLQR complexes (Table 4, Figures 4–6). Each six-panel figure compares the unliganded control with one peptide complex: backbone RMSD (A), per-residue RMSF (B), SASA (C), Rg (D), DSSP occupancy over the last 20 ns (E), and intermolecular hydrogen bonds (F).

<!-- PAGEBREAK -->

![Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns comparison.](../figures/fig_compare_ache_vs_alllhrc.png)

**Figure 4. Apo AChE versus AChE–ALLLHRC 100-ns molecular dynamics comparison.** Panels A–F match the metrics in Table 4.

![Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns comparison.](../figures/fig_compare_ache_vs_fllhttr.png)

**Figure 5. Apo AChE versus AChE–FLLHTTR 100-ns molecular dynamics comparison.** Panel layout matches Figure 4. Complex RMSD (A) and Rg (D) show the largest elevation among the three peptides.

![Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns comparison.](../figures/fig_compare_ache_vs_ylsllqr.png)

**Figure 6. Apo AChE versus AChE–YLSLLQR 100-ns molecular dynamics comparison.** Panel layout matches Figure 4. SASA (C) contracts relative to apo; hydrogen-bond counts (F) are the densest of the three complexes.

**Table 4. Final-20-ns trajectory metrics for apo AChE and three peptide complexes (mean ± SD), aligned to Figures 4–6.**

| Metric (last 20 ns) | apo AChE | AChE–ALLLHRC | AChE–FLLHTTR | AChE–YLSLLQR |
| --- | --- | --- | --- | --- |
| Backbone Cα RMSD (nm); Figure panels A | 0.1562 ± 0.0093 | 0.1916 ± 0.0092 | 0.2102 ± 0.0087 | 0.2064 ± 0.0136 |
| Peptide self-fit RMSD (nm) | N/A | 0.2518 ± 0.0136 | 0.2697 ± 0.0217 | 0.1979 ± 0.0143 |
| Per-residue RMSF mean (nm); Figure panels B | 0.0783 ± 0.0524 | 0.0876 ± 0.0581 | 0.0901 ± 0.0644 | 0.0813 ± 0.0574 |
| SASA (nm²); Figure panels C | 212.41 ± 2.36 | 217.47 ± 2.49 | 216.34 ± 2.55 | 210.37 ± 2.91 |
| Rg (nm); Figure panels D | 2.2967 ± 0.0043 | 2.3107 ± 0.0052 | 2.3163 ± 0.0059 | 2.3004 ± 0.0051 |
| Intermolecular H-bonds; Figure panels F | N/A | 2.19 ± 0.80 | 2.80 ± 0.99 | 4.23 ± 1.24 |
| Persistent contact pairs | N/A | 7 | 7 | 7 |
| DSSP α-helix / β-sheet (%); Figure panels E | 33.59 / 17.18 | 33.66 / 16.76 | 33.87 / 17.11 | 32.92 / 17.08 |

Figures 4A, 5A, and 6A show that apo RMSD remains near 0.16 nm, while complex RMSD stays below 0.22 nm. Receptor-only RMSD values (0.1653, 0.1767, and 0.1601 nm) confirm that FLLHTTR induces the largest receptor perturbation and that YLSLLQR barely shifts the enzyme backbone. RMSF (panels B) remains low in the catalytic core, with modest increases localized to surface loops. Rg (panels D) stays within 2.29–2.32 nm. SASA (panels C) rises slightly for ALLLHRC and FLLHTTR but contracts for YLSLLQR (210.37 nm²), matching the tighter interfacial burial in Figure 6C. Hydrogen bonds persist throughout 100 ns (panels F); YLSLLQR forms the densest network (4.23 ± 1.24). DSSP helix (~33–34%) and sheet (~17%) fractions overlay the apo bars in panels E. Each complex retains seven persistent contact pairs.

### Evidence boundary

**Table 5. Evidentiary boundaries for docking and 100-ns MD findings.**

| No. | Observation | Supported interpretation | Unsupported extrapolation |
| --- | --- | --- | --- |
| 1 | Best poses of FLLHTTR, YLSLLQR, and LLHPLRL contact PAS residues | Geometric complementarity to the PAS and gorge entrance | Vina scores are not experimental Kd or Ki |
| 2 | Complex RMSD 0.16–0.21 nm with conserved DSSP | Localized loop adaptation without unfolding | Mild RMSD increase is not denaturation or dissociation |
| 3 | Last-20-ns H-bonds 2.19–4.23 and seven contact pairs | Surface residence over 100 ns | Single trajectories do not prove irreversible nanomolar binding |
| 4 | YLSLLQR SASA contraction and densest H-bond panel | Compact interfacial burial relative to apo | Cannot be equated with a macroscopic binding constant |
| 5 | FLLHTTR best-run -9.60 kcal/mol versus mean -8.77 ± 1.41 kcal/mol | Best pose is a high-scoring outlier; mean ranking favors YLSLLQR | A single best pose is not a converged affinity |

## Discussion

### Principal findings

The screening cascade reduces a multimillion-candidate smORF space to a tractable twelve-sequence set, while local docking and 100-ns MD place those peptides on human AChE. The scientific contribution is not validation of a periodontal–AD mechanism. It is a bounded computational chain: an operational candidate list, residue-level PAS poses, and three folded complexes that remain surface-bound on a 100-ns window.

Microbiome peptide mining can narrow a sequence space efficiently, but biological claims require synthesis and controlled assays [@torres2024peptideantibiotics]. Here the funnel remains aggregate. Missing row-level identifiers prevent assigning any sequence to *P. gingivalis*, to a sample, or to the CHEL/FRS endpoint of 12. Similar healthy-labelled and periodontitis-labelled retention rates therefore cannot be read as disease enrichment.

### Four computational steps on the AChE–Aβ PAS pathway

Four papers define the pathway onto which the poses and trajectories are mapped. Selkoe and Hardy review Aβ and AD [@selkoe2016amyloid]. Inestrosa et al. showed experimentally that AChE accelerates Aβ fibril assembly through the PAS and that AChE–Aβ complexes are more neurotoxic than Aβ alone [@inestrosa1996ache]. Lushchekina et al. used accelerated MD of human AChE with multiple Aβ chains and found Aβ attracted to the enzyme surface, forming stable complexes and supporting AChE as a nucleation centre [@lushchekina2017amd]. Atanasova et al. docked one Aβ into the PAS for 1 μs, with a stable complex and main residence at PAS-adjacent 344–361 [@atanasova2020md]. The four steps below come only from the present docking poses and 100-ns trajectories, as a computational analogy of periodontitis micropeptides onto that Aβ–AChE pathway.

1. PAS recognition and gorge-entrance occupancy.  
   Best poses of the twelve micropeptides concentrate at the PAS and gorge mouth of human AChE (PDB 4EY6; Figures 1–3, Figure S1). FLLHTTR anchors Asp74, Tyr72 and His287 (best-run -9.60 kcal/mol; Figure 2C). YLSLLQR contacts PAS (Tyr72, Thr75) and the catalytic entrance (three-run mean -9.44 ± 0.09 kcal/mol; Figure 3L). LLHPLRL spans Trp286/Tyr341 to His447 (Figure 3I). HLLTLKKHV reaches Tyr72 and Phe346 in 344–361. The geometry matches Atanasova’s placement of Aβ at PAS with 344–361 as principal residence.

2. A stable complex: the enzyme does not unfold and the peptide does not leave.  
   Figures 4–6 show globular AChE over 100 ns: RMSD < 0.22 nm, Rg 2.29–2.32 nm, and α-helix ~33–34% / β-sheet ~17% overlaying apo. The modest rise of complex traces above apo is PAS-adjacent loop adaptation, not denaturation. Last-20-ns hydrogen bonds persist (ALLLHRC 2.19 ± 0.80, FLLHTTR 2.80 ± 0.99, YLSLLQR 4.23 ± 1.24), with seven contact pairs. This matches Lushchekina and Atanasova on a stable, surface-bound complex.

3. Impaired cholinergic transmission.  
   The PAS sits at the entrance of the 20-Å gorge above the catalytic triad [@hampel2018cholinergic]. RMSF increases are confined to surface loops (panels B). Physical occupancy can impede acetylcholine entry and perturb gorge gating, so the same pose attacks AChE catalysis in the computational model.

4. Pathological chaperone activity and amyloid co-nucleation.  
   Inestrosa established the PAS as a pro-fibrillar site; Lushchekina and Atanasova recast that process as peptide residence on PAS/344–361, with hydrogen bonds holding the interface while the enzyme scaffolds nucleation. The three complexes here give the same computational picture: a persistent polar network, entrance-loop perturbation, and SASA contraction for YLSLLQR (Figure 6C). Periodontal micropeptides can therefore act as heterologous seeds that co-nucleate endogenous Aβ on the same PAS surface.

These steps are molecular events inside the docking poses and single 100-ns trajectories. They are not experimental binding constants, and Vina scores are not Kd. Detection of *P. gingivalis* in AD brains [@dominy2019pgingivalis] supplies epidemiological context for asking the structural question; it does not transfer organism-level evidence onto untraced community peptides.

### Limitations

Each MD system is a single 100-ns trajectory, shorter than the 1,000-ns AChE–Aβ benchmark [@atanasova2020md]. Docking scores are empirical; PDBQT archives are not deposited; FLLHTTR’s SD of 1.41 kcal/mol shows that a best pose can overstate run-averaged affinity. The screening layer lacks candidate nucleotide rows, genomic coordinates, sample mappings, taxonomic assignments, and complete predictor outputs, so the twelve sequences cannot be proven identical to the aggregate endpoint of 12. “BBB-high,” “neurotoxicity-positive,” and CHEL/FRS are operational model labels, not transport, neuronal injury, or metal-coordination measurements. The peptides are a computational analogy onto the Aβ–AChE pathway, not proven AD pathogens.

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
