## 摘要

牙周炎相关口腔菌群失调可能参与阿尔茨海默病（AD）相关炎症，但尚未建立明确的分子连接。微生物组小开放阅读框（smORF）构成规模庞大的候选肽空间，可用于计算优选。本研究旨在重建口腔smORF汇总筛选级联，并形成可供机制随访的适量肽候选集。本研究为纯计算二次分析，整合序列/蛋白质组过滤、ESM-2嵌入与任务特异性卷积网络、ESM2-t30神经毒性模型、两级神经网络金属结合预测器、多任务抗氧化卷积网络、序列组成分析及独立乙酰胆碱酯酶（AChE）对接汇总。从11,269,961条和11,721,988条smORF起始库中分别保留31,510条和33,786条候选。牙周炎标记分支中3,518条候选达到BBB高分；NTxPred2评价3,299条，其中923条为模型阳性；后续筛选依次保留111、15、12和8条候选。另一张表包含12条互不重复的7–9 aa序列，其AChE Vina均值范围为−9.60至−8.25 kcal/mol。序列组成和评分排序可以复核，但逐行对应关系和对接执行仍未解决。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微肽；smORF；深度学习；乙酰胆碱酯酶；分子动力学

## 引言

阿尔茨海默病（AD）是一种进行性神经退行性疾病，其病理涉及淀粉样蛋白β（Aβ）、tau、突触、免疫、血管和代谢异常的相互作用[@scheltens2021alzheimer]。淀粉样蛋白仍是疾病生物学的核心组成，但其负荷本身不能解释AD在时间过程和临床表现上的异质性[@selkoe2016amyloid]。因此，外周炎症状态更适合被理解为多层次疾病过程中的潜在修饰因素，而不是单一充分病因。

牙周炎是由失调性多微生物生物膜与易感宿主反应共同驱动的慢性炎症性疾病。它可能造成持续炎症负担和微生物产物的间歇性系统暴露，由此推动口腔—脑轴研究[@chalmers2025primer]。在该生态系统中，牙龈卟啉单胞菌（*Porphyromonas gingivalis*）是研究较充分的革兰阴性厌氧条件致病菌。牙龈蛋白酶、免疫调节、组织降解、营养获取和群落协作使该菌即使在丰度不占优势时也可能重塑牙周生态位[@guo2010gingipain]。这些特征提供机制背景，但不能把缺少来源链的群落肽直接归属于*P. gingivalis*。

若干研究支持继续探索，同时也显示出现有证据缺口。AD相关死后组织中曾检出*P. gingivalis*相关DNA或蛋白信号，但疾病组织中的检出不能确定暴露方向、时间或因果作用[@dominy2019pgingivalis]。小鼠反复口腔暴露可产生神经炎症、神经退行性和Aβ相关改变，说明特定模型下具有生物学合理性，但不能直接外推至人类[@ilievski2018oral]。外膜囊泡可能运输浓缩的细菌货物并触发宿主细胞信号，但其在人类自然暴露中的生物分布和有效剂量仍不确定[@nara2021omv]。相反，孟德尔随机化分析未确认牙周病对AD的遗传因果效应，为强因果表述提供了必要限制[@hu2024mendelian]。这些结果能够提出分子研究问题，但尚未形成确定的因果通路。

微生物组编码的小蛋白和微肽可能构成尚未充分研究的分子中介。人类微生物组大规模分析发现许多保守的小基因家族，其中多数缺少已知结构域或功能[@sberro2019smallgenes]。专用smORF注释通过整合编码特征等信息提高检出灵敏度，而不是沿用常规蛋白长度阈值[@durrant2021sorf]。然而，预测smORF不一定被转录或翻译；检出的肽也不一定从生物膜释放、在血液中稳定、跨越血脑屏障（BBB）或在神经组织中发挥作用。

