# 牙周炎口腔微肽的深度学习筛选、分子对接与对人源乙酰胆碱酯酶的分子动力学

## 摘要

牙周炎与阿尔茨海默病（AD）在临床和实验中有关联，但仍缺少能够作用于突触酶的肽水平配体。用 EMBOSS getorf 从 PRJNA678453 宏基因组组装基因组预测小开放阅读框（sORF；健康 24 例、牙周炎 26 例），再用 UniDL4BioPep 打分。12 条 7–9 残基肽对接到人源乙酰胆碱酯酶（AChE）。apo AChE 与三种复合物随后做 100 ns 分子动力学（MD）。健康标记库 11,269,961 条与牙周炎标记库 11,721,988 条均按 ≥0.80 跑完 22 个分类头。随后仅对牙周炎分支与口腔基因组、宏蛋白质组目录做精确匹配。血脑屏障肽头阳性在健康库为 1,095,861 条（9.72%），在牙周炎库为 1,125,832 条（9.60%）。与 33,786 条目录支持的独特肽取交集得 3,518 条；经 NTxPred2、mebipred 与 AnOxPePred 收至 12 条明示序列。12 条均为 7–9 残基、pH 7.4 带净正电荷且富亮氨酸。本地 AutoDock Vina（三次）最优构象介于 −8.25 至 −9.60 kcal/mol。FLLHTTR、YLSLLQR 与 LLHPLRL 接触外周阴离子位点（PAS）。100 ns 内 FLLHTTR 与 YLSLLQR 复合物比 apo 更紧凑（骨架 RMSD 0.1640、0.1625 nm，相对 apo 0.1897 nm）。FLLHTTR 氢键网最密（7.03 ± 1.28）；仅 YLSLLQR 收缩溶剂可及面积。计算勾勒出口腔微肽占据促 Aβ 成纤同一 PAS 的可能路径。

**关键词：** 阿尔茨海默病；牙周炎；微肽；分子对接；分子动力学

## 引言

阿尔茨海默病（AD）在漫长临床前过程中同时出现淀粉样沉积、tau 病理、突触衰竭、免疫激活和血管损伤[@scheltens2021alzheimer]。APP 经 β、γ 分泌酶依次切割，释放 Aβ40 和 Aβ42；可溶寡聚体损伤突触；家族性 APP/PSEN 突变改变肽长度和产量[@selkoe2016amyloid]。淀粉样负荷解释不了疾病的空间与临床异质性，因此外周炎症暴露被当作易感性的可能修饰因素，而不是单一充分病因。

基底前脑乙酰胆碱丢失解释相当部分认知表型，故 AChE 抑制剂仍在常规使用[@hampel2018cholinergic]。对该酶而言，催化只是一部分功能。AChE 经外周阴离子位点（PAS）加速 Aβ 成纤，AChE–Aβ 颗粒毒性高于游离肽[@inestrosa1996ache]。一段疏水 PAS 基序即足以产生这种伴侣效应[@deferrari2001motif]。PAS 导向小分子可在生化体系中阻断 AChE 诱导的聚集[@bartolini2003pas]。同一蛋白表面因而把胆碱能衰竭与淀粉样沉积连在一起。

慢性牙周炎在破损黏膜屏障维持低度炎症负荷，并使微生物产物进入血液[@chalmers2025primer]。口腔活动具物种和位点特异性，16S 丰度不能替代分子配体[@belstrom2021periodontitis]。综合分析报告牙周病与认知障碍相关，但效应随病例定义而变动[@larvin2023periodontalcognition]。AD 队列中牙周炎与后续下降相关[@ide2016periodontitis]。两样本孟德尔随机化并未支持牙周病对 AD 的遗传因果效应[@hu2024mendelian]。流行病学因此推动分子搜寻，本身并不给出配体。

牙龈卟啉单胞菌的牙龈蛋白酶与外膜囊泡是一对已定位的毒力因子[@guo2010gingipain; @ho2015omv]。AD 脑内曾检出该菌与牙龈蛋白酶[@dominy2019pgingivalis]，小鼠反复口腔感染可产生神经炎症和 Aβ 相关改变[@ilievski2018oral]。这些观察支持检查口腔产物，但并不能单独指出占据 AChE 的肽。

微生物组 smORF 编码大量尚未绘图的小蛋白[@sberro2019smallgenes; @durrant2021sorf]。人体微生物组抗菌肽挖掘先对数百万条翻译开放阅读框打分，再做实验过滤[@torres2024peptideantibiotics]。UniDL4BioPep 在 ESM-2 嵌入上提供二十余个二分类活性头[@du2023unidl4biopep]。此处沿用同一顺序：先预测，再与目录匹配。分类器分数回答不了结构问题，即 7–9 aa 牙周炎肽能否占据 Aβ 结合 PAS。

加速 MD 把 Aβ 放到 AChE 表面，并把该酶视为成核中心[@lushchekina2017amd]。1 μs、以 PAS 为中心的 AChE–Aβ 轨迹保持结合，主驻留区为残基 344–361[@atanasova2020md]。PDB 4EY6 给出 2.40 Å 人源 AChE 对接框架[@cheung2012ache]。连接催化三联体与 PAS 的芳香峡部早先在电鳗 AChE 上被定位[@kryger1999e2020]。仍缺少的是从口腔 smORF 取出、并在同一 PAS 上检验的肽水平配体。

本研究用 EMBOSS getorf 从 PRJNA678453 的 MAG 预测 sORF（健康 24 例、牙周炎 26 例），对两库做 22 项 UniDL4BioPep 打分，将牙周炎分支与口腔基因组和宏蛋白质组目录匹配，再用 NTxPred2、mebipred 和 AnOxPePred 收窄名单。12 条 7–9 aa 肽对接到人源 AChE。三个复合物与 apo 酶一起做 100 ns 模拟，跟踪肽在 PAS 上的驻留，折叠保持闭合。

## 材料与方法

### 研究设计

工作为纯计算。未新增患者、标本、测序或湿实验。健康与牙周炎标记是文库标签，不是肽水平临床诊断。对接使用本地三次 AutoDock Vina 构象。MD 使用 apo AChE 与三种肽复合物的 100 ns GROMACS 轨迹。

### 来源文库与 sORF 预测

