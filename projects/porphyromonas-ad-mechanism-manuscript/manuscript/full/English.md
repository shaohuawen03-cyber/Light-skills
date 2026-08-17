## Abstract

**Background:** Periodontitis-associated oral dysbiosis may contribute to Alzheimer’s disease (AD)-relevant inflammation, but the molecular entities linking the oral microbiome to the brain remain unresolved. Microbiome small open reading frames (smORFs) provide a large, poorly characterized peptide space for computational prioritization.

**Objective:** To reconstruct an aggregate oral-smORF screening cascade, characterize a supplied peptide shortlist, and define testable AChE, metal/redox, blood–brain barrier (BBB), and neurotoxicity hypotheses.

**Methods:** This computation-only secondary analysis integrated sequence/proteomic filtering, ESM-2 embeddings with task-specific convolutional networks, a fine-tuned ESM2-t30 neurotoxicity model, a two-tier neural-network metal-binding predictor, a multi-task antioxidant convolutional network, and a separate AChE docking summary.

**Results:** Filtering retained 31,510 and 33,786 candidates in the two supplied branches. In the periodontitis-labelled branch, 3,518 candidates were BBB-high; 3,299 were within the NTxPred2 length domain and 923 were model-positive. Subsequent filters retained 111, 15, 12, and 8 candidates. A separate dataset contained twelve unique 7–9-residue sequences with AChE Vina means from −9.60 to −8.25 kcal/mol. Sequence composition and score ordering were reproducible, whereas sequence-level funnel linkage and docking execution could not be reconstructed from the available material.

**Conclusions:** The analysis yields a bounded shortlist for independent computational and experimental validation rather than evidence of peptide expression, brain exposure, *Porphyromonas gingivalis* origin, AChE engagement, or an AD mechanism. A prespecified 100-ns GROMACS extension will add trajectory-derived stability and contact analyses after completion and quality control.

**Keywords:** Alzheimer’s disease; *Porphyromonas gingivalis*; periodontitis; oral microbiome; smORF; deep learning; acetylcholinesterase; molecular dynamics

## Introduction

### Alzheimer’s disease as a multilevel biological problem

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder in which amyloid-β (Aβ) deposition, tau pathology, synaptic failure, glial activation, vascular dysfunction, and systemic comorbidity interact over a prolonged preclinical and clinical continuum [@scheltens2021alzheimer]. The amyloid hypothesis remains central to disease biology, particularly as a framework for initiating events, but amyloid burden alone does not account for the full spatial, temporal, and clinical heterogeneity of AD [@selkoe2016amyloid]. Contemporary interpretation therefore places amyloid and tau within a broader network that includes innate immune signalling, neuronal vulnerability, lipid and metal homeostasis, cerebrovascular integrity, and age-dependent loss of resilience. This systems view is important when evaluating peripheral exposures: a biologically plausible contributor need not be a single sufficient cause, but it must still be connected to disease-relevant tissue through traceable molecular and temporal evidence.

The cholinergic system illustrates the distinction between clinical relevance and causal sufficiency. Loss of cholinergic function contributes to cognitive symptoms, and acetylcholinesterase (AChE) inhibitors remain established symptomatic treatments [@hampel2018cholinergic]. AChE also has non-catalytic interactions with Aβ assembly, creating a structural link between cholinergic biology and amyloid research [@inestrosa1996ache]. Neither observation means that every predicted AChE-interacting molecule is relevant to AD. Target engagement, direction of effect, tissue exposure, concentration, selectivity, and downstream phenotype must all be established. This evidentiary sequence provides a useful standard for evaluating microbial molecules proposed to participate in an oral–brain axis.

Chronic peripheral inflammatory states have consequently attracted attention as possible modifiers of neurodegenerative vulnerability. Periodontitis is of particular interest because it combines persistent mucosal inflammation, a dysbiotic polymicrobial biofilm, episodic access of microbial products to the circulation, and strong age and comorbidity gradients [@chalmers2025primer]. These same features make causal interpretation difficult. Periodontitis may contribute to systemic inflammatory burden, but it may also share determinants with cognitive decline, while declining cognition can worsen oral hygiene and access to dental care. A rigorous molecular study must therefore separate association, route plausibility, molecular identity, and demonstrated function rather than treating them as interchangeable evidence.

### Periodontal dysbiosis and *Porphyromonas gingivalis*

Periodontitis is an ecological disease of the tooth-supporting tissues rather than the consequence of a single pathogen. In susceptible hosts, altered community structure, inflammatory nutrient release, and impaired resolution can reinforce one another, producing a dysbiotic environment with site-specific transcriptional activity. Paired oral metagenomic and metatranscriptomic data show that disease-associated signals vary by species and oral site and that taxonomic abundance cannot substitute for functional activity [@belstrom2021periodontitis]. Cross-study metatranscriptomic synthesis further shows that disease signatures depend on cohort definition, sampling site, sequencing depth, normalization, covariates, and subject-level replication [@ovsepian2024periodontal]. These observations argue against describing every sequence recovered from a disease-labelled branch as disease-specific.

Within this community, *Porphyromonas gingivalis* is a well-studied Gram-negative anaerobic pathobiont. Its importance derives not simply from abundance but from its capacity to reshape host–microbial interactions through proteolysis, immune modulation, community cooperation, and vesicle-mediated cargo delivery. Gingipains have context-dependent effects on host proteins, complement pathways, inflammation, tissue integrity, and nutrient acquisition [@guo2010gingipain]. *P. gingivalis* outer-membrane vesicles can concentrate and transport bacterial components beyond the producing cell and alter interactions with host tissues and neighbouring microorganisms [@ho2015omv]. These properties make *P. gingivalis* biologically relevant to oral–systemic hypotheses, but they do not justify assigning an untraced community-derived peptide to this organism.