因此，相关分子机制仍不清楚。本研究定位于早期计算优选，而不是机制检验。我们重建汇总候选漏斗，按照实际算法描述各模型架构，表征一份12条序列清单，并限定现有AChE对接评分表的解释范围。研究目标是在不夸大模型输出的前提下缩小候选空间，并形成从序列追溯、独立计算、分子动力学（MD）到实验验证的科学顺序。

## 材料与方法

### 研究设计与数据来源

本研究为纯计算二次分析，使用汇总筛选计数、模型汇总、一张12条序列表及相应AChE对接评分表。本文未开展参与者招募、标本采集、湿实验、新组学处理、预测器再训练或对接重跑；MD轨迹分析作为预设扩展正在进行。所提供的健康与牙周炎标签仅作为分支标签保留，不视为已经核实的候选层面疾病归属。

我们核查公共登录号背景，以区分来源项目与衍生组装。PRJNA678453是配对口腔宏基因组和宏转录组测量的来源项目[@belstrom2021periodontitis]。PRJEB65451并非独立临床队列，而是由PRJNA678453衍生、使用metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的第三方注释宏基因组组装项目。由于现有材料不含一致的登录号—分组表、样本—组装映射和bin层面清单，本文省略具体参与者、标本、组装分析和宏基因组组装基因组总数。

现有数据不含完整漏斗的候选核苷酸行、完整肽序列行、基因组坐标、样本映射、分类学归属、肽谱匹配、完整预测器输出或原始发现管线。因此，无法估计参与者层面患病率，不能进行分类学归属和疾病富集检验，也不能重建所有模型阶段之间的精确候选交接。

### smORF候选定义与序列证据过滤

所提供分析保留编码4–50 aa肽的翻译smORF。健康标记和牙周炎标记起始库分别包含11,269,961条和11,721,988条候选。候选序列与指定口腔序列和蛋白质组资源进行精确匹配并去冗余，最终保留31,510条健康标记候选和33,786条牙周炎标记候选。精确匹配仅解释为序列存在或曾在相关资源中被观察的支持信息，而不是分析疾病标记分支中真实表达的证明。

过滤后候选分为短肽（5–30 aa）和长肽（31–50 aa）分支。健康标记分支含30,557条短肽和953条长肽；牙周炎标记分支含32,754条短肽和1,032条长肽。虽然初始定义包括4 aa肽，但下游分箱从5 aa开始，因此无法根据汇总表确定4 aa序列的去向。

### 深度学习引导的多模型优选

第一层功能优选采用UniDL4BioPep。该架构使用预训练ESM-2模型`esm2_t6_8M_UR50D`把每条肽编码为320维上下文表示，随后输入用于二分类肽活性任务的六层任务特异性卷积神经网络[@du2023unidl4biopep]。包括BBB任务在内均使用≥0.80阈值。由于该极短微生物组肽域缺少校准和实验转运信息，本文把输出称为“BBB高分”，而不是BBB可透过。

牙周炎标记BBB高分集合随后进入NTxPred2肽模式。该模型在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[@rathore2025ntxpred2]。仅将处于文献规定7–50 aa输入范围的肽视为已评估；更短候选记为超出模型覆盖，而不是阴性。

Mebipred评价Cu、Fe和Zn相关结合潜力。与ESM模型不同，mebipred把氨基酸组成、理化描述符和金属结合5-mer频率整合到两级人工神经网络框架中：一般金属结合网络之后连接离子特异性分类器[@aptekmann2022mebipred]，判定阈值为0.50。

抗氧化相关性质采用多任务深度卷积神经网络AnOxPePred评价。经one-hot编码的肽序列依次通过一维卷积、平均池化和256单元全连接层，产生自由基清除（FRS）和螯合（CHEL）输出[@olsen2020anoxpepred]。保留三个操作终点：CHEL≥0.25；CHEL≥0.25且FRS<0.50；CHEL≥0.25且FRS<0.45。由于多个模型重复利用序列组成且训练终点异质，串行模型一致仅作为计算分流，不视为相互独立的生物学确认。

### 序列表征与对接评分分析

