# 牙周炎来源微肽占据乙酰胆碱酯酶外周阴离子位点：计算筛选、分子对接与100 ns分子动力学

## 摘要

牙周炎相关口腔菌群失调已与阿尔茨海默病（AD）相关联，但从口腔微生物组到特定突触酶的肽水平通路仍不完整。本研究为纯计算工作，将口腔小开放阅读框（smORF）筛选级联，与12条7–9 aa候选微肽对人源乙酰胆碱酯酶（AChE，PDB 4EY6）的本地 AutoDock Vina 对接，以及 apo AChE 与三种复合物（ALLLHRC、FLLHTTR、YLSLLQR）的 100 ns 全原子分子动力学（MD）衔接。序列/蛋白质组过滤从 11,721,988 条牙周炎标记 smORF 中保留 33,786 条候选；其中 3,518 条为血脑屏障（BBB）高分，923 条为 NTxPred2 阳性，后续过滤得到 12 条序列集。本地三次 Vina 最优打分介于 -8.25 至 -9.60 kcal/mol，三次均值介于 -8.07 ± 0.16 至 -9.44 ± 0.09 kcal/mol。FLLHTTR 最优构象最强但运行间 SD 最大；YLSLLQR 三次均值最强，并与 FLLHTTR、LLHPLRL 接触外周阴离子位点（PAS）。100 ns 内三种复合物保持球状折叠（骨架 RMSD < 0.22 nm；α-螺旋约 33–34%，β-折叠约 17%），分子间氢键持续（后 20 ns 为 2.19–4.23 个），仅 YLSLLQR 出现 SASA 收缩。上述构象与轨迹是把牙周炎微肽映射到实验确立的 AChE–淀粉样蛋白β（Aβ）PAS 伴侣通路上的计算类比，不是已测亲和力，也不能证明 AD 因果。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微肽；smORF；乙酰胆碱酯酶；外周阴离子位点；分子对接；分子动力学

## 引言

阿尔茨海默病是进行性神经退行性疾病，淀粉样蛋白β（Aβ）、tau、突触衰竭、免疫激活与血管损伤相互作用，而不是单一线性级联[@scheltens2021alzheimer]。淀粉样生物学仍居核心：APP 经 β/γ 分泌酶切出 Aβ40/Aβ42，可溶寡聚体损伤突触，家族性 APP/PSEN 突变改变 Aβ 产量与长度[@selkoe2016amyloid]。基底前脑胆碱能传递丧失参与认知症状，AChE 抑制剂仍是既定对症治疗[@hampel2018cholinergic]。独立于催化功能，AChE 经外周阴离子位点（PAS）加速 Aβ 成纤，AChE–Aβ 复合物比游离 Aβ 更具神经毒性[@inestrosa1996ache]。PAS 疏水基序促进该伴侣活性[@deferrari2001motif]。这些事实使 AChE 成为有生物学依据的结构靶点，但并不使每一个获得计算评分的配体都成为 AD 致病因子。

慢性牙周炎可维持系统性炎症负担和微生物产物的间歇暴露，由此推动口腔—脑轴研究[@chalmers2025primer]。疾病相关口腔活动具有物种和位点特异性，分类学丰度不能替代分子中介[@belstrom2021periodontitis]。牙龈卟啉单胞菌（*Porphyromonas gingivalis*）的牙龈蛋白酶与外膜囊泡提供了较充分的毒力背景[@guo2010gingipain; @ho2015omv]。观察性综合报告牙周病与认知障碍相关，效应估计随病例定义和校正而变化[@larvin2023periodontalcognition]；AD 队列中牙周炎与后续认知下降相关[@ide2016periodontitis]。AD 脑内曾检出 *P. gingivalis* 与牙龈蛋白酶[@dominy2019pgingivalis]，小鼠反复口腔暴露可驱动神经炎症和 Aβ 相关改变[@ilievski2018oral]。孟德尔随机化尚未确立牙周病对 AD 的遗传因果效应[@hu2024mendelian]。人体关联、实验合理性与遗传证据回答的是不同问题。

