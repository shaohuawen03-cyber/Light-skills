# Stage 6 — Scientific visualisation / 科学可视化

Workflows: K-Dense `scientific-visualization` + Nature `nature-figure` principles  
Rule: all scientific graphics are programmatically generated; no generative image model was used.

## 1. Figure set

| Figure | Files | Script | Purpose |
| --- | --- | --- | --- |
| Figure 1 | `manuscript/figures/prioritization_funnel.svg` and `.png` | `scripts/generate_funnel_figure.py` | Shows aggregate branches, denominators, operational thresholds and the source-handoff gap. |
| Figure 2 | `manuscript/figures/evidence_ladder.svg` and `.png` | `scripts/generate_evidence_ladder.py` | Distinguishes the achieved prediction endpoint from missing identity, expression, transport, phenotype, mechanism and disease evidence. |

## 2. Data lineage

Figure 1 values are hard-coded only from the principal source and deterministic Stage-5 audit:

- healthy raw/filtered/BBB-high counts;
- periodontitis raw/filtered/BBB-high counts;
- NTxPred2 evaluated/not-evaluated/positive counts;
- source-reported mebipred-positive count;
- CHEL/FRS threshold counts.

The dashed NTxPred2→mebipred transition is intentional: no row-level handoff was supplied. Figure 2 contains no empirical magnitude; it is an evidence-class schematic based on the locked claim boundaries.

## 3. Design decisions

- White background, dark high-contrast text and restrained, colour-blind-compatible categorical colours.
- Counts are printed; box widths are not mapped to count magnitude, avoiding misleading area encoding.
- Healthy values are labelled “descriptive context” and are not visually marked as a statistical comparator.
- “Predicted”, “source-reported”, “not evaluated”, “blocked” and “not tested” are explicit.
- Future evidence stages are grey and cannot be mistaken for completed results.
- PNG dimensions: Figure 1, 1800×1540; Figure 2, 1800×980.
- SVG originals remain editable. PNGs were rendered directly with ImageMagick primitives because the installed ImageMagick SVG delegate lacks `rsvg-convert`.

## 4. Caption requirements

### Figure 1

**EN:** Evidence-bounded aggregate computational prioritisation. Counts and operational thresholds were transcribed from the principal source record. Healthy-branch values are descriptive context only. The dashed transition indicates that the row-level handoff to mebipred was unavailable; 111/923 is therefore not presented as an audited transition rate. The 12-candidate main set and 8-candidate stricter subset are source-reported predictions, not experimentally validated peptides.

**ZH:** 证据约束的聚合层面计算优先排序。计数和操作性阈值转录自主证据记录；健康分支仅作描述性背景。虚线表示缺少进入 mebipred 的逐行交接，因此不把 111/923 写成经审计的转化率。12 条主集合和 8 条严格子集是来源报告的预测结果，并非实验验证肽。

### Figure 2

**EN:** Evidence ladder for interpretation. The current source package reaches aggregate computational prioritisation only. Candidate identities and row-level scores are unavailable, and translation/expression, BBB transport, cellular toxicity, metal-dependent biochemical effects and disease association/causality were not tested.

**ZH:** 解释证据阶梯。当前来源包仅达到聚合层面计算优先排序；候选身份和逐行分数不可用，且未检验翻译/表达、BBB 转运、细胞毒性、金属依赖性生化效应及疾病关联/因果性。

## 5. Visual audit

- Both PNGs were opened and visually inspected after regeneration.
- No clipped funnel text or overlapping labels were observed in Figure 1.
- Figure 2 was revised after the first render to remove overlapping labels and fit the progression text inside its panel.
- Exact counts agree with `statistics_audit.json`.

## 6. Integrity statement

The figures communicate uncertainty and missing evidence rather than filling gaps with illustrative biology. No cells, brains, bacteria, peptides, chemical structures or molecular interactions are depicted as observed.
