## Abstract

Periodontitis-associated oral dysbiosis has been proposed as a modifiable contributor to neuroinflammatory processes relevant to Alzheimer’s disease (AD), but the molecular entities connecting the oral microbiome to the brain remain unresolved. Microbiome small open reading frames (smORFs) encode a largely uncharacterized peptide space that is amenable to computational triage but not to direct mechanistic inference. Here, we performed a computation-only reconstruction of an aggregate oral-smORF prioritization workflow and integrated a separately archived acetylcholinesterase (AChE) docking summary under explicit provenance controls. Candidate libraries were filtered by sequence/proteomic evidence and prioritized with a deep-learning-guided cascade comprising ESM-2 embeddings with task-specific convolutional networks, a fine-tuned ESM2-t30 neurotoxicity model, a two-tier neural-network metal-binding predictor, and a multi-task antioxidant CNN. Evidence filtering retained 31,510 and 33,786 candidates in the two supplied branches. In the periodontitis-labelled branch, 3,518 candidates were BBB-high; 3,299 were within the NTxPred2 peptide-length domain, 923 were model-positive, and the source record subsequently reported 111 metal-binding-positive candidates, 15 CHEL-priority candidates, a 12-member main set, and an 8-member stricter subset. The external record listed twelve unique 7–9-residue sequences whose composition was independently reproducible and reported AChE Vina means spanning −9.60 to −8.25 kcal/mol. These docking values could be ordered but not independently reproduced or interpreted as affinities because prepared structures, configurations, raw runs, logs, and poses were unavailable. A prospective 100-ns GROMACS protocol was registered from a versioned external workflow, whereas incomplete trajectory analyses were excluded and no molecular-dynamics result is reported. The resulting shortlist is therefore a transparent hypothesis set rather than evidence of translation, brain exposure, neurotoxicity, metal-dependent chemistry, AChE engagement, a periodontitis-specific peptidome, or an AD mechanism.

**Keywords:** deep learning; protein language model; oral microbiome; small open reading frame; micropeptide; periodontitis; blood–brain barrier; neurotoxicity prediction; metal-binding prediction; acetylcholinesterase; molecular docking; molecular dynamics; provenance; hypothesis generation

## 1. Introduction

### 1.1 Alzheimer’s disease as a multilevel biological problem

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder in which amyloid-β (Aβ) deposition, tau pathology, synaptic failure, glial activation, vascular dysfunction, and systemic comorbidity interact over a prolonged preclinical and clinical continuum [20]. The amyloid hypothesis remains central to disease biology, particularly as a framework for initiating events, but amyloid burden alone does not account for the full spatial, temporal, and clinical heterogeneity of AD [21]. Contemporary interpretation therefore places amyloid and tau within a broader network that includes innate immune signalling, neuronal vulnerability, lipid and metal homeostasis, cerebrovascular integrity, and age-dependent loss of resilience. This systems view is important when evaluating peripheral exposures: a biologically plausible contributor need not be a single sufficient cause, but it must still be connected to disease-relevant tissue through traceable molecular and temporal evidence.

The cholinergic system illustrates the distinction between clinical relevance and causal sufficiency. Loss of cholinergic function contributes to cognitive symptoms, and acetylcholinesterase (AChE) inhibitors remain established symptomatic treatments [22]. AChE also has non-catalytic interactions with Aβ assembly, creating a structural link between cholinergic biology and amyloid research [23]. Neither observation means that every predicted AChE-interacting molecule is relevant to AD. Target engagement, direction of effect, tissue exposure, concentration, selectivity, and downstream phenotype must all be established. This evidentiary sequence provides a useful standard for evaluating microbial molecules proposed to participate in an oral–brain axis.

Chronic peripheral inflammatory states have consequently attracted attention as possible modifiers of neurodegenerative vulnerability. Periodontitis is of particular interest because it combines persistent mucosal inflammation, a dysbiotic polymicrobial biofilm, episodic access of microbial products to the circulation, and strong age and comorbidity gradients [43]. These same features make causal interpretation difficult. Periodontitis may contribute to systemic inflammatory burden, but it may also share determinants with cognitive decline, while declining cognition can worsen oral hygiene and access to dental care. A rigorous molecular study must therefore separate association, route plausibility, molecular identity, and demonstrated function rather than treating them as interchangeable evidence.

### 1.2 Periodontal dysbiosis and *Porphyromonas gingivalis*

Periodontitis is an ecological disease of the tooth-supporting tissues rather than the consequence of a single pathogen. In susceptible hosts, altered community structure, inflammatory nutrient release, and impaired resolution can reinforce one another, producing a dysbiotic environment with site-specific transcriptional activity. Paired oral metagenomic and metatranscriptomic data show that disease-associated signals vary by species and oral site and that taxonomic abundance cannot substitute for functional activity [6]. Cross-study metatranscriptomic synthesis further shows that disease signatures depend on cohort definition, sampling site, sequencing depth, normalization, covariates, and subject-level replication [7]. These observations argue against describing every sequence recovered from a disease-labelled branch as disease-specific.

Within this community, *Porphyromonas gingivalis* is a well-studied Gram-negative anaerobic pathobiont. Its importance derives not simply from abundance but from its capacity to reshape host–microbial interactions through proteolysis, immune modulation, community cooperation, and vesicle-mediated cargo delivery. Gingipains have context-dependent effects on host proteins, complement pathways, inflammation, tissue integrity, and nutrient acquisition [48]. *P. gingivalis* outer-membrane vesicles can concentrate and transport bacterial components beyond the producing cell and alter interactions with host tissues and neighbouring microorganisms [47]. These properties make *P. gingivalis* biologically relevant to oral–systemic hypotheses, but they do not justify assigning an untraced community-derived peptide to this organism.

The distinction between an organism-level hypothesis and a community-peptide hypothesis is fundamental. Detection of *P. gingivalis* DNA, antigen, gingipain-associated signal, or vesicular material does not imply that a particular short peptide was expressed, secreted, stable in blood, transported across the blood–brain barrier (BBB), or active in neural tissue. Conversely, a metagenome-derived peptide that cannot be assigned to *P. gingivalis* could still originate from another oral taxon or from an assembly artefact. The oral metagenome is therefore treated here as a community sequence space, while *P. gingivalis* provides mechanistic context rather than a presumed taxonomic label.

### 1.3 Human, experimental, and genetic evidence do not carry equal causal weight

The periodontitis–AD literature contains several evidence classes that address different questions. Observational reviews and meta-analyses commonly report associations between periodontal disease and cognitive disorders, but their estimates vary with periodontal definitions, dementia ascertainment, follow-up, age structure, and adjustment strategy [35]. Clinical syntheses likewise identify a recurring association while emphasizing heterogeneity and the limited ability of retrospective designs to establish directionality [36]. Reviews focused on oral bacteria broaden the candidate mechanisms but also reveal that organism detection, antibody responses, oral disease status, and dementia outcomes are often measured in different populations [37]. More recent evidence assessments continue to classify periodontitis as a possible risk marker while calling for stronger longitudinal and interventional designs [38].

