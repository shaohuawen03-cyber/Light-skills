# 口腔微肽与牙周炎—阿尔茨海默病机制研究稿件包

## 当前版本

v3.7.0同时提供完整稿和扩展后的精简稿，每种版本均包含独立英文、中文DOCX及其Markdown源文件：

- `manuscript/full/English.docx`
- `manuscript/full/Chinese.docx`
- `manuscript/concise/English.docx`
- `manuscript/concise/Chinese.docx`

四份DOCX均从结构式摘要开始，不显示论文标题，不含页眉、页脚、页码、批注或图像。英文稿参照*Journal of Alzheimer's Disease Reports* Research Article的核心要求，采用IMRaD结构、无编号标题、≤250词结构式摘要、12磅Times New Roman、双倍行距和1英寸页边距；中文稿保持同步结构。具体对齐和用户要求形成的例外见`quality_reports/journal_format_alignment_v37.md`。完整稿含4个三线表和55条参考文献；扩展精简稿含2个三线表和22条参考文献，英文正文较v3.6.0增加约74%。所有表格仅保留顶线、表头下横线和底线，不使用竖线、内部正文横线或表头底色。结论之后直接进入参考文献，不含Declarations或其他管理性章节。

## 科学定位

项目以`source_materials/材料与方法及结果_机制研究版.docx`为主要科学材料，报告纯计算、汇总层面的口腔smORF候选优选。候选级联包括UniDL4BioPep的ESM-2/CNN、NTxPred2肽模式的ESM2-t30微调模型、mebipred两级人工神经网络和AnOxPePred多任务一维CNN。

当前结果支持描述性筛选漏斗、12条独立序列的组成核对及现有AChE Vina评分排序，但不支持牙周炎特异性、*Porphyromonas gingivalis*来源、当前队列表达、BBB通过、神经毒性、金属化学、AChE结合/功能、AD机制或因果关系。100 ns GROMACS轨迹分析作为预设扩展正在进行；稳定性、收敛性和接触结果将在分析与质量控制完成后补充。

正文不报告具体参与者、标本、组装分析或MAG总数。用户说明的296个MAG在`evidence/mag_count_audit.md`中保留为待核查信息，未进入稿件。

## 图和表

`manuscript/figures/`保留历史SVG/PNG源文件，便于项目内部追踪，但它们不是v3.7.0稿件DOCX的一部分。当前DOCX包经OpenXML检查不含`word/media/`、drawing对象或图像关系。

## 引文与Zotero

四份Markdown正文使用Pandoc格式的真实BibTeX键，例如`[@scheltens2021alzheimer]`，统一链接到`references/references.bib`。标准库DOCX构建器依据各版本参考文献表自动生成连续编号的Vancouver式缓存文字。

本环境未暴露Pandoc或正在运行的Better BibTeX端点，因此提交的DOCX不被误称为Zotero-live。严格的Better BibTeX探针、官方`zotero.lua`过滤器构建和OpenXML字段检查位于：

- `scripts/test_better_bibtex.py`
- `scripts/build_zotero_live_docx.py`
- `references/ZOTERO_WORD_ACCEPTANCE.md`
- `quality_reports/zotero_live_status.json`

桌面Word/Zotero刷新和Add/Edit Bibliography是尚待用户执行的验收门。普通`[N]`文字不能通过Zotero Refresh自动变为live fields。

## 可重复构建

从项目根目录运行：

```bash
python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/full/English.md \
  --output manuscript/full/English.docx \
  --title English

python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/full/Chinese.md \
  --output manuscript/full/Chinese.docx \
  --title Chinese

python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/concise/English.md \
  --output manuscript/concise/English.docx \
  --title English

python3 scripts/build_docx_stdlib.py --clean-manuscript \
  --timestamp 2026-08-17T00:00:00Z \
  --bibliography references/references.bib \
  --input manuscript/concise/Chinese.md \
  --output manuscript/concise/Chinese.docx \
  --title Chinese
```

## 当前审计

```bash
python3 scripts/audit_submission_manuscripts.py
python3 scripts/audit_full_manuscripts.py
python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
python3 scripts/audit_full_docx_reproducibility.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py
python3 scripts/generate_artifact_checksums.py
python3 scripts/build_repository_inventory.py
```

`quality_reports/submission_manuscript_audit.json`检查四份DOCX的无标题摘要起始、结论后直接进入参考文献、图像完全缺失、三线表结构、敏感数量省略、科学边界、BibTeX键和引用清单。`quality_reports/full_docx_reproducibility.json`要求四份DOCX隔离重建后逐字节一致。

## 证据和历史材料

内部证据记录、哈希、版本提交、排除材料和复现边界保留在`evidence/`、`revision_v2/`、`revision_v3/`和`VERSION_HISTORY.md`中。此类管理信息用于项目追踪，不进入当前SCI稿件正文。历史双语组合稿、补充表和图件不属于v3.7.0四份稿件交付物。