微生物组编码的小蛋白构成规模庞大、映射仍不充分的候选空间[@sberro2019smallgenes; @durrant2021sorf]。牙周炎来源的 7–9 aa 微肽能否占据与 Aβ 相同的 AChE PAS，是筛选分数本身无法回答的结构问题。对人 AChE 与多条 Aβ 的加速 MD 显示 Aβ 被酶表面吸引，支持 AChE 作为成核中心[@lushchekina2017amd]。以 PAS 为中心的 1 μs AChE–Aβ 轨迹保持结合，主驻留区为毗邻 PAS 的 344–361[@atanasova2020md]。PAS 导向配体可在生化体系中抑制 AChE 诱导的 Aβ 聚集[@bartolini2003pas]，PDB 4EY6 提供 2.40 Å 人源 AChE 结构用于对接[@cheung2012ache]。

因此，本文将此前分开的两层计算工作合并。其一，重建口腔 smORF 级联，说明 12 条 7–9 aa 序列如何被优先保留；其二，在本地将这 12 条肽对接入人源 AChE，并对三条代表性复合物相对 apo 对照完成 100 ns 模拟。目标是形成一篇边界清楚的原创研究叙述：筛选漏斗加上已完成的对接与 MD，作为把牙周炎微肽放到 AChE–Aβ PAS 通路上的计算类比。

## 材料与方法

### 研究设计

本研究为纯计算分析。筛选层是对汇总 smORF 计数、模型汇总和一张 12 条序列表的二次重建；未开展参与者招募、标本采集、预测器再训练或新组学处理。健康与牙周炎标签仅作为分支标签保留，不视为已经核实的肽层面疾病归属。对接与 MD 层使用本地三次 AutoDock Vina 构象和已完成的 100 ns GROMACS 轨迹，不沿用筛选稿中较旧的对接评分表。

### 口腔 smORF 筛选级联

编码 4–50 aa 肽的翻译 smORF 构成起始库（健康标记 11,269,961 条，牙周炎标记 11,721,988 条）。候选与指定口腔基因组和宏蛋白质组资源精确匹配，包括 HOMD[@chen2010homd] 和唾液宏蛋白质组目录[@belstrom2016metaproteomics]，随后去冗余。精确匹配支持序列存在或曾被观察，不能证明分析分支中的表达。来源口腔宏基因组/宏转录组项目的公共登录号背景为 PRJNA678453[@belstrom2021periodontitis]。

UniDL4BioPep 提供第一层功能筛选：ESM-2（`esm2_t6_8M_UR50D`）嵌入后接任务特异性卷积网络，输出阈值 ≥0.80，包括操作性“BBB 高分”标签[@du2023unidl4biopep]。牙周炎标记 BBB 高分且长度 7–50 aa 的肽用 NTxPred2（ESM2-t30 神经毒性模型）评价[@rathore2025ntxpred2]。Mebipred 以两级神经网络评估 Cu、Fe、Zn 相关结合潜力，阈值 0.50[@aptekmann2022mebipred]。AnOxPePred 提供多任务自由基清除（FRS）和螯合（CHEL）输出[@olsen2020anoxpepred]；串联终点为 CHEL≥0.25、CHEL≥0.25 且 FRS<0.50、以及 CHEL≥0.25 且 FRS<0.45。模型串联一致仅作为计算分诊，不是独立生物学确证。

另一张表列出 12 条互不重复的 7–9 aa 序列。长度以及组氨酸、半胱氨酸和碱性残基计数均由各字符串重新计算。因缺少稳定标识符，该清单与汇总 CHEL/FRS 终点的对应关系无法在行层面证明。

### 分子对接

人源重组 AChE（rhAChE，PDB 4EY6，2.40 Å）[@cheung2012ache] 经去除加兰他敏与结晶水、修复内部链断裂并按生理 pH 7.4 分配质子化状态后用作受体。12 条微肽 ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC、HVLLLRQCA、LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR 和 YLSLLQR 采用 AutoDock Vina（exhaustiveness = 32）[@trott2010vina; @eberhardt2021vina] 对接到以 PAS（Tyr72、Asp74、Thr75、Leu76、Trp286、His287、Tyr341）为中心、并覆盖峡部颈部（Phe295）、胆碱结合亚位点（Trp86、Glu202、Tyr337）及催化三联体（Ser203、His447、Glu334）的网格。每条配体独立运行三次（`N_Success` = 3）。最优单次打分、三次运行均值±SD、氢键几何与 PAS 接触取自本地三次运行汇总表及各配体打分最高的单一构象。逐条 PDBQT 文件与配置日志未归档。Vina 打分为经验排序指标，不能等同于实验结合自由能。

