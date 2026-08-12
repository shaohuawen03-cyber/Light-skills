# Literature coverage and verification report

Date: 2026-08-12

## Scope

This was a targeted evidence search to support an original computational manuscript, not a systematic review. Coverage focused on four domains:

1. oral-microbiome sORFs and small proteins;
2. provenance of the named metagenomic, oral-reference and metaproteomic resources;
3. UniDL4BioPep, NTxPred2, mebipred and AnOxPePred;
4. periodontitis/oral bacteria and cognitive disorders/Alzheimer’s disease, including limits on causal interpretation and future AChE–Aβ structural work.

## Search approach

- DOI landing pages, publisher pages, PubMed/PMC, ProteomeXchange records and scholarly index pages were queried.
- Searches used identifiers and exact titles when available.
- Tool papers were checked against DOI publisher pages and PubMed or an independent scholarly metadata source when available.
- Periodontitis–AD framing used recent systematic reviews/meta-analyses plus selected mechanistic and structural studies.
- The included set is documented in `references/verified_references.md`; reusable BibTeX is in `references/references.bib`.

## Coverage achieved

- Verified the primary model papers for all four prediction tools.
- Verified PRJNA678453’s association with the 2021 Belstrøm et al. oral microbiota study.
- Verified HOMD/eHOMD as oral microbial taxonomy/genome resources.
- Verified PXD004319 as a periodontitis/caries/healthy salivary metaproteomics dataset.
- Verified PXD026727 as a lung-cancer salivary metaproteomics dataset; this limits any “periodontitis-specific” interpretation.
- Located independent literature identifying PXD003151 as an oral dysbiosis/caries-risk biofilm dataset; its accession record should be rechecked directly in PRIDE before submission.
- Verified observational syntheses supporting an association between periodontitis and cognitive outcomes while showing substantial design/severity/classification dependence.
- Verified literature that motivates *P. gingivalis*/gingipain and AChE–Aβ hypotheses, while keeping them outside the present Results.

## Unresolved items

1. **PRJEB65451**: exact accession searches did not yield a credible scholarly/ENA match in available search results. Direct ENA/NCBI API requests previously failed with `SSLZeroReturnError`. It remains UNRESOLVED.
2. **Row-level candidate evidence**: sequences, SeqIDs, per-model scores, taxonomic assignments and handoff files were not supplied; literature cannot repair this provenance gap.
3. **Model run provenance**: exact software commits, model versions, server access dates and environment were not supplied.
4. **Long-branch support status**: the source describes the 31–50-aa branch as HOMD-derived while also describing the combined candidates as proteomics-supported. HOMD is not a mass-spectrometry repository, so this must be clarified by the original analyst.
5. **mebipred handoff denominator**: the narrative is sequential but no row-level input list establishes whether all 923 NTxPred2 positives or another subset entered mebipred.
6. **Formal retraction/update check**: the repository script could not reach its resolver reliably. Publication-integrity status is UNRESOLVED and must not be represented as “clean.”

## Failed or rejected search paths

- The repository’s `domain_map.py` and `biomedical_search.py` entered an offline synthetic fallback and returned unrelated goat records. Those files were deleted and no claim uses them.
- The repository’s automated DOI verifier returned HTTP 0/`DOI_NOT_FOUND` for known-valid DOIs because the resolver was unreachable. Those verdicts were rejected.
- Direct ENA/NCBI API attempts failed at TLS. This is a transport failure, not evidence that an accession does not exist.

## Bias and completeness statement

The search was purposive and identifier-driven. It may omit relevant studies, especially negative results, non-English literature, newly indexed records and database corrections. It should not be reported as PRISMA-compliant or exhaustive. Before journal submission, authors should run a documented database search with explicit dates and terms if the target journal expects a systematic background review; otherwise, the present targeted bibliography is adequate for framing a computational original article.

## Bottom line

The literature base is sufficient to support conservative background, tool description and discussion. It is not sufficient to upgrade the aggregate computational outputs into mechanistic, causal, taxonomic or experimental claims. The principal submission blockers are missing row-level data/code and unresolved provenance—not lack of narrative literature.