The distinction between an organism-level hypothesis and a community-peptide hypothesis is fundamental. Detection of *P. gingivalis* DNA, antigen, gingipain-associated signal, or vesicular material does not imply that a particular short peptide was expressed, secreted, stable in blood, transported across the blood–brain barrier (BBB), or active in neural tissue. Conversely, a metagenome-derived peptide that cannot be assigned to *P. gingivalis* could still originate from another oral taxon or from an assembly artefact. The oral metagenome is therefore treated here as a community sequence space, while *P. gingivalis* provides mechanistic context rather than a presumed taxonomic label.

### Human, experimental, and genetic evidence do not carry equal causal weight

The periodontitis–AD literature contains several evidence classes that address different questions. Observational reviews and meta-analyses commonly report associations between periodontal disease and cognitive disorders, but their estimates vary with periodontal definitions, dementia ascertainment, follow-up, age structure, and adjustment strategy [@larvin2023periodontalcognition]. Clinical syntheses likewise identify a recurring association while emphasizing heterogeneity and the limited ability of retrospective designs to establish directionality [@kaliamoorthy2022periodontitisad]. Reviews focused on oral bacteria broaden the candidate mechanisms but also reveal that organism detection, antibody responses, oral disease status, and dementia outcomes are often measured in different populations [@liu2023oralbacteriaad]. More recent evidence assessments continue to classify periodontitis as a possible risk marker while calling for stronger longitudinal and interventional designs [@kim2025periodontitisdementia].

Longitudinal observations provide temporal information but remain susceptible to confounding and reverse causation. In an AD cohort, periodontitis was associated with subsequent cognitive decline and a pro-inflammatory state [@ide2016periodontitis]. Public-data and text-mining analyses have also proposed shared molecular signals [@jiang2021periodontitis]. Such studies can prioritize pathways, yet they cannot determine whether periodontal exposure caused neurodegeneration, whether emerging cognitive impairment altered oral health, or whether both were influenced by age, smoking, diabetes, medication, frailty, socioeconomic conditions, or health-care access.

Genetic-instrument approaches provide an important counterweight to an exclusively positive narrative. A two-sample Mendelian-randomization analysis did not establish evidence for a genetic causal effect of periodontal disease on AD [@hu2024mendelian]. A broader synthesis of Mendelian-randomization studies similarly illustrates that putative systemic consequences of periodontitis are not uniformly supported across outcomes or instrument choices [@zhao2026mendelian]. These findings do not prove the absence of every acquired inflammatory or microbial pathway, because genetic liability and time-varying exposure are not identical. They do, however, weaken claims that the epidemiological association by itself demonstrates causality.

Mechanistic studies answer narrower questions under controlled conditions. *P. gingivalis* material and gingipain-associated signals have been reported in AD-related post-mortem samples [@dominy2019pgingivalis]. Earlier tissue work also examined the presence of *P. gingivalis* in AD brain material [@poole2013pg]. Repeated oral exposure in wild-type mice produced brain inflammation, neurodegenerative changes, and Aβ-related alterations [@ilievski2018oral]. Infected neuronal systems have shown persistent gingipain activity and AD-like cellular phenotypes [@haditsch2020cor388]. Vesicle-focused studies provide a plausible vehicle for concentrated microbial cargo and host signalling [@nara2021omv]. The strength of these studies is mechanistic resolution; their limitation is transferability. Differences in dose, exposure route, model organism, cell system, disease stage, and endpoint prevent direct extrapolation to naturally occurring human peptide exposure.

Taken together, the literature supports a research question, not a settled pathway. Human associations establish relevance, experimental models establish selected possibilities, and negative or equivocal causal analyses constrain interpretation. A defensible study should identify a molecular entity, trace it to its source, demonstrate exposure, and then test a prespecified function. The present work addresses only the first computational steps of that sequence.

### Candidate routes from the periodontal niche to the brain

Several non-exclusive routes have been proposed to connect periodontal dysbiosis with neurodegenerative processes. One is indirect: chronic periodontal inflammation may alter circulating cytokines, acute-phase responses, endothelial activation, or immune-cell states, which could influence neurovascular and glial function without requiring a viable organism to enter the brain [@chalmers2025primer]. A second involves episodic dissemination of bacterial cells or soluble products during tissue inflammation or routine mechanical disturbance. A third involves outer-membrane vesicles, which protect and concentrate lipids, proteins, nucleic acids, and other bacterial cargo [@ho2015omv]. A fourth involves specific enzymes or molecular fragments, including gingipain-related products, that could modify host substrates [@guo2010gingipain]. The relative contribution of these routes in humans remains uncertain.

Each route imposes a different evidence requirement. An inflammatory route requires exposure-response and mediation evidence. A dissemination route requires matched oral and systemic molecular identities. A vesicular route requires cargo characterization, biodistribution, and barrier-transport data. A direct peptide route additionally requires proof that the small open reading frame is translated, that the peptide survives processing and proteolysis, and that a sufficient concentration reaches the relevant tissue compartment. BBB prediction alone cannot satisfy these requirements because permeability depends on peptide conformation, charge, transport mechanisms, serum binding, degradation, efflux, and experimental context.

Microbially encoded small proteins and peptides remain underexplored within this framework. Short molecules could in principle act as ligands, enzyme modulators, membrane-active agents, immune signals, metal-binding species, or inert degradation products. The hypothesis space is therefore broad, but broad plausibility is not evidence for a particular sequence. The unresolved molecular gap is whether any traceable oral-microbial peptide is expressed in the relevant ecological context, disseminates beyond the mouth, and exerts a reproducible neural or vascular effect. Computational prioritization is valuable only insofar as it reduces this space without erasing these sequential requirements.

### Microbiome smORFs form a legitimate but technically difficult discovery space

