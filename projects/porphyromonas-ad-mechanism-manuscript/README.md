# 牙周炎队列口腔微肽与 AD 相关特征的多模型计算优先排序论文

## 项目目标

以 `材料与方法及结果_机制研究版` 为主要依据，形成中英文分节对照的原创研究型 SCI 科学内容草案，并完整保留原始材料、提取文本、证据台账、参考文献、构建脚本和质量报告。

本研究定位为**描述性多模型计算优先排序**，不声称已经证明牙周炎微肽导致 AD，也不把候选归因于牙龈卟啉单胞菌。

## 主要交付物

- `manuscript/manuscript_bilingual.docx`：中英文分节对照主稿。
- `manuscript/manuscript_bilingual.md`：中英文分节对照可追踪源稿。
- `manuscript/manuscript_en.md`：英文完整稿。
- `manuscript/manuscript_zh.md`：中文完整稿。
- `manuscript/supplementary_tables_bilingual.docx`：中英文补充表。
- `manuscript/supplementary_tables_bilingual.md`：补充表源文件。
- `manuscript/figures/prioritization_funnel.svg`：可编辑矢量流程图。
- `manuscript/figures/prioritization_funnel.png`：DOCX 使用的流程图。

## 证据与参考文献

- `evidence/source_understanding_and_scope.md`：原始材料理解、研究定位、可报告结果和禁用外推。
- `evidence/claim_evidence_ledger.md`：逐项主张—证据—措辞台账。
- `evidence/extracted/`：五份 DOCX 的标准库依赖无关提取文本、结构 JSON 和媒体。
- `references/verified_references.md`：17 条保留文献的元数据和 claim-use 边界。
- `references/references.bib`：与中英文稿件一致的 BibTeX。

## 质量报告

- `quality_reports/source_checksum_verification.txt`：6/6 原始文件哈希通过。
- `quality_reports/manuscript_consistency_audit.json`：中英文核心数字、禁用主张和参考文献序号一致性。
- `quality_reports/citation_inventory_audit.json`：17 个 DOI 在英文稿、中文稿、核验记录和 BibTeX 之间一致。
- `quality_reports/docx_package_audit.json`：DOCX ZIP/XML、正文 token、表格和媒体结构检查。
- `quality_reports/draft_lint.txt`、`mechanical_check.json`、`contribution_consistency.json`：Light 写作检查。
- `quality_reports/statistical_expression_scan.json`、`tortured_phrase_scan.json`：统计表达式和扭曲短语扫描。
- `quality_reports/research_ethics_review.md`：投稿前诚信、伦理、署名、AI 披露和数据可重复性审查。
- `quality_reports/reviewer_self_review.md`：审稿人视角的 major/minor concerns。
- `quality_reports/literature_coverage.md`：检索覆盖、失败路径和未解决项。

## 原始材料保护

`source_materials/` 中的原始 DOCX/PDF 不被覆盖。`SHA256SUMS.txt` 仍保持用户提交时的裸文件名格式；使用项目脚本从 `source_materials/` 验证：

```bash
python3 scripts/verify_source_checksums.py
```

## 可重复构建草案

以下命令均只依赖 Python 标准库；生成 PNG 时优先使用本地 ImageMagick，SVG 始终可生成：

```bash
python3 scripts/generate_funnel_figure.py
python3 scripts/build_bilingual_markdown.py
python3 scripts/build_docx_stdlib.py \
  --input manuscript/manuscript_bilingual.md \
  --output manuscript/manuscript_bilingual.docx \
  --title "Computational Prioritization / 牙周炎队列口腔微肽的计算优先级排序"
python3 scripts/build_docx_stdlib.py \
  --input manuscript/supplementary_tables_bilingual.md \
  --output manuscript/supplementary_tables_bilingual.docx \
  --title "Supplementary Tables / 补充表"
python3 scripts/audit_manuscript_consistency.py
```

## 当前状态与投稿边界

科学内容草案已完成，可交作者审阅；**尚不是投稿就绪包**。主要待办为：补齐 12/8 条候选的序列和逐行分数、原始代码与模型版本；核实 PRJEB65451；澄清长肽证据类型和 mebipred 交接分母；由作者补齐署名、经费、利益冲突和机构伦理口径；投稿前重核撤稿/更正状态并进行人工版面审阅。

当前环境没有 Office/LibreOffice/LaTeX/PDF 渲染器，因此 DOCX 已通过结构和内容检查，但未声称完成逐页视觉渲染审查。
