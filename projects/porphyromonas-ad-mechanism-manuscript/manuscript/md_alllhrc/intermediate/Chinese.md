## 分析方法

### 分子对接

人源重组乙酰胆碱酯酶（rhAChE，PDB 4EY6，分辨率 2.40 Å）经去除加兰他敏与结晶水、修复内部链断裂并按生理 pH 7.4 分配质子化状态后用作受体。12 条 7–9 个氨基酸候选微肽 ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC、HVLLLRQCA、LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR 和 YLSLLQR 采用 AutoDock Vina（exhaustiveness = 32）对接到以外周阴离子位点（PAS：Tyr72、Asp74、Thr75、Leu76、Trp286、His287、Tyr341）为中心、并覆盖峡部颈部（Phe295）、胆碱结合亚位点（Trp86、Glu202、Tyr337）及催化三联体（Ser203、His447、Glu334）的网格。每条配体独立运行三次（`N_Success` = 3）。最优单次打分、三次运行均值±SD、氢键几何与 PAS 接触均取自本地三次运行汇总表及各配体打分最高的单一构象。逐条 PDBQT 文件与配置日志未归档。

### 分子动力学

四个显式溶剂体系在 GROMACS 2025 中以 Amber99SB-ILDN 力场和 TIP3P 水、0.15 M NaCl 进行模拟：apo AChE（单一 A 链）以及 AChE–ALLLHRC、AChE–FLLHTTR、AChE–YLSLLQR 复合物。各体系置于溶质至边界缓冲 1.0 nm 的三斜盒子。平衡包括 2,000 步最速下降能量最小化、1.0 ns 受限 NVT 升温至 300 K、1.0 ns 受限 NPT 密度平衡和 1.0 ns 无约束 NPT 预平衡。产物模拟在 NPT 系综（300 K，1.0 bar）运行 100 ns（dt = 2.0 fs），采用 LINCS、1.2 nm 截断和粒子网格Ewald 静电。轨迹每 20 ps 输出一帧。

与图4–6对应的轨迹指标包括骨架 Cα RMSD、逐残基 RMSF、SASA、回转半径（Rg）、DSSP 二级结构占有率和分子间氢键（`gmx hbond`；供体–受体距离 ≤ 3.0 Å）。另记录微肽自拟合 RMSD 与持续性界面接触（7.0 Å 截断）。稳态值为最后 20 ns（80.0–100.0 ns）的均值±SD。

## 结果

### 对接亲和力与 PAS 结合

12 条配体的本地 Vina 打分均有利。最优单次打分介于 -8.25 至 -9.60 kcal/mol，三次运行均值介于 -8.07 ± 0.16 至 -9.44 ± 0.09 kcal/mol（表1，图1）。按最优构象排序，FLLHTTR 居首（-9.60 kcal/mol），随后为 YLSLLQR（-9.49 kcal/mol）和 ALLLHRC（-9.29 kcal/mol）。按三次运行均值排序，则 YLSLLQR 居首（-9.44 ± 0.09 kcal/mol），ALLLHRC 次之（-9.18 ± 0.11 kcal/mol）。FLLHTTR 保留最强单次构象，但三次运行 SD 最大（-8.77 ± 1.41 kcal/mol）。各最优构象形成 3–10 个氢键（平均键长 2.83–3.28 Å；图2、图3；图S1）。

**表1. 12条候选微肽对人源AChE（PDB 4EY6）的本地AutoDock Vina打分与PAS结合。**