公共来源为 PRJNA678453，即牙周炎与口腔健康供体的成对口腔宏基因组与宏转录组[@belstrom2021periodontitis]。同一 BioProject 另有派生的 MGnify 第三方组装 PRJEB65451（metaSPAdes v3.15.3），并非第二个临床队列。宏基因组组装基因组（MAG）按健康标记 24 例、牙周炎标记 26 例分入样本目录，296 个 MAG 文件经 GCA–SRR 元数据匹配。开放阅读框用 EMBOSS getorf 预测：细菌密码子表 11，起始密码子至终止密码子（`-find 0`），长度窗口 15–150 bp[@rice2000emboss]。完全相同的氨基酸串合并。各独特串在样本中的有无按存在/缺失记录，未把读段重新回贴到 MAG。打分库为健康标记 11,269,961 条、牙周炎标记 11,721,988 条 5–50 aa 肽。未新招患者；本研究完成的是 getorf 预测、22 项筛选、目录匹配、对接与 MD。

### UniDL4BioPep（22 项任务）

两库均先跑 UniDL4BioPep，顺序与微生物组抗菌肽挖掘的“先预测再过滤”一致[@torres2024peptideantibiotics; @du2023unidl4biopep]。Du 等固定 ESM-2（`esm2_t6_8M_UR50D`，6 层、800 万参数、残基态 320 维），对残基嵌入取平均，使任意长度肽落到同一向量。卷积分类器在该向量上按活性分别训练，骨架跨数据集复用，而不是为每个终点另设计网络。原文在 20 项二分类任务中有 15 项超过当时最优。本研究未再训练。打分的 22 个头为：ACE 抑制、DPP-IV 抑制、苦味、鲜味、抗菌、抗疟（备选）、抗疟（主）、群体感应、抗癌（主）、抗癌（备选）、抗 MRSA、TTCA、BBB（BBP）、抗寄生虫（APP）、NeuroPred、抗细菌、抗真菌、抗病毒、毒性、抗氧化 FRS、致敏性和细胞穿透肽（CPP）。各头截断均为 ≥0.80。“BBB 高分”只是 BBP 头上的该截断，不是实测跨细胞转运。Augur 等其他 BBB 工具的阳性集与编码不同，其发表 AUC 不能搬到这些 4–50 aa 口腔串[@gu2024bbb]。

### 目录匹配（仅牙周炎分支）

打分之后，仅将牙周炎标记序列与口腔基因组、宏蛋白质组资源精确匹配并合并为独特肽。HOMD 与 eHOMD 提供经整理的呼吸道–消化道基因组[@chen2010homd; @escapa2018ehomd]。唾液宏蛋白质组在其自身错误发现框架内记录肽[@belstrom2016metaproteomics]。其他口腔宏蛋白质组集合补充不同临床背景下的序列观察[@jiang2022oralmetaproteomics; @yuan2025osample]。匹配支持该字符串曾经被观察到，不能证明它在 PRJNA678453 样本中表达。牙周炎库得到 33,786 条目录支持的独特肽，与 1,125,832 条牙周炎 BBB（BBP）命中取交集，得到 3,518 条（5–30 aa 3,446；31–50 aa 72）。健康库停留在 22 项打分表，不去冗余。

### NTxPred2

NTxPred2 把肽模型和蛋白模型分开，因为单一神经毒素分类器不能在长度等级之间迁移[@rathore2025ntxpred2]。肽集为神经毒性与非毒性各 877 条，蛋白集各 775 条。组成/二元谱机器学习模型 AUC 为肽 0.97、蛋白 0.85。在肽集上微调 ESM2-t30 后，独立集 AUC 达 0.98（MCC 0.90）。公开服务器对 7–50 aa 用 ESM2-t30（默认概率 0.5），对 ≥51 aa 用 extra-trees。我们对 3,518 集合中 7–50 aa 成员使用肽模式（ESM2-t30）。阳性是分类器标签，不是神经元实验。

### mebipred

mebipred 只靠序列、不做比对，因而可用于短翻译片段[@aptekmann2022mebipred]。输入为 219 维序列特征：氨基酸组成、理化描述符、金属结合 5-mer 计数。第一级前馈网（两层 219 个 ReLU，dropout 0.2，RMSprop）区分是否结合金属；第二级给出 11 种离子。作者报告金属有无准确率 >80%，精确率–召回率曲线下面积 0.91。离子默认概率 0.5，提到 0.9 会提高精确率、降低召回。Cu、Fe、Zn 相关分数此处保持 0.50。输出不是实测 Kd，也不给出配位几何。

### AnOxPePred

AnOxPePred 是一维 CNN，两个头分别打自由基清除（FRS）和金属螯合（CHEL），输入为 one-hot 肽序列[@olsen2020anoxpepred]。阳性来自 BIOPEP-UWM 和抗氧化肽文献，每条标 FRS、螯合或二者。FRS 头优于 k-NN 基线；螯合头较弱，因该训练子集小。两头输出 [0, 1]。串联截断为 CHEL≥0.25，再加 FRS<0.50，再加 FRS<0.45。四个工具的一致是过滤栈，不是独立实验重复。

### 理化描述符

对 12 条互不重复的 7–9 aa 字符串重新计算长度、组氨酸、半胱氨酸、Arg+Lys、平均分子量、等电点、pH 7.4 净电荷、Kyte–Doolittle GRAVY、Ikai 脂肪族指数、疏水残基比例（A、I、L、M、F、V、W、Y）和 Boman 指数。标度只作用于氨基酸字符串，未做 HPLC 或 CD。

### 分子对接

人源重组 AChE（PDB 4EY6，2.40 Å）去除加兰他敏与结晶水，修复链断裂，并按 pH 7.4 分配质子化[@cheung2012ache]。12 条配体 ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC、HVLLLRQCA、LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR 和 YLSLLQR 用 AutoDock Vina 对接，exhaustiveness = 32[@trott2010vina; @eberhardt2021vina]。网格以 PAS（Tyr72、Asp74、Thr75、Leu76、Trp286、His287、Tyr341）为中心，覆盖峡部颈（Phe295）、胆碱亚位点（Trp86、Glu202、Tyr337）和催化三联体（Ser203、His447、Glu334）。每条配体跑三次。报告最优单次亲和力、三次均值±SD、氢键数和最优构象的 PAS 接触。Vina 分数用于排序，不是实验自由能。

### 分子动力学

四个显式溶剂体系在 GROMACS 中以 Amber99SB-ILDN 和 TIP3P、0.15 M NaCl 构建[@abraham2015gromacs; @lindorfflarsen2010amber]：apo AChE（A 链）以及 ALLLHRC、FLLHTTR、YLSLLQR 复合物。盒子为三斜，溶质至壁缓冲 1.0 nm。平衡为 2,000 步最速下降、1.0 ns 受限 NVT 升至 300 K、1.0 ns 受限 NPT 和 1.0 ns 自由 NPT。生产相 100 ns（dt = 2.0 fs），300 K、1.0 bar，LINCS、1.2 nm 截断和粒子网格 Ewald。每 20 ps 存一帧。