### 分子动力学

四个显式溶剂体系在 GROMACS[@abraham2015gromacs] 中以 Amber99SB-ILDN[@lindorfflarsen2010amber] 力场和 TIP3P 水、0.15 M NaCl 进行模拟：apo AChE（单一 A 链）以及 AChE–ALLLHRC、AChE–FLLHTTR、AChE–YLSLLQR 复合物。各体系置于溶质至边界缓冲 1.0 nm 的三斜盒子。平衡包括 2,000 步最速下降能量最小化、1.0 ns 受限 NVT 升温至 300 K、1.0 ns 受限 NPT 密度平衡和 1.0 ns 无约束 NPT 预平衡。产物模拟在 NPT 系综（300 K，1.0 bar）运行 100 ns（dt = 2.0 fs），采用 LINCS、1.2 nm 截断和粒子网格Ewald 静电。轨迹每 20 ps 输出一帧。

与图4–6对应的轨迹指标包括骨架 Cα RMSD、逐残基 RMSF、溶剂可及表面积（SASA）、回转半径（Rg）、DSSP 占有率和分子间氢键（`gmx hbond`；供体–受体距离 ≤ 3.0 Å）。另记录微肽自拟合 RMSD 与持续性界面接触（7.0 Å 截断）。稳态值为最后 20 ns（80.0–100.0 ns）的均值±SD。方案沿用 Atanasova 等 AChE–Aβ MD 的逻辑，窗口为 100 ns 而非 1 μs[@atanasova2020md]。

## 结果

### 筛选漏斗与12条序列组成

序列证据过滤保留健康标记候选 31,510/11,269,961（0.2796%）和牙周炎标记候选 33,786/11,721,988（0.2882%）。牙周炎标记分支中，短肽 3,446 条、长肽 72 条为 BBB 高分（合计 3,518）。NTxPred2 评价 3,299/3,518（93.77%），其中 923/3,299（27.98%）为模型阳性；219 条超出 7–50 aa 覆盖窗口。后续汇总过滤依次保留 mebipred 阳性 111 条、CHEL≥0.25 者 15 条、CHEL≥0.25 且 FRS<0.50 者 12 条、CHEL≥0.25 且 FRS<0.45 者 8 条（表1）。UniDL4BioPep 抗菌输出近饱和（牙周炎标记短肽中 99.90% 超过 0.80），表明同一阈值在不同任务上校准并不等同。

**表1. 口腔smORF汇总优选计数。**

| 阶段 | 操作规则 | n | 分母或限制 |
| --- | --- | ---: | --- |
| 健康标记 smORF | 4–50 aa | 11,269,961 | 起始库 |
| 牙周炎标记 smORF | 4–50 aa | 11,721,988 | 起始库 |
| 证据过滤后健康标记 | 精确匹配并去冗余 | 31,510 | 11,269,961 |
| 证据过滤后牙周炎标记 | 精确匹配并去冗余 | 33,786 | 11,721,988 |
| BBB 高分短肽 | UniDL4BioPep 输出≥0.80；5–30 aa | 3,446 | 32,754 |
| BBB 高分长肽 | UniDL4BioPep 输出≥0.80；31–50 aa | 72 | 1,032 |
| BBB 高分合计 | 短肽 + 长肽 | 3,518 | 算术加和 |
| NTxPred2 已评价 | 7–50 aa | 3,299 | 3,518 |
| NTxPred2 阳性 | 模型阳性标签 | 923 | 3,299 |
| 金属结合阳性 | Mebipred 输出≥0.50 | 111 | 行层面交接不可用 |
| CHEL 优先 | CHEL≥0.25 | 15 | 111 |
| 主集 | CHEL≥0.25 且 FRS<0.50 | 12 | 111 |
| 更严子集 | CHEL≥0.25 且 FRS<0.45 | 8 | 序列归属不可用 |

