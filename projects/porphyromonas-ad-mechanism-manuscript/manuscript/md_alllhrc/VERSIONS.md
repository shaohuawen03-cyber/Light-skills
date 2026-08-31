# 独立对接与动力学报告：三版对照与图文核对

本文件记录 `manuscript/md_alllhrc/` 下**简洁版、中间版、完整版**的定位、共用数据权威、图文对应关系，以及各版删减边界。三版均为中英对照，**全部嵌入同一套 7 幅 PNG**。口腔 smORF 筛选稿（`manuscript/full|intermediate|concise/`）不在本包内，仍保持无图、不导入对接/MD 结果。

## 1. 交付路径

| 版本 | 英文 | 中文 |
| --- | --- | --- |
| 完整版 | `full/English.md` · `full/English.docx` | `full/Chinese.md` · `full/Chinese.docx` |
| 中间版 | `intermediate/English.md` · `intermediate/English.docx` | `intermediate/Chinese.md` · `intermediate/Chinese.docx` |
| 简洁版 | `concise/English.md` · `concise/English.docx` | `concise/Chinese.md` · `concise/Chinese.docx` |

三版共用结构：无显示标题、摘要、关键词或引言；一级标题仅为「分析方法 / Analysis methods」「结果 / Results」「讨论 / Discussion」。方法与结果不含 `[@…]` 引文标记。讨论引用高分 SCI 文献并附参考文献。DOCX 无页眉、页脚、页码或批注；正文 12 磅、双倍行距、1 英寸页边距。图4/图5/图6 前均有分页，避免被对接构象图遮挡。

## 2. 三版差异（科学内容相同，叙述深度不同）

| 项目 | 简洁版 | 中间版 | 完整版 |
| --- | --- | --- | --- |
| 英文词数 / 中文字符 | 2095 / 7915 | 2229 / 9217 | 5761 / 23040 |
| 用途 | 快速查看打分、构象与三条 100 ns 对比图 | 保留关键方法参数与 PAS/轨迹解读 | 可复核的方法学全文与机制讨论 |
| 方法 | 两段：Vina 三次运行 + 100 ns GROMACS | 对接一节 + MD 一节（含四阶段平衡要点） | 对接准备、四阶段平衡、9 项轨迹分析的完整协议 |
| 表1 | 12 行；列压缩为氢键/最优/均值/PAS 是否 | 12 行；保留关键残基与简短 PAS 说明 | 12 行；完整 PAS 结构描述 |
| 表2 | 6 行，与图4–6 的 A–F 面板一一对应 | 8 行：六面板 + 肽 RMSD + 接触对 | 13 行：含 Delta、RDF、Turn/Bend/Coil |
| 表3 | 4 行证据边界 | 5 行证据边界 | 7 行证据边界 |
| 讨论 | 按 Atanasova AChE–Aβ 轨迹逻辑写四步致病机制（PAS 占位、复合物稳定、胆碱能峡部、病理性伴侣共成核）；不含后续实验计划 | 机制、文献对照、局限三节 | 四步机制、五条文献对照、验证路线 |
| 参考文献 | 7 条 | 8 条 | 12 条 |
| 嵌入图 | **7 幅，与完整版字节相同** | **7 幅，与完整版字节相同** | **7 幅** |

三版**不得改写数值**。对接打分、氢键数、PAS 残基、最后 20 ns 的 RMSD/RMSF/SASA/Rg/氢键/DSSP 均以同一权威表为准（见第 3 节）。缩短只删叙述和次级指标，不改图、不改核心数字。

## 3. 数据与图件权威（三版共用）

### 3.1 对接打分（图1 / 表1）

- 权威表：`source_materials/md_results/local_vina_docking_summary.csv`
- 作图脚本：`scripts/generate_docking_score_figure.py`
- 图文件：`manuscript/figures/fig5_docking_scores.png`（SHA-256 `9762e4a1f892894c57d216168869d47d3d3e6670839024264a8dbc73077c4ff3`）