与图5–7对齐的指标包括 Cα RMSD、逐残基 RMSF、SASA、Rg、DSSP 占有率和分子间氢键（`gmx hbond`；供体–受体 ≤ 3.0 Å）。另记录微肽自拟合 RMSD 和持续性接触（7.0 Å）。均值±SD 取最后 20 ns（80–100 ns）。方案沿用 Atanasova 等 AChE–Aβ MD 的逻辑，窗口为 100 ns 而非 1 μs[@atanasova2020md]。

## 结果

### 两库 22 项 UniDL4BioPep 任务

图1概括筛选。两库均按 ≥0.80 跑完 22 个头（表1、表2）。命中率接近。抗菌在牙周炎库为 10,302,093/11,721,988（87.89%），健康库为 9,882,657/11,269,961（87.69%）。BBB（BBP）分别为 1,125,832（9.60%）与 1,095,861（9.72%）。抗寄生虫（APP）和群体感应次之；两库最小的都是 DPP-IV 抑制。标签可重叠。两库 BBB 率只差 0.12 个百分点，故 BBB 高分不是牙周炎特异印记。22 个头大多接近（表3）。牙周炎高于健康 ≥1 个百分点的只有群体感应（+1.39）。健康高于牙周炎 ≥1 个百分点的有抗真菌（−2.50）、抗寄生虫（−2.36）、抗氧化 FRS（−1.95）、抗病毒（−1.89）、抗细菌（−1.42）、CPP（−1.24）、抗癌主（−1.22）和鲜味（−1.00）。抗菌几乎持平（87.89% 对 87.69%）。这是全库打分率，不是序列水平差异肽：没有逐条交集表，不能说这 12 条对接序列在健康库中不存在。下游对接只用牙周炎、目录匹配后的分支。

**表1. 牙周炎标记库（11,721,988 条 smORF）的 UniDL4BioPep 计数（≥0.80）。**

| 序号 | 任务 | n | % |
| --- | --- | ---: | ---: |
| 1 | ACE 抑制 | 1,236,442 | 10.55 |
| 2 | DPP-IV 抑制 | 139,056 | 1.19 |
| 3 | 苦味 | 1,831,185 | 15.62 |
| 4 | 鲜味 | 3,100,811 | 26.45 |
| 5 | 抗菌 | 10,302,093 | 87.89 |
| 6 | 抗疟（备选） | 695,608 | 5.93 |
| 7 | 抗疟（主） | 2,010,724 | 17.15 |
| 8 | 群体感应 | 4,491,507 | 38.32 |
| 9 | 抗癌（主） | 2,357,718 | 20.11 |
| 10 | 抗癌（备选） | 2,015,652 | 17.20 |
| 11 | 抗 MRSA | 843,977 | 7.20 |
| 12 | TTCA | 2,666,759 | 22.75 |
| 13 | 血脑屏障（BBP） | 1,125,832 | 9.60 |
| 14 | 抗寄生虫（APP） | 5,462,493 | 46.60 |
| 15 | NeuroPred | 1,714,373 | 14.63 |
| 16 | 抗细菌 | 2,597,877 | 22.16 |
| 17 | 抗真菌 | 2,960,118 | 25.25 |
| 18 | 抗病毒 | 3,275,203 | 27.94 |
| 19 | 毒性 | 1,714,299 | 14.62 |
| 20 | 抗氧化 FRS | 2,521,106 | 21.51 |
| 21 | 致敏性 | 1,713,798 | 14.62 |
| 22 | 细胞穿透肽（CPP） | 925,627 | 7.90 |

**表2. 健康标记库（11,269,961 条 smORF）的 UniDL4BioPep 计数（≥0.80）。**

| 序号 | 任务 | n | % |
| --- | --- | ---: | ---: |
| 1 | ACE 抑制 | 1,237,451 | 10.98 |
| 2 | DPP-IV 抑制 | 131,426 | 1.17 |
| 3 | 苦味 | 1,840,368 | 16.33 |
| 4 | 鲜味 | 3,094,287 | 27.46 |
| 5 | 抗菌 | 9,882,657 | 87.69 |
| 6 | 抗疟（备选） | 703,632 | 6.24 |
| 7 | 抗疟（主） | 1,954,667 | 17.34 |
| 8 | 群体感应 | 4,161,825 | 36.93 |
| 9 | 抗癌（主） | 2,404,084 | 21.33 |
| 10 | 抗癌（备选） | 1,979,643 | 17.57 |
| 11 | 抗 MRSA | 769,955 | 6.83 |
| 12 | TTCA | 2,618,849 | 23.24 |
| 13 | 血脑屏障（BBP） | 1,095,861 | 9.72 |
| 14 | 抗寄生虫（APP） | 5,517,278 | 48.96 |
| 15 | NeuroPred | 1,690,436 | 15.00 |
| 16 | 抗细菌 | 2,658,234 | 23.59 |
| 17 | 抗真菌 | 3,128,057 | 27.76 |
| 18 | 抗病毒 | 3,362,295 | 29.83 |
| 19 | 毒性 | 1,725,268 | 15.31 |
| 20 | 抗氧化 FRS | 2,643,538 | 23.46 |
| 21 | 致敏性 | 1,635,019 | 14.51 |
| 22 | 细胞穿透肽（CPP） | 1,029,770 | 9.14 |

**表3. 两库打分率之差（牙周炎% − 健康%）。BBB 供对照。**

| 任务 | 健康 % | 牙周炎 % | Δ 百分点 |
| --- | ---: | ---: | ---: |
| 群体感应 | 36.93 | 38.32 | +1.39 |
| 鲜味 | 27.46 | 26.45 | −1.00 |
| 抗癌（主） | 21.33 | 20.11 | −1.22 |
| 细胞穿透肽（CPP） | 9.14 | 7.90 | −1.24 |
| 抗细菌 | 23.59 | 22.16 | −1.42 |
| 抗病毒 | 29.83 | 27.94 | −1.89 |
| 抗氧化 FRS | 23.46 | 21.51 | −1.95 |
| 抗寄生虫（APP） | 48.96 | 46.60 | −2.36 |
| 抗真菌 | 27.76 | 25.25 | −2.50 |
| 血脑屏障（BBP） | 9.72 | 9.60 | −0.12 |

![图1. 从口腔smORF文库到12条肽和3个MD复合物的筛选级联。](../figures/fig_screening_cascade.png)