12 条明示序列均为标准氨基酸组成的互不重复 7–9 aa 肽（表2）。11 条含组氨酸，6 条含半胱氨酸，每条至少含 1 个 Arg 或 Lys。组成仅提供合成与金属配位假说，不能确立分类学、翻译、BBB 转运，或与汇总 12 条终点的同一性。923 条 NTxPred2 阳性肽均 ≤30 aa，因此 72 条 BBB 高分长肽均未进入下游金属/CHEL/FRS 过滤。

**表2. 12条7–9 aa候选微肽的序列组成。**

| 序号 | 序列 | 长度 | His | Cys | Arg+Lys |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | ALLLHRC | 7 | 1 | 1 | 1 |
| 2 | FCLHLQLR | 8 | 1 | 1 | 1 |
| 3 | FLLHTTR | 7 | 1 | 0 | 1 |
| 4 | HLLTLKKHV | 9 | 2 | 0 | 2 |
| 5 | HLPLLHRCC | 9 | 1 | 2 | 1 |
| 6 | HVLLLRQCA | 9 | 1 | 1 | 1 |
| 7 | LLHLPKRTT | 9 | 1 | 0 | 2 |
| 8 | LLHPLRC | 7 | 1 | 1 | 1 |
| 9 | LLHPLRL | 7 | 1 | 0 | 1 |
| 10 | WLLVHLKK | 8 | 1 | 0 | 2 |
| 11 | YHHLLCRR | 8 | 2 | 1 | 2 |
| 12 | YLSLLQR | 7 | 0 | 0 | 1 |

### 本地三次对接与PAS结合

12 条配体的本地 Vina 打分均有利。最优单次打分介于 -8.25 至 -9.60 kcal/mol，三次运行均值介于 -8.07 ± 0.16 至 -9.44 ± 0.09 kcal/mol（表3，图1）。按最优构象排序，FLLHTTR 居首（-9.60 kcal/mol），随后为 YLSLLQR（-9.49 kcal/mol）和 ALLLHRC（-9.29 kcal/mol）。按三次运行均值排序，则 YLSLLQR 居首（-9.44 ± 0.09 kcal/mol），ALLLHRC 次之（-9.18 ± 0.11 kcal/mol）。FLLHTTR 保留最强单次构象，但三次运行 SD 最大（-8.77 ± 1.41 kcal/mol）。各最优构象形成 3–10 个氢键（平均键长 2.83–3.28 Å；图2、图3；图S1）。

**表3. 12条候选微肽对人源AChE（PDB 4EY6）的本地AutoDock Vina打分与PAS结合。**

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

![图1. 12条候选微肽对人源AChE的本地AutoDock Vina对接打分。](../figures/fig5_docking_scores.png)

**图1. 12条候选微肽对人源AChE（PDB 4EY6）的本地AutoDock Vina对接打分。** 蓝色圆点为三次运行均值，误差棒为标准差，橙色菱形为最优单次打分。横轴顺序与最优单次打分排序一致。Vina打分为经验排序指标，不能等同于实验结合自由能。

![图2. ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC和HVLLLRQCA的最优对接构象。](../figures/fig_docking_poses_A_F.png)

**图2. ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC和HVLLLRQCA的最优对接构象（A–F）。** 微肽为橙色，接触残基为青色，氢键以虚线标示。FLLHTTR（C面板）为最密集的PAS构象。

![图3. LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR和YLSLLQR的最优对接构象。](../figures/fig_docking_poses_G_L.png)

**图3. LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR和YLSLLQR的最优对接构象（G–L）。** LLHPLRL（I面板）从PAS的Trp286/Tyr341跨越至催化His447；YLSLLQR（L面板）桥接PAS与催化入口。

![图S1. 12条微肽最优对接构象总览。](../figures/fig_docking_poses_12_combined.png)

**图S1. 12条微肽最优对接构象总览。** 单页汇总A–L面板。

最优构象中直接对接经典 PAS 的配体为 FLLHTTR（图2C）、YLSLLQR（图3L）、FCLHLQLR、HVLLLRQCA、HLLTLKKHV 和 LLHPLRL（图3I）。ALLLHRC 结合催化 Ser203，平均氢键最短（2.83 Å），而非外侧 PAS 芳香核心（图2A）。三次运行均值将可重复的高亲和力配体（YLSLLQR、ALLLHRC、LLHPLRL）与最优构象强于运行均值的配体（FLLHTTR、FCLHLQLR、YHHLLCRR）区分开来。