Longitudinal observations provide temporal information but remain susceptible to confounding and reverse causation. In an AD cohort, periodontitis was associated with subsequent cognitive decline and a pro-inflammatory state [39]. Public-data and text-mining analyses have also proposed shared molecular signals [40]. Such studies can prioritize pathways, yet they cannot determine whether periodontal exposure caused neurodegeneration, whether emerging cognitive impairment altered oral health, or whether both were influenced by age, smoking, diabetes, medication, frailty, socioeconomic conditions, or health-care access.

Genetic-instrument approaches provide an important counterweight to an exclusively positive narrative. A two-sample Mendelian-randomization analysis did not establish evidence for a genetic causal effect of periodontal disease on AD [41]. A broader synthesis of Mendelian-randomization studies similarly illustrates that putative systemic consequences of periodontitis are not uniformly supported across outcomes or instrument choices [42]. These findings do not prove the absence of every acquired inflammatory or microbial pathway, because genetic liability and time-varying exposure are not identical. They do, however, weaken claims that the epidemiological association by itself demonstrates causality.

Mechanistic studies answer narrower questions under controlled conditions. *P. gingivalis* material and gingipain-associated signals have been reported in AD-related post-mortem samples [44]. Earlier tissue work also examined the presence of *P. gingivalis* in AD brain material [45]. Repeated oral exposure in wild-type mice produced brain inflammation, neurodegenerative changes, and Aβ-related alterations [46]. Infected neuronal systems have shown persistent gingipain activity and AD-like cellular phenotypes [49]. Vesicle-focused studies provide a plausible vehicle for concentrated microbial cargo and host signalling [50]. The strength of these studies is mechanistic resolution; their limitation is transferability. Differences in dose, exposure route, model organism, cell system, disease stage, and endpoint prevent direct extrapolation to naturally occurring human peptide exposure.

Taken together, the literature supports a research question, not a settled pathway. Human associations establish relevance, experimental models establish selected possibilities, and negative or equivocal causal analyses constrain interpretation. A defensible study should identify a molecular entity, trace it to its source, demonstrate exposure, and then test a prespecified function. The present work addresses only the first computational steps of that sequence.

### 1.4 Candidate routes from the periodontal niche to the brain

Several non-exclusive routes have been proposed to connect periodontal dysbiosis with neurodegenerative processes. One is indirect: chronic periodontal inflammation may alter circulating cytokines, acute-phase responses, endothelial activation, or immune-cell states, which could influence neurovascular and glial function without requiring a viable organism to enter the brain [43]. A second involves episodic dissemination of bacterial cells or soluble products during tissue inflammation or routine mechanical disturbance. A third involves outer-membrane vesicles, which protect and concentrate lipids, proteins, nucleic acids, and other bacterial cargo [47]. A fourth involves specific enzymes or molecular fragments, including gingipain-related products, that could modify host substrates [48]. The relative contribution of these routes in humans remains uncertain.

Each route imposes a different evidence requirement. An inflammatory route requires exposure-response and mediation evidence. A dissemination route requires matched oral and systemic molecular identities. A vesicular route requires cargo characterization, biodistribution, and barrier-transport data. A direct peptide route additionally requires proof that the small open reading frame is translated, that the peptide survives processing and proteolysis, and that a sufficient concentration reaches the relevant tissue compartment. BBB prediction alone cannot satisfy these requirements because permeability depends on peptide conformation, charge, transport mechanisms, serum binding, degradation, efflux, and experimental context.

Microbially encoded small proteins and peptides remain underexplored within this framework. Short molecules could in principle act as ligands, enzyme modulators, membrane-active agents, immune signals, metal-binding species, or inert degradation products. The hypothesis space is therefore broad, but broad plausibility is not evidence for a particular sequence. The unresolved molecular gap is whether any traceable oral-microbial peptide is expressed in the relevant ecological context, disseminates beyond the mouth, and exerts a reproducible neural or vascular effect. Computational prioritization is valuable only insofar as it reduces this space without erasing these sequential requirements.

### 1.5 Microbiome smORFs form a legitimate but technically difficult discovery space

Small open reading frames (smORFs) are systematically under-annotated because short coding regions are difficult to distinguish from random open reading frames, provide limited phylogenetic signal, and often fall below conventional gene-calling thresholds. Large-scale analysis of human-associated microbiomes nevertheless identified thousands of conserved small-gene families, many lacking known domains [1]. Dedicated annotation approaches improve discovery by combining profile models, coding features, conservation, and other evidence rather than applying protein-length cut-offs designed for conventional genes [2]. High-resolution multi-omics can strengthen candidate status by linking predictions to transcriptional and proteomic observations [3].

The evidence ladder remains steep. A predicted smORF is not necessarily transcribed; a transcript is not necessarily translated; a peptide-spectrum match is not automatically unique or correctly assigned; and a detected peptide is not necessarily stable or functional. Reviews of short-ORF biology emphasize the need for orthogonal validation and careful nomenclature [4]. Proteogenomic studies likewise show that translation evidence must be interpreted with tissue, reading-frame, false-discovery, and functional context [5]. These constraints are amplified in metagenomes, where fragmented assemblies, homologous sequences, strain variation, and six-frame translation can create millions of short candidates.

Oral sequence and metaproteome resources provide complementary but non-equivalent evidence. HOMD and eHOMD curate oral and aerodigestive taxonomic and genomic information [8]. Salivary metaproteome datasets can support peptide detection within their own sample and false-discovery framework [10]. A lung-cancer oral metaproteome provides another context-specific observation space [11]. Contemporary salivary metaproteomics emphasizes host depletion, microbial enrichment, peptide- and protein-level error control, taxonomic ambiguity, and public raw-data preservation [12]. An exact match against any one resource may support sequence existence or prior observation, but it cannot by itself establish expression in the current disease-labelled branch.

This distinction makes sample-level provenance indispensable. A disease comparison requires a chain from sequence to contig, assembly or bin, specimen, participant, oral site, clinical group, and processing batch. Without that chain, candidate counts are computational accounting units rather than independent biological replicates. The present record preserves aggregate branch labels and counts but not the row-level mapping needed to estimate prevalence, enrichment, taxonomic origin, or between-participant uncertainty. Accordingly, the term “periodontitis-labelled branch” is used instead of “periodontitis-specific peptidome.”

### 1.6 Deep-learning-guided prioritization is triage, not validation

The scale of the smORF search space motivates sequence-based models, but their outputs inherit the assumptions and domain limits of their training data. UniDL4BioPep uses contextual embeddings from a pretrained ESM-2 model followed by task-specific convolutional neural networks for peptide-bioactivity classification [13]. Protein language models can capture sequence regularities that are difficult to encode manually, yet an output score remains model-specific: it is not a calibrated biological probability unless calibration has been demonstrated in a comparable sequence and task domain.