**图1. 筛选级联。** 两库均先跑 UniDL4BioPep（22 项）。目录匹配与后续过滤只用于牙周炎分支，最终 12 条 7–9 aa 肽做对接，3 个复合物做 100 ns MD。

### 牙周炎漏斗至 12 条序列

牙周炎库目录匹配保留 33,786 条独特肽，与 BBB 高分交集得 3,518 条。NTxPred2 评价 3,299/3,518（93.77%），阳性 923/3,299（27.98%）。后续截断留下 mebipred 阳性 111 条、CHEL≥0.25 者 15 条、CHEL≥0.25 且 FRS<0.50 者 12 条、更严 FRS<0.45 者 8 条（表4）。923 条 NTxPred2 阳性肽均 ≤30 aa，故金属/CHEL/FRS 步骤只保留短肽。

**表4. UniDL4BioPep 打分后的牙周炎分支。**

| 阶段 | 规则 | n | 分母 |
| --- | --- | ---: | ---: |
| 牙周炎 smORF | 4–50 aa | 11,721,988 | 文库 |
| BBB（BBP） | 评分 ≥0.80 | 1,125,832 | 11,721,988 |
| 目录支持的独特肽 | 精确匹配 | 33,786 | 11,721,988 |
| BBB 高分 ∩ 目录支持 | 交集 | 3,518 | 1,125,832 ∩ 33,786 |
| 短肽（5–30 aa） | 长度 | 3,446 | 3,518 |
| 长肽（31–50 aa） | 长度 | 72 | 3,518 |
| NTxPred2 已评 | 7–50 aa | 3,299 | 3,518 |
| NTxPred2 阳性 | 模型标签 | 923 | 3,299 |
| mebipred 阳性 | ≥0.50 | 111 | — |
| CHEL 优先 | CHEL≥0.25 | 15 | 111 |
| 主集 | CHEL≥0.25 且 FRS<0.50 | 12 | 111 |
| 更严子集 | CHEL≥0.25 且 FRS<0.45 | 8 | — |

### 12 条肽的理化轮廓

下列描述符刻画这 12 条对接配体，不是健康库与牙周炎库的比较。

12 条为标准残基组成的互不重复 7–9 aa 肽（表5）。11 条含组氨酸，6 条含半胱氨酸，每条至少 1 个 Arg 或 Lys。分子量 825.03–1,097.30 Da。等电点偏碱（8.28–11.54）。pH 7.4 净电荷全部为正（0.85–2.08）。10 条 GRAVY 为正，与富亮氨酸核心一致；LLHLPKRTT（−0.36）与 YHHLLCRR（−0.95）为两条亲水例外。脂肪族指数从 97.5（YHHLLCRR）到 222.9（LLHPLRL）。YLSLLQR 是唯一不含组氨酸的肽。这些数字描述组成，不是 HPLC 或 CD 实测。

**表5. 12条7–9 aa肽的组成与计算理化描述符。**

| 肽 | aa | MW (Da) | pI | z（pH 7.4） | GRAVY | AI | His | Cys | R+K |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ALLLHRC | 7 | 825.03 | 9.00 | 0.92 | 1.14 | 181.4 | 1 | 1 | 1 |
| FCLHLQLR | 8 | 1029.26 | 9.00 | 0.92 | 0.69 | 146.2 | 1 | 1 | 1 |
| FLLHTTR | 7 | 887.04 | 11.09 | 1.04 | 0.19 | 111.4 | 1 | 0 | 1 |
| HLLTLKKHV | 9 | 1088.35 | 10.63 | 2.08 | 0.08 | 162.2 | 2 | 0 | 2 |
| HLPLLHRCC | 9 | 1091.35 | 8.28 | 0.85 | 0.43 | 130.0 | 2 | 2 | 1 |
| HVLLLRQCA | 9 | 1052.30 | 9.00 | 0.92 | 0.97 | 173.3 | 1 | 1 | 1 |
| LLHLPKRTT | 9 | 1078.32 | 11.54 | 2.04 | −0.36 | 130.0 | 1 | 0 | 2 |
| LLHPLRC | 7 | 851.07 | 9.00 | 0.92 | 0.66 | 167.1 | 1 | 1 | 1 |
| LLHPLRL | 7 | 861.09 | 11.09 | 1.04 | 0.84 | 222.9 | 1 | 0 | 1 |
| WLLVHLKK | 8 | 1036.32 | 10.63 | 2.04 | 0.46 | 182.5 | 1 | 0 | 2 |
| YHHLLCRR | 8 | 1097.30 | 9.91 | 1.96 | −0.95 | 97.5 | 2 | 1 | 2 |
| YLSLLQR | 7 | 892.06 | 9.89 | 0.99 | 0.04 | 167.1 | 0 | 0 | 1 |

### 对人源 AChE 的对接

12 条配体均给出有利 Vina 分数（表6，图2）。最优单次 −8.25 至 −9.60 kcal/mol；三次均值 −8.07 ± 0.16 至 −9.44 ± 0.09 kcal/mol。最优构象排序为 FLLHTTR（−9.60）、YLSLLQR（−9.49）、ALLLHRC（−9.29）。均值排序 YLSLLQR 居首（−9.44 ± 0.09），ALLLHRC 次之（−9.18 ± 0.11）。FLLHTTR 单次最强、SD 最大（−8.77 ± 1.41）。最优构象形成 3–10 个氢键（平均键长 2.83–3.28 Å；图3、图4）。

**表6. 对人源AChE（PDB 4EY6）的三次 AutoDock Vina 打分。**

| 肽 | 氢键 | 最优 | 均值±SD（n=3） | PAS | 主要接触 |
| --- | ---: | ---: | --- | --- | --- |
| ALLLHRC | 3 | −9.29 | −9.18 ± 0.11 | 否 | Ser125, Ser203, Tyr124 |
| FCLHLQLR | 7 | −9.27 | −8.96 ± 0.48 | 是 | Ser203, Thr75, Tyr341 |
| FLLHTTR | 8 | −9.60 | −8.77 ± 1.41 | 是 | Asp74, Tyr72, His287 |
| HLLTLKKHV | 6 | −8.88 | −8.69 ± 0.20 | 是 | Tyr72, Phe346 |
| HLPLLHRCC | 4 | −8.35 | −8.28 ± 0.07 | 否 | Ser125, Tyr124, Tyr337 |
| HVLLLRQCA | 4 | −8.25 | −8.07 ± 0.16 | 是 | Thr75 |
| LLHLPKRTT | 3 | −9.01 | −8.89 ± 0.16 | 邻近 | Ser203, Val340 |
| LLHPLRC | 4 | −8.91 | −8.78 ± 0.11 | 否 | Ser125, Ser293 |
| LLHPLRL | 10 | −8.94 | −8.91 ± 0.05 | 是 | Trp286, Tyr341, His447 |
| WLLVHLKK | 4 | −8.94 | −8.64 ± 0.26 | 否 | Asn283, Gln279 |
| YHHLLCRR | 7 | −9.03 | −8.62 ± 0.43 | 否 | Trp86, Ser203 |
| YLSLLQR | 7 | −9.49 | −9.44 ± 0.09 | 是 | Tyr72, Thr75, Glu202 |

