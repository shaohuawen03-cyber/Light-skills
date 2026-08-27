## 分析方法

12 条牙周炎来源的 7–9 个氨基酸微肽以 AutoDock Vina（exhaustiveness = 32；三次独立成功运行）对接到人源 AChE（PDB 4EY6）。网格以外周阴离子位点（PAS：Tyr72、Asp74、Thr75、Trp286、His287、Tyr341）为中心，并覆盖峡部颈部与催化三联体（Ser203、His447、Glu334）。最优单次打分、三次运行均值±SD、氢键与 PAS 接触取自本地汇总表及各配体单一最优构象。PDBQT 文件未归档。

四个 GROMACS 体系（apo AChE 以及 ALLLHRC、FLLHTTR、YLSLLQR 复合物）以 Amber99SB-ILDN、TIP3P 水、0.15 M NaCl、LINCS 和粒子网格Ewald 静电，在 300 K、1.0 bar 下模拟 100 ns。图4–6 对应指标为骨架 RMSD、逐残基 RMSF、SASA、回转半径（Rg）、DSSP 占有率和分子间氢键。报告值为最后 20 ns 的均值±SD。

## 结果

### 分子对接

最优单次打分介于 -8.25 至 -9.60 kcal/mol，三次运行均值介于 -8.07 ± 0.16 至 -9.44 ± 0.09 kcal/mol（表1，图1）。外周阴离子位点（PAS）接触残基均取自各配体最优构象。FLLHTTR 最优构象最强（-9.60 kcal/mol），但 SD 最大（-8.77 ± 1.41 kcal/mol）。YLSLLQR 三次均值最强（-9.44 ± 0.09 kcal/mol）；ALLLHRC 均值居次（-9.18 ± 0.11 kcal/mol），但其最优构象位于催化口袋而非外侧 PAS。各最优构象形成 3–10 个氢键（图2、图3；图S1）。

**表1. 12条微肽对人源AChE（PDB 4EY6）的本地三次AutoDock Vina打分。**

| 序号 | 微肽 | 氢键数 | 最优打分 (kcal/mol) | 三次均值±SD (kcal/mol) | 最优构象PAS |
| --- | --- | --- | --- | --- | --- |
| 1 | ALLLHRC | 3 | -9.29 | -9.18 ± 0.11 | 否（Ser203峡部颈部） |
| 2 | FCLHLQLR | 7 | -9.27 | -8.96 ± 0.48 | 是（Thr75、Tyr341） |
| 3 | FLLHTTR | 8 | -9.60 | -8.77 ± 1.41 | 是（Asp74、Tyr72、His287） |
| 4 | HLLTLKKHV | 6 | -8.88 | -8.69 ± 0.20 | 是（Tyr72、Phe346） |
| 5 | HLPLLHRCC | 4 | -8.35 | -8.28 ± 0.07 | 否 |
| 6 | HVLLLRQCA | 4 | -8.25 | -8.07 ± 0.16 | 是（Thr75） |
| 7 | LLHLPKRTT | 3 | -9.01 | -8.89 ± 0.16 | 邻近（Val340） |
| 8 | LLHPLRC | 4 | -8.91 | -8.78 ± 0.11 | 否 |
| 9 | LLHPLRL | 10 | -8.94 | -8.91 ± 0.05 | 是（Trp286/Tyr341至His447） |
| 10 | WLLVHLKK | 4 | -8.94 | -8.64 ± 0.26 | 否 |
| 11 | YHHLLCRR | 7 | -9.03 | -8.62 ± 0.43 | 否（Trp86口袋） |
| 12 | YLSLLQR | 7 | -9.49 | -9.44 ± 0.09 | 是（Tyr72、Thr75、Ser203） |

![图1. 12条候选微肽对人源AChE的本地AutoDock Vina对接打分。](../../figures/fig5_docking_scores.png)

**图1. 12条候选微肽对人源AChE（PDB 4EY6）的本地AutoDock Vina对接打分。** 蓝色圆点为三次均值，误差棒为标准差，橙色菱形为最优单次打分。横轴顺序与最优单次打分排序一致。

![图2. ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC和HVLLLRQCA的最优对接构象。](../../figures/fig_docking_poses_A_F.png)

**图2. 最优构象A–F（ALLLHRC至HVLLLRQCA）。** FLLHTTR（C面板）为最密集的PAS构象。

![图3. LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR和YLSLLQR的最优对接构象。](../../figures/fig_docking_poses_G_L.png)

**图3. 最优构象G–L。** LLHPLRL（I面板）从PAS跨越至His447；YLSLLQR（L面板）桥接PAS与催化入口。

![图S1. 12条微肽最优对接构象总览。](../../figures/fig_docking_poses_12_combined.png)

**图S1. A–L面板总览。**

### 100 ns全原子分子动力学模拟

apo AChE 与三种复合物在 100 ns 内保持球状折叠（表2，图4–6）。各图采用源文件 `fig_compare.png` 的六面板布局：RMSD（A）、RMSF（B）、SASA（C）、Rg（D）、最后 20 ns 的 DSSP（E）和分子间氢键（F）。

<!-- PAGEBREAK -->

![图4. apo AChE与AChE–ALLLHRC 100 ns对比。](../../figures/fig_compare_ache_vs_alllhrc.png)

**图4. apo AChE与AChE–ALLLHRC。** 复合物RMSD（A）平台约 0.19 nm；氢键（F）持续存在。

