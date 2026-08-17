# Journal-format alignment for v3.7.0

## Working target

The English manuscripts are formatted against the core Research Article
conventions of **Journal of Alzheimer's Disease Reports** because the study is
explicitly AD-focused and computational/oral-microbiome oriented.

Current author instructions:
https://journals.sagepub.com/author-instructions/alr

## Implemented conventions

- Structured abstract with **Background, Objective, Methods, Results, and
  Conclusions** labels.
- English abstract not exceeding 250 words:
  - full manuscript: 239 whitespace-delimited tokens including labels/keywords;
  - concise manuscript: 213 whitespace-delimited tokens including
    labels/keywords.
- Main-text order: Introduction, Materials and methods, Results, Discussion,
  Conclusion, References.
- Unnumbered section and subsection headings.
- 12-point Times New Roman body text.
- Double-spaced body and references.
- One-inch margins.
- Black, restrained heading typography without decorative color.
- AD named in the abstract and keywords.
- Numbered references ordered by first citation.
- Full English body below 10,000 words; expanded concise English body is
  approximately 3,200 words and is treated as a condensed Research Article,
  not as a journal Short Communication.
- Editable three-line tables and no embedded figures.

## User-required deviations retained

The journal instructions normally require submission metadata such as a visible
title, page numbers, author information, and declarations. The current DOCX
files intentionally retain the user's standing requirements instead:

- no visible article title;
- no page numbers, headers, or footers;
- Conclusion followed directly by References;
- no Declarations section in the article body;
- neutral `English.docx` and `Chinese.docx` filenames and metadata.

Accordingly, v3.7.0 is aligned to the journal's **scientific article structure
and typography**, but a submission portal would still require a separate title
page and author/funding/conflict/ethics metadata as applicable. These items were
not invented from unavailable source material.

## MD integration state

The manuscript describes the ongoing 100-ns GROMACS extension and states that
trajectory-derived stability, convergence, and contact measurements will be
incorporated after analysis and quality control. It does not state that MD
results will never be reported and does not fabricate interim measurements.