Small open reading frames (smORFs) are systematically under-annotated because short coding regions are difficult to distinguish from random open reading frames, provide limited phylogenetic signal, and often fall below conventional gene-calling thresholds. Large-scale analysis of human-associated microbiomes nevertheless identified thousands of conserved small-gene families, many lacking known domains [@sberro2019smallgenes]. Dedicated annotation approaches improve discovery by combining profile models, coding features, conservation, and other evidence rather than applying protein-length cut-offs designed for conventional genes [@durrant2021sorf]. High-resolution multi-omics can strengthen candidate status by linking predictions to transcriptional and proteomic observations [@davin2026multiomics].

The validation sequence remains demanding. A predicted smORF is not necessarily transcribed; a transcript is not necessarily translated; a peptide-spectrum match is not automatically unique or correctly assigned; and a detected peptide is not necessarily stable or functional. Reviews of short-ORF biology emphasize the need for orthogonal validation and careful nomenclature [@couso2017sorfs]. Proteogenomic studies likewise show that translation evidence must be interpreted with tissue, reading-frame, false-discovery, and functional context [@vanheesch2019heart]. These constraints are amplified in metagenomes, where fragmented assemblies, homologous sequences, strain variation, and six-frame translation can create millions of short candidates.

Oral sequence and metaproteome resources provide complementary but non-equivalent evidence. HOMD and eHOMD curate oral and aerodigestive taxonomic and genomic information [@chen2010homd]. Salivary metaproteome datasets can support peptide detection within their own sample and false-discovery framework [@belstrom2016metaproteomics]. A lung-cancer oral metaproteome provides another context-specific observation space [@jiang2022oralmetaproteomics]. Contemporary salivary metaproteomics emphasizes host depletion, microbial enrichment, peptide- and protein-level error control, taxonomic ambiguity, and public raw-data preservation [@yuan2025osample]. An exact match against any one resource may support sequence existence or prior observation, but it cannot by itself establish expression in the current disease-labelled branch.

This distinction makes sample-level traceability indispensable. A disease comparison requires a chain from sequence to contig, assembly or bin, specimen, participant, oral site, clinical group, and processing batch. Without that chain, candidate counts are computational accounting units rather than independent biological replicates. The available data preserve aggregate branch labels and counts but not the row-level mapping needed to estimate prevalence, enrichment, taxonomic origin, or between-participant uncertainty. Accordingly, the term “periodontitis-labelled branch” is used instead of “periodontitis-specific peptidome.”

### Deep-learning-guided prioritization is triage, not validation

The scale of the smORF search space motivates sequence-based models, but their outputs inherit the assumptions and domain limits of their training data. UniDL4BioPep uses contextual embeddings from a pretrained ESM-2 model followed by task-specific convolutional neural networks for peptide-bioactivity classification [@du2023unidl4biopep]. Protein language models can capture sequence regularities that are difficult to encode manually, yet an output score remains model-specific: it is not a calibrated biological probability unless calibration has been demonstrated in a comparable sequence and task domain.

BBB-peptide prediction illustrates this limitation. Augur combines engineered descriptors, feature selection, class-balancing and a random-forest classifier rather than deep learning [@gu2024bbb]. B3BPFN represents a different model family and dataset construction strategy [@liu2026b3bpfn]. Differences among methods in positive-set definition, redundancy reduction, negative sampling, sequence length, class balance, and validation design can materially change apparent performance. Very short, leucine-rich, cationic or compositionally unusual microbiome peptides may lie outside the distributions on which these models were evaluated. A “BBB-high” output therefore defines a prioritization threshold, not measured transport.

The downstream tools are likewise heterogeneous. The peptide mode of NTxPred2 fine-tunes an ESM2-t30 protein language model for neurotoxic-peptide classification [@rathore2025ntxpred2]. Mebipred uses engineered sequence descriptors and a two-tier artificial-neural-network framework to estimate general and ion-related metal-binding potential [@aptekmann2022mebipred]. AnOxPePred uses one-dimensional convolution and multi-task outputs for free-radical-scavenging and chelation-related properties [@olsen2020anoxpepred]. Serial agreement among these tools is not orthogonal replication: the models reuse sequence composition, were trained on different endpoints, and may propagate correlated biases through the funnel.

The appropriate interpretation is triage. “Neurotoxic-positive” is not neuronal toxicity; “metal-binding-positive” is not a measured dissociation constant or coordination geometry; CHEL and FRS outputs are not redox chemistry. A strong precedent from microbiome peptide mining shows that computational candidates become biological findings only after synthesis and controlled functional testing [@torres2024peptideantibiotics]. In a computation-only study, the scientific contribution is therefore the transparent reduction of a candidate space, explicit model descriptions, domain warnings, and a reproducible account of what remains untested.

### AChE, metal homeostasis, docking, and molecular dynamics define a structural hypothesis

AChE provides a biologically motivated but demanding structural follow-up. Beyond hydrolysing acetylcholine, AChE can accelerate Aβ fibril assembly [@inestrosa1996ache]. A defined AChE motif has been implicated in promoting Aβ fibril formation [@deferrari2001motif], and PAS-directed ligands can inhibit AChE-induced Aβ aggregation in biochemical systems [@bartolini2003pas]. Structural studies map an aromatic gorge connecting the catalytic machinery with the peripheral site [@kryger1999e2020]. The human AChE structure represented by PDB 4EY6 provides an experimentally determined receptor framework for ligand-oriented questions [@cheung2012ache]. These findings justify asking whether a candidate peptide can occupy a reproducible region of the AChE surface; they do not establish binding, inhibition, or an effect on Aβ.

Docking flexible 7–9-residue peptides is especially uncertain because peptide protonation, termini, initial conformers, receptor flexibility, search-space placement, scoring stochasticity, and post-docking refinement can alter rank order. AutoDock Vina is a useful screening engine, but its scores are not experimental affinities or binding free energies [@trott2010vina]. Later Vina implementations expand methods and interfaces without removing the need for complete preparation and execution records [@eberhardt2021vina]. Peptide-specific refinement methods such as FlexPepDock illustrate the higher-resolution standard that could be applied after a transparent initial screen [@london2011flexpepdock].