BBB-peptide prediction illustrates this limitation. Augur combines engineered descriptors, feature selection, class-balancing and a random-forest classifier rather than deep learning [14]. B3BPFN represents a different model family and dataset construction strategy [15]. Differences among methods in positive-set definition, redundancy reduction, negative sampling, sequence length, class balance, and validation design can materially change apparent performance. Very short, leucine-rich, cationic or compositionally unusual microbiome peptides may lie outside the distributions on which these models were evaluated. A “BBB-high” output therefore defines a prioritization threshold, not measured transport.

The downstream tools are likewise heterogeneous. The peptide mode of NTxPred2 fine-tunes an ESM2-t30 protein language model for neurotoxic-peptide classification [16]. Mebipred uses engineered sequence descriptors and a two-tier artificial-neural-network framework to estimate general and ion-related metal-binding potential [17]. AnOxPePred uses one-dimensional convolution and multi-task outputs for free-radical-scavenging and chelation-related properties [18]. Serial agreement among these tools is not orthogonal replication: the models reuse sequence composition, were trained on different endpoints, and may propagate correlated biases through the funnel.

The appropriate interpretation is triage. “Neurotoxic-positive” is not neuronal toxicity; “metal-binding-positive” is not a measured dissociation constant or coordination geometry; CHEL and FRS outputs are not redox chemistry. A strong precedent from microbiome peptide mining shows that computational candidates become biological findings only after synthesis and controlled functional testing [19]. In a computation-only study, the scientific contribution is therefore the transparent reduction of a candidate space, explicit model descriptions, domain warnings, and a reproducible account of what remains untested.

### 1.7 AChE, metal homeostasis, docking, and molecular dynamics define a structural hypothesis

AChE provides a biologically motivated but demanding structural follow-up. Beyond hydrolysing acetylcholine, AChE can accelerate Aβ fibril assembly [23]. A defined AChE motif has been implicated in promoting Aβ fibril formation [24], and PAS-directed ligands can inhibit AChE-induced Aβ aggregation in biochemical systems [25]. Structural studies map an aromatic gorge connecting the catalytic machinery with the peripheral site [26]. The human AChE structure represented by PDB 4EY6 provides an experimentally determined receptor framework for ligand-oriented questions [27]. These findings justify asking whether a candidate peptide can occupy a reproducible region of the AChE surface; they do not establish binding, inhibition, or an effect on Aβ.

Docking flexible 7–9-residue peptides is especially uncertain because peptide protonation, termini, initial conformers, receptor flexibility, search-space placement, scoring stochasticity, and post-docking refinement can alter rank order. AutoDock Vina is a useful screening engine, but its scores are not experimental affinities or binding free energies [51]. Later Vina implementations expand methods and interfaces without removing the need for complete preparation and execution records [52]. Peptide-specific refinement methods such as FlexPepDock illustrate the higher-resolution standard that could be applied after a transparent initial screen [53].

Molecular dynamics (MD) can test whether a prepared complex remains within a defined conformational basin under a specified force field and solvent model, but MD cannot rescue an untraceable or poorly prepared docking pose. Published AChE–Aβ simulations demonstrate that peptide residence and contacts can change over time [28]. Accelerated simulations further show how alternative AChE surface interactions may be explored [29]. For the present candidates, meaningful MD would require versioned starting coordinates, topology and protonation decisions, independently seeded trajectories, convergence assessment, and prespecified analyses. Until those elements and complete trajectories are available, MD remains a protocol rather than a result.

Metal biology defines a second structural hypothesis. Copper, iron, and zinc dyshomeostasis intersects with Aβ aggregation, redox chemistry, lipid peroxidation, and neuronal injury [30]. Broader elementomic perspectives place these interactions within a network rather than a single-metal mechanism [31]. Histidine- and cysteine-containing peptides may offer potential coordination groups, but composition cannot determine affinity, selectivity, stoichiometry, geometry, oxidation state, or redox consequence. Tau fragments show experimentally that Cu(II) coordination can alter peptide structure and Aβ aggregation [32]. The tau26–44 fragment further illustrates how a short dynamic peptide can be connected to membrane and cellular phenotypes through dedicated experiments [33]. Bacterial amyloid exposure can modify aggregation phenotypes in model systems [34]. These studies define testable comparators, not transferable activity.

### 1.8 Knowledge gap and study objectives

The literature converges on a carefully bounded gap. Periodontitis and AD have a heterogeneous observational relationship; *P. gingivalis* offers organism-specific mechanistic plausibility; and oral microbiomes encode a large, poorly characterized small-peptide space. What is missing is a traceable molecular chain linking a defined microbial smORF to translation, host exposure, BBB passage, target engagement, and a disease-relevant phenotype. No single computational score can bridge those levels.

This study therefore addresses an earlier, narrower question: can an aggregate oral-smORF record be reconstructed into an auditable candidate funnel, and can a separately reported AChE docking summary be integrated without converting incomplete provenance into biological certainty? The first objective was to recompute all reported proportions, check branch arithmetic and applicability constraints, and describe each prediction model according to its documented architecture. The second was to audit the supplied twelve-sequence set for uniqueness and composition and to preserve the external AChE score ordering as source-reported. The third was to register a reproducible downstream MD protocol while withholding incomplete trajectory outputs.

The contribution is a provenance-aware computational hypothesis set, not a new predictor, a clinical cohort analysis, an independently reproduced docking study, an MD result, or a validated AD mechanism. This framing preserves the value of deep-learning-guided prioritization while making the next evidentiary requirements explicit.

## 2. Materials and Methods

### 2.1 Study design and evidence tiers

This was a computation-only, aggregate-level reconstruction with cross-repository structural follow-up. No wet-laboratory experiment, participant recruitment, specimen collection, new omics processing, docking rerun, or completed molecular-dynamics analysis was performed in this manuscript. Evidence was assigned to four tiers before writing:

1. **Tier A—principal-source screening:** counts, thresholds, and workflow descriptions from `材料与方法及结果_机制研究版.docx` (SHA-256 `f4132a02cb9955c808739c3cbf15edd947f6203d577e8586490933a5d2daa4b5`).
2. **Tier B—external source record summary:** twelve sequences, composition claims, docking method labels, and Vina mean±SD values from commit `e28c06db0614512eeb2bca217d2f9a760e804051` of the separately archived external repository. File hashes and acceptance decisions are recorded in `evidence/external_v04_integration.md`.
3. **Tier C—prospective MD protocol:** versioned GROMACS scripts and 100-ns MDP files from commit `f11cd3751e8fce53dbf1a335ef1d8fa777751ef5` of `shaohuawen03-cyber/asd`. This tier defines future computation but supplies no accepted result.
4. **Tier D—literature context:** peer-reviewed evidence used to synthesize AD, periodontitis, *P. gingivalis*, AChE/PAS, metal, oral-microbiome, and validation questions. Literature was not used to manufacture missing results.