![图2. 12条候选微肽的本地 AutoDock Vina 打分。](../figures/fig5_docking_scores.png)

**图2. 对人源AChE（PDB 4EY6）的三次 Vina 打分。** 蓝点为均值，误差棒为 SD，橙菱为最优单次。横轴按最优单次排序。

![图3. ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC 和 HVLLLRQCA 的最优构象。](../figures/fig_docking_poses_A_F.png)

**图3. 第1–6条肽的最优对接构象（A–F）。** 微肽橙色，接触残基青色。FLLHTTR（C）为最密 PAS 构象。

![图4. LLHLPKRTT、LLHPLRC、LLHPLRL、WLLVHLKK、YHHLLCRR 和 YLSLLQR 的最优构象。](../figures/fig_docking_poses_G_L.png)

**图4. 第7–12条肽的最优对接构象（G–L）。** LLHPLRL（I）从 PAS 的 Trp286/Tyr341 跨越至催化 His447。YLSLLQR（L）桥接 PAS 与峡部入口。

最优构象中接触 PAS 的有 FLLHTTR（图3C）、YLSLLQR（图4L）、FCLHLQLR、HVLLLRQCA、HLLTLKKHV 和 LLHPLRL（图4I）。ALLLHRC 结合催化 Ser203，平均氢键最短（2.83 Å），而不是外侧 PAS 芳香核（图3A）。三次均值把跨运行仍强的配体（YLSLLQR、ALLLHRC、LLHPLRL）与最优构象强于运行平均的配体（FLLHTTR、FCLHLQLR、YHHLLCRR）分开。

### apo AChE 与三种复合物的 100 ns 动力学

apo AChE 以及 ALLLHRC、FLLHTTR、YLSLLQR 复合物完成生产相（表7，图5–7）。每幅六面板图比较 apo 与一条复合物：RMSD（A）、RMSF（B）、SASA（C）、Rg（D）、最后 20 ns DSSP（E）和分子间氢键（F）。

<!-- PAGEBREAK -->

![图5. apo AChE 与 AChE–ALLLHRC，100 ns。](../figures/fig_compare_mixed_ache_vs_alllhrc.png)

**图5. apo AChE 与 AChE–ALLLHRC。** A–F 与表7对应。复合物 RMSD（A）跟随 apo；氢键（F）由早期占有降至后 20 ns 约 2 个。

![图6. apo AChE 与 AChE–FLLHTTR，100 ns。](../figures/fig_compare_mixed_ache_vs_fllhttr.png)

**图6. apo AChE 与 AChE–FLLHTTR。** 约 50 ns 后复合物 RMSD（A）低于 apo。氢键计数（F）在 100 ns 全程维持约 6–10。

![图7. apo AChE 与 AChE–YLSLLQR，100 ns。](../figures/fig_compare_mixed_ache_vs_ylsllqr.png)

**图7. apo AChE 与 AChE–YLSLLQR。** 后期 RMSD（A）低于 apo。SASA（C）是唯一相对 apo 收缩的复合物。

**表7. apo AChE 与三种复合物最后 20 ns 指标（均值±SD）。**

| 指标 | apo AChE | ALLLHRC | FLLHTTR | YLSLLQR |
| --- | --- | --- | --- | --- |
| Cα RMSD (nm) | 0.1897 ± 0.0090 | 0.1916 ± 0.0092 | 0.1640 ± 0.0080 | 0.1625 ± 0.0078 |
| 微肽自拟合 RMSD (nm) | — | 0.2518 ± 0.0136 | 0.1752 ± 0.0111 | 0.0911 ± 0.0098 |
| RMSF 均值 (nm) | 0.0835 ± 0.0659 | 0.0876 ± 0.0581 | 0.0778 ± 0.0504 | 0.0771 ± 0.0498 |
| SASA (nm²) | 212.25 ± 2.89 | 217.47 ± 2.49 | 213.88 ± 2.36 | 209.71 ± 2.35 |
| Rg (nm) | 2.3045 ± 0.0056 | 2.3107 ± 0.0052 | 2.2967 ± 0.0047 | 2.3028 ± 0.0051 |
| 分子间氢键 | — | 2.19 ± 0.80 | 7.03 ± 1.28 | 2.93 ± 1.14 |
| 持续性接触对 | — | 7 | 7 | 7 |
| DSSP α-螺旋 / β-折叠 (%) | 33.44 / 17.35 | 33.66 / 16.76 | 32.92 / 17.52 | 33.31 / 17.02 |

apo RMSD 平台约 0.19 nm（图5A–7A）。ALLLHRC 跟随对照（复合物 0.1916 nm）。FLLHTTR 与 YLSLLQR 在 50–70 ns 后低于 apo（0.1640 和 0.1625 nm），读作变刚性而非解折叠。微肽自拟合 RMSD 以 ALLLHRC 最高（0.2518 nm）、YLSLLQR 最低（0.0911 nm）。催化核心 RMSF 保持低值；FLLHTTR 与 YLSLLQR 的均值 RMSF 低于 apo。Rg 维持 2.30–2.31 nm。SASA 在 ALLLHRC 升至 217.47 nm²，FLLHTTR 接近 apo（213.88 nm²），仅 YLSLLQR 降至 209.71 nm²（图7C）。氢键历史不同：ALLLHRC 衰减至 2.19 ± 0.80；FLLHTTR 全程维持 7.03 ± 1.28（图6F）；YLSLLQR 均值 2.93 ± 1.14。螺旋（约 33%）与折叠（约 17%）与 apo 柱重叠。各复合物保留 7 对持续性接触。质心 RDF 峰位于 1.22 nm（ALLLHRC）、1.80 nm（FLLHTTR）和 1.62 nm（YLSLLQR），即表面驻留而非本体溶剂。

## 讨论