Molecular dynamics (MD) can test whether a prepared complex remains within a defined conformational basin under a specified force field and solvent model, but MD cannot rescue an untraceable or poorly prepared docking pose. Published AChE–Aβ simulations demonstrate that peptide residence and contacts can change over time [@atanasova2020md]. Accelerated simulations further show how alternative AChE surface interactions may be explored [@lushchekina2017amd]. For the present candidates, meaningful MD would require versioned starting coordinates, topology and protonation decisions, independently seeded trajectories, convergence assessment, and prespecified analyses. The ongoing MD extension will evaluate residence, conformational stability, and contact persistence after the predefined trajectory analyses and quality-control checks are complete.

Metal biology defines a second structural hypothesis. Copper, iron, and zinc dyshomeostasis intersects with Aβ aggregation, redox chemistry, lipid peroxidation, and neuronal injury [@bush2013metal]. Broader elementomic perspectives place these interactions within a network rather than a single-metal mechanism [@lei2021elements]. Histidine- and cysteine-containing peptides may offer potential coordination groups, but composition cannot determine affinity, selectivity, stoichiometry, geometry, oxidation state, or redox consequence. Tau fragments show experimentally that Cu(II) coordination can alter peptide structure and Aβ aggregation [@dinatale2018tau]. The tau26–44 fragment further illustrates how a short dynamic peptide can be connected to membrane and cellular phenotypes through dedicated experiments [@perini2019tau]. Bacterial amyloid exposure can modify aggregation phenotypes in model systems [@chen2016curli]. These studies define testable comparators, not transferable activity.

### Knowledge gap and study objectives

The literature converges on a carefully bounded gap. Periodontitis and AD have a heterogeneous observational relationship; *P. gingivalis* offers organism-specific mechanistic plausibility; and oral microbiomes encode a large, poorly characterized small-peptide space. What remains missing is a traceable molecular chain linking a defined microbial smORF to translation, host exposure, BBB passage, target engagement, and a disease-relevant phenotype. No single computational score can bridge those levels.

This study addressed an earlier and narrower question: whether the available aggregate oral-smORF data support a coherent candidate-prioritization funnel and whether a separate AChE docking summary can be interpreted without converting incomplete methodological information into biological certainty. We recomputed proportions, checked branch arithmetic and predictor applicability, characterized a supplied twelve-sequence set, and retained the reported AChE score ordering as a descriptive result. We also specified a prospective MD extension with predefined trajectory outputs. The study therefore provides a computational hypothesis set rather than a new predictor, a clinical cohort analysis, an independently reproduced docking study, or a validated AD mechanism.

## Materials and methods

### Study design and data scope

This study was a computation-only secondary analysis of aggregate candidate counts, model summaries, a twelve-sequence table, and a corresponding AChE docking-score table. No participant recruitment, specimen collection, wet-laboratory experiment, new omics processing, predictor retraining, or docking rerun was performed. MD trajectory analysis is ongoing as a predefined extension. The healthy and periodontitis labels were retained as supplied branch labels and were not interpreted as verified candidate-level disease assignments.

The available material did not include candidate nucleotide or amino-acid rows for the full funnel, genomic coordinates, subject/sample mappings, accession-to-group assignments, bin manifests, taxonomy, peptide-spectrum matches, complete model outputs, run logs, or the original discovery pipeline. These omissions precluded participant-level prevalence estimates, disease-enrichment tests, taxonomic assignment, and row-by-row reconstruction of the final filters.

### Accessions, candidate construction, and sequence-evidence filtering

The aggregate analysis identified PRJNA678453 and PRJEB65451 as the relevant public accessions. PRJNA678453 is the source project for paired oral metagenomic and metatranscriptomic data [@belstrom2021periodontitis]. PRJEB65451 is a derived EBI-EMG/MGnify-brokered Third Party Annotation metagenomic assembly project generated from PRJNA678453 with metaSPAdes v3.15.3, not an independent clinical cohort. Participant, specimen, assembly-analysis, and metagenome-assembled-genome totals are not reported because consistent sample-to-assembly and bin-level manifests were unavailable.

The supplied analysis retained translated smORFs 4–50 aa long and grouped them into healthy-labelled and periodontitis-labelled libraries containing 11,269,961 and 11,721,988 candidates, respectively. Candidates were exact-matched to the named oral sequence and proteomic resources, including HOMD/eHOMD and the PXD003151, PXD004319, and PXD026727 datasets, and then dereplicated [@chen2010homd; @escapa2018ehomd; @belstrom2016metaproteomics; @jiang2022oralmetaproteomics; @yuan2025osample]. This produced 31,510 healthy-labelled and 33,786 periodontitis-labelled candidates. The filtered sets were divided into a short branch (5–30 aa: 30,557 and 32,754 candidates) and a long branch (31–50 aa: 953 and 1,032 candidates). The supplied rules included 4-aa candidates initially, whereas the downstream bins began at 5 aa; the disposition of 4-aa sequences could not be determined. Resource matches were treated as sequence-supporting evidence rather than proof of expression in the study cohort.

### Deep-learning-guided candidate prioritization

UniDL4BioPep was used as the first functional-prioritization model. Its documented architecture applies the pretrained ESM-2 model `esm2_t6_8M_UR50D` to encode each peptide as a 320-dimensional contextual embedding, followed by a six-layer task-specific convolutional neural network for binary peptide-bioactivity classification [@du2023unidl4biopep]. The supplied analysis used an output threshold of ≥0.80, including for the BBB task. Because calibration in this very-short-peptide domain was not available, outputs are described as “model-positive” or “BBB-high,” not as measured transport or confirmed activity. Published BBB predictors use heterogeneous architectures and datasets, which further limits direct transfer of performance estimates to these candidates [@gu2024bbb] [@liu2026b3bpfn].