Tier A remained the sole authority for the screening funnel. Tier B did not retroactively fill principal-source row-level lineage. Tier C was restricted to prospective methods. Tier D supplied interpretation boundaries only.

### 2.2 Cohort and accession provenance

The principal record named PRJNA678453 and PRJEB65451. Accession and publication checks established that PRJNA678453 is the source paired oral metagenomic/metatranscriptomic project [6]. PRJEB65451 is not an independent clinical cohort; it is an EBI-EMG/MGnify-brokered Third Party Annotation metagenomic assembly project derived from PRJNA678453 with metaSPAdes v3.15.3. The full manuscript does not report participant, specimen, assembly-analysis, or metagenome-assembled-genome totals because the supplied package did not include the mapping and bin-level manifests needed to audit those units consistently.

No new participants were recruited, no specimens were collected, and no primary omics or clinical analysis was performed for this reconstruction. Candidate nucleotide/amino-acid rows, genomic coordinates, subject/sample mappings, accession-to-group assignments, MAG-bin manifests, bin-quality tables, taxonomy, peptide-spectrum matches, model outputs, run logs, database snapshots, and the original pipeline were absent from the principal package. Accession identifiers were therefore used only to delimit data provenance, not as candidate-level denominators or as independent confirmation of group labels.

### 2.3 Principal-source smORF construction and evidence filtering

According to the principal record, sample-specific mapping was used to construct healthy and periodontitis smORF libraries, and translated sequences 4–50 aa long were retained. The raw libraries contained 11,269,961 and 11,721,988 smORFs. Candidates were then exact-matched to named oral sequence/proteomic resources and dereplicated. The resulting evidence-filtered libraries contained 31,510 healthy and 33,786 periodontitis-branch candidates.

The filtered sets were divided into a short branch (5–30 aa: healthy 30,557; periodontitis 32,754) and a long branch (31–50 aa: healthy 953; periodontitis 1,032). The initial rule includes 4-aa candidates, but the downstream bins begin at 5 aa; the disposition of 4-aa sequences remains undocumented. Resource matches were treated as filter evidence rather than current-cohort expression or disease specificity.

### 2.4 Deep-learning sequence representation and BBB-high definition

UniDL4BioPep was used as the first functional-prioritization layer. Its documented architecture applies the pretrained ESM-2 model `esm2_t6_8M_UR50D` to encode each peptide as a 320-dimensional contextual embedding, followed by a six-layer task-specific convolutional neural network for binary peptide-bioactivity classification [13]. The supplied workflow applied an output threshold of ≥0.80, including for the BBB task. Because the exact server build, task-specific calibration, model hash, and external validation in this very-short-peptide domain were unavailable, outputs were described as “model-positive” or “BBB-high,” not as measured transport or confirmed activity. BBB-model literature was used only to contextualize domain and calibration limitations [14] [15]. Healthy and periodontitis counts remained descriptive branch summaries, and no candidate-count group-comparison test was performed.

### 2.5 Deep-learning-guided downstream prioritization

The periodontitis BBB-high set was next evaluated with the peptide mode of NTxPred2, which uses transfer learning by fine-tuning the ESM2-t30 protein language model on neurotoxic-peptide sequences [16]. Analysis was restricted to the documented 7–50-aa input range; shorter candidates were classified as outside model coverage rather than negative.

Cu-, Fe-, and Zn-related binding potential was then evaluated with mebipred. This alignment-free method integrates amino-acid composition, physicochemical descriptors, and metal-binding 5-mer frequencies in a two-tier artificial-neural-network framework comprising a general metal-binding network and ion-specific neural classifiers [17]. The supplied workflow applied a decision threshold of 0.50.

Antioxidant-related properties were evaluated with AnOxPePred, a multi-task deep convolutional neural network. One-hot-encoded peptide sequences pass through a one-dimensional convolutional layer, average pooling, and a 256-unit fully connected layer before separate free-radical-scavenging (FRS) and chelation (CHEL) outputs are generated [18]. Three operational endpoints were retained: CHEL≥0.25; CHEL≥0.25 and FRS<0.50 (main set); and CHEL≥0.25 and FRS<0.45 (stricter subset).

No model was retrained in the present reconstruction. The principal package did not contain exact server snapshots, submitted inputs, model hashes, random seeds, row-level outputs, or the NTxPred2-to-mebipred handoff. The source-reported count of 111 was therefore retained as a downstream result, but 111/923 was not interpreted as an audited transition rate. Agreement across models was treated as serial computational prioritization, not orthogonal biological confirmation.

### 2.6 External twelve-sequence list and composition audit

The external source manuscript listed twelve sequences as the main CHEL/FRS candidate set. Their linkage to the principal source’s twelve rows could not be independently checked because stable IDs, CHEL/FRS rows, and mapping files were unavailable. For each sequence, length, histidine count, cysteine count, basic-residue count (Arg+Lys), and aromatic-residue count (Phe+Tyr+Trp) were recalculated with Python standard-library code (`scripts/audit_external_docking_summary.py`). Checks required twelve unique standard-amino-acid sequences, lengths 7–9 aa, and agreement with the external composition summary.

### 2.7 External docking summary

The external source report stated that the twelve peptides were docked with AutoDock Vina 1.2.5 against human AChE PDB 4EY6 using a 40×40×40 Å³ PAS-centred box [27,51,52]. It supplied mean±SD Vina values and narrative statements about PAS/gorge placement. The current reconstruction transcribed the twelve means and SDs, checked ordering and ranges, and generated a descriptive plot.

Docking was not rerun. The reviewed repository did not contain receptor or ligand preparation files, PDBQT inputs, exact grid-centre coordinates, protonation/charge settings, configurations, exhaustiveness, numbers of runs, seeds, raw scores, commands, software environment, logs, poses, or interaction tables. Consequently, the values are labelled “source-reported.” SD does not have an interpretable experimental or computational denominator until the missing run definition is supplied. Vina scores were not converted to binding affinities or free energies [51,52]. The imported PDF is retained as a provenance artefact; the revised SVG/PNG adds the reporting boundary directly to the figure.

### 2.8 Prospective GROMACS molecular-dynamics protocol