AChE 在胆碱能突触水解乙酰胆碱。AD 组织中，同一酶出现在淀粉样斑块上。Inestrosa 等证明 AChE 经 PAS 加速 Aβ 成纤，且 AChE–Aβ 颗粒毒性高于游离肽[@inestrosa1996ache]。Alvarez 等分离出稳定的酶–肽复合物，改变 AChE 生化性质并提高纤丝神经毒性，并显示酶结合的是生长中的纤丝而非游离单体[@alvarez1998ache; @alvarez1997ache]。一段疏水 PAS 基序即足以产生伴侣效应[@deferrari2001motif]。Reyes 等用抗 AChE 单抗阻断该效应[@reyes1997mab]。Bartolini 等用 PAS 导向小分子达到同一终点[@bartolini2003pas]。小鼠中过量 AChE 促进皮层 Aβ 斑块[@rees2003ache]。关于 AD 中 AChE 的综述把斑块相关酶放进与 Aβ、磷酸化 tau 的交叉对话，且仍对 PAS 阻断敏感[@garciaayllon2011ache; @carvajal2011ache; @inestrosa2008ache]。Dinamarca 等用海马注射证明 AChE–Aβ 复合物的损伤强于游离纤丝[@dinamarca2010ache]。Johnson 与 Moore 把 PAS 定为 Tyr72、Asp74、Tyr124、Trp286 和 Tyr341，距峡部底部催化三联体约 20 Å[@johnson2006pas]。这些实验把 PAS 定为胆碱能衰竭与淀粉样沉积之间的结构铰链[@selkoe2016amyloid; @hampel2018cholinergic]。本研究的对接与 100 ns 轨迹查看牙周炎来源微肽对该铰链的占据。

口腔暴露路径在菌体和蛋白酶水平已有具体事例。Poole 等在短期死后 AD 脑组织中检出牙周致病毒力因子[@poole2013pg]。Dominy 等在 AD 脑内报告 *P. gingivalis* 与牙龈蛋白酶，并显示小鼠口腔感染升高脑内 Aβ1–42[@dominy2019pgingivalis]。Haditsch 等在持续表达活性牙龈蛋白酶的感染神经元中观察到 AD 样变性[@haditsch2020cor388]。Ilievski 等在野生型小鼠反复口腔给予牙周病原后产生神经炎症和 Aβ 相关改变[@ilievski2018oral]。Lei 等显示 *P. gingivalis* 菌血症经 Mfsd2a/Caveolin-1 转胞吞路径增加内皮通透性[@lei2023pgbbb]。牙龈蛋白酶与外膜囊泡可把细菌货物送出产生细胞[@guo2010gingipain; @ho2015omv]。综合分析与 AD 队列把牙周炎与后续认知下降联系起来[@larvin2023periodontalcognition; @ide2016periodontitis]。两样本孟德尔随机化并未支持遗传因果效应[@hu2024mendelian]。这些报告支持在 PAS 上检查口腔产物。把 12 条肽归于 *P. gingivalis*，或证明某一字符串穿过内皮，都不在这些报告之内[@chalmers2025primer; @gu2024bbb; @belstrom2021periodontitis]。牙龈蛋白酶、脂多糖和囊泡已经在走，7–9 aa 阳离子肽比这些货物更小。该肽在唾液、血清和内皮中能否存活，不在本次计算范围内。下文对接与 MD 处理的是占据：口腔七肽放到 AChE 上时，是否停在 Inestrosa 与 Alvarez 指认为成纤相关的 PAS。

深度学习肽挖掘提供了此处的过滤栈。Torres 等先对数百万条翻译的微生物组开放阅读框打分，再做实验过滤[@torres2024peptideantibiotics]。UniDL4BioPep 在 ESM-2 嵌入上沿用同一先预测再过滤逻辑[@du2023unidl4biopep]。NTxPred2、mebipred 与 AnOxPePred 分别针对神经毒性、金属结合和抗氧化终点训练，并非针对 AChE 占据[@rathore2025ntxpred2; @aptekmann2022mebipred; @olsen2020anoxpepred]。与 HOMD、eHOMD 和唾液宏蛋白质组的目录匹配支持该字符串曾经被观察到，这与其他口腔肽研究中这些资源的角色相同[@chen2010homd; @escapa2018ehomd; @belstrom2016metaproteomics; @jiang2022oralmetaproteomics; @yuan2025osample; @sberro2019smallgenes]，因而串联分数用作分诊栈。12 条对接配体为 7–9 残基、碱性、pH 7.4 净正电，核心偏亮氨酸。该组成与 PAS 的静电性质相符。Barak 等发现 Asp74 与 Trp286 构成外周配体的共同核心[@barak1994pas]。Mallender 等证明阳离子底物首先停在 Asp74[@mallender2000asp74]。短阳离子肽在化学上是合理的 PAS 占据者，结构上仍待显示。

人源 AChE（PDB 4EY6）为峡部与 PAS 提供实验框架[@cheung2012ache]，沿用 Sussman 在电鳗 AChE 上的芳香峡部定位[@sussman1991ache; @kryger1999e2020]。Dvir 等重申 20 Å 峡部把底部催化三联体与 rim 外周簇耦联[@dvir2010ache]。AutoDock Vina 是第一轮排序引擎[@trott2010vina; @eberhardt2021vina]。反复出现的接触落在 PAS 阵列上，而不是新口袋。FLLHTTR 与 Asp74、Tyr72、His287 形成氢键。YLSLLQR 在峡部入口桥接 Tyr72 与 Thr75。LLHPLRL 跨越 Trp286 与 Tyr341 并到达催化 His447，即 4EY6 中 donepezil 的 PAS–催化双重几何。HLLTLKKHV 到达 Atanasova 等 1 μs 轨迹中 Aβ 驻留的 344–361 区 Phe346[@atanasova2020md]。Bourne 等把 PAS 配体结晶在 Trp286 与 Tyr341 之间；LLHPLRL 出现同一对残基[@bourne2003pas]。ALLLHRC 是例外：它结合催化 Ser203，不接触外侧 PAS 芳香残基。12 个最优构象中有 6 个碰到 PAS 残基。FCLHLQLR、HVLLLRQCA、HLLTLKKHV 与 LLHPLRL 补全该 PAS 阳性组；HLPLLHRCC、LLHPLRC、WLLVHLKK 与 YHHLLCRR 停在外侧芳香残基之外，LLHLPKRTT 在旁侧。三条 MD 配体是打分最强者，其中两条 PAS 阳性。−8.25 至 −9.60 kcal/mol 的 Vina 分数是第一轮排序，不是结合常数。它们把 12 条串放进有利窗口，本身并不能把 PAS 占据者与催化位点占据者分开。分开来自接触名单：Asp74/Tyr72/Trp286/Tyr341 对 Ser203。FLLHTTR 与 YLSLLQR 属前一组。ALLLHRC 属后一组。对两组都做 MD，是把强 Vina 分数与 PAS 几何并排比较，看持续复合物需要哪一项。