The periodontitis-labelled BBB-high set was next evaluated with the peptide mode of NTxPred2, which fine-tunes the ESM2-t30 protein language model on neurotoxic-peptide sequences [@rathore2025ntxpred2]. Analysis was restricted to the documented 7–50-aa range; shorter candidates were classified as outside model coverage rather than negative. Cu-, Fe-, and Zn-related binding potential was then evaluated with mebipred. This alignment-free method combines amino-acid composition, physicochemical descriptors, and metal-binding 5-mer frequencies in a two-tier artificial-neural-network framework comprising a general metal-binding network and ion-specific classifiers [@aptekmann2022mebipred]. The applied decision threshold was 0.50.

Antioxidant-related properties were evaluated with AnOxPePred, a multi-task deep convolutional neural network. One-hot-encoded sequences pass through a one-dimensional convolutional layer, average pooling, and a 256-unit fully connected layer before separate free-radical-scavenging (FRS) and chelation (CHEL) outputs are generated [@olsen2020anoxpepred]. Three operational endpoints were examined: CHEL≥0.25; CHEL≥0.25 with FRS<0.50; and CHEL≥0.25 with FRS<0.45. No model was retrained. Because row-level outputs and the NTxPred2-to-mebipred handoff were unavailable, agreement across models was interpreted as serial computational triage rather than independent biological confirmation.

### Sequence characterization and docking-score analysis

A separate table contained twelve peptide sequences described as the CHEL/FRS main set. Their correspondence to the twelve aggregate endpoint rows could not be established because stable identifiers and sequence-level CHEL/FRS values were unavailable. Sequence length and counts of histidine, cysteine, basic residues (Arg+Lys), and aromatic residues (Phe+Tyr+Trp) were recalculated directly from each string. The analysis required unique sequences composed only of standard amino acids.

The available docking summary stated that the twelve peptides had been docked with AutoDock Vina 1.2.5 against human AChE PDB 4EY6 using a 40×40×40 Å³ box centred on the peripheral anionic site [@cheung2012ache; @trott2010vina; @eberhardt2021vina]. Means and standard deviations were transcribed, checked for numeric range and ordering, and analyzed descriptively. Docking was not rerun because prepared receptor and ligand structures, PDBQT files, exact box-centre coordinates, protonation and charge settings, configurations, exhaustiveness, run numbers, random seeds, raw scores, logs, poses, and interaction tables were unavailable. The Vina values were therefore treated as screening scores rather than binding affinities or free energies. The standard deviations cannot be linked to a known replication unit without run-level information.

### Prospective molecular-dynamics protocol

A prospective 100-ns MD protocol was specified for apo human AChE and AChE complexes labelled for ALLLHRC, FLLHTTR, and YLSLLQR. Simulations were planned with GROMACS [@abraham2015gromacs] using the Amber99SB-ILDN force field [@lindorfflarsen2010amber], TIP3P water, a triclinic periodic box with a 1.0-nm solute-to-boundary distance, neutralization, and 0.15 mol/L NaCl. Energy minimization comprised 2,000 steepest-descent steps with 1,255 kJ mol⁻¹ nm⁻² heavy-atom positional restraints. The equilibration schedule comprised 1.0 ns restrained NVT heating from 10 to 300 K, 1.0 ns restrained NPT equilibration, and 1.0 ns unrestrained NPT equilibration at 300 K and 1 bar.

The prospective production stage was 100 ns with a 2-fs time step, LINCS constraints on hydrogen-containing bonds, 1.2-nm real-space cutoffs, force-switched van der Waals interactions from 1.0 nm, particle-mesh Ewald electrostatics, velocity-rescale temperature coupling, and Berendsen pressure coupling. Coordinates were scheduled every 20 ps, corresponding to 5,000 planned frames per trajectory. Prespecified analyses included complex-, AChE-, and peptide-level RMSD and RMSF, radius of gyration, solvent-accessible surface area, radial distribution functions, DSSP-derived secondary structure, hydrogen bonds, residue contacts, and bridging-water analyses. Complete starting coordinates, terminal and protonation states, topologies, random seeds, replicate definitions, run logs, trajectories, checkpoint files, energies, and final coordinates are required for acceptance of the trajectory analyses. Trajectory processing and quality control are ongoing, and the resulting stability, convergence, contact, and between-system measurements will be incorporated after the prespecified analysis is complete.

### Statistical analysis

All analyses were descriptive. Percentages were calculated as 100×n/N using the stated denominator for each transition. Candidate sequences are computational units nested within samples, assemblies, genomes, and homologous sequence groups; they are not independent biological replicates. Without subject- or sample-to-candidate rows, Fisher or χ² tests on aggregate peptide counts would introduce pseudoreplication. Therefore, no p values, confidence intervals, effect estimates, receiver-operating-characteristic analyses, power calculations, or multiplicity corrections were calculated for healthy-versus-periodontitis comparisons. Branch sums, numerator≤denominator constraints, the evaluated/not-evaluated partition, downstream monotonicity, the 8-of-12 sensitivity, sequence composition, and score ordering were checked deterministically.

## Results

### Sequence-evidence filtering reduced both smORF libraries by more than 99.7%

The healthy-labelled and periodontitis-labelled branches began with 11,269,961 and 11,721,988 smORFs. Sequence-evidence filtering and dereplication retained 31,510 (0.2796%) and 33,786 (0.2882%) candidates, respectively (Table 1). Short- plus long-branch counts reproduced each filtered total. These percentages describe computational retention, not participant prevalence or disease enrichment.

**Table 1. Aggregate candidate libraries and BBB-high outputs.**

