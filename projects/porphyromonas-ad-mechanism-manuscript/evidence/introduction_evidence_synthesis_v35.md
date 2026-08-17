# Evidence synthesis for the expanded full-manuscript Introduction

Synthesis date: 2026-08-17

## Workflow provenance

The Introduction revision follows the evidence-first principles in `ZZL-Zoro/Life-Science-Evidence-Review`, reviewed at commit `1798aac7f1269a0d717b6228734747c642010f22`: establish biological context, prioritize primary literature, compare evidence classes, identify agreement and conflict, separate evidence from inference, and end with a traceable knowledge gap. The external workflow informed synthesis discipline only; it is not represented as a biological data source or a manuscript result.

## Research question

Can aggregate oral-metagenome smORF screening and a source-reported AChE docking follow-up define testable microbial-peptide hypotheses at the periodontitis–Alzheimer’s disease interface without implying translation, exposure, target engagement or causality?

## Evidence architecture

| Theme | Highest relevant evidence in the 53-reference corpus | What it supports | What it does not support |
| --- | --- | --- | --- |
| AD biology | Broad disease synthesis; amyloid and cholinergic primary/landmark studies [20–29] | AD is multicomponent; AChE/PAS is a biologically motivated structural question | AChE binding or AD modification by the present candidates |
| Periodontitis–AD association | Observational syntheses, longitudinal work and Mendelian-randomization studies [35–43] | A heterogeneous association literature and a plausible oral–brain research question | A substantial established causal effect |
| *P. gingivalis* | Tissue-detection, infection-model, neuronal, gingipain and vesicle studies [44–50] | Organism-specific mechanistic plausibility in bounded systems | Taxonomic assignment of community-derived candidate peptides |
| Oral meta-omics | Paired oral metagenome/metatranscriptome and metaproteome resources [6–12] | Disease-associated ecological activity and the need for sample-level provenance | Current-cohort expression from cross-resource exact matches alone |
| Microbiome smORFs | Large-scale smORF discovery, annotation, multi-omics and proteogenomics [1–5] | A large under-annotated microbial peptide space and an evidence ladder for discovery | Translation or function from an ORF prediction alone |
| Peptide models | UniDL4BioPep, BBB comparators, NTxPred2, mebipred and AnOxPePred [13–18] | Transparent computational triage with architecture-specific limitations | Measured BBB transport, neurotoxicity, metal chemistry or antioxidant activity |
| Experimental benchmark | Microbiome peptide mining and short-peptide/metal studies [19,32–34] | How computational candidates can become validated molecules | Transfer of another peptide’s activity to this candidate set |
| Docking and MD | AChE structures, Vina, FlexPepDock and AChE–Aβ simulation studies [26–29,51–53] | Structural hypothesis generation and requirements for reproducibility | Affinity, stability, catalysis or mechanism without raw inputs and trajectories |

## Synthesis decisions

1. Open with AD as a systems-level neurodegenerative process, then introduce periodontal inflammation and *P. gingivalis* before discussing the candidate peptide space.
2. Compare human observational, genetic-causal, tissue, cell and animal evidence rather than merging them into one causal narrative.
3. Treat possible inflammatory, vesicular and microbial-product routes as hypotheses with different evidentiary strengths.
4. Explicitly distinguish a dysbiotic community from a single-organism peptidome.
5. Explain why smORFs and micropeptides are a plausible but technically difficult molecular layer.
6. Connect the oral meta-omics provenance problem to the inability to assign candidates to participants, samples or taxa.
7. Describe each prediction tool by its actual architecture and task; do not call every tool deep learning.
8. Present AChE/PAS, metal homeostasis and MD as linked structural hypotheses, not validated outcomes.
9. End with the precise research contribution: aggregate reconstruction, deterministic audit, sequence-level composition checks and a source-reported docking ranking.
10. Keep every Introduction citation bracket to one reference.

## Remaining gaps

- no candidate-to-sample, candidate-to-assembly or candidate-to-taxon map;
- no independently auditable MAG manifest or bin-quality table;
- no row-level predictor outputs or model snapshots;
- no cohort-matched expression or translation evidence;
- no measured BBB transport, toxicity, metal coordination, AChE activity or Aβ effect;
- no reproducible docking package;
- no completed, prespecified MD analysis package.

These gaps define the manuscript’s interpretation boundary and prevent a causal or experimentally validated claim.
