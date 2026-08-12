# Stage 8 — Scientific language polishing / 科学语言润色

Workflow: Nature `nature-polishing`, applied after the evidence-first rewrite  
Polishing principle: improve clarity and stance without strengthening claims or changing numbers.

## 1. Polishing dimensions

### Stance

- Replaced activity statements with “model-positive”, “high-output”, “predicted”, or “source-reported” where appropriate.
- Reserved “reported association” for observational literature.
- Added current causal counter-evidence before any disease implication.
- Avoided “first”, “novel”, “prove”, “confirm”, “mechanism” and “specific” as claims about the present result.

### Terminology

- Standardized `smORF`, `BBB-high`, `CHEL`, `FRS`, `model-positive`, `not evaluated`, `evidence-filtered candidate`, and `aggregate-level`.
- Distinguished candidate identity, translation/expression, exposure, phenotype, biochemical mechanism, and disease causality.
- Used “penetration” for the peptide BBB prediction label and “transport/permeability assay” for future empirical testing.

### Sentence and paragraph structure

- Each Introduction paragraph now performs one move: field, oral context, model context, disease boundary, aim.
- Methods follow source → construction/filtering → predictors → statistics.
- Results report observations and denominators without mechanistic interpretation.
- Discussion proceeds from contribution to standards, statistics, predictors, disease context, evidence ladder, and limitations.

### Bilingual meaning preservation

- Chinese follows the same argument order and level of certainty as English.
- No English claim was strengthened in translation.
- Mathematical symbols, thresholds, counts, accessions, model names, and citation numbers were preserved.

## 2. Mechanical checks

- `draft_lint.py --final`: no FAIL-level issue in either language.
- Chinese draft-lint warning for an English-named `Funding` heading is a language-detection limitation; the `经费` section is present.
- `mechanical_check.py`: English findings were predominantly passive-voice/style heuristics. Passive constructions were retained where the unknown/source-reported agent or Methods register made them more accurate.
- The English “Very short” heuristic hit was removed.
- A bibliographic-title hit on the word “novel” was not altered because it is part of the verified Sberro article title.
- Chinese punctuation warnings were ignored because the checker assumes English punctuation and full-width marks are correct in Chinese prose.

## 3. Quantitative and structural checks

`quality_reports/manuscript_consistency.json`:

- all required aggregate values present in both languages;
- prohibited claims absent;
- placeholders absent;
- references sequential 1–25 in both files;
- verdict PASS.

`quality_reports/language_structure_audit.json`:

- eight matching top-level sections per language;
- all references 1–25 cited in both bodies;
- no placeholder markers;
- current English file: 36,046 characters and 4,482 whitespace-delimited tokens;
- current Chinese file: 15,916 characters and 1,401 whitespace-delimited tokens;
- journal-neutral English count: structured abstract 244 tokens; Introduction through Conclusions 3,204; main text including declarations and excluding references 3,550 (`quality_reports/manuscript_word_count.json`).

## 4. Items intentionally not polished away

- Missing sequences/data/code remain explicit.
- The unresolved BioProject remains unresolved.
- The heterogeneous resource contexts remain named.
- The mebipred handoff remains unauditable.
- Weak novelty and possible journal rejection remain acknowledged.
- Author, funding, conflict, ethics, and contribution details remain incomplete pending human input.

## 5. Verdict

**PASS for controlled bilingual polishing.** Language is submission-oriented and internally consistent, but polishing does not convert the aggregate package into a fully reproducible or experimentally validated study.
