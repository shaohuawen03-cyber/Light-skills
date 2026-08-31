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

与 Atanasova 等对 AChE–Aβ 复合物的判断相同：酶本身保持稳定，肽在表面驻留而不是解离。复合物 RMSD 均低于 0.22 nm，属于亚纳米局部适应，不是解折叠。YLSLLQR 是唯一 SASA 相对 apo 收缩的复合物（图6C），氢键也最密（4.23 ± 1.24）。各图 E 面板中螺旋（约 33–34%）与折叠（约 17%）与 apo 重叠。三个复合物均保留 7 对持续性接触，F 面板氢键在 100 ns 内不中断。

### 证据边界

**表3. 图件与表格所支持及不支持的解释。**

| 序号 | 支持 | 不支持 |
| --- | --- | --- |
| 1 | FLLHTTR、YLSLLQR、LLHPLRL最优构象接触PAS残基 | Vina打分不是实验Kd或Ki |
| 2 | 100 ns复合物保持折叠（RMSD < 0.22 nm；DSSP守恒） | RMSD微增不是解折叠 |
| 3 | 后20 ns氢键2.19–4.23个在F面板持续 | 单条100 ns轨迹不是不可逆结合 |
| 4 | FLLHTTR最优-9.60 kcal/mol而均值为-8.77 ± 1.41 kcal/mol | 最优构象不是收敛亲和力 |

## 讨论

文献中能够直接称为致病肽的，首先是 β-淀粉样肽（Aβ）本身。Selkoe 与 Hardy 综述的淀粉样级联指出：APP 经 β/γ 分泌酶切出 Aβ40/Aβ42，可溶寡聚体损伤突触，斑块为病理终点；家族性 AD 的 APP、PSEN 突变改变 Aβ 产量与长度，构成 Aβ 参与 AD 的遗传主证据。单凭一篇 AChE–Aβ 模拟不足以承担这一层。

第二层是实验：AChE 如何帮 Aβ 致病。Inestrosa 等证明 AChE 经外周阴离子位点（PAS）加速 Aβ 成纤，AChE–Aβ 复合物比游离 Aβ 更具神经毒性。De Ferrari 等进一步定位 PAS 附近疏水基序，合成肽即可模拟全酶的促纤效应。Silman 与 Sussman 指出同一 PAS 还是 20 Å 活性峡部的静电门控，因此占位可同时打击催化与伴侣两种功能。

第三层才是动力学。Lushchekina 等对人 AChE 与多条 Aβ 做加速 MD，显示 Aβ 被酶表面强烈吸引并形成稳定复合物，提出 AChE 为聚集成核中心。Atanasova 等将单条 Aβ 对接到 PAS 并运行 1 μs：复合物保持稳定，主驻留区为毗邻 PAS 的 344–361，结合靠氢键、芳香接触和疏水作用，酶骨架不解折叠。下列四步完全由本次对接构象与 100 ns 轨迹推出，是把牙周炎微肽放到上述 Aβ–AChE 病理链上的计算类比，而不是把这三条肽写成已被实验证实的 AD 致病肽。

1. PAS 识别与峡部入口占位。  
   12 条微肽的最优构象富集于人源 AChE（PDB 4EY6）的 PAS 与峡部入口（图1–3，图S1）。FLLHTTR 锚定 Asp74、Tyr72、His287（最优 −9.60 kcal/mol，图2C）；YLSLLQR 同时接触 PAS（Tyr72、Thr75）与催化入口（Ser203、Glu202；三次均值 −9.44 ± 0.09 kcal/mol，图3L）；LLHPLRL 从门控残基 Trp286/Tyr341 跨越至催化 His447（10 个氢键，图3I）；HLLTLKKHV 触及 Tyr72 与 344–361 区的 Phe346。这与 Atanasova 将 Aβ 放置于 PAS、并在 344–361 发现主驻留区的几何逻辑一致：外源短肽同样可以成为 PAS 成核面上的配体。