正文展示为常规四舍五入（最优打分与均值保留两位小数）。图1 横轴按**最优单次打分**从强到弱：FLLHTTR、YLSLLQR、ALLLHRC、FCLHLQLR、YHHLLCRR、LLHLPKRTT、LLHPLRL、WLLVHLKK、LLHPLRC、HLLTLKKHV、HLPLLHRCC、HVLLLRQCA。表1 仍按原序号 1–12 排列，数字与图1 各点一致。

| 肽 | 最优 (kcal/mol) | 三次均值±SD (kcal/mol) | 与图1 |
| --- | --- | --- | --- |
| FLLHTTR | -9.60 | -8.77 ± 1.41 | 最左侧；橙点最低、误差棒最长 |
| YLSLLQR | -9.49 | -9.44 ± 0.09 | 均值最强，误差棒极短 |
| ALLLHRC | -9.29 | -9.18 ± 0.11 | 均值第二 |
| FCLHLQLR | -9.27 | -8.96 ± 0.48 | 误差棒较长 |
| YHHLLCRR | -9.03 | -8.62 ± 0.43 | |
| LLHLPKRTT | -9.01 | -8.89 ± 0.16 | |
| LLHPLRL | -8.94 | -8.91 ± 0.05 | 均值与最优几乎重合 |
| WLLVHLKK | -8.94 | -8.64 ± 0.26 | |
| LLHPLRC | -8.91 | -8.78 ± 0.11 | |
| HLLTLKKHV | -8.88 | -8.69 ± 0.20 | |
| HLPLLHRCC | -8.35 | -8.28 ± 0.07 | |
| HVLLLRQCA | -8.25 | -8.07 ± 0.16 | 最右侧，打分最弱 |

氢键数、关键残基与 PAS 判读来自最优构象几何分析，与图2/图3/图S1 面板一致，**不以**旧表 `docking_12peptides_summary.csv` 的转录 SD 为准（该表 SD 与本地三次运行不符，例如 FLLHTTR 旧 SD 0.08 vs 本地 1.41）。

### 3.2 对接构象（图2、图3、图S1）

| 正文 | 文件 | 面板内容 |
| --- | --- | --- |
| 图2 | `fig_docking_poses_A_F.png` | A ALLLHRC；B FCLHLQLR；C FLLHTTR；D HLLTLKKHV；E HLPLLHRCC；F HVLLLRQCA |
| 图3 | `fig_docking_poses_G_L.png` | G LLHLPKRTT；H LLHPLRC；I LLHPLRL；J WLLVHLKK；K YHHLLCRR；L YLSLLQR |
| 图S1 | `fig_docking_poses_12_combined.png` | A–L 单页总览 |

来源为用户上传的 `docking/sci_composite_figures/` 复合图，哈希与 `manuscript/figures/` 副本相同。

### 3.3 100 ns 动力学对比（图4–6 / 表2）

来源仓库 `shaohuawen03-cyber/asd` 分支 `arena/01a03d09-asd` 提交 `1cb17b64103417a57d0c38adba00866a3ae8d59c`（见 `source_materials/md_results/COMPARE_FIGURE_PROVENANCE.md`）。

| 正文 | 源路径 | PNG SHA-256 | 文件大小 |
| --- | --- | --- | --- |
| 图4 ALLLHRC | `gromacs_md/compare_ache_vs_alllhrc/fig_compare.png` | `01a82f635c6d1f779166a458731d08b8c00dbbd6a0b9e3bde058185ca8a6172a` | 905253 B |
| 图5 FLLHTTR | `gromacs_md/compare_ache_vs_fllhttr/fig_compare.png` | `16df70af688e2ff1355cd3bb446be2fb22625fa609edd975a50e6201ee3e95ed` | 903830 B |
| 图6 YLSLLQR | `gromacs_md/compare_ache_vs_ylsllqr/fig_compare.png` | `db214b1c62000596367e25912bd67b3068d74803d0043b1c5a479e464e6cda7b` | 877546 B |

每图标题均为 `ache (AChE apo control) vs <peptide> (AChE-peptide complex) — 100 ns each`。六面板与表2 对齐：