另一张表包含12条被描述为CHEL/FRS主集合的肽序列。因缺少稳定标识符和序列层面CHEL/FRS输出，无法确认其是否对应汇总终点。我们直接依据字符串重算长度，以及组氨酸、半胱氨酸、碱性残基（Arg+Lys）和芳香残基（Phe+Tyr+Trp）数量，并检查序列唯一性及标准氨基酸组成。

选择AChE作为结构背景，是因为其外周区域与加速Aβ组装有关[@inestrosa1996ache]。PDB 4EY6提供具有配体结合信息的实验测定人AChE结构[@cheung2012ache]。现有对接表描述12条肽的AutoDock Vina 1.2.5评分。Vina适用于初步筛选，但评分受受体制备、配体质子化、初始构象、搜索空间位置、exhaustiveness和随机采样影响[@trott2010vina]。较新Vina实现扩展了方法，但不能消除这些依赖[@eberhardt2021vina]。因此，本文仅对均值和标准差进行描述性分析，不把评分换算为亲和力或自由能。制备结构、精确网格中心、运行定义、原始分数、日志、构象和相互作用表均不可获得。

### 正在进行的分子动力学扩展

预设的100 ns MD扩展包括游离人AChE以及标记为ALLLHRC、FLLHTTR和YLSLLQR的AChE复合物。计划使用GROMACS[@abraham2015gromacs]、Amber99SB-ILDN力场[@lindorfflarsen2010amber]、TIP3P水模型、溶质至盒边界1.0 nm的三斜周期盒，并在中和后加入0.15 mol/L NaCl。能量最小化包括2,000步最速下降及重原子位置约束。平衡过程包括1.0 ns约束NVT升温（10至300 K）、1.0 ns约束NPT平衡和300 K、1 bar条件下1.0 ns无约束NPT平衡。

生产阶段设定为100 ns，步长2 fs；含氢键采用LINCS约束，静电相互作用采用粒子网格Ewald法，温度耦合采用velocity-rescale方法，压力耦合采用Berendsen方法。坐标每20 ps保存一次，即每条轨迹计划得到5,000帧。预设输出包括复合物、AChE和肽层面的RMSD/RMSF、回转半径、溶剂可及表面积、二级结构、径向分布函数、氢键、残基接触及桥连水。轨迹处理与质量控制正在进行；稳定性、收敛性和接触结果将在预设分析完成后补充。

## 结果

### 序列证据过滤与BBB高分输出

序列证据过滤分别保留31,510/11,269,961条健康标记候选（0.2796%）和33,786/11,721,988条牙周炎标记候选（0.2882%）。健康标记分支中，3,359/30,557条短肽（10.99%）和40/953条长肽（4.20%）为BBB高分。牙周炎标记分支中，3,446/32,754条短肽（10.52%）和72/1,032条长肽（6.98%）为BBB高分，总计3,518条；其中短肽占97.95%。

所提供牙周炎标记长度汇总包括5–7 aa 547条、8–15 aa 2,893条、16–30 aa 6条以及31–50 aa 72条。因此，优选集合以短序列为主。由于缺少逐行身份，无法评价序列重叠、分类学分布或参与者层面患病率。

广义抗菌输出接近饱和：健康标记短肽中30,537/30,557条（99.93%）、牙周炎标记短肽中32,721/32,754条（99.90%）超过共同0.80阈值。这种近乎普遍的阳性不太可能代表具有实验活性的口腔抗菌肽比例，更可能提示序列域偏移、校准限制或该标签不适合采用共同阈值。

### 串行模型优选

NTxPred2评价3,299/3,518条牙周炎标记BBB高分候选（93.77%）；219/3,518条（6.23%）超出规定长度范围。在已评估候选中，923/3,299条（27.98%）为模型阳性。后续汇总筛选依次保留111条mebipred阳性、15条CHEL≥0.25、12条CHEL≥0.25且FRS<0.50，以及8条CHEL≥0.25且FRS<0.45候选（表1）。收紧FRS阈值后保留主集合的8/12（66.67%）。由于缺少候选层面交接数据，111/923不解释为已验证转换率。