| 序号 | 微肽 | 氢键数 | 关键残基 | 最优打分 (kcal/mol) | 三次均值±SD (kcal/mol) | PAS结合 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ALLLHRC | 3 | SER-125, SER-203, TYR-124 | -9.29 | -9.18 ± 0.11 | 否；催化Ser203/峡部颈部 |
| 2 | FCLHLQLR | 7 | SER-203, THR-75, TYR-124, TYR-337, TYR-341 | -9.27 | -8.96 ± 0.48 | 是；Thr75、Tyr341 |
| 3 | FLLHTTR | 8 | ASP-74, HIS-287, LEU-289, PHE-295, TYR-337, TYR-72 | -9.60 | -8.77 ± 1.41 | 是；广泛PAS（Asp74、Tyr72、His287）；SD最大 |
| 4 | HLLTLKKHV | 6 | PHE-346, TYR-124, TYR-337, TYR-72, TYR-77 | -8.88 | -8.69 ± 0.20 | 是；Tyr72及344–361（Phe346） |
| 5 | HLPLLHRCC | 4 | SER-125, TYR-124, TYR-337 | -8.35 | -8.28 ± 0.07 | 否；峡部边缘 |
| 6 | HVLLLRQCA | 4 | SER-125, THR-75, TYR-124 | -8.25 | -8.07 ± 0.16 | 是；Thr75 |
| 7 | LLHLPKRTT | 3 | SER-203, TYR-337, VAL-340 | -9.01 | -8.89 ± 0.16 | 邻近PAS（Val340） |
| 8 | LLHPLRC | 4 | SER-125, SER-293, TYR-124 | -8.91 | -8.78 ± 0.11 | 否；峡部入口 |
| 9 | LLHPLRL | 10 | HIS-447, PHE-295, TRP-286, TYR-124, TYR-337, TYR-341 | -8.94 | -8.91 ± 0.05 | 是；双位点跨越至His447；SD最小 |
| 10 | WLLVHLKK | 4 | ASN-283, GLN-279, SER-293, TYR-124 | -8.94 | -8.64 ± 0.26 | 否；外周环区 |
| 11 | YHHLLCRR | 7 | SER-125, SER-203, TRP-86, TYR-124, TYR-337 | -9.03 | -8.62 ± 0.43 | 否；胆碱口袋Trp86 |
| 12 | YLSLLQR | 7 | GLU-202, SER-203, THR-75, TYR-124, TYR-337, TYR-72 | -9.49 | -9.44 ± 0.09 | 是；PAS兼催化入口；均值最强 |

![图1. 12条候选微肽对人源AChE的本地AutoDock Vina对接打分。](../../figures/fig5_docking_scores.png)

**图1. 12条候选微肽对人源AChE（PDB 4EY6）的本地AutoDock Vina对接打分。** 蓝色圆点为三次运行均值，误差棒为标准差，橙色菱形为最优单次打分。横轴顺序与最优单次打分排序一致。Vina打分为经验排序指标，不能等同于实验结合自由能。

![图2. ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC和HVLLLRQCA的最优对接构象。](../../figures/fig_docking_poses_A_F.png)

**图2. ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC和HVLLLRQCA的最优对接构象（A–F）。** 微肽为橙色，接触残基为青色，氢键以虚线标示。

![图3. LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR和YLSLLQR的最优对接构象。](../../figures/fig_docking_poses_G_L.png)

**图3. LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR和YLSLLQR的最优对接构象（G–L）。** LLHPLRL（I面板）从PAS的Trp286/Tyr341跨越至催化His447。

![图S1. 12条微肽最优对接构象总览。](../../figures/fig_docking_poses_12_combined.png)

**图S1. 12条微肽最优对接构象总览。** 单页汇总A–L面板。

最优构象中直接对接经典外周阴离子位点（PAS：Tyr72、Asp74、Trp286、Tyr341等）的配体为FLLHTTR（图2C）、YLSLLQR（图3L）、FCLHLQLR、HVLLLRQCA、HLLTLKKHV和LLHPLRL（图3I）。ALLLHRC结合催化Ser203，平均氢键最短（2.83 Å），而非外侧PAS芳香核心（图2A）。三次运行均值将可重复的高亲和力配体（YLSLLQR、ALLLHRC、LLHPLRL）与最优构象强于运行均值的配体（FLLHTTR、FCLHLQLR、YHHLLCRR）区分开来。

### apo AChE与三种复合物的100 ns分子动力学

对 apo AChE 以及 ALLLHRC、FLLHTTR、YLSLLQR 复合物完成产物轨迹（表2，图4–6）。每幅六面板图比较无配体对照与一条肽复合物：骨架RMSD（A）、逐残基RMSF（B）、SASA（C）、Rg（D）、最后20 ns的DSSP占有率（E）和分子间氢键（F）。

<!-- PAGEBREAK -->

![图4. apo AChE与AChE–ALLLHRC 100 ns对比。](../../figures/fig_compare_ache_vs_alllhrc.png)

**图4. apo AChE与AChE–ALLLHRC 100 ns分子动力学对比。** A–F面板与表2指标对应。

![图5. apo AChE与AChE–FLLHTTR 100 ns对比。](../../figures/fig_compare_ache_vs_fllhttr.png)

**图5. apo AChE与AChE–FLLHTTR 100 ns分子动力学对比。** 面板布局与图4相同。复合物RMSD（A）与Rg（D）在三条肽中升幅最大。