| Branch | Raw smORFs | Evidence-filtered | Short background (5–30 aa) | BBB-high short, n (%) | Long background (31–50 aa) | BBB-high long, n (%) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Healthy-labelled | 11,269,961 | 31,510 | 30,557 | 3,359 (10.99) | 953 | 40 (4.20) |
| Periodontitis-labelled | 11,721,988 | 33,786 | 32,754 | 3,446 (10.52) | 1,032 | 72 (6.98) |

Short-branch BBB-high rates were 10.99% and 10.52%, whereas long-branch rates were 4.20% and 6.98%. The periodontitis-labelled branch contributed 3,446 short and 72 long BBB-high outputs, for a combined 3,518; 97.95% were in the short branch. Its supplied short-candidate length summary contained 547 sequences at 5–7 aa, 2,893 at 8–15 aa, and 6 at 16–30 aa, with 72 long candidates at 31–50 aa. Missing row identities prevented overlap, taxonomic, and participant-distribution analyses.

The broad antimicrobial output showed near-complete positivity: 30,537/30,557 healthy-labelled short candidates (99.93%) and 32,721/32,754 periodontitis-labelled short candidates (99.90%) exceeded the common 0.80 threshold. This saturation is unlikely to estimate experimentally active oral antibiotics and instead suggests sequence-domain shift, calibration limitations, or an unsuitable common threshold for this label.

### Serial model filtering yielded 12- and 8-candidate endpoints

NTxPred2 evaluated 3,299/3,518 periodontitis-labelled BBB-high candidates (93.77%); 219/3,518 (6.23%) were below the stated model range. Among evaluated candidates, 923/3,299 (27.98%) were model-positive. The subsequent aggregate counts were 111 mebipred-positive candidates, 15 candidates with CHEL≥0.25, 12 candidates with CHEL≥0.25 and FRS<0.50, and 8 candidates with CHEL≥0.25 and FRS<0.45 (Table 2). Tightening the FRS threshold retained 8/12 (66.67%) of the main count. The absence of row-level handoff data prevents interpretation of 111/923 as a verified transition rate.

**Table 2. Aggregate periodontitis-labelled prioritization results.**

| Stage | Operational rule | n | Denominator or limitation |
| --- | --- | ---: | --- |
| BBB-high short | UniDL4BioPep BBB output≥0.80; 5–30 aa | 3,446 | 32,754 short candidates |
| BBB-high long | UniDL4BioPep BBB output≥0.80; 31–50 aa | 72 | 1,032 long candidates |
| BBB-high total | Short + long | 3,518 | Arithmetic sum |
| NTxPred2 evaluated | Stated range 7–50 aa | 3,299 | 3,518 BBB-high candidates |
| NTxPred2 not evaluated | Below stated range | 219 | 3,518 BBB-high candidates |
| NTxPred2-positive | Model-positive label | 923 | 3,299 evaluated candidates |
| Metal-binding-positive | Mebipred output≥0.50 | 111 | Row-level handoff unavailable |
| CHEL-priority | CHEL≥0.25 | 15 | 111 metal-positive candidates |
| Main set | CHEL≥0.25 and FRS<0.50 | 12 | 111 metal-positive candidates |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | Sequence membership unavailable |

### The twelve supplied sequences were compositionally distinct

The separate sequence table contained twelve unique peptides composed of standard amino acids and ranging from 7 to 9 residues (Table 3). Eleven contained histidine, six contained cysteine, and every sequence contained at least one Arg or Lys. These properties are useful for synthesis planning and hypothesis design, but they do not establish metal binding, BBB transport, toxicity, taxonomy, or correspondence to the twelve aggregate endpoint rows. The identities of the stricter 8-of-12 subset remain unknown because sequence-level FRS labels were unavailable.

**Table 3. Twelve-sequence set and recalculated composition.**

| Rank by Vina mean | Sequence | Length | His | Cys | Arg+Lys | Phe+Tyr+Trp |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | 1 | 0 | 1 | 1 |
| 2 | YLSLLQR | 7 | 0 | 0 | 1 | 1 |
| 3 | ALLLHRC | 7 | 1 | 1 | 1 | 0 |
| 4 | FCLHLQLR | 8 | 1 | 1 | 1 | 1 |
| 5 | YHHLLCRR | 8 | 2 | 1 | 2 | 1 |
| 6 | LLHLPKRTT | 9 | 1 | 0 | 2 | 0 |
| 7 | LLHPLRL | 7 | 1 | 0 | 1 | 0 |
| 8 | WLLVHLKK | 8 | 1 | 0 | 2 | 1 |
| 9 | LLHPLRC | 7 | 1 | 1 | 1 | 0 |
| 10 | HLLTLKKHV | 9 | 2 | 0 | 2 | 0 |
| 11 | HLPLLHRCC | 9 | 1 | 2 | 1 | 0 |
| 12 | HVLLLRQCA | 9 | 1 | 1 | 1 | 0 |

### Available Vina summaries provided a descriptive ordering only

The docking table contained Vina means from −9.60 to −8.25 kcal/mol and standard deviations from 0.04 to 0.12 (Table 4). FLLHTTR, YLSLLQR, and ALLLHRC had the three lowest means, whereas HLPLLHRCC and HVLLLRQCA had the two highest. The approximately 1.35-kcal/mol range describes only this scoring table. Without prepared inputs, run definitions, poses, or interaction files, residue-level contacts, target-site preference, affinity, and functional activity could not be evaluated.

**Table 4. Available AutoDock Vina summary for human AChE PDB 4EY6.**