**表1. 汇总计算优选结果。**

| 阶段 | 操作规则 | n | 分母或限制 |
| --- | --- | ---: | --- |
| 健康标记smORF | 4–50 aa | 11,269,961 | 起始库 |
| 牙周炎标记smORF | 4–50 aa | 11,721,988 | 起始库 |
| 证据过滤后健康标记候选 | 精确匹配与去冗余 | 31,510 | 11,269,961 |
| 证据过滤后牙周炎标记候选 | 精确匹配与去冗余 | 33,786 | 11,721,988 |
| 短肽BBB高分 | UniDL4BioPep输出≥0.80；5–30 aa | 3,446 | 32,754 |
| 长肽BBB高分 | UniDL4BioPep输出≥0.80；31–50 aa | 72 | 1,032 |
| BBB高分总计 | 短肽+长肽 | 3,518 | 算术和 |
| NTxPred2已评估 | 7–50 aa | 3,299 | 3,518 |
| NTxPred2阳性 | 模型阳性标签 | 923 | 3,299 |
| 金属结合阳性 | Mebipred输出≥0.50 | 111 | 逐行交接不可获得 |
| CHEL优先 | CHEL≥0.25 | 15 | 111 |
| 主集合 | CHEL≥0.25且FRS<0.50 | 12 | 111 |
| 严格子集 | CHEL≥0.25且FRS<0.45 | 8 | 序列成员未知 |

### 12条序列与对接评分排序

另一张表包含12条互不重复、仅由标准氨基酸组成的肽，长度为7–9个残基。其中11条含组氨酸，6条含半胱氨酸，每条均至少含一个Arg或Lys。这些性质可提出合成和配位假设，但不能证明金属结合、BBB转运、毒性、分类学归属或与汇总终点的对应关系。

Vina均值范围为−9.60至−8.25 kcal/mol，标准差范围为0.04至0.12（表2）。FLLHTTR、YLSLLQR和ALLLHRC的均值最低，HLPLLHRCC和HVLLLRQCA的均值最高。1.35 kcal/mol的跨度仅描述该评分表。标准差的逐次运行分母不可获得；在缺少构象时也无法评价残基层面相互作用。

**表2. 12条序列及现有AChE对接评分。**

| 排名 | 序列 | 长度（aa） | 平均评分（kcal/mol） | SD |
| ---: | --- | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | −9.60 | 0.08 |
| 2 | YLSLLQR | 7 | −9.49 | 0.05 |
| 3 | ALLLHRC | 7 | −9.29 | 0.11 |
| 4 | FCLHLQLR | 8 | −9.27 | 0.09 |
| 5 | YHHLLCRR | 8 | −9.03 | 0.07 |
| 6 | LLHLPKRTT | 9 | −9.01 | 0.06 |
| 7 | LLHPLRL | 7 | −8.94 | 0.10 |
| 8 | WLLVHLKK | 8 | −8.94 | 0.04 |
| 9 | LLHPLRC | 7 | −8.91 | 0.08 |
| 10 | HLLTLKKHV | 9 | −8.88 | 0.05 |
| 11 | HLPLLHRCC | 9 | −8.35 | 0.12 |
| 12 | HVLLLRQCA | 9 | −8.25 | 0.09 |

## 讨论

### 主要发现

本研究重建一条计算漏斗，把数百万条smORF候选缩减为12条主集合和8条严格子集的汇总终点，同时表征另一份12条明确序列并保留现有AChE对接表的评分顺序。主要科学贡献不是验证牙周炎—AD机制，而是形成边界清楚的候选集、明确模型适用性限制，并为恢复缺失的序列层面和实验依据提供有序路径。

### 模型级联的解释

