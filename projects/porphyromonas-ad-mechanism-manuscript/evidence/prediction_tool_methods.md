# Prediction-tool method verification

Verification date: 2026-08-14

## Methods represented in the supplied funnel

| Tool | Recorded role | Published/current implementation | Classification |
| --- | --- | --- | --- |
| UniDL4BioPep | Multi-activity predictions, including BBB probability | Pretrained ESM-2 `esm2_t6_8M_UR50D` embeddings (320 dimensions) followed by a six-layer CNN for task-specific binary classification | Protein-language-model representation plus deep CNN |
| NTxPred2 | Neurotoxicity classification for 7–50-aa candidates | Peptide mode fine-tunes ESM2-t30; protein and combined modes use Extra Trees classifiers with ESM-2-derived embeddings | Fine-tuned protein language model for peptides; conventional ensemble classifier in other modes |
| mebipred | General and Cu/Fe/Zn-related metal-binding prediction | Alignment-free sequence features (composition, physicochemical properties and metal-binding 5-mer counts) feed a general feed-forward neural network and ion-specific second-tier models | Engineered-feature neural networks |
| AnOxPePred | Free-radical-scavenging and chelation outputs | One-hot sequence encoding, one-dimensional convolution, average pooling, a 256-node fully connected layer and two task outputs | Deep convolutional neural network |

For the peptide workflow, UniDL4BioPep, the peptide-specific NTxPred2 mode and AnOxPePred are deep-learning architectures; mebipred contributes a two-tier artificial-neural-network classifier. The concise manuscripts therefore describe the workflow as a **deep-learning-guided multi-model cascade** and report the architecture relevant to each peptide-analysis stage. NTxPred2 Extra Trees models are documented here for completeness but are not presented as the peptide mode used in the manuscript.

## Sources and software pages

- UniDL4BioPep paper: https://doi.org/10.1093/bib/bbad135
- UniDL4BioPep source: https://github.com/dzjxzyd/UniDL4BioPep
- NTxPred2 paper: https://doi.org/10.1002/pro.70200
- NTxPred2 server: https://webs.iiitd.edu.in/raghava/ntxpred2/
- NTxPred2 source: https://github.com/raghavagps/ntxpred2/
- mebipred paper: https://doi.org/10.1093/bioinformatics/btac358
- mebipred server: https://services.bromberglab.org/mebipred/home
- AnOxPePred paper: https://doi.org/10.1038/s41598-020-78319-w
- AnOxPePred source: https://github.com/TobiasHeOl/AnOxPePred

## Reproducibility boundary

The supplied material preserves tool names, aggregate thresholds and counts, but not exact historical server snapshots, model hashes, submitted input files or row-level outputs. The algorithm descriptions above document the cited implementations; they do not prove which deployed server build generated every supplied value and do not constitute a rerun.

For context, Augur—cited elsewhere in the full manuscript as a BBB-prediction comparator—uses engineered sequence/physicochemical features, information-gain feature selection, borderline-SMOTE and a random-forest classifier (https://doi.org/10.1186/s12915-024-01883-4); it is not a deep-learning model and is not represented as a stage in the supplied aggregate funnel.