| Rank | Sequence | Mean score (kcal/mol) | SD |
| ---: | --- | ---: | ---: |
| 1 | FLLHTTR | −9.60 | 0.08 |
| 2 | YLSLLQR | −9.49 | 0.05 |
| 3 | ALLLHRC | −9.29 | 0.11 |
| 4 | FCLHLQLR | −9.27 | 0.09 |
| 5 | YHHLLCRR | −9.03 | 0.07 |
| 6 | LLHLPKRTT | −9.01 | 0.06 |
| 7 | LLHPLRL | −8.94 | 0.10 |
| 8 | WLLVHLKK | −8.94 | 0.04 |
| 9 | LLHPLRC | −8.91 | 0.08 |
| 10 | HLLTLKKHV | −8.88 | 0.05 |
| 11 | HLPLLHRCC | −8.35 | 0.12 |
| 12 | HVLLLRQCA | −8.25 | 0.09 |

## Discussion

### Principal findings

This computation-only analysis reduced a very large oral-smORF search space to two clearly bounded objects for follow-up: an aggregate endpoint of 12 candidates with a stricter count of 8, and a separate list of twelve explicit 7–9-aa sequences accompanied by descriptive AChE docking scores. The aggregate arithmetic, predictor applicability, sequence composition, and score ordering could be checked. The sequence-level connection between the funnel and the explicit peptide list, however, could not be established. The main value is therefore prioritization and identification of the information required for validation, not demonstration of a peptide-mediated AD mechanism.

The filtering sequence should not be interpreted as accumulating independent evidence. ESM-derived representations, sequence-composition features, and task-specific training sets can produce correlated errors. Near-universal antimicrobial positivity in the short-peptide branches highlights this concern. A score above a threshold may be useful for ranking, but it does not establish BBB transport, neurotoxicity, metal binding, antioxidant activity, or biological exposure.

### Relation to current smORF and peptide-discovery standards

Contemporary smORF discovery increasingly combines coding evidence, transcriptomics, ribosome association, targeted proteomics, conservation, and functional assays [@sberro2019smallgenes; @durrant2021sorf; @davin2026multiomics; @couso2017sorfs; @vanheesch2019heart]. The present exact-match filter narrows the sequence space and may support prior observation of a peptide or related sequence, but a match across heterogeneous oral resources does not demonstrate expression in the supplied disease-labelled branch. Taxonomic ambiguity is particularly important for short peptides because many sequences may map to multiple taxa, homologues, or translated frames.

A defensible follow-up requires a candidate-level matrix linking each sequence to genomic coordinates, assembly, sample, clinical label, taxonomic assignment, peptide-spectrum evidence, predictor scores, applicability flags, and final membership. Without this structure, the similar aggregate retention fractions in the two starting libraries cannot be interpreted as enrichment or depletion, and the periodontitis label cannot be transferred to an individual peptide.

### Interpretation of the AChE docking hypothesis

AChE is a reasonable structural target for hypothesis generation because its peripheral region has been linked to Aβ assembly and can be modulated by ligands [@inestrosa1996ache; @deferrari2001motif; @bartolini2003pas; @kryger1999e2020; @cheung2012ache]. AutoDock Vina provides an efficient first-pass scoring framework [@trott2010vina; @eberhardt2021vina], but flexible 7–9-aa peptides are challenging docking ligands. Protonation, terminal states, initial conformers, receptor flexibility, box placement, exhaustiveness, and stochastic sampling can change rank order. The available means therefore define a list for independent reproduction rather than evidence of binding.

The reported standard deviations cannot be interpreted without knowing the replication unit. Scores from a single target and protocol do not establish selectivity, peripheral-site preference, catalytic inhibition, Aβ modulation, or cellular activity. Independent reproduction should use deposited prepared structures, exact parameters, multiple peptide conformers and seeds, all raw scores and poses, and peptide-appropriate refinement. FlexPepDock or an equivalent peptide-specific method could be used to evaluate whether the ranking is stable after flexible refinement [@london2011flexpepdock]. MD should begin only from documented and independently inspected starting complexes; it cannot compensate for an uncertain docking pose.

### Metal-binding and neurotoxicity hypotheses

The high frequency of histidine and cysteine provides plausible coordination groups, but composition and mebipred scores do not determine metal affinity, selectivity, stoichiometry, geometry, oxidation state, or redox consequence. Experimental studies of metal–peptide systems show that these properties require direct structural and biophysical measurement [@bush2013metal; @lei2021elements; @dinatale2018tau; @perini2019tau]. Likewise, NTxPred2 positivity is a sequence-classification result rather than evidence of neuronal injury.

A minimum validation package would quantify Cu(II), Fe(II/III), and Zn(II) interactions by complementary spectroscopic and thermodynamic methods and test metal-dependent reactive oxygen species and lipid peroxidation. Controls should include peptide-only, metal-only, scrambled-sequence, composition-matched, and established positive and negative conditions. Toxicology should use concentration–response designs in neuronal and non-neuronal cells, with membrane-integrity and nonspecific-aggregation controls. Predictions should determine experimental order, not the interpretation of experimental outcomes.

### Periodontitis and AD remain a hypothesis-generating context

Observational and longitudinal studies support continued investigation of the periodontitis–AD relationship, but heterogeneity, confounding, reverse causation, and negative genetic causal analyses constrain interpretation [@larvin2023periodontalcognition; @kaliamoorthy2022periodontitisad; @liu2023oralbacteriaad; @kim2025periodontitisdementia; @ide2016periodontitis; @jiang2021periodontitis; @hu2024mendelian; @zhao2026mendelian; @chalmers2025primer]. Specific *P. gingivalis* studies support the plausibility of gingipain, inflammatory, infection-related, or vesicle-associated routes [@dominy2019pgingivalis; @poole2013pg; @ilievski2018oral; @ho2015omv; @guo2010gingipain; @haditsch2020cor388; @nara2021omv]. None of those findings assigns the twelve peptides to *P. gingivalis* or demonstrates their presence outside the oral cavity.

Accordingly, the current results do not show that the candidates are periodontitis-specific, *P. gingivalis*-derived, translated in the relevant oral community, present in blood or brain, or causally related to AD. Establishing such a chain would require sequence-to-assembly-to-sample mapping, cohort-matched expression evidence, systemic exposure measurements, BBB transport experiments, target-engagement assays, and disease-relevant phenotypes.