该级联整合现代神经网络架构，但不能视为多次独立确认。UniDL4BioPep和NTxPred2均使用蛋白质语言模型表示，而mebipred和AnOxPePred包含组成衍生信息，相关序列特征可能沿连续筛选传播。不同训练集在终点定义、序列长度、去冗余、类别平衡和阴性集构建上也存在差异。对于富亮氨酸、带正电且仅7–9 aa的微生物组肽，这些问题尤为重要，因为候选可能偏离训练分布。

接近饱和的抗菌输出提供内部校准警示。它不否定所有排序，但表明共同概率阈值在不同任务中可能具有完全不同的意义。因此，“BBB高分”“神经毒性阳性”“金属结合阳性”、CHEL和FRS都只是操作性模型标签，并不等同于转运、神经元损伤、结合常数、配位几何或氧化还原活性。

### AChE、金属与肽结构假设

AChE外周区域可影响Aβ组装，因此具有生物学相关性，但这一背景不能把对接评分转化为靶点结合。柔性肽具有多种可达构象，质子化、末端状态、受体柔性、初始结构和搜索设置均可能改变排序。独立重现应包含制备后的受体和配体文件、多种起始构象、明确随机种子、全部原始分数与构象，以及FlexPepDock等肽特异性柔性精修[@london2011flexpepdock]。正在进行的MD扩展可从记录完整的起始复合物评价接触持续性和构象行为，而不能替代不确定的对接制备。

组氨酸和半胱氨酸富集提供潜在金属配位基团，但序列组成不能确定亲和力、化学计量、离子选择性、配位几何、氧化态或氧化还原后果。直接测量应在受控pH和化学计量下比较Cu(II)、Fe(II/III)和Zn(II)，并包括光谱、热力学、活性氧及脂质过氧化终点。需要设置仅肽、仅金属、打乱序列、组成匹配及明确阳性和阴性对照。

### 牙周与AD解释

牙周背景仍属于假设生成。人体关联可能受到年龄、吸烟、糖尿病、用药、衰弱、社会经济因素、口腔护理可及性和反向因果影响。*P. gingivalis*实验系统在规定剂量和暴露路径下证明若干可能性，但不能转移到缺少追溯关系的群落肽。当前标签不能证明任何序列具有牙周炎特异性、由*P. gingivalis*编码、在来源口腔群落中表达、进入循环或到达脑组织。

可信的分子链需要序列到contig或组装的映射、样本和临床分组、分类学解析、队列匹配的转录或翻译证据、系统暴露、BBB转运以及可重复的靶点或细胞表型。每一步回答不同问题，不能通过累积更多计算评分来替代。

### 验证优先级与局限

首要任务是恢复候选层面数据表，将序列、稳定标识符、基因组坐标、组装、样本、分组、分类学、肽谱证据、每个预测器评分与适用性标记、CHEL/FRS值、主/严格集合成员及对接配体身份连接起来。这将解决12条明确序列是否对应汇总终点，并确定严格8条子集。

固定版本计算重现后，合成肽应依次接受身份、纯度、溶解性、聚集和血清/蛋白酶稳定性检验。BBB转运与细胞毒性应分别采用浓度—反应设计和非神经元对照。随后在预设条件下评价金属化学、AChE/BChE活性、直接结合及Aβ聚集。正在进行的MD扩展将在质量控制后提供轨迹稳定性和接触指标；只有分子身份、暴露、可重复生化活性和生物学重复表型均成立时，才适合进入疾病模型。

决定性局限包括缺少漏斗逐行数据、12与8终点成员未解决、缺少原始对接输入和构象、MD轨迹分析仍在进行，以及缺少生物学测量。健康标记与牙周炎标记库相近的汇总保留率不能支持疾病富集，因为适当推断单位应是参与者或样本。这些限制将当前研究限定为计算优选与验证规划。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
4. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
5. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
6. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
7. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
8. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
9. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
10. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
11. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
12. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
13. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
14. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
15. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
16. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
17. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
18. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
19. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
20. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
21. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
22. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