AChE–Aβ 的 MD 已把该酶当作成核中心。加速采样把 Aβ 拉到 AChE 表面[@lushchekina2017amd]。1 μs、以 PAS 为中心的轨迹保持结合且不使折叠打开[@atanasova2020md]。同一占据模式在此出现在 100 ns 窗口。apo 的 Cα RMSD 约 0.19 nm。ALLLHRC 跟随该对照（0.1916 nm）。FLLHTTR 与 YLSLLQR 在 50–70 ns 后落到 apo 之下（0.1640 与 0.1625 nm）。复合物 RMSD 低于 apo 轨迹，可读作结合后局部变刚，而不是去折叠。该读法与 Lushchekina 描述的表面结合、不解离复合物相符。肽自身拟合 RMSD 给配体排序：ALLLHRC 0.2518 nm，FLLHTTR 0.1752 nm，YLSLLQR 0.0911 nm。YLSLLQR 是酶上最紧凑的配体。未碰到 PAS 的 ALLLHRC 最活动。apo AChE 本已是刚性 α/β 水解酶；Sussman 等描述的深芳香峡部不需要大结构域运动即可催化[@sussman1991ache]。相对该 apo 基线下降 0.03 nm，是已经紧凑的折叠再收紧，幅度达不到重建酶。

FLLHTTR 平均 RMSF 为 0.0778 nm，YLSLLQR 为 0.0771 nm，均低于 apo 的 0.0835 nm；ALLLHRC 为 0.0876 nm，略高于 apo。四个体系中催化核心涨落都低。峡部 rim 的 loop 比三联体更活动，符合 PAS 是表面簇而非埋藏口袋[@bourne2003pas; @johnson2006pas]。Bourne 与 Johnson 把 PAS 结合写成不必打开折叠的表面事件；RMSF 轨迹与该描述相符。回转半径在 apo 与三个复合物中保持 2.30–2.31 nm。这一量级的位移是七肽的空间容纳，不是 α/β 水解酶核心拆开。DSSP 螺旋（约 33%）与片层（约 17%）与 apo 柱重叠，二级结构在此窗口未被改写。Lushchekina 与 Atanasova 把更低的复合物 RMSD 加上保留的二级结构读作配体诱导的变刚；本轨迹沿用该读法。

氢键历史比 RMSD 更能分开配体。ALLLHRC 从早期占据衰减到最后 20 ns 的 2.19 ± 0.80。FLLHTTR 全程维持 7.03 ± 1.28。YLSLLQR 平均 2.93 ± 1.14。每个复合物有 7 对持续分子间接触。质心 RDF 峰在 1.22–1.80 nm，即表面驻留而非体相溶剂。SASA 在 ALLLHRC 上升（217.47 nm²，apo 为 212.25 nm²），FLLHTTR 接近 apo，仅 YLSLLQR 下降（209.71 nm²）。SASA 下降可读作更紧凑的复合物；该读法适用于 YLSLLQR。因此 FLLHTTR 像富氢键的 PAS 占据者，使蛋白变刚但不额外埋藏表面。YLSLLQR 像紧凑的 PAS 占据者，确实埋藏表面。ALLLHRC 尽管在 Ser203 上 Vina 分数强，并未留下持续的 PAS 型网络。FLLHTTR 仍是富氢键 PAS 配体，YLSLLQR 是紧凑 PAS 配体，ALLLHRC 则是随后失去占据的催化位点高分者。Bartolini 的测定已把抑制 AChE 诱导聚集的 PAS 导向配体与不必如此的催化位点配体分开[@bartolini2003pas]。Atanasova 的 1 μs Aβ 轨迹与此处 100 ns 肽轨迹在配体长度和采样窗口上不同。两者都显示配体留在 PAS 上且折叠未打开。

四步机制由上述 PAS 文献推出。第一，PAS 识别：占据 Asp74、Tyr72、Trp286、Tyr341，把异源肽放在通向催化三联体的峡部入口，即 Mallender 赋予阳离子底物的第一步[@mallender2000asp74; @hampel2018cholinergic; @cheung2012ache]。第二，持续的酶–肽复合物：分子间氢键持续，与 Lushchekina、Atanasova 的 AChE–Aβ 轨迹以及 Alvarez 分离的稳定复合物一致[@alvarez1998ache]。第三，乙酰胆碱进入受限：20 Å 峡部入口的物理占据可在催化核心仍折叠时妨碍底物，即 PAS 配体的空间阻断方式[@johnson2006pas; @dvir2010ache]。第四，病理性伴侣活性：PAS 是已记录的促纤位点[@inestrosa1996ache; @deferrari2001motif; @carvajal2011ache]，停在那里的肽可降低内源 Aβ 的成核壁垒。折叠的 AChE 于是出示覆肽 PAS，Aβ 寡聚体可在其上共组装，这是 Dinamarca 等用来解释 AChE–Aβ 颗粒损伤强于游离纤丝的几何[@dinamarca2010ache]。

AChE 的 PAS 药理学此前多为小分子。Bartolini 的 PAS 配体在不要求占据催化位点的情况下降低 AChE 诱导的聚集[@bartolini2003pas]。4EY6 中的 donepezil 从 PAS Trp286 跨到催化阴离子位点，即 Kryger 在电鳗 AChE 上定位的双结合模板[@kryger1999e2020; @cheung2012ache]。Johnson 与 Moore 把该表面当作调节异源蛋白结合（包括 Aβ）的设计把手[@johnson2006pas]。短阳离子肽占据的表面大于这些配体。此处构象把口腔七肽放在同一芳香簇上。双结合抑制剂被设计成同时占据 PAS 与催化阴离子位点，治疗意图是同时减慢乙酰胆碱水解和 PAS 模板化的 Aβ 组装[@inestrosa2008ache; @johnson2006pas]。只盖住 rim 的口腔七肽不能按该双结合模板打分。FLLHTTR 与 YLSLLQR 留在 rim，即 Inestrosa 当作伴侣触发的占据。Cheung 为 donepezil 结晶的是更长的双结合构象。

按上述文献，从 PRJNA678453 MAG 预测的短、带正电、富亮氨酸口腔微肽可以占据实验已定位的 Aβ 结合 PAS，并在 100 ns 尺度上留在那里。结合测定和 Aβ 聚集实验仍不可少。

## 结论

