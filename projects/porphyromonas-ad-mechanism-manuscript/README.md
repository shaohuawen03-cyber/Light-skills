# 口腔微肽与牙周炎—阿尔茨海默病机制研究稿件包

## 当前版本

v3.12.0精简独立ALLLHRC–AChE分子动力学报告包：仅保留完整英文、中文版本，删除MD简洁版，不创建MD中间版；两份报告均删除摘要、关键词、引言、引文标记和参考文献，仅保留详细分析方法、结果与讨论。六份口腔smORF筛选DOCX逐字节保持不变，且不导入任何ALLLHRC动力学结果。

当前交付物均提供彼此分离的英文、中文DOCX及Markdown源文件：

- 筛选完整稿：`manuscript/full/{English,Chinese}.{docx,md}`
- 筛选中间稿：`manuscript/intermediate/{English,Chinese}.{docx,md}`
- 筛选简洁稿：`manuscript/concise/{English,Chinese}.{docx,md}`
- 独立MD完整报告：`manuscript/md_alllhrc/full/{English,Chinese}.{docx,md}`

筛选稿完整、中间和简洁三个版本均采用无标题、单段非结构式摘要起始；包含Introduction、Materials and methods、Results、Discussion和References，不设独立“统计分析”小节或“结论”章节。完整稿含6个三线表、约6,900个英文正文词和55条参考文献；中间稿含4个三线表、约4,600个英文正文词和40条参考文献；简洁稿含3个三线表、约3,700个英文正文词和22条参考文献。

独立MD报告是明确例外：DOCX直接从`Analysis methods`或`分析方法`开始，仅含分析方法、结果和讨论三个一级章节；无显示标题、摘要、关键词、引言、引文、参考文献、统计分析章节或独立结论。每份MD报告保留2个三线表。

八份当前DOCX均不含页眉、页脚、页码、批注或图像；使用12磅正文、双倍行距和1英寸页边距。正文普通段落采用480 twip首行缩进，摘要、章节标题、表题、表格和参考文献等非普通正文元素不缩进。所有表格仅保留顶线、表头下横线和底线，不使用竖线、内部正文横线或表头底色。

## 科学定位

项目以`source_materials/材料与方法及结果_机制研究版.docx`为主要筛选科学材料，报告纯计算、汇总层面的口腔smORF候选优选。候选级联包括UniDL4BioPep的ESM-2/CNN、NTxPred2肽模式的ESM2-t30微调模型、mebipred两级人工神经网络和AnOxPePred多任务一维CNN。

筛选稿三个版本均支持描述性漏斗、12条独立序列的组成核对及现有AChE Vina评分排序，但不支持牙周炎特异性、*Porphyromonas gingivalis*来源、当前队列表达、BBB通过、神经毒性、金属化学、AChE结合/功能、AD机制或因果关系。中间版保留完整的22项长/短肽多维结果、级联计数、12条序列与评分及长肽流失局限，但压缩文献综合和验证细节。

主源中的长肽和短肽多维功能输出均已恢复。流程局限明确披露：牙周炎标记分支中72条经宏蛋白质组支持、去重且BBB高分的31–50 aa长肽均未进入NTxPred2阳性集合；923条NTxPred2阳性序列全部≤30 aa，因而后续金属结合与CHEL/FRS网页预测及最终12条汇总候选只保留短肽。这不能证明长肽没有神经毒性或金属相关活性，而可能反映串行阈值、模型适用性/校准和网页预测器实现方式。

独立MD包仅解释用户指定的ALLLHRC–AChE单条100 ns输出：AChE骨架偏差有限，ALLLHRC约在23和56 ns发生两次内部构象转变，并呈现优选质心间距、较窄SASA范围和间歇氢键。该结果不整合至筛选稿，也不能证明结合亲和力、PAS驻留、AChE抑制、Aβ聚集改变、BBB转运或AD相关作用。RMSD数值来自图线数字化；源图继承的AChE–Aβ标题与ALLLHRC体系说明不一致，仍需拓扑—轨迹标识符核实。

筛选正文不报告具体参与者、标本、组装分析或MAG总数。用户说明的296个MAG在`evidence/mag_count_audit.md`中保留为待核查信息，未进入稿件。

## 图、表与引文

`manuscript/figures/`保留历史SVG/PNG源文件，便于项目内部追踪，但不是当前稿件DOCX的一部分。按用户要求，ALLLHRC–AChE结果图仅作为解读证据，不嵌入MD报告。

六份筛选Markdown使用Pandoc格式的BibTeX键并链接`references/references.bib`；标准库DOCX构建器生成连续编号的Vancouver式缓存文字。本环境未暴露Pandoc或Better BibTeX端点，因此筛选DOCX不被误称为Zotero-live。桌面Word/Zotero刷新仍是外部验收门。两份MD报告不含任何引文标记、编号引文、参考文献或Zotero字段。

相关Zotero验收工具与说明位于：

- `scripts/test_better_bibtex.py`
- `scripts/build_zotero_live_docx.py`
- `references/ZOTERO_WORD_ACCEPTANCE.md`
- `quality_reports/zotero_live_status.json`

## 可重复构建

从项目根目录运行：

```bash
for language in English Chinese; do
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input "manuscript/full/${language}.md" --output "manuscript/full/${language}.docx" --title "${language}"
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --bibliography references/references.bib --input "manuscript/intermediate/${language}.md" --output "manuscript/intermediate/${language}.docx" --title "${language}"
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-17T00:00:00Z --bibliography references/references.bib --input "manuscript/concise/${language}.md" --output "manuscript/concise/${language}.docx" --title "${language}"
  python3 scripts/build_docx_stdlib.py --clean-manuscript --timestamp 2026-08-23T00:00:00Z --input "manuscript/md_alllhrc/full/${language}.md" --output "manuscript/md_alllhrc/full/${language}.docx" --title "${language}"
done
```

## 当前审计

```bash
python3 scripts/verify_source_checksums.py
python3 scripts/audit_submission_manuscripts.py
python3 scripts/audit_full_manuscripts.py
python3 scripts/audit_intermediate_package.py
python3 scripts/audit_concise_package.py
python3 scripts/audit_docx_packages.py
python3 scripts/audit_full_docx_reproducibility.py
python3 scripts/audit_citation_inventory.py
python3 scripts/audit_excluded_source_scope.py
python3 scripts/stage5_statistics_audit.py
python3 scripts/audit_external_docking_summary.py
python3 scripts/audit_md_alllhrc_package.py
python3 scripts/generate_artifact_checksums.py
python3 scripts/build_repository_inventory.py
```

`quality_reports/submission_manuscript_audit.json`检查六份筛选稿；`quality_reports/intermediate_package_audit.json`核验中间版及冻结的完整/简洁筛选DOCX；`quality_reports/full_docx_reproducibility.json`要求六份筛选DOCX隔离重建后逐字节一致；`quality_reports/md_alllhrc_package_audit.json`单独检查两份MD报告的三章节结构、关键轨迹数值、分析细节、数字化RMSD来源、Aβ标题标注差异、解释边界、无图无引文DOCX、三线表、隔离重建、已删除MD简洁目录以及六份筛选DOCX哈希不变。

## 证据和历史材料

内部证据记录、哈希、版本提交、排除材料和复现边界保留在`evidence/`、`revision_v2/`、`revision_v3/`和`VERSION_HISTORY.md`中。此类管理信息用于项目追踪，不进入当前SCI稿件正文。历史组合稿、补充表和图件不属于当前独立中英文DOCX交付物。
