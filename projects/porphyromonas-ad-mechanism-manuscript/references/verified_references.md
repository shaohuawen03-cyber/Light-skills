# Verified bibliography and claim-use record

Checked: 2026-08-12. “Verified” here means that title/identifier/core metadata were cross-checked against the linked DOI publisher page and, where available, PubMed/PMC or another independent scholarly record. It does **not** mean that the Light stage-10 canonical online registry passed; resolver/network limitations are reported in `quality_reports/literature_coverage.md`.

## Included references

1. **Sberro H, Fremin BJ, Zlitni S, et al.** Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. DOI: [10.1016/j.cell.2019.07.016](https://doi.org/10.1016/j.cell.2019.07.016).
   Use: rationale for examining overlooked small proteins in human-associated microbiomes.
   Support boundary: general sORF/small-protein rationale only; does not validate this study’s candidates.

2. **Belstrøm D, Constancias F, Drautz-Moses DI, Schuster SC, Veleba M, Mahé F, Givskov M.** Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms and Microbiomes*. 2021;7:76. DOI: [10.1038/s41522-021-00247-y](https://doi.org/10.1038/s41522-021-00247-y).
   Use: verified publication associated with PRJNA678453 and the oral metagenome/metatranscriptome context.
   Support boundary: does not independently verify the unresolved PRJEB65451 accession or every aggregate count in the supplied analysis.

3. **Chen T, Yu WH, Izard J, Baranova OV, Lakshmanan A, Dewhirst FE.** The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. DOI: [10.1093/database/baq013](https://doi.org/10.1093/database/baq013).
   Use: HOMD resource description.
   Support boundary: HOMD is a curated sequence/taxonomy resource, not itself mass-spectrometric expression evidence.

4. **Escapa IF, Chen T, Huang Y, Gajare P, Dewhirst FE, Lemon KP.** New insights into human nostril microbiome from the expanded Human Oral Microbiome Database (eHOMD): a resource for the microbiome of the human aerodigestive tract. *mSystems*. 2018;3(6):e00187-18. DOI: [10.1128/mSystems.00187-18](https://doi.org/10.1128/mSystems.00187-18).
   Use: updated eHOMD context.
   Support boundary: same as reference 3.

5. **Belstrøm D, Jersie-Christensen RR, Lyon D, Damgaard C, Jensen LJ, Holmstrup P, Olsen JV.** Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. DOI: [10.7717/peerj.2433](https://doi.org/10.7717/peerj.2433). PMID: [27672500](https://pubmed.ncbi.nlm.nih.gov/27672500/).
   Use: PXD004319 cohort and salivary metaproteomics context.
   Support boundary: exact sequence matching to this dataset supports prior observation in that dataset, not expression in the metagenomic cohort analyzed here.

6. **Jiang X, Zhang Y, Wang H, Wang Z, Hu S, Cao C, Xiao H.** In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research (Washington, DC)*. 2022;2022:9781578. DOI: [10.34133/2022/9781578](https://doi.org/10.34133/2022/9781578).
   Use: identifies the biological context of PXD026727.
   Support boundary: this is a lung-cancer salivary dataset and cannot confer periodontitis specificity.

7. **Du Z, Ding X, Xu Y, Li Y.** UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Briefings in Bioinformatics*. 2023;24(3):bbad135. DOI: [10.1093/bib/bbad135](https://doi.org/10.1093/bib/bbad135). PMID: [37020337](https://pubmed.ncbi.nlm.nih.gov/37020337/).
   Use: model family and peptide-bioactivity prediction rationale.
   Support boundary: model outputs are predictions; a score threshold is not experimental validation or a clinically calibrated probability.

8. **Rathore AS, Jain S, Choudhury S, Raghava GPS.** A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Science*. 2025;34(8):e70200. DOI: [10.1002/pro.70200](https://doi.org/10.1002/pro.70200).
   Use: NTxPred2 method.
   Support boundary: sequence-based neurotoxicity prediction does not replace cell or animal toxicology.

9. **Aptekmann AA, Buongiorno J, Giovannelli D, Glamoclija M, Ferreiro DU, Bromberg Y.** mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. DOI: [10.1093/bioinformatics/btac358](https://doi.org/10.1093/bioinformatics/btac358). PMID: [35639953](https://pubmed.ncbi.nlm.nih.gov/35639953/).
   Use: sequence-based metal-binding-potential prediction.
   Support boundary: no experimental affinity, ion-specific stoichiometry, binding residue, or coordination geometry follows from a positive prediction.

10. **Olsen TH, Yesiltas B, Marin FI, et al.** AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Scientific Reports*. 2020;10:21471. DOI: [10.1038/s41598-020-78319-w](https://doi.org/10.1038/s41598-020-78319-w).
    Use: CHEL and FRS prediction.
    Support boundary: high CHEL plus lower FRS is an operational prioritization pattern, not evidence of pro-oxidant activity.

11. **Larvin H, Gao C, Kang J, Aggarwal VR, Pavitt S, Wu J.** The impact of study factors in the association of periodontal disease and cognitive disorders: systematic review and meta-analysis. *Age and Ageing*. 2023;52(2):afad015. DOI: [10.1093/ageing/afad015](https://doi.org/10.1093/ageing/afad015).
    Use: observational periodontitis–cognitive-disorder association and heterogeneity.
    Support boundary: association estimates vary with severity, classification and other study factors; no direct peptide mechanism is established.

12. **Kaliamoorthy S, Nagarajan M, Sethuraman V, Jayavel K, Lakshmanan V, Palla S.** Association of Alzheimer’s disease and periodontitis—a systematic review and meta-analysis of evidence from observational studies. *Medicine and Pharmacy Reports*. 2022;95(2):144–151. DOI: [10.15386/mpr-2278](https://doi.org/10.15386/mpr-2278). PMID: [35721037](https://pubmed.ncbi.nlm.nih.gov/35721037/).
    Use: observational synthesis reporting OR 1.67 (95% CI 1.21–2.32).
    Support boundary: this pooled association is not a causal estimate and does not support any specific peptide mediator.

13. **Liu S, Dashper SG, Zhao R.** Association between oral bacteria and Alzheimer’s disease: a systematic review and meta-analysis. *Journal of Alzheimer’s Disease*. 2023;91(1):129–150. DOI: [10.3233/JAD-220627](https://doi.org/10.3233/JAD-220627). PMID: [36404545](https://pubmed.ncbi.nlm.nih.gov/36404545/).
    Use: clinical oral-bacteria/AD evidence and inconsistency of microbiome-wide findings.
    Support boundary: does not identify or validate the screened peptides.

14. **Dominy SS, Lynch C, Ermini F, et al.** *Porphyromonas gingivalis* in Alzheimer’s disease brains: evidence for disease causation and treatment with small-molecule inhibitors. *Science Advances*. 2019;5(1):eaau3333. DOI: [10.1126/sciadv.aau3333](https://doi.org/10.1126/sciadv.aau3333).
    Use: mechanistic motivation for periodontal-pathogen/AD research.
    Support boundary: this manuscript has no taxonomic assignment to *P. gingivalis* and must not transfer that attribution to its candidates.

15. **Chalmers JC, Hernandez-Kapila YL.** The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontology 2000*. 2025;98(1):220–227. DOI: [10.1111/prd.12631](https://doi.org/10.1111/prd.12631). PMID: [40495582](https://pubmed.ncbi.nlm.nih.gov/40495582/).
    Use: current boundary that human causality remains unproven and translational evidence is incomplete.
    Support boundary: review/context, not direct evidence for candidate peptides.

16. **Atanasova M, Dimitrov I, Ivanov S.** Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybernetics and Information Technologies*. 2020;20(6):140–154. DOI: [10.2478/cait-2020-0068](https://doi.org/10.2478/cait-2020-0068).
    Use: future AChE–Aβ structural-analysis rationale.
    Support boundary: no docking or molecular dynamics involving the present candidates was performed.

17. **Kim J, Han DH.** Periodontitis as a risk factor for dementia: a systematic review and meta-analysis. *Journal of Evidence-Based Dental Practice*. 2025;25:102094. DOI: [10.1016/j.jebdp.2025.102094](https://doi.org/10.1016/j.jebdp.2025.102094). PMID: [40335202](https://pubmed.ncbi.nlm.nih.gov/40335202/).
    Use: recent severity-stratified periodontitis/dementia association.
    Support boundary: observational synthesis; prevention claims require prospective intervention evidence.

## Dataset records used or named by the supplied workflow

- PRJNA678453 — linked to Belstrøm et al. 2021 (reference 2).
- PRJEB65451 — **UNRESOLVED in this drafting session**; do not assign metadata by inference.
- PXD003151 — oral dysbiosis/caries-risk biofilm proteomics context; accession metadata should be rechecked in PRIDE before submission.
- PXD004319 — verified against ProteomeXchange and reference 5.
- PXD026727 — verified as lung-cancer salivary metaproteomics against ProteomeXchange and reference 6.

## Publication-integrity status

No cited work was intentionally represented as retracted. Because the repository’s automated retraction checker could not complete authoritative online resolution in this environment, formal retraction/correction status remains **UNRESOLVED**, not “clean.” Authors should rerun Crossref/Crossmark and Retraction Watch checks immediately before submission.