A downstream MD protocol was registered from the `gromacs_md/` directory of `shaohuawen03-cyber/asd` at commit `f11cd3751e8fce53dbf1a335ef1d8fa777751ef5` (https://github.com/shaohuawen03-cyber/asd/tree/arena/019ff90e-asd/gromacs_md). The controlling files were the executable `mdp/100ns/*.mdp` parameter set and `scripts/run_all.sh`, rather than narrative references elsewhere in that repository to a different production duration. The planned systems comprise apo human AChE and AChE complexes labelled for ALLLHRC, FLLHTTR, and YLSLLQR. At the audited commit, the required complex PDB inputs were not present in the repository input directory; the protocol is therefore reported prospectively and not as an executed analysis.

The configured workflow uses GROMACS with `amber99sb-ildn` as the default force field, TIP3P water topology, a triclinic periodic box with a 1.0-nm solute–boundary distance, and neutralization plus 0.15 mol/L NaCl. Energy minimization is specified as 2,000 steepest-descent steps with 1,255 kJ mol⁻¹ nm⁻² heavy-atom positional restraints. This is followed by 1.0 ns restrained NVT heating from 10 to 300 K with velocity-rescale temperature coupling, 1.0 ns restrained NPT equilibration, and 1.0 ns unrestrained NPT equilibration at 300 K and 1 bar. The prospective production stage is 100 ns with a 2-fs time step, LINCS constraints on hydrogen-containing bonds, 1.2-nm real-space cutoffs, force-switched van der Waals interactions from 1.0 nm, particle-mesh Ewald electrostatics, velocity-rescale temperature coupling, and Berendsen pressure coupling. Coordinates are scheduled every 20 ps, yielding 5,000 planned frames per trajectory.

Prespecified trajectory outputs include complex-, AChE-, and peptide-level RMSD/RMSF, radius of gyration, solvent-accessible surface area, radial distribution functions, DSSP-derived secondary structure, hydrogen bonds, residue contacts, and bridging-water analyses. Before any MD result can be accepted, the starting coordinates, terminal and protonation states, topology hashes, exact GROMACS version, random seeds, replicate design, commands, logs, TPR, trajectory, energy, checkpoint, and final-coordinate files must be archived. Incomplete analysis artefacts in the referenced repository were excluded; no stability, convergence, contact, or between-system MD conclusion is reported here.

### 2.9 Descriptive statistics and audit rules

Counts were transcribed from Tier A. Percentages were recomputed as 100×n/N with explicit denominators. Candidate sequences are computational accounting units nested within samples, genomes, and homologous sequence groups; they are not independent biological replicates. Without subject/sample-to-candidate rows, nominal Fisher or χ² tests on aggregate peptide counts would create pseudoreplication and artificially narrow uncertainty. No p value, confidence interval, effect estimate, receiver-operating characteristic, power calculation, or multiplicity correction was therefore reported for healthy-versus-periodontitis comparisons.

Standard-library scripts checked branch sums, numerator≤denominator constraints, the NTxPred2 evaluated/not-evaluated partition, downstream monotonicity, the 8/12 threshold sensitivity, sequence composition, and score ordering. These are arithmetic and provenance checks, not independent reruns of the biological pipeline or docking.

### 2.10 Literature and reporting integrity

The external bibliography was not imported wholesale. Duplicates, correction-note-only erroneous identifiers, material associated with previously excluded files, and references not used by the revised argument were removed. The final 53-reference set was checked for DOI inventory parity across English, Chinese, the verification record, and BibTeX. The curated DOI inventory was retained as the reference-control record for this analysis.

## 3. Results

### 3.1 Evidence filtering reduced each raw smORF library by more than 99.7%

The healthy and periodontitis branches began with 11,269,961 and 11,721,988 smORFs. Evidence filtering and dereplication retained 31,510 healthy candidates (0.2796%) and 33,786 periodontitis-branch candidates (0.2882%). Short- plus long-branch counts exactly reproduced each filtered total. These percentages describe computational retention, not participant prevalence or disease enrichment.

**Table 1. Aggregate candidate libraries and BBB-high outputs**

| Branch | Raw smORFs | Evidence-filtered | Short background (5–30 aa) | BBB-high short, n (%) | Long background (31–50 aa) | BBB-high long, n (%) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 30,557 | 3,359 (10.99) | 953 | 40 (4.20) |
| Periodontitis cohort | 11,721,988 | 33,786 | 32,754 | 3,446 (10.52) | 1,032 | 72 (6.98) |

### 3.2 BBB-high rates differed descriptively by length branch

The short-branch BBB-high rates were 10.99% in healthy and 10.52% in periodontitis, whereas the long-branch rates were 4.20% and 6.98%. The periodontitis branch contributed 3,446 short and 72 long BBB-high outputs, for a combined 3,518. Short candidates constituted 3,446/3,518 (97.95%), and long candidates 72/3,518 (2.05%). These parallel proportions were not subjected to inferential testing because candidate-level independence was not established.

The principal record’s short-candidate length summary contained 547 sequences at 5–7 aa, 2,893 at 8–15 aa, and 6 at 16–30 aa; the 72 long candidates were 31–50 aa. Thus, the periodontitis BBB-high set was dominated by short sequences, but the missing row-level identities prevented overlap, taxonomic, and participant-distribution analyses.

### 3.3 Multi-activity outputs included a saturation warning

The complete UniDL4BioPep category summaries are preserved in the supplement. One distribution is particularly important for interpretation: 30,537/30,557 healthy short candidates (99.93%) and 32,721/32,754 periodontitis short candidates (99.90%) were model-positive for the broad antimicrobial label. Near-universal positivity under a common 0.80 threshold is not a plausible estimate of experimentally active oral antibiotics. It signals possible sequence-domain shift, task calibration limitations, or a label-specific threshold problem and argues against treating cross-model agreement as independent validation.

### 3.4 The periodontitis branch narrowed from 3,518 BBB-high candidates to 12/8 source-reported endpoints

NTxPred2 evaluated 3,299/3,518 candidates (93.77%); 219/3,518 (6.23%) fell below the stated model range and were not evaluated. Among evaluated candidates, 923/3,299 (27.98%) were predicted positive. The principal record then reported 111 mebipred-positive candidates. Of these, 15/111 (13.51%) met CHEL≥0.25, 12/111 (10.81%) additionally met FRS<0.50, and 8/111 (7.21%) met FRS<0.45. Tightening FRS retained 8/12 (66.67%) of the main count.

**Table 2. Aggregate periodontitis-branch prioritization record**

| Stage | Operational rule | n | Auditable denominator/status |
| --- | --- | ---: | --- |
| BBB-high short | UniDL4BioPep BBB output≥0.80; 5–30 aa | 3,446 | 32,754 short candidates |
| BBB-high long | UniDL4BioPep BBB output≥0.80; 31–50 aa | 72 | 1,032 long candidates |
| BBB-high total | Short + long | 3,518 | Arithmetic sum |
| NTxPred2 evaluated | Stated range 7–50 aa | 3,299 | 3,518 BBB-high candidates |
| NTxPred2 not evaluated | Below stated range | 219 | 3,518 BBB-high candidates |
| NTxPred2-positive | Source model label | 923 | 3,299 evaluated candidates |
| Metal-binding-positive | Mebipred output≥0.50 | 111 | Source-reported downstream count; row-level handoff absent |
| CHEL-priority | CHEL≥0.25 | 15 | 111 reported metal-positive candidates |
| Main set | CHEL≥0.25 and FRS<0.50 | 12 | 111 reported metal-positive candidates |
| Stricter subset | CHEL≥0.25 and FRS<0.45 | 8 | 111 reported metal-positive candidates; membership unavailable |

![Figure 1. Evidence-bounded aggregate prioritization funnel](../figures/prioritization_funnel.png)

**Figure 1.** Aggregate screening funnel. Solid transitions are arithmetically reconstructable. The NTxPred2-to-mebipred transition remains dashed because row-level linkage is absent. The principal source lacks candidate identities; the external source record supplies twelve sequences but not their row-level screening lineage.

### 3.5 The external sequence list was compositionally auditable

The external source report listed twelve unique sequences, all composed of standard amino acids and 7–9 residues long (Table 3). Eleven contained histidine, six contained cysteine, and every sequence contained at least one Arg/Lys. These composition statements were reproduced directly from the strings. They are useful for synthesis and hypothesis design, but composition alone does not verify metal binding, BBB transport, toxicity, taxonomy, or correspondence to the principal source’s twelve rows.

**Table 3. Externally reported twelve-sequence set and independently recomputed composition**

| Rank by reported Vina mean | Sequence | Length | His | Cys | Arg+Lys | Phe+Tyr+Trp |
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

The stricter 8-of-12 membership remains unknown because sequence-level FRS labels were not present in either evidence tier.

### 3.6 Source-reported Vina summaries ordered the twelve sequences but did not reproduce docking

The external report supplied Vina means from −9.60 to −8.25 kcal/mol and SDs from 0.04 to 0.12 (Table 4; Figure 2). The ordering, uniqueness, and numeric ranges passed deterministic checks. The first three reported means were FLLHTTR −9.60, YLSLLQR −9.49, and ALLLHRC −9.29 kcal/mol; the last two were HLPLLHRCC −8.35 and HVLLLRQCA −8.25 kcal/mol.

**Table 4. Source-reported AutoDock Vina summary against human AChE PDB 4EY6**

| Rank | Sequence | Reported mean (kcal/mol) | Reported SD | Current evidentiary status |
| ---: | --- | ---: | ---: | --- |
| 1 | FLLHTTR | −9.60 | 0.08 | Summary transcribed; raw runs/poses unavailable |
| 2 | YLSLLQR | −9.49 | 0.05 | Same |
| 3 | ALLLHRC | −9.29 | 0.11 | Same |
| 4 | FCLHLQLR | −9.27 | 0.09 | Same |
| 5 | YHHLLCRR | −9.03 | 0.07 | Same |
| 6 | LLHLPKRTT | −9.01 | 0.06 | Same |
| 7 | LLHPLRL | −8.94 | 0.10 | Same |
| 8 | WLLVHLKK | −8.94 | 0.04 | Same |
| 9 | LLHPLRC | −8.91 | 0.08 | Same |
| 10 | HLLTLKKHV | −8.88 | 0.05 | Same |
| 11 | HLPLLHRCC | −8.35 | 0.12 | Same |
| 12 | HVLLLRQCA | −8.25 | 0.09 | Same |

![Figure 2. Source-reported PAS-focused docking score summary](../figures/fig5_docking_scores.png)

**Figure 2.** Descriptive visualization of source-reported Vina means±SD against PDB 4EY6. Values were transcribed from external source record and were not independently reproduced. The missing run definition prevents interpreting SD as a known number of independent repetitions; Vina scores are not binding free energies [51,52].

The external narrative additionally described PAS/gorge contacts, but no pose or interaction file was available. Residue-level contact claims were therefore not promoted to audited observations. The defensible structural result is limited to a reported within-set score ordering with unresolved computational provenance.

### 3.7 The evidence ladder advanced only partially

The external sequence list resolves the practical problem of having no molecules to synthesize, but it does not resolve lineage: no stable identifier links each sequence to a subject, assembly, evidence match, predictor row, CHEL/FRS row, or the stricter subset. Likewise, docking summaries do not replace reproducible docking artefacts. Translation/expression, BBB transport, cellular toxicity, metal-dependent chemistry, and disease relevance remain untested.

![Figure 3. Evidence ladder](../figures/evidence_ladder.png)

**Figure 3.** Evidence ladder after integration of the external source record and prospective MD workflow. Aggregate screening is reached; the twelve sequences and docking scores are partial, source-reported additions; the MD stage contains a registered method but no accepted trajectory result. Raw lineage and docking artefacts, expression, exposure, phenotype, mechanism, and causality remain unresolved or untested.

## 4. Discussion

### 4.1 Main contribution of the expanded reconstruction

This reconstruction now has enough scientific depth to show both the biological rationale and the evidentiary bottlenecks. The principal screening record describes a severe narrowing: more than 11.7 million periodontitis-branch smORFs become 33,786 evidence-filtered candidates, 3,518 BBB-high outputs, 923 NTxPred2-positive outputs among 3,299 evaluated sequences, and finally source-reported counts of 12 and 8 under CHEL/FRS rules. The external source record integration adds twelve explicit 7–9-aa sequences and a reported AChE docking ranking. This turns an anonymous endpoint count into a concrete, synthesis-ready hypothesis set.

The expansion does not justify stronger causal language. The twelve sequences cannot yet be traced row by row through the principal funnel, and the docking cannot be reproduced from the available project. The central advance is therefore **provenance-aware actionability**: investigators can see what to synthesize, which source-reported ranking to attempt to reproduce, what information is missing, and which claims remain prohibited.

### 4.2 Comparison with current smORF and peptide-discovery standards

Current smORF work combines prediction with translation or proteomic evidence [1–5]. Current oral metaproteomics uses explicit error control, taxonomy, and deposited spectra [10–12]. Strong peptide-mining studies synthesize candidates and measure function [19]. The present record falls short of those standards in three ways. First, evidence matching cannot be inspected at the sequence/spectrum level. Second, participant and sample mapping is absent. Third, neither source provides an executable screening workflow with locked versions and databases.

The external twelve-sequence list is nevertheless useful. It enables exact duplicate searches, taxonomy assignment, model-domain assessment, synthesis feasibility review, and direct re-execution of predictors—once provenance is confirmed. It also reveals a composition pattern: the set is short, cationic, leucine-rich, and enriched for histidine/cysteine. Such a pattern may reflect the intended metal-binding filters, but it could also reflect sequence-domain bias, membrane-active motifs, or correlated predictor features. Composition-matched decoys and alternative predictors are needed before assigning biological meaning.

### 4.3 Interpretation of the AChE/PAS docking follow-up

AChE PAS is a defensible target for an AD-oriented hypothesis because AChE can accelerate Aβ assembly and PAS-directed ligands can modulate that process [23–29]. PDB 4EY6 provides a human AChE structure with pharmacologically characterized ligands [27]. A reported PAS-centred Vina screen may therefore be a reasonable first structural triage [51,52]. The external score range suggests that all twelve were retained by the chosen scoring protocol, with approximately 1.35 kcal/mol separating the extreme means.

Several reasons prevent treating this range as evidence of binding. Flexible 7–9-aa peptides have many conformers; receptor rigidity, protonation, termini, peptide initialization, box location, exhaustiveness, and scoring stochasticity can change ranking. The external project did not provide these details or any poses. The SDs cannot be interpreted without knowing whether they describe modes, seeds, repeated preparations, or another unit. Scores from one target and protocol do not establish selectivity, PAS preference over alternative sites, catalytic inhibition, Aβ modulation, or in-cell activity. A reproducible follow-up should deposit prepared receptor and ligand files, exact commands, seeds, all scores and poses, and a container or environment. Flexible refinement or peptide-specific protocols such as FlexPepDock could then test ranking stability [53].

### 4.4 Metal-binding and short-neuroactive-peptide hypotheses

Eleven histidine-containing and six cysteine-containing sequences provide plausible coordination handles, but no binding constant, stoichiometry, selectivity, oxidation state, geometry, or redox behavior follows from composition or mebipred. Tau-fragment studies demonstrate how these questions can be measured: Cu(II) coordination can be linked to structural change and effects on Aβ aggregation [32], while tau26–44 provides cell- and biophysics-based evidence for a short neuroactive peptide [33]. Curli experiments show that bacterial amyloid exposure can alter aggregation phenotypes in model organisms [34]. These are experimental templates, not analogical proof.

A minimum metal-validation package would compare Cu(II), Fe(II/III), and Zn(II) using spectroscopy and calorimetry, estimate stoichiometry and affinity, and measure metal-dependent ROS and lipid peroxidation with peptide-only, metal-only, scrambled-sequence, composition-matched, and positive/negative controls. Any effect should be replicated across independently synthesized lots and tested for concentration dependence. A “pro-oxidant” label should require increased oxidation specifically under defined metal conditions, not merely CHEL-high/FRS-lower predictions.

### 4.5 Periodontitis–AD interpretation remains hypothesis-generating

The epidemiological record can motivate but not prove the pathway [35–43]. Periodontitis may correlate with age, smoking, diabetes, socioeconomic status, oral care, medication, frailty, and reverse-causal cognitive decline. Recent genetic causal analyses provide a necessary counterweight to strong mechanistic narratives [41,42]. Specific *P. gingivalis* studies support the plausibility of gingipain, inflammatory, vesicular, or infection-related routes [44–50], but those findings cannot be transferred to unassigned community sequences.

Therefore, the current study does not claim that the twelve peptides are periodontitis-specific, *P. gingivalis*-derived, present in blood or brain, or causally related to AD. The only cohort-related statement is that the principal workflow prioritized them through a periodontitis-labelled branch. Taxonomic assignment and cohort prevalence require sequence-to-assembly-to-sample mapping and appropriate subject-level statistics.

### 4.6 Why aggregate candidate counts do not support inferential group tests

The external source record applied peptide-level 2×2 tests. We did not retain them. Millions of smORFs from the same participant, homologous sequences across participants, candidates from the same assembly, and repeated exact matches are correlated. Treating each sequence as independent inflates the effective sample size and can generate small p values for negligible differences. The proper unit is the participant or sample, with candidate outcomes aggregated or modelled while accounting for clustering, repeated sequences, depth, oral site, and covariates.

A valid healthy–periodontitis comparison would require a participant-by-candidate or participant-by-feature matrix, prespecified outcomes, consistent denominators, duplicate/homology handling, and mixed or permutation models operating at the participant level. None of those rows are available. Descriptive percentages are therefore the maximum defensible analysis.

### 4.7 Reproducibility priorities

The highest priority is to reconstruct a single candidate-level table containing: sequence; stable ID; genomic coordinates; assembly; participant/sample; group; taxonomy; sequence/proteomic evidence and spectrum-level statistics; every predictor version, score, threshold decision, and applicability flag; CHEL/FRS values; main/strict membership; and the link to each docking ligand. The screening workflow should include database snapshots, exact commands, environment locking, and checksums.

For docking, the release should add receptor accession and chain, missing-residue handling, protonation, termini, charges, waters/cofactors, ligand conformers, PDBQT files, box centre and size, exhaustiveness, number of modes, energy range, seeds, raw logs, all poses, clustering, and interaction-analysis code. The prospective GROMACS workflow now records a 100-ns protocol, but its starting complex structures and complete simulation packages are not present in the reviewed snapshot. No partial trajectory metric is used in this manuscript. Any later MD report must version the final parameter set, resolve the production pressure-coupling and seed/replicate plan prospectively, archive all raw trajectories and logs, and apply the prespecified analyses without outcome-driven changes.

### 4.8 Experimental validation roadmap and stopping rules

A staged validation plan reduces cost and prevents downstream narrative from compensating for upstream uncertainty:

1. **Lineage and computational reproduction:** verify all twelve rows, recover the 8-of-12 subset, rerun predictors and docking, and test alternate peptide conformers/protocols.
2. **Translation/expression:** use cohort-matched metatranscriptomics, ribosome profiling where feasible, or targeted metaproteomics with peptide-level false-discovery control and taxonomic uniqueness.
3. **Chemical identity and stability:** synthesize peptides, verify purity/mass, measure serum/protease stability, solubility, aggregation, and nonspecific membrane disruption.
4. **BBB and toxicology:** use permeability/transport models, then neuronal and non-neuronal viability, membrane integrity, and dose–response assays. Predicted BBB and NTx labels should be evaluated separately.
5. **Metal chemistry:** quantify Cu/Fe/Zn binding and metal-dependent ROS/lipid peroxidation under controlled stoichiometry and oxidation states.
6. **AChE/Aβ tests:** measure AChE/BChE activity, direct binding if appropriate, and Aβ aggregation with peptide-only and metal-conditioned designs. Docking should guide, not substitute for, assay choice.
7. **Disease relevance:** only candidates with verified identity, exposure, reproducible biochemical activity, and biologically replicated phenotypes should enter complex disease models.

Stopping rules are essential. A sequence that cannot be traced should not proceed to mechanistic interpretation. A peptide without expression evidence may remain a synthetic hypothesis but not a cohort biomarker. A peptide that fails reproducible metal-dependent or toxicological assays should not be described as a neurotoxic mechanism regardless of docking score.

### 4.9 Strengths and limitations

Strengths include a clearly separated evidence architecture, complete aggregate arithmetic, explicit denominators, rejection of pseudoreplicated inferential tests, integration of a concrete sequence list, independent sequence-composition audit, transparent docking provenance, a prospectively versioned MD protocol, evidence-synthesized mechanistic context, and reproducible SVG/document construction. The manuscript also preserves negative boundaries rather than hiding missing materials.

Limitations remain decisive. Principal-source row-level data and code are absent. The external sequence list has no auditable link to the twelve principal-source rows or stricter eight. The docking summary lacks raw artefacts and was not reproduced. The MD starting structures and complete raw simulation packages are unavailable, trajectory analysis is incomplete, and no MD result is reported. Candidate taxonomy, translation, cohort expression, BBB transport, toxicity, metal chemistry, AChE binding/function, Aβ effects, and disease association were not measured. The accession relationship is resolved, but candidate-to-sample, accession-to-group and MAG-bin mappings remain unavailable. These limitations cannot be removed by adding prose or references.

## 5. Conclusions

A provenance-aware reconstruction can make an aggregate-only study more scientifically useful without overstating it. The principal record supports an auditable numerical funnel ending in 12 main and 8 stricter candidate counts. The separately archived external source report adds twelve explicit 7–9-aa sequences and a source-reported AChE Vina ranking; sequence composition and score ordering are reproducible, but screening lineage and docking execution are not. The result is an expanded, actionable hypothesis package rather than a validated peptide mechanism.

The next computational steps are release or reconstruction of row-level screening and docking artefacts and completion of the registered MD workflow with versioned inputs, full trajectories, logs, replicate definitions, and prespecified analyses. Subsequent experimental work would still be required to evaluate expression, transport, toxicology, metal chemistry, and AChE/Aβ effects. Until then, no disease-specific, target-binding, dynamic-stability, or causal claim is warranted.

## Declarations

### Ethics approval and consent to participate

The available materials describe aggregate secondary computational analyses of public-data-derived sequences and contain no identifiable participant data. No new recruitment, intervention, or specimen collection was conducted for this reconstruction. This manuscript therefore reports no new human-participant activity and does not assign an ethics-approval identifier.

### Consent for publication

Not applicable; no identifiable individual material is included.

### Data availability

The principal record names PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727, and HOMD/eHOMD. PRJEB65451 is a derived EBI-EMG/MGnify TPA assembly project linked to PRJNA678453; the article does not report cohort or MAG totals because recountable mapping and bin manifests were unavailable. The external source report supplies the twelve sequences reproduced in Table 3, but not their stable IDs, subject/sample mapping, spectra, taxonomy, predictor rows, strict-subset labels, or principal-source linkage. PDB 4EY6 is public [27]. Raw docking inputs, runs, logs, and poses were unavailable. The prospective MD scripts are versioned at `shaohuawen03-cyber/asd`, commit `f11cd3751e8fce53dbf1a335ef1d8fa777751ef5`; complete starting structures and raw production trajectories were not available for this analysis.

### Code availability

This repository contains code for document extraction, aggregate arithmetic, sequence-composition checks, editable-text SVG figures, DOCX packaging, and quality audits. It does not contain the original smORF discovery/prediction pipeline or an executable reproduction of the external docking. The referenced MD repository contains a prospective workflow but not the complete inputs and raw trajectories required for an accepted result. The available code therefore reproduces reported arithmetic and document-level audits, but not analyses for which inputs and execution artefacts are missing.

### Funding

Funding information was not available in the source materials.

### Competing interests

A competing-interest declaration was not available in the source materials.

### Author contributions

Author identities and CRediT contributions were not available in the source materials; authorship was not inferred from file provenance.

### Generative artificial intelligence use

A generative-AI assistant supported source organization, bilingual drafting, deterministic checks, figure scripting, and language editing. It did not generate new biological observations or independently reproduce the missing screening/docking analyses. Scientific claims were constrained to the cited literature and auditable source records.

## References

1. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
2. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
3. Davin ME, Ortís Sunyer J, Delgado LF, et al. High-resolution multi-omics enhances prediction and detection of smORF-encoded proteins in the human gut microbiome. *Nat Commun*. 2026. doi:10.1038/s41467-026-72762-5.
4. Couso JP, Patra P. Short ORFs: finding gems in hidden places. *Curr Opin Genet Dev*. 2017;45:14–21. doi:10.1016/j.gde.2017.04.002.
5. van Heesch S, Wit F, Botter J, et al. The translational landscape of the human heart. *Cell*. 2019;178(1):236–251.e24. doi:10.1016/j.cell.2019.05.010.
6. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
7. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
8. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
9. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
10. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
11. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
12. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
13. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
14. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
15. Liu X, Zhao Z, Guan J, et al. Prediction of blood-brain barrier-penetrating peptides using B3BPFN. *Front Mol Biosci*. 2026;13:1858506. doi:10.3389/fmolb.2026.1858506.
16. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
17. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
18. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
19. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
20. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
21. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
22. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
23. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
24. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
25. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
26. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept). *Structure*. 1999;7(3):297–307. doi:10.1016/s0969-2126(99)80040-9.
27. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
28. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
29. Lushchekina SV, Kots ED, Novichkova DA, et al. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7:396–402. doi:10.1007/s12668-016-0375-x.
30. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
31. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer’s disease. *J Biol Chem*. 2021;296:100105. doi:10.1074/jbc.REV120.008207.
32. Di Natale G, Bellia F, Sciacca MFM, et al. Tau-peptide fragments and their copper(II) complexes: effects on amyloid-β aggregation. *Inorg Chim Acta*. 2018;472:82–92. doi:10.1016/j.ica.2017.09.061.
33. Perini G, Ciasca G, Minelli E, et al. Dynamic structural determinants underlie the neurotoxicity of the N-terminal tau 26–44 peptide. *Int J Biol Macromol*. 2019;141:278–289. doi:10.1016/j.ijbiomac.2019.08.220.
34. Chen SG, Stribinskis V, Rane MJ, et al. Exposure to the functional bacterial amyloid protein curli enhances alpha-synuclein aggregation. *Sci Rep*. 2016;6:34477. doi:10.1038/srep34477.
35. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
36. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
37. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
38. Kim J, Han DH. Periodontitis as a risk factor for dementia. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
39. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
40. Jiang Z, Shi Y, Zhao W, et al. Association between chronic periodontitis and the risk of Alzheimer’s disease. *BMC Oral Health*. 2021;21:466. doi:10.1186/s12903-021-01827-2.
41. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
42. Zhao Y, Zhang C, Chang X, et al. Causal association between periodontitis and systemic diseases: a systematic review and meta-analysis of Mendelian randomization studies. *BMC Oral Health*. 2026;26:383. doi:10.1186/s12903-026-07725-9.
43. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
44. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
45. Poole S, Singhrao SK, Kesavalu L, et al. Determining the presence of *Porphyromonas gingivalis* in Alzheimer’s disease brain. *J Alzheimers Dis*. 2013;33(3):665–678. doi:10.3233/JAD-2012-121149.
46. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
47. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
48. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
49. Haditsch U, Roth T, Rodriguez L, et al. Alzheimer’s disease-like neurodegeneration in *Porphyromonas gingivalis* infected neurons with persistent expression of active gingipains. *J Alzheimers Dis*. 2020;75(4):1361–1376. doi:10.3233/JAD-200393.
50. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
51. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
52. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
53. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