![图6. apo AChE与AChE–YLSLLQR 100 ns对比。](../../figures/fig_compare_ache_vs_ylsllqr.png)

**图6. apo AChE与AChE–YLSLLQR 100 ns分子动力学对比。** 面板布局与图4相同。SASA（C）相对apo收缩；氢键计数（F）在三条复合物中最密。

**表2. apo AChE与三种肽复合物最后20 ns轨迹指标（均值±SD），与图4–6对齐。**

| 指标（最后20 ns） | apo AChE | AChE–ALLLHRC | AChE–FLLHTTR | AChE–YLSLLQR |
| --- | --- | --- | --- | --- |
| 骨架Cα RMSD (nm)；图A面板 | 0.1562 ± 0.0093 | 0.1916 ± 0.0092 | 0.2102 ± 0.0087 | 0.2064 ± 0.0136 |
| 微肽自拟合RMSD (nm) | 不适用 | 0.2518 ± 0.0136 | 0.2697 ± 0.0217 | 0.1979 ± 0.0143 |
| 逐残基RMSF均值 (nm)；图B面板 | 0.0783 ± 0.0524 | 0.0876 ± 0.0581 | 0.0901 ± 0.0644 | 0.0813 ± 0.0574 |
| SASA (nm²)；图C面板 | 212.41 ± 2.36 | 217.47 ± 2.49 | 216.34 ± 2.55 | 210.37 ± 2.91 |
| Rg (nm)；图D面板 | 2.2967 ± 0.0043 | 2.3107 ± 0.0052 | 2.3163 ± 0.0059 | 2.3004 ± 0.0051 |
| 分子间氢键；图F面板 | 不适用 | 2.19 ± 0.80 | 2.80 ± 0.99 | 4.23 ± 1.24 |
| 持续性接触对 | 不适用 | 7 | 7 | 7 |
| DSSP α-螺旋 / β-折叠 (%)；图E面板 | 33.59 / 17.18 | 33.66 / 16.76 | 33.87 / 17.11 | 32.92 / 17.08 |

图4A、图5A和图6A显示 apo RMSD 维持在约 0.16 nm，复合物 RMSD 均低于 0.22 nm。仅受体部分 RMSD（0.1653、0.1767、0.1601 nm）表明 FLLHTTR 对酶主链扰动最大，YLSLLQR 几乎不移动受体骨架。RMSF（B面板）在催化核心保持低值，升幅主要位于表面环区。Rg（D面板）维持在 2.29–2.32 nm。SASA（C面板）在 ALLLHRC 与 FLLHTTR 中略升，在 YLSLLQR 中降至 210.37 nm²，与图6C更紧密的界面埋藏一致。氢键在 100 ns 全程持续（F面板）；YLSLLQR 网络最密（4.23 ± 1.24）。DSSP 螺旋（约 33–34%）与折叠（约 17%）与 apo 柱形重叠（E面板）。三个复合物均保留 7 对持续性接触。

### 证据边界

**表3. 分子对接与100 ns动力学结果的支持与不支持解释。**

| 序号 | 观察 | 支持的解释 | 不支持的外推 |
| --- | --- | --- | --- |
| 1 | FLLHTTR、YLSLLQR、LLHPLRL最优构象接触PAS残基 | 对PAS及峡部入口具有几何互补 | Vina打分不能等同实验Kd或Ki |
| 2 | 复合物RMSD为0.16–0.21 nm且DSSP守恒 | 局部环区适应而非解折叠 | RMSD微增不是变性或解离 |
| 3 | 后20 ns氢键2.19–4.23个且各有7对接触 | 100 ns尺度的表面驻留 | 单条轨迹不能证明不可逆纳摩尔结合 |
| 4 | YLSLLQR的SASA收缩与最密氢键面板 | 相对apo的紧密界面埋藏 | 不能直接等同宏观结合常数 |
| 5 | FLLHTTR最优-9.60 kcal/mol而均值为-8.77 ± 1.41 kcal/mol | 最优构象为高分离群；均值排序更支持YLSLLQR | 单一最优构象不是收敛亲和力 |

## 讨论

### 以PAS靶向为工作假说的AD机制