牙周炎标记口腔 smORF 库中的 12 条 7–9 aa 肽对接到人源 AChE。FLLHTTR、YLSLLQR 与 ALLLHRC 在 100 ns 内停在表面且不使酶解折叠。FLLHTTR 形成最密 PAS 氢键网；YLSLLQR 是唯一收缩溶剂可及面积的复合物。计算支持一种可能机制：口腔致病肽占据 AChE，妨碍乙酰胆碱进入，并在同一 PAS 上与 Aβ 共成核。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
4. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
5. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
6. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
7. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
8. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
9. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
10. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
11. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
12. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
13. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
14. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
15. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
16. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
17. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
18. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
19. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
20. Lushchekina SV, Kots ED, Novichkova DA, Petrov KA, Masson P. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7(2):396–402. doi:10.1007/s12668-016-0375-x.
21. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
22. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
23. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept): implications for drug design. *Structure*. 1999;7(3):297–307. doi:10.1016/s0969-2126(99)80040-9.
24. Rice P, Longden I, Bleasby A. EMBOSS: the European Molecular Biology Open Software Suite. *Trends Genet*. 2000;16(6):276–277. doi:10.1016/S0168-9525(00)02024-2.
25. Gu Y, Chen P, Wang B, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
26. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
27. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database (eHOMD). *mSystems*. 2018;3(3):e00187-18. doi:10.1128/mSystems.00187-18.
28. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
29. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research (Wash D C)*. 2022;2022:9781578. doi:10.34133/2022/9781578.
30. Yuan J, Cao Q, Chen M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
31. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
32. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
33. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
34. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
35. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
36. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
37. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
38. Alvarez A, Alarcón R, Opazo C, Campos EO, Muñoz FJ, Calderón FH, Dajas F, Gentry MK, Doctor BP, De Mello FG, Inestrosa NC. Stable complexes involving acetylcholinesterase and amyloid-β peptide change the biochemical properties of the enzyme and increase the neurotoxicity of Alzheimer’s fibrils. *J Neurosci*. 1998;18(9):3213–3223. doi:10.1523/JNEUROSCI.18-09-03213.1998.
39. Alvarez A, Opazo C, Alarcón R, Garrido J, Inestrosa NC. Acetylcholinesterase promotes the aggregation of amyloid-β-peptide fragments by forming a complex with the growing fibrils. *J Mol Biol*. 1997;272(3):348–361. doi:10.1006/jmbi.1997.1245.
40. Reyes AE, Perez DR, Alvarez A, Garrido J, Gentry MK, Doctor BP, Inestrosa NC. A monoclonal antibody against acetylcholinesterase inhibits the formation of amyloid fibrils induced by the enzyme. *Biochem Biophys Res Commun*. 1997;232(3):652–655. doi:10.1006/bbrc.1997.6357.
41. Rees T, Hammond PI, Soreq H, Younkin S, Brimijoin S. Acetylcholinesterase promotes β-amyloid plaques in cerebral cortex. *Neurobiol Aging*. 2003;24(6):777–787. doi:10.1016/S0197-4580(02)00230-0.
42. García-Ayllón MS, Small DH, Avila J, Sáez-Valero J. Revisiting the role of acetylcholinesterase in Alzheimer’s disease: cross-talk with P-tau and β-amyloid. *Front Mol Neurosci*. 2011;4:22. doi:10.3389/fnmol.2011.00022.
43. Carvajal FJ, Inestrosa NC. Interactions of AChE with Aβ aggregates in Alzheimer’s brain: therapeutic relevance of IDN 5706. *Front Mol Neurosci*. 2011;4:19. doi:10.3389/fnmol.2011.00019.
44. Inestrosa NC, Dinamarca MC, Alvarez A. Amyloid–cholinesterase interactions. *FEBS J*. 2008;275(4):625–632. doi:10.1111/j.1742-4658.2007.06238.x.
45. Dinamarca MC, Sagal JP, Quintanilla RA, Godoy JA, Arrázola MS, Inestrosa NC. Amyloid-β–acetylcholinesterase complexes potentiate neurodegenerative changes induced by the Aβ peptide. Implications for the pathogenesis of Alzheimer’s disease. *Mol Neurodegener*. 2010;5:4. doi:10.1186/1750-1326-5-4.
46. Johnson G, Moore SW. The peripheral anionic site of acetylcholinesterase: structure, functions and potential role in rational drug design. *Curr Pharm Des*. 2006;12(2):217–225. doi:10.2174/138161206775193127.
47. Poole S, Singhrao SK, Kesavalu L, Curtis MA, Crean S. Determining the presence of periodontopathic virulence factors in short-term postmortem Alzheimer’s disease brain tissue. *J Alzheimers Dis*. 2013;36(4):665–677. doi:10.3233/JAD-121918.
48. Haditsch U, Roth T, Rodriguez L, et al. Alzheimer’s disease-like neurodegeneration in *Porphyromonas gingivalis* infected neurons with persistent expression of active gingipains. *J Alzheimers Dis*. 2020;75(4):1361–1376. doi:10.3233/JAD-200393.
49. Lei S, Li J, Yu J, et al. *Porphyromonas gingivalis* bacteremia increases the permeability of the blood-brain barrier via the Mfsd2a/Caveolin-1 mediated transcytosis pathway. *Int J Oral Sci*. 2023;15:3. doi:10.1038/s41368-022-00215-y.
50. Barak D, Kronman C, Ordentlich A, Ariel N, Bromberg A, Marcus D, Lazar A, Velan B, Shafferman A. Acetylcholinesterase peripheral anionic site degeneracy conferred by amino acid arrays sharing a common core. *J Biol Chem*. 1994;269(9):6296–6305. doi:10.1016/S0021-9258(17)37603-X.
51. Mallender WD, Szegletes T, Rosenberry TL. Acetylthiocholine binds to Asp74 at the peripheral site of human acetylcholinesterase as the first step in the catalytic pathway. *Biochemistry*. 2000;39(26):7753–7763. doi:10.1021/bi000210o.
52. Sussman JL, Harel M, Frolow F, Oefner C, Goldman A, Toker L, Silman I. Atomic structure of acetylcholinesterase from *Torpedo californica*: a prototypic acetylcholine-binding protein. *Science*. 1991;253(5022):872–879. doi:10.1126/science.1678899.
53. Dvir H, Silman I, Harel M, Rosenberry TL, Sussman JL. Acetylcholinesterase: from 3D structure to function. *Chem Biol Interact*. 2010;187(1-3):10–22. doi:10.1016/j.cbi.2010.01.042.
54. Bourne Y, Taylor P, Radić Z, Marchot P. Structural insights into ligand interactions at the acetylcholinesterase peripheral anionic site. *EMBO J*. 2003;22(1):1–12. doi:10.1093/emboj/cdg005.