![图5. apo AChE与AChE–FLLHTTR 100 ns对比。](../../figures/fig_compare_ache_vs_fllhttr.png)

**图5. apo AChE与AChE–FLLHTTR。** 三条肽中 RMSD（A）与 Rg（D）升幅最大。

![图6. apo AChE与AChE–YLSLLQR 100 ns对比。](../../figures/fig_compare_ache_vs_ylsllqr.png)

**图6. apo AChE与AChE–YLSLLQR。** SASA（C）低于 apo；氢键计数（F）最密。

**表2. 与图4–6面板对齐的最后20 ns指标（均值±SD）。**

| 指标 | apo AChE | ALLLHRC | FLLHTTR | YLSLLQR | 图面板 |
| --- | --- | --- | --- | --- | --- |
| 骨架RMSD (nm) | 0.1562 ± 0.0093 | 0.1916 ± 0.0092 | 0.2102 ± 0.0087 | 0.2064 ± 0.0136 | A |
| RMSF均值 (nm) | 0.0783 ± 0.0524 | 0.0876 ± 0.0581 | 0.0901 ± 0.0644 | 0.0813 ± 0.0574 | B |
| SASA (nm²) | 212.41 ± 2.36 | 217.47 ± 2.49 | 216.34 ± 2.55 | 210.37 ± 2.91 | C |
| Rg (nm) | 2.2967 ± 0.0043 | 2.3107 ± 0.0052 | 2.3163 ± 0.0059 | 2.3004 ± 0.0051 | D |
| DSSP α-螺旋 / β-折叠 (%) | 33.59 / 17.18 | 33.66 / 16.76 | 33.87 / 17.11 | 32.92 / 17.08 | E |
| 分子间氢键 | 不适用 | 2.19 ± 0.80 | 2.80 ± 0.99 | 4.23 ± 1.24 | F |

复合物 RMSD 均低于 0.22 nm。YLSLLQR 是唯一 SASA 相对 apo 收缩的复合物，与图6C一致，其氢键网络也最密（4.23 ± 1.24）。各图 E 面板中螺旋（约 33–34%）与折叠（约 17%）与 apo 柱形重叠。三个复合物均保留 7 对持续性接触。

### 证据边界

**表3. 图件与表格所支持及不支持的解释。**

| 序号 | 支持 | 不支持 |
| --- | --- | --- |
| 1 | FLLHTTR、YLSLLQR、LLHPLRL最优构象接触PAS残基 | Vina打分不是实验Kd或Ki |
| 2 | 100 ns复合物保持折叠（RMSD < 0.22 nm；DSSP守恒） | RMSD微增不是解折叠 |
| 3 | 后20 ns氢键2.19–4.23个在F面板持续 | 单条100 ns轨迹不是不可逆结合 |
| 4 | FLLHTTR最优-9.60 kcal/mol而均值为-8.77 ± 1.41 kcal/mol | 最优构象不是收敛亲和力 |

## 讨论

在牙周炎导致血脑屏障通透性增加的假说下，候选微肽可占据 AChE 的 PAS。最优构象对接与 100 ns 表面驻留为峡部封堵（胆碱能功能受损）以及 PAS 介导的 Aβ 病理性伴侣作用提供结构假说，并与 Atanasova 等、Inestrosa 等、Silman 与 Sussman 以及 Dominy 等关于脑内 *P. gingivalis* 的发现相一致。上述内容仍为计算假说。各体系目前为单条 100 ns 轨迹；计划验证包括等温滴定量热、表面等离子共振和 Ellman 抑制实验。

### 参考文献

1. Atanasova, M., Dimitrov, I., & Ivanov, S. (2020). Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. *Cybernetics and Information Technologies*, 20(6), 140–154. https://doi.org/10.2478/cait-2020-0068
2. Dominy, S. S., Lynch, C., Ermini, F., Benedyk, M., Marczyk, A., Forbes, A., Haditsch, M., et al. (2019). *Porphyromonas gingivalis* in Alzheimer's disease brains: Evidence for disease causation and treatment with small-molecule inhibitors. *Science Advances*, 5(1), eaau3333. https://doi.org/10.1126/sciadv.aau3333
3. Silman, I., & Sussman, J. L. (2005). Acetylcholinesterase: ‘classical’ and ‘non-classical’ functions and pharmacology. *Current Opinion in Pharmacology*, 5(3), 293–302. https://doi.org/10.1016/j.coph.2005.01.014
4. Inestrosa, N. C., Alvarez, A., Pérez, C. A., Moreno, R. D., Vicente, M., Link, C. A., Dayoub, O. I., et al. (1996). Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. *Neuron*, 16(4), 881–891. https://doi.org/10.1016/S0896-6273(00)80108-7
5. Inestrosa, N. C., Dinamarca, M. C., & Alvarez, A. (2008). Amyloid-cholinesterase interactions. Implications for Alzheimer's disease. *Molecular Neurobiology*, 38(3), 262–273. https://doi.org/10.1007/s12035-008-8043-6
6. Hampel, H., Mesulam, M. M., Cuello, A. C., Farlow, M. R., Giacobini, E., Grossberg, G. T., Khachaturian, A. S., et al. (2018). The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. *Brain*, 141(7), 1917–1933. https://doi.org/10.1093/brain/awy132
7. Bartus, R. T., Dean, R. L., Beer, B., & Lippa, A. S. (1982). The cholinergic hypothesis of geriatric memory dysfunction. *Science*, 217(4558), 408–414. https://doi.org/10.1126/science.7046051