2. 复合物稳定、酶不崩解、肽不脱落。  
   图4–6 的 apo 对照与三条复合物表明，AChE 在 100 ns 内保持球状折叠：骨架 RMSD < 0.22 nm，Rg 2.29–2.32 nm，α-螺旋约 33–34%、β-折叠约 17% 与 apo 重叠（E 面板）。复合物曲线略高于 apo，对应肽结合后 PAS 邻近环区的局部适应，而不是变性。F 面板氢键持续存在（后 20 ns：ALLLHRC 2.19 ± 0.80，FLLHTTR 2.80 ± 0.99，YLSLLQR 4.23 ± 1.24），各体系保留 7 对界面接触。计算意义上，肽处于 AChE 表面的结合态，具备作为病理性伴侣配体的驻留条件。

3. 胆碱能传递受损。  
   PAS 位于催化三联体上方约 20 Å 的峡部入口。轨迹中 RMSF 升幅集中于表面环区（B 面板），与门控呼吸被配体占用相符。物理占位可阻碍乙酰胆碱进入峡部并扰动门控，从而在计算模型中同时打击 AChE 的经典催化功能。这把 Bartus、Hampel 所述的胆碱能缺损，落到 PAS 被微肽占据这一具体结构事件上。

4. 病理性伴侣与淀粉样共成核。  
   Inestrosa、De Ferrari 的实验把 PAS 定为促纤位点；Lushchekina 的加速 MD 与 Atanasova 的 1 μs 轨迹把该过程落实为肽在 PAS/344–361 多模式驻留、氢键维持界面、酶作为支架降低成核能垒。本次三条复合物给出同一类计算图景——稳定界面、持续极性网络、入口环区微扰、YLSLLQR 的 SASA 收缩（图6C）显示更紧密的界面埋藏。牙周炎微肽因此可作为异源“种子”改变 PAS 静电/疏水微环境，促进内源 Aβ 在同一表面上共成核；AChE–微肽–Aβ 三元组装在该模型中同时携带胆碱能阻断和增强的淀粉样毒性。Dominy 等在 AD 脑内检出 *Porphyromonas gingivalis*，为口腔来源配体进入中枢 PAS 提供病理背景。

上述四步是对接与单条 100 ns 轨迹内的分子事件，不是实验结合常数，也不把 Vina 打分当作 Kd。FLLHTTR 最优构象（−9.60 kcal/mol）相对三次均值（−8.77 ± 1.41 kcal/mol）偏强，机制讨论以 PAS 几何与动力学驻留为主，不以单一最优打分排序致病性。

### 参考文献

1. Atanasova, M., Dimitrov, I., & Ivanov, S. (2020). Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. *Cybernetics and Information Technologies*, 20(6), 140–154. https://doi.org/10.2478/cait-2020-0068
2. Dominy, S. S., Lynch, C., Ermini, F., Benedyk, M., Marczyk, A., Forbes, A., Haditsch, M., et al. (2019). *Porphyromonas gingivalis* in Alzheimer's disease brains: Evidence for disease causation and treatment with small-molecule inhibitors. *Science Advances*, 5(1), eaau3333. https://doi.org/10.1126/sciadv.aau3333
3. Silman, I., & Sussman, J. L. (2005). Acetylcholinesterase: ‘classical’ and ‘non-classical’ functions and pharmacology. *Current Opinion in Pharmacology*, 5(3), 293–302. https://doi.org/10.1016/j.coph.2005.01.014
4. Inestrosa, N. C., Alvarez, A., Pérez, C. A., Moreno, R. D., Vicente, M., Link, C. A., Dayoub, O. I., et al. (1996). Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. *Neuron*, 16(4), 881–891. https://doi.org/10.1016/S0896-6273(00)80108-7
5. Inestrosa, N. C., Dinamarca, M. C., & Alvarez, A. (2008). Amyloid-cholinesterase interactions. Implications for Alzheimer's disease. *Molecular Neurobiology*, 38(3), 262–273. https://doi.org/10.1007/s12035-008-8043-6
6. Hampel, H., Mesulam, M. M., Cuello, A. C., Farlow, M. R., Giacobini, E., Grossberg, G. T., Khachaturian, A. S., et al. (2018). The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. *Brain*, 141(7), 1917–1933. https://doi.org/10.1093/brain/awy132
7. Bartus, R. T., Dean, R. L., Beer, B., & Lippa, A. S. (1982). The cholinergic hypothesis of geriatric memory dysfunction. *Science*, 217(4558), 408–414. https://doi.org/10.1126/science.7046051