### Statistical interpretation, validation sequence, and limitations

Candidate counts cannot serve as independent participant-level observations. Millions of smORFs may be correlated within a sample, assembly, genome, or homologous sequence family. A valid healthy–periodontitis comparison would require a participant- or sample-level feature matrix, prespecified outcomes, consistent denominators, homology handling, and models that account for clustering and relevant covariates. Descriptive percentages are therefore the maximum supported analysis for the available aggregate data.

Validation should proceed sequentially. First, the twelve explicit sequences should be linked to the 12-candidate endpoint and the stricter subset of 8, and all predictor outputs should be regenerated with fixed model versions. Second, translation and expression should be tested by cohort-matched metatranscriptomics, ribosome profiling where feasible, and targeted metaproteomics with peptide-level false-discovery control. Third, synthesized peptides should undergo identity, purity, solubility, aggregation, and serum/protease-stability testing. BBB transport, cytotoxicity, metal chemistry, AChE/BChE activity, direct binding, and Aβ assays should follow only for candidates that pass the earlier steps. Complex disease models are warranted only after identity, exposure, reproducible biochemical activity, and biologically replicated phenotypes have been established.

The principal limitations are the absence of row-level funnel data, the unresolved relationship between the aggregate endpoint and the explicit peptide list, lack of raw docking inputs and poses, ongoing MD trajectory analysis, and the absence of experimental measurements. Candidate taxonomy, translation, cohort expression, BBB transport, toxicity, metal chemistry, AChE binding or function, Aβ effects, and disease association were not measured. These limitations define the current study as computational prioritization rather than mechanism validation.

## Conclusion

Aggregate computational data support a transparent candidate-prioritization funnel ending in 12 main and 8 stricter candidate counts. A separate table provides twelve explicit 7–9-aa peptides and an AChE Vina score ordering, but the sequence-level link to the funnel and the docking execution cannot be reconstructed from the available material. The prespecified MD extension will add trajectory-derived stability and contact measurements after analysis and quality control are complete. The current shortlist is suitable for independent computational reproduction and staged experimental testing, but it does not establish peptide expression, *P. gingivalis* origin, BBB passage, neurotoxicity, metal-dependent activity, AChE engagement, AD relevance, or causality.

## References

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
4. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
5. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
6. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
7. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
8. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
9. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
10. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
11. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
12. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
13. Kim J, Han DH. Periodontitis as a risk factor for dementia. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
14. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
15. Jiang Z, Shi Y, Zhao W, et al. Association between chronic periodontitis and the risk of Alzheimer’s disease. *BMC Oral Health*. 2021;21:466. doi:10.1186/s12903-021-01827-2.
16. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
17. Zhao Y, Zhang C, Chang X, et al. Causal association between periodontitis and systemic diseases: a systematic review and meta-analysis of Mendelian randomization studies. *BMC Oral Health*. 2026;26:383. doi:10.1186/s12903-026-07725-9.
18. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
19. Poole S, Singhrao SK, Kesavalu L, et al. Determining the presence of *Porphyromonas gingivalis* in Alzheimer’s disease brain. *J Alzheimers Dis*. 2013;33(3):665–678. doi:10.3233/JAD-2012-121149.
20. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
21. Haditsch U, Roth T, Rodriguez L, et al. Alzheimer’s disease-like neurodegeneration in *Porphyromonas gingivalis* infected neurons with persistent expression of active gingipains. *J Alzheimers Dis*. 2020;75(4):1361–1376. doi:10.3233/JAD-200393.
22. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
23. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
24. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
25. Davin ME, Ortís Sunyer J, Delgado LF, et al. High-resolution multi-omics enhances prediction and detection of smORF-encoded proteins in the human gut microbiome. *Nat Commun*. 2026. doi:10.1038/s41467-026-72762-5.
26. Couso JP, Patra P. Short ORFs: finding gems in hidden places. *Curr Opin Genet Dev*. 2017;45:14–21. doi:10.1016/j.gde.2017.04.002.
27. van Heesch S, Wit F, Botter J, et al. The translational landscape of the human heart. *Cell*. 2019;178(1):236–251.e24. doi:10.1016/j.cell.2019.05.010.
28. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
29. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
30. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
31. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
32. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
33. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
34. Liu X, Zhao Z, Guan J, et al. Prediction of blood-brain barrier-penetrating peptides using B3BPFN. *Front Mol Biosci*. 2026;13:1858506. doi:10.3389/fmolb.2026.1858506.
35. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
36. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
37. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
38. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
39. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
40. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
41. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept). *Structure*. 1999;7(3):297–307. doi:10.1016/s0969-2126(99)80040-9.
42. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
43. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
44. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
45. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
46. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
47. Lushchekina SV, Kots ED, Novichkova DA, et al. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7:396–402. doi:10.1007/s12668-016-0375-x.
48. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
49. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer’s disease. *J Biol Chem*. 2021;296:100105. doi:10.1074/jbc.REV120.008207.
50. Di Natale G, Bellia F, Sciacca MFM, et al. Tau-peptide fragments and their copper(II) complexes: effects on amyloid-β aggregation. *Inorg Chim Acta*. 2018;472:82–92. doi:10.1016/j.ica.2017.09.061.
51. Perini G, Ciasca G, Minelli E, et al. Dynamic structural determinants underlie the neurotoxicity of the N-terminal tau 26–44 peptide. *Int J Biol Macromol*. 2019;141:278–289. doi:10.1016/j.ijbiomac.2019.08.220.
52. Chen SG, Stribinskis V, Rane MJ, et al. Exposure to the functional bacterial amyloid protein curli enhances alpha-synuclein aggregation. *Sci Rep*. 2016;6:34477. doi:10.1038/srep34477.
53. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
54. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
55. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