| 面板 | 图中坐标轴 | 权威 CSV 指标 | apo | ALLLHRC | FLLHTTR | YLSLLQR |
| --- | --- | --- | --- | --- | --- | --- |
| A | Backbone Cα RMSD (nm) vs Time | `Backbone_RMSD_last20ns_(nm)` | 0.1562 ± 0.0093 | 0.1916 ± 0.0092 | 0.2102 ± 0.0087 | 0.2064 ± 0.0136 |
| B | Backbone Cα RMSF (nm) vs residue | `Backbone_RMSF_per-residue_mean_(nm)` | 0.0783 ± 0.0524 | 0.0876 ± 0.0581 | 0.0901 ± 0.0644 | 0.0813 ± 0.0574 |
| C | SASA (nm²) vs Time | `SASA_last20ns_(nm2)` | 212.41 ± 2.36 | 217.47 ± 2.49 | 216.34 ± 2.55 | 210.37 ± 2.91 |
| D | Rg (nm) vs Time | `Rg_last20ns_(nm)` | 2.2967 ± 0.0043 | 2.3107 ± 0.0052 | 2.3163 ± 0.0059 | 2.3004 ± 0.0051 |
| E | DSSP occupancy last 20 ns (%) | helix / sheet | 33.59 / 17.18 | 33.66 / 16.76 | 33.87 / 17.11 | 32.92 / 17.08 |
| F | Intermolecular H-bonds vs Time | `AChE-Peptide_Hbonds_last20ns_(count)` | — | 2.19 ± 0.80 | 2.80 ± 0.99 | 4.23 ± 1.24 |

CSV：`source_materials/md_results/compare_summary_{alllhrc,fllhttr,ylsllqr}.csv`。

肉眼可核对的图文要点（三版正文均保留）：

1. **图5A / FLLHTTR**：蓝线（复合物）在后段明显高于红线（apo），对应最大 RMSD（0.2102 nm）与最大受体净扰动。
2. **图6C / YLSLLQR**：蓝线 SASA 整体低于红线，对应唯一低于 apo 的复合物 SASA（210.37 vs 212.41 nm²）。
3. **图6F / YLSLLQR**：氢键计数明显高于图4F、图5F，对应 4.23 ± 1.24。
4. **图4–6 的 E 面板**：apo 与复合物的 α-螺旋、β-折叠柱高几乎重合（Δ < 0.7%），对应“未解折叠”。
5. **图4–6 的 D 面板**：Rg 全部落在约 2.29–2.32 nm，对应球状折叠保持。

AChE-only RMSD（0.1653 / 0.1767 / 0.1601 nm）和产物阶段氢键（3.88 / 2.90 / 3.80）来自 `source_materials/md_results/RESULTS_ANALYSIS_v1.md`，与复合物整体 RMSD/氢键不是同一列：完整版表2 同时列出两者；中间/简洁版表2 与图面板一致，使用**复合物整体** CSV 值，以免和图中蓝线（Complex BB / Complex SASA / Complex Rg）错位。

## 4. 明确不支持的外推（三版相同）

- Vina 打分 ≠ 实验 Kd / Ki / ΔG。
- 单条 100 ns 轨迹 ≠ 不可逆纳摩尔结合或 AD 因果。
- FLLHTTR 最优构象 -9.60 kcal/mol 不能当作三次运行收敛亲和力。
- 筛选稿中的外部 v0.4 转录对接表与本包本地三次运行不是同一权威。

## 5. 重建

```bash
for version in full intermediate concise; do
  for language in English Chinese; do
    python3 scripts/build_docx_stdlib.py --clean-manuscript --allow-images \
      --timestamp 2026-08-23T00:00:00Z \
      --input "manuscript/md_alllhrc/${version}/${language}.md" \
      --output "manuscript/md_alllhrc/${version}/${language}.docx" \
      --title "${language}"
  done
done
python3 scripts/audit_md_alllhrc_package.py
```

审计要求：六份报告均嵌入 7 幅 PNG；核心数值字符串与图文件哈希三版一致；英文词数/中文字数满足完整版 > 中间版 > 简洁版；六份筛选 DOCX 哈希不变。