### apo AChE与三种复合物的100 ns分子动力学

对 apo AChE 以及 ALLLHRC、FLLHTTR、YLSLLQR 复合物完成产物轨迹（表4，图4–6）。每幅六面板图比较无配体对照与一条肽复合物：骨架 RMSD（A）、逐残基 RMSF（B）、SASA（C）、Rg（D）、最后 20 ns 的 DSSP 占有率（E）和分子间氢键（F）。

<!-- PAGEBREAK -->

![图4. apo AChE与AChE–ALLLHRC 100 ns对比。](../figures/fig_compare_ache_vs_alllhrc.png)

**图4. apo AChE与AChE–ALLLHRC 100 ns分子动力学对比。** A–F面板与表4指标对应。

![图5. apo AChE与AChE–FLLHTTR 100 ns对比。](../figures/fig_compare_ache_vs_fllhttr.png)

**图5. apo AChE与AChE–FLLHTTR 100 ns分子动力学对比。** 面板布局与图4相同。复合物RMSD（A）与Rg（D）在三条肽中升幅最大。

![图6. apo AChE与AChE–YLSLLQR 100 ns对比。](../figures/fig_compare_ache_vs_ylsllqr.png)

**图6. apo AChE与AChE–YLSLLQR 100 ns分子动力学对比。** 面板布局与图4相同。SASA（C）相对apo收缩；氢键计数（F）在三条复合物中最密。

**表4. apo AChE与三种肽复合物最后20 ns轨迹指标（均值±SD），与图4–6对齐。**

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

**表5. 分子对接与100 ns动力学结果的支持与不支持解释。**

| 序号 | 观察 | 支持的解释 | 不支持的外推 |
| --- | --- | --- | --- |
| 1 | FLLHTTR、YLSLLQR、LLHPLRL最优构象接触PAS残基 | 对PAS及峡部入口具有几何互补 | Vina打分不能等同实验Kd或Ki |
| 2 | 复合物RMSD为0.16–0.21 nm且DSSP守恒 | 局部环区适应而非解折叠 | RMSD微增不是变性或解离 |
| 3 | 后20 ns氢键2.19–4.23个且各有7对接触 | 100 ns尺度的表面驻留 | 单条轨迹不能证明不可逆纳摩尔结合 |
| 4 | YLSLLQR的SASA收缩与最密氢键面板 | 相对apo的紧密界面埋藏 | 不能直接等同宏观结合常数 |
| 5 | FLLHTTR最优-9.60 kcal/mol而均值为-8.77 ± 1.41 kcal/mol | 最优构象为高分离群；均值排序更支持YLSLLQR | 单一最优构象不是收敛亲和力 |

## 讨论

### 主要发现

筛选级联把数百万条 smORF 空间收束为可操作的 12 条序列集，本地对接与 100 ns MD 则把这些肽放到人源 AChE 上。科学贡献不是验证牙周—AD 机制，而是一条有边界的计算链：操作性候选清单、残基水平 PAS 构象，以及在 100 ns 窗口内保持表面结合的三种折叠复合物。

微生物组肽挖掘可以有效缩小序列空间，但生物学主张需要合成与受控实验[@torres2024peptideantibiotics]。本文漏斗仍是汇总层面。缺少行级标识符，因此不能把任何序列归属于 *P. gingivalis*、某个样本或 CHEL/FRS 的 12 条终点。健康标记与牙周炎标记相近的保留率也不能解读为疾病富集。

### 映射到AChE–Aβ PAS通路的四步计算机制

四篇文献界定了构象与轨迹所映射的通路。Selkoe 与 Hardy 综述 Aβ 与 AD[@selkoe2016amyloid]。Inestrosa 等用实验证明 AChE 经 PAS 加速 Aβ 成纤，AChE–Aβ 复合物比游离 Aβ 更具神经毒性[@inestrosa1996ache]。Lushchekina 等对人 AChE 与多条 Aβ 做加速 MD，显示 Aβ 被酶表面吸引并形成稳定复合物，提出 AChE 为聚集成核中心[@lushchekina2017amd]。Atanasova 等将单条 Aβ 对接到 PAS 并运行 1 μs，复合物保持稳定，主驻留区为毗邻 PAS 的 344–361[@atanasova2020md]。下列四步仅由本次对接与 100 ns 轨迹推出，是把牙周炎微肽放到这条 Aβ–AChE 链上的计算类比。