慢性牙周炎可使 *Porphyromonas gingivalis* 产物进入体循环，并在细胞因子与牙龈蛋白酶损伤紧密连接后跨越受损血脑屏障。进入皮层间质后，候选微肽可占据门控 20 Å 活性峡部的 AChE PAS。最优对接将 FLLHTTR 置于 Asp74/Tyr72/His287，将 LLHPLRL 从 Trp286/Tyr341 跨越至 His447，将 YLSLLQR 同时锚定 PAS 与催化入口。100 ns 轨迹显示这些复合物保持球状折叠（Rg 2.29–2.32 nm；螺旋/折叠守恒），并维持分子间氢键（后 20 ns 为 2.19–4.23 个）。PAS 空间占位因此是乙酰胆碱进入受阻的结构假说，而不是已测定的 IC50。

独立于催化功能，AChE 可通过同一 PAS 作为病理性伴侣加速 Aβ 组装。本肽靶向 PAS，HLLTLKKHV 还接触邻近 344–361 区（Phe346）。持续表面驻留可能降低 Aβ 成核能垒、重塑入口环区或提供两亲性种子。上述内容仍为计算假说，有待等温滴定量热、表面等离子共振、PAS 突变体 Ellman 抑制及 ThT/TEM 聚集实验验证。

### 与高分文献的对应

Atanasova 等（2020）报道以 PAS 及 344–361 残基为中心、由氢键与桥连水稳定的 1 μs AChE–Aβ 模拟。Silman 与 Sussman（2005）将 PAS 描述为静电门控。Inestrosa 等（Neuron, 1996; Molecular Neurobiology, 2008）确立 PAS 依赖的伴侣加速 Aβ 纤维化。Dominy 等（Science Advances, 2019）在 AD 脑内检测到 *P. gingivalis* 与牙龈蛋白酶。胆碱能假说（Bartus et al., 1982; Hampel et al., 2018）与淀粉样级联假说（Selkoe & Hardy, 2016）在此仅作为工作模型交汇：PAS 对接原则上既可封堵峡部，也可重塑促聚集表面。

### 局限性

各体系目前为单条 100 ns 轨迹，短于 1,000 ns 基准。对接打分为经验指标；PDBQT 档案未沉积；FLLHTTR 的 SD 达 1.41 kcal/mol，说明最优构象可能高估运行平均亲和力。计划验证包括等温滴定量热、表面等离子共振、Ellman IC50 以及 ThT/TEM 纤维实验。

### 参考文献

1. Atanasova, M., Dimitrov, I., & Ivanov, S. (2020). Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. *Cybernetics and Information Technologies*, 20(6), 140–154. https://doi.org/10.2478/cait-2020-0068
2. Dominy, S. S., Lynch, C., Ermini, F., Benedyk, M., Marczyk, A., Forbes, A., Haditsch, M., et al. (2019). *Porphyromonas gingivalis* in Alzheimer's disease brains: Evidence for disease causation and treatment with small-molecule inhibitors. *Science Advances*, 5(1), eaau3333. https://doi.org/10.1126/sciadv.aau3333
3. Silman, I., & Sussman, J. L. (2005). Acetylcholinesterase: ‘classical’ and ‘non-classical’ functions and pharmacology. *Current Opinion in Pharmacology*, 5(3), 293–302. https://doi.org/10.1016/j.coph.2005.01.014
4. Inestrosa, N. C., Alvarez, A., Pérez, C. A., Moreno, R. D., Vicente, M., Link, C. A., Dayoub, O. I., et al. (1996). Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. *Neuron*, 16(4), 881–891. https://doi.org/10.1016/S0896-6273(00)80108-7
5. Inestrosa, N. C., Dinamarca, M. C., & Alvarez, A. (2008). Amyloid-cholinesterase interactions. Implications for Alzheimer's disease. *Molecular Neurobiology*, 38(3), 262–273. https://doi.org/10.1007/s12035-008-8043-6
6. Hampel, H., Mesulam, M. M., Cuello, A. C., Farlow, M. R., Giacobini, E., Grossberg, G. T., Khachaturian, A. S., et al. (2018). The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. *Brain*, 141(7), 1917–1933. https://doi.org/10.1093/brain/awy132
7. Bartus, R. T., Dean, R. L., Beer, B., & Lippa, A. S. (1982). The cholinergic hypothesis of geriatric memory dysfunction. *Science*, 217(4558), 408–414. https://doi.org/10.1126/science.7046051
8. Selkoe, D. J., & Hardy, J. (2016). The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Molecular Medicine*, 8(6), 595–608. https://doi.org/10.15252/emmm.201606210