1. PAS 识别与峡部入口占位。  
   12 条微肽的最优构象富集于人源 AChE（PDB 4EY6）的 PAS 与峡部入口（图1–3，图S1）。FLLHTTR 锚定 Asp74、Tyr72、His287（最优 -9.60 kcal/mol，图2C）；YLSLLQR 同时接触 PAS（Tyr72、Thr75）与催化入口（三次均值 -9.44 ± 0.09 kcal/mol，图3L）；LLHPLRL 从 Trp286/Tyr341 跨越至 His447（图3I）；HLLTLKKHV 触及 Tyr72 与 344–361 的 Phe346。几何上与 Atanasova 将 Aβ 置于 PAS、主驻留 344–361 一致。

2. 复合物稳定、酶不崩解、肽不脱落。  
   图4–6 显示 100 ns 内 AChE 保持球状折叠：RMSD < 0.22 nm，Rg 2.29–2.32 nm，α-螺旋约 33–34%、β-折叠约 17% 与 apo 重叠。复合物曲线略高于 apo，是 PAS 邻近环区适应，不是变性。后 20 ns 氢键持续（ALLLHRC 2.19 ± 0.80，FLLHTTR 2.80 ± 0.99，YLSLLQR 4.23 ± 1.24），各体系 7 对接触。这与 Lushchekina、Atanasova 的“复合物稳定、肽不进入本体溶剂”一致。

3. 胆碱能传递受损。  
   PAS 位于催化三联体上方约 20 Å 的峡部入口[@hampel2018cholinergic]。RMSF 升幅集中于表面环区（B 面板）。物理占位可阻碍乙酰胆碱进入并扰动门控，在计算模型中同时打击 AChE 的催化功能。

4. 病理性伴侣与淀粉样共成核。  
   Inestrosa 把 PAS 定为促纤位点；Lushchekina 与 Atanasova 把该过程落实为肽在 PAS/344–361 驻留、氢键维持界面、酶作为成核支架。本次三条复合物给出同一类计算图景：稳定界面、持续极性网络、入口环区微扰，以及 YLSLLQR 的 SASA 收缩（图6C）。牙周炎微肽因此可作为异源种子，促进内源 Aβ 在同一 PAS 表面上共成核。

上述步骤是对接与单条 100 ns 轨迹内的分子事件，不是实验结合常数，也不把 Vina 打分当作 Kd。AD 脑内检出 *P. gingivalis*[@dominy2019pgingivalis] 为提出这一结构问题提供流行病学背景，但不能把菌种层面证据转移到缺少来源链的群落肽上。

### 局限性

各 MD 体系目前为单条 100 ns 轨迹，短于 1,000 ns 的 AChE–Aβ 基准[@atanasova2020md]。对接打分为经验指标；PDBQT 档案未沉积；FLLHTTR 的 SD 达 1.41 kcal/mol，说明最优构象可能高估运行平均亲和力。筛选层缺少候选核苷酸行、基因组坐标、样本映射、分类学归属和完整预测器输出，因此不能证明 12 条明示序列等同于汇总终点的 12。BBB 高分、神经毒性阳性和 CHEL/FRS 都是操作性模型标签，不等于转运、神经元损伤或金属配位测量。这些肽是映射到 Aβ–AChE 通路上的计算类比，不是已证实的 AD 致病因子。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
4. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
5. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
6. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
7. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
8. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
9. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
10. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
11. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
12. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
13. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
14. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
15. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
16. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
17. Lushchekina SV, Kots ED, Novichkova DA, Petrov KA, Masson P. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7(2):396–402. doi:10.1007/s12668-016-0375-x.
18. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
19. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
20. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
21. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
22. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
23. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
24. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
25. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
26. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
27. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
28. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
29. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
30. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
31. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
