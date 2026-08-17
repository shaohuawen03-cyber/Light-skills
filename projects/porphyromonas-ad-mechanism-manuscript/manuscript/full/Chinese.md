## 摘要

**背景：** 牙周炎相关口腔菌群失调可能参与阿尔茨海默病（AD）相关炎症，但连接口腔微生物组与脑组织的具体分子仍未明确。微生物组小开放阅读框（smORF）构成规模庞大且尚未充分表征的候选肽空间，可用于计算优选。

**目的：** 重建口腔smORF汇总筛选级联，表征所提供的肽候选清单，并形成可检验的AChE、金属/氧化还原、血脑屏障（BBB）和神经毒性假设。

**方法：** 本研究为纯计算二次分析，整合序列/蛋白质组过滤、ESM-2嵌入与任务特异性卷积网络、微调ESM2-t30神经毒性模型、两级神经网络金属结合预测器、多任务抗氧化卷积网络及独立AChE对接汇总。

**结果：** 两个分支经过滤后分别保留31,510条和33,786条候选。牙周炎标记分支中3,518条候选达到BBB高分；3,299条处于NTxPred2适用长度范围内，其中923条为模型阳性；后续筛选依次保留111、15、12和8条候选。另一张数据表包含12条互不重复的7–9 aa序列，其AChE Vina均值范围为−9.60至−8.25 kcal/mol。序列组成和评分排序可以复核，但根据现有材料仍无法重建序列层面的漏斗对应关系和对接执行。

**结论：** 本研究形成了边界明确的候选清单，可供独立计算和实验验证，但不能据此证明肽表达、脑暴露、*Porphyromonas gingivalis*来源、AChE结合或AD机制。预设的100 ns GROMACS扩展将在分析和质量控制完成后补充轨迹稳定性与接触结果。

**关键词：** 阿尔茨海默病；牙龈卟啉单胞菌；牙周炎；口腔微生物组；smORF；深度学习；乙酰胆碱酯酶；分子动力学

## 引言

### 阿尔茨海默病是多层次生物学问题

阿尔茨海默病（Alzheimer’s disease，AD）是一种进行性神经退行性疾病，淀粉样蛋白β（Aβ）沉积、tau病理、突触衰竭、胶质细胞激活、血管功能障碍和系统性共病在漫长的临床前及临床连续体中相互作用[@scheltens2021alzheimer]。淀粉样蛋白假说仍是解释疾病起始事件的重要框架，但单独的淀粉样蛋白负荷不能解释AD在空间、时间和临床表现上的全部异质性[@selkoe2016amyloid]。当前观点因而把淀粉样蛋白和tau置于更广泛的网络中，其中包括先天免疫信号、神经元易损性、脂质和金属稳态、脑血管完整性以及随年龄增长而下降的系统韧性。评价外周暴露时，这种系统视角非常重要：某一具有生物学合理性的因素未必是充分病因，但仍必须通过可追溯的分子和时间证据与疾病相关组织连接起来。

胆碱能系统体现了临床相关性与因果充分性之间的差别。胆碱能功能丧失参与认知症状，乙酰胆碱酯酶（AChE）抑制剂仍是成熟的对症治疗[@hampel2018cholinergic]。AChE还与Aβ装配存在非催化相互作用，从而在胆碱能生物学与淀粉样研究之间形成结构联系[@inestrosa1996ache]。但这两点都不意味着每个预测可与AChE相互作用的分子均与AD相关。靶标占据、作用方向、组织暴露、浓度、选择性和下游表型都必须分别建立。这一证据顺序也适用于评价口腔—脑轴中的微生物分子。

慢性外周炎症状态因而被视为可能调节神经退行性易损性的因素。牙周炎尤其受到关注，因为它同时包含持续黏膜炎症、菌群失调的多微生物生物膜、微生物产物间歇进入循环的可能性，以及显著的年龄和共病梯度[@chalmers2025primer]。但这些特征也使因果解释变得困难。牙周炎可能增加系统炎症负担，也可能与认知下降共享决定因素，而认知下降又会恶化口腔卫生和牙科服务可及性。因此，严格的分子研究必须区分关联、路径合理性、分子身份和已证实功能，不能把它们视为同一层证据。

### 牙周菌群失调与牙龈卟啉单胞菌

牙周炎是牙支持组织的生态性疾病，而不是单一病原体造成的结果。在易感宿主中，群落结构改变、炎症性营养释放和炎症消退受损可以相互强化，形成具有位点特异性转录活动的失调生态。配对口腔宏基因组和宏转录组数据表明，疾病相关信号随物种和口腔位点变化，分类丰度不能代替功能活性[@belstrom2021periodontitis]。跨研究宏转录组综合还显示，疾病信号受到队列定义、采样位点、测序深度、标准化、协变量和受试者层面重复的影响[@ovsepian2024periodontal]。因此，不能把疾病标注分支中恢复的每条序列都称为疾病特异序列。

在这一群落中，牙龈卟啉单胞菌（*Porphyromonas gingivalis*）是研究最充分的革兰阴性厌氧条件致病菌之一。其重要性并不只来自丰度，还来自通过蛋白水解、免疫调节、群落协作和囊泡载荷输送重塑宿主—微生物相互作用的能力。牙龈蛋白酶可依赖具体背景影响宿主蛋白、补体通路、炎症、组织完整性和营养获取[@guo2010gingipain]。*P. gingivalis*外膜囊泡能够浓缩并运输细菌成分，改变其与宿主组织及邻近微生物的相互作用[@ho2015omv]。这些性质使该菌适合作为口腔—系统假设的生物学背景，但不能据此把无法追溯的群落来源肽归属于该菌。

必须区分微生物种层面的假设与群落肽假设。检出*P. gingivalis* DNA、抗原、牙龈蛋白酶相关信号或囊泡物质，并不意味着某条短肽已经表达、分泌、在血液中稳定、跨越血脑屏障（BBB）或在神经组织中发挥作用。反过来，无法归属于*P. gingivalis*的宏基因组来源肽也可能来自其他口腔分类单元或组装伪影。因此，本文把口腔宏基因组视为群落序列空间，而把*P. gingivalis*作为机制背景而非预设分类标签。

### 人体、实验和遗传证据具有不同因果权重

牙周炎—AD文献包含回答不同问题的多类证据。观察性综述和荟萃分析通常报告牙周病与认知障碍相关，但效应估计随牙周定义、痴呆判定、随访时间、人群年龄结构和校正策略而变化[@larvin2023periodontalcognition]。临床综合同样发现反复出现的关联，同时强调异质性以及回顾性设计难以确定方向性[@kaliamoorthy2022periodontitisad]。聚焦口腔细菌的综述扩展了候选机制，也显示微生物检出、抗体反应、口腔疾病状态和痴呆结局经常来自不同人群[@liu2023oralbacteriaad]。较新的证据评价仍把牙周炎视为潜在风险标志，同时要求更强的纵向和干预设计[@kim2025periodontitisdementia]。

纵向观察提供时间信息，但仍易受混杂和反向因果影响。一项AD队列研究观察到牙周炎与后续认知下降及促炎状态相关[@ide2016periodontitis]。公共数据和文本挖掘分析也提出了共享分子信号[@jiang2021periodontitis]。这类研究可用于优选通路，却不能判断牙周暴露是否导致神经退行性改变、早期认知受损是否改变口腔健康，或二者是否共同受年龄、吸烟、糖尿病、药物、虚弱、社会经济条件和医疗可及性影响。

遗传工具研究为单向正面叙事提供了重要制衡。两样本孟德尔随机化分析没有建立牙周病遗传风险对AD的因果效应[@hu2024mendelian]。更广泛的孟德尔随机化综合同样说明，牙周炎的系统性影响并未在不同结局和工具选择中得到一致支持[@zhao2026mendelian]。这些结果不能排除所有后天炎症或微生物路径，因为遗传易感性与随时间变化的暴露并不相同；但它们削弱了“仅凭流行病学关联即可证明因果”的说法。

机制实验在受控条件下回答更窄的问题。AD相关死后样本中曾报告*P. gingivalis*物质和牙龈蛋白酶相关信号[@dominy2019pgingivalis]，更早的组织研究也考察了AD脑材料中该菌的存在[@poole2013pg]。野生型小鼠反复口腔暴露可产生脑炎症、神经退行性变化和Aβ相关改变[@ilievski2018oral]。感染神经元体系中也观察到持续牙龈蛋白酶活性和AD样细胞表型[@haditsch2020cor388]。囊泡研究则为浓缩微生物载荷及宿主信号提供一种合理载体[@nara2021omv]。这些研究的优势是机制分辨率，局限是可迁移性：剂量、暴露途径、模型生物、细胞体系、疾病阶段和终点差异使其不能直接外推至自然发生的人体肽暴露。

综合而言，现有文献支持提出研究问题，却没有建立确定通路。人体关联说明问题具有相关性，实验模型证明部分过程具有可能性，而阴性或不确定的因果分析约束解释。可辩护研究应先识别分子实体、追溯来源、证明暴露，再检验预先指定的功能。本研究仅处理这一证据序列中的前端计算步骤。

### 从牙周生态位到脑组织的候选路径

牙周菌群失调可能通过多条非互斥路径与神经退行性过程连接。第一条是间接路径：慢性牙周炎症可改变循环细胞因子、急性期反应、内皮激活或免疫细胞状态，从而在不需要活菌进入脑组织的情况下影响神经血管和胶质功能[@chalmers2025primer]。第二条涉及组织炎症或日常机械扰动期间细菌细胞或可溶性产物的间歇播散。第三条涉及外膜囊泡，其可保护并浓缩脂质、蛋白质、核酸和其他细菌载荷[@ho2015omv]。第四条涉及特定酶或分子片段，包括可能修饰宿主底物的牙龈蛋白酶相关产物[@guo2010gingipain]。这些路径在人类中的相对贡献仍不确定。

每条路径要求不同证据。炎症路径需要暴露—反应和中介证据；播散路径需要口腔与系统区室中匹配的分子身份；囊泡路径需要载荷表征、生物分布和屏障转运数据；直接肽路径还需要证明smORF被翻译、肽能够耐受加工与蛋白水解，并以足够浓度到达相关组织。BBB预测不能满足这些要求，因为通透性还取决于肽构象、电荷、转运机制、血清结合、降解、外排和实验背景。

微生物编码的小蛋白和小肽在这一框架中仍研究不足。短分子原则上可以是配体、酶调节剂、膜活性物质、免疫信号、金属结合分子或无活性的降解产物。因此，假设空间很广，但广泛合理性不是特定序列的证据。尚未解决的分子空白是：是否存在可追溯的口腔微生物肽，在相关生态背景中表达、离开口腔并产生可重复的神经或血管效应。计算优选只有在缩小候选空间的同时保留这些连续证据要求时才有价值。

### 微生物组smORF是合理但技术困难的发现空间

smORF长期存在系统性漏注释，因为短编码区难以与随机开放阅读框区分，可提供的系统发育信号有限，而且常低于面向常规基因的识别阈值。对人类相关微生物组的大规模分析仍识别出数千个保守小基因家族，其中许多缺少已知结构域[@sberro2019smallgenes]。专用注释方法通过整合谱模型、编码特征、保守性和其他证据，而不是套用常规蛋白长度阈值，提高发现能力[@durrant2021sorf]。高分辨率多组学则可把预测与转录和蛋白质组观察相连接，从而提高候选可信度[@davin2026multiomics]。

但验证序列依然严格。预测smORF不一定被转录；转录本不一定被翻译；肽谱匹配不一定唯一或归属正确；被检出的肽也不一定稳定或具有功能。短ORF生物学综述强调正交验证和谨慎命名[@couso2017sorfs]。蛋白质基因组研究同样表明，翻译证据必须结合组织、阅读框、错误发现和功能背景解释[@vanheesch2019heart]。在宏基因组中，组装碎片、同源序列、菌株变异和六框翻译会进一步产生数百万短候选。

口腔序列与宏蛋白质组资源提供互补但不等价的证据。HOMD和eHOMD整理口腔及呼吸消化道分类和基因组信息[@chen2010homd]。唾液宏蛋白质组可在自身样本和错误发现框架内支持肽检出[@belstrom2016metaproteomics]。肺癌口腔宏蛋白质组则提供另一种背景特异性观察空间[@jiang2022oralmetaproteomics]。当代唾液宏蛋白质组流程强调宿主去除、微生物富集、肽和蛋白层面错误控制、分类歧义及公共原始数据保存[@yuan2025osample]。与任一资源精确匹配可支持序列存在或曾被观察，但不能单独建立当前疾病标注分支中的表达。

因此，样本层面来源链不可缺少。疾病比较需要把序列连接到contig、组装或bin、标本、参与者、口腔位点、临床分组和处理批次。缺少这条链时，候选计数只是计算记账单位，不是独立生物学重复。当前记录保留汇总分支标签和计数，但缺少估计流行度、富集、分类来源和参与者间不确定性所需的逐行映射。因此，本文使用“牙周炎标注分支”，而不是“牙周炎特异肽组”。

### 深度学习引导的优选是分流而非验证

smORF搜索空间的规模促使研究使用序列模型，但模型输出继承训练数据的假设和适用域限制。UniDL4BioPep以预训练ESM-2生成上下文嵌入，再通过任务特异性卷积神经网络完成肽活性分类[@du2023unidl4biopep]。蛋白质语言模型能够捕获难以人工编码的序列规律，但输出分数仍是模型特异值；除非在可比较的序列和任务域中完成校准，否则不能把它解释为生物学概率。

BBB肽预测可说明这一局限。Augur整合工程化描述符、特征选择、类别平衡和随机森林分类器，并非深度学习模型[@gu2024bbb]。B3BPFN则代表不同的模型家族和数据集构建方式[@liu2026b3bpfn]。阳性集合定义、去冗余、阴性采样、序列长度、类别平衡和验证设计差异都会实质影响表观性能。极短、富亮氨酸、带正电或组成异常的微生物组肽可能位于模型评估分布之外。因此，“BBB高分”只定义优选阈值，不等于实测转运。

下游工具同样具有异质性。NTxPred2肽模式在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[@rathore2025ntxpred2]。Mebipred使用工程化序列描述符和两级人工神经网络框架，估计一般及离子相关金属结合潜力[@aptekmann2022mebipred]。AnOxPePred使用一维卷积和多任务输出预测自由基清除与螯合相关性质[@olsen2020anoxpepred]。这些工具的串联一致不是正交重复，因为模型重复使用序列组成，训练终点不同，还可能沿漏斗传播相关偏倚。

恰当解释是计算分流。“神经毒性阳性”不是神经元毒性，“金属结合阳性”不是实测解离常数或配位几何，CHEL和FRS输出也不是氧化还原化学。微生物组肽挖掘的有力先例表明，计算候选只有经过合成和受控功能实验后才成为生物学发现[@torres2024peptideantibiotics]。对于纯计算研究，科学贡献应是透明缩小候选空间、准确描述模型、提示适用域风险，并可重复记录仍未检验的内容。

### AChE、金属稳态、对接与分子动力学构成结构假设

AChE提供一个具有生物学依据但要求严格的结构随访方向。除水解乙酰胆碱外，AChE可加速Aβ纤维装配[@inestrosa1996ache]。AChE特定基序被认为可促进Aβ纤维形成[@deferrari2001motif]，PAS定向配体则可在生化体系中抑制AChE诱导的Aβ聚集[@bartolini2003pas]。结构研究描绘了连接催化区域与外周位点的芳香性峡谷[@kryger1999e2020]。PDB 4EY6所代表的人AChE结构为配体导向问题提供实验确定的受体框架[@cheung2012ache]。这些发现支持提出“候选肽能否稳定占据AChE某一区域”，但不能建立结合、抑制或Aβ效应。

柔性7–9残基肽的对接尤其不确定，因为肽质子化、端基、初始构象、受体柔性、搜索空间位置、评分随机性和对接后精修均可改变排序。AutoDock Vina适合初筛，但其分数不是实验亲和力或结合自由能[@trott2010vina]。后续Vina实现扩展了方法和接口，却没有消除完整制备及执行记录的必要性[@eberhardt2021vina]。FlexPepDock等肽特异精修方法体现了透明初筛后可采用的更高分辨率标准[@london2011flexpepdock]。

分子动力学（MD）可以在规定力场和溶剂模型下检验制备复合物是否停留于某一构象区域，但不能挽救无法追溯或制备不充分的对接构象。已发表AChE–Aβ模拟显示肽的停留位置和接触可随时间改变[@atanasova2020md]，加速模拟也说明可以探索AChE表面的替代相互作用[@lushchekina2017amd]。对当前候选而言，有意义的MD需要版本化起始坐标、拓扑和质子化决策、独立种子轨迹、收敛性评价及预先指定分析。正在开展的MD扩展将在预设轨迹分析和质量控制完成后评价驻留行为、构象稳定性及接触持续性。

金属生物学构成第二个结构假设。铜、铁和锌稳态失衡与Aβ聚集、氧化还原化学、脂质过氧化和神经元损伤相交[@bush2013metal]。更广义的元素组学视角把这些相互作用置于网络而非单金属机制中[@lei2021elements]。含组氨酸和半胱氨酸的肽可能具有配位基团，但组成不能决定亲和力、选择性、化学计量、几何、氧化态或氧化还原结果。Tau片段实验显示Cu(II)配位可改变肽结构和Aβ聚集[@dinatale2018tau]；tau26–44进一步说明如何通过专门实验把短动态肽连接到膜和细胞表型[@perini2019tau]。细菌淀粉样蛋白暴露也可改变模型系统中的聚集表型[@chen2016curli]。这些研究提供可检验比较对象，而不是可转移的活性。

### 知识空白与研究目标

现有文献共同指向一个边界清楚但尚未解决的问题：牙周炎与AD之间存在异质性观察关联，*P. gingivalis*提供菌种层面的机制合理性，而口腔微生物组编码庞大且尚未充分表征的短肽空间。真正缺失的是一条可追溯分子链，即把特定微生物smORF依次连接到翻译、宿主暴露、BBB通过、靶点作用及疾病相关表型。任何单一计算评分都不能跨越这些层次。

本研究聚焦更早且更窄的问题：现有口腔smORF汇总数据能否形成逻辑一致的候选优选漏斗，以及另一份AChE对接汇总能否在不把方法信息缺失转化为生物学确定性的前提下得到解释。我们重算比例、检查分支算术和预测器适用范围、表征所提供的12条序列，并把AChE评分顺序作为描述性结果保留；同时给出具有预设轨迹输出的前瞻性MD扩展。因此，本研究提供的是计算假设集合，而不是新预测器、临床队列分析、独立重现的对接研究或经验证的AD机制。

## 材料与方法

### 研究设计与数据范围

本研究为纯计算二次分析，使用汇总候选计数、模型汇总结果、一张12条序列表及其AChE对接评分表。本文未开展参与者招募、标本采集、湿实验、新组学处理、预测器再训练或对接重跑；MD轨迹分析作为预设扩展正在进行。健康与牙周炎标签仅作为所提供的分支标签保留，不解释为已经核实的候选层面疾病归属。

现有材料不包含完整漏斗的候选核苷酸或氨基酸逐行数据、基因组坐标、受试者/样本映射、登录号与分组对应关系、bin清单、分类学信息、肽谱匹配、完整模型输出、运行日志或原始发现管线。因此，无法估计参与者层面的患病率或富集，不能进行菌种归属，也不能逐行重建最终筛选过程。

### 公共登录号、候选构建与序列证据过滤

汇总分析涉及公共登录号PRJNA678453和PRJEB65451。PRJNA678453是配对口腔宏基因组和宏转录组数据的来源项目[@belstrom2021periodontitis]。PRJEB65451并非独立临床队列，而是由PRJNA678453衍生、使用metaSPAdes v3.15.3组装并由EBI-EMG/MGnify代理的第三方注释宏基因组组装项目。由于缺少一致的样本—组装映射和bin层面清单，本文不报告参与者、标本、组装分析或宏基因组组装基因组总数。

所提供分析保留编码4–50 aa肽的smORF，并形成分别含11,269,961条和11,721,988条候选的健康标记库与牙周炎标记库。候选与指定口腔序列和蛋白质组资源进行精确匹配，包括HOMD/eHOMD以及PXD003151、PXD004319和PXD026727数据集，随后去冗余[@chen2010homd; @escapa2018ehomd; @belstrom2016metaproteomics; @jiang2022oralmetaproteomics; @yuan2025osample]，得到31,510条健康标记候选和33,786条牙周炎标记候选。过滤后集合分为短肽分支（5–30 aa：30,557条和32,754条）与长肽分支（31–50 aa：953条和1,032条）。初始规则纳入4 aa候选，但下游分箱从5 aa开始，因此无法确定4 aa序列的去向。跨资源精确匹配被视为序列支持信息，而不是研究队列内表达的证明。

### 深度学习引导的候选优选

第一层功能优选采用UniDL4BioPep。其文献所述架构使用预训练ESM-2模型`esm2_t6_8M_UR50D`，把每条肽编码为320维上下文嵌入，随后输入用于二分类肽活性任务的六层任务特异性卷积神经网络[@du2023unidl4biopep]。所提供分析采用≥0.80阈值，包括BBB任务。由于缺少该极短肽域中的校准信息，本文把输出称为“模型阳性”或“BBB高分”，而不表述为实测转运或已确认活性。已发表BBB预测器采用异质架构和数据集，也限制了性能估计向本研究候选的直接迁移[@gu2024bbb] [@liu2026b3bpfn]。

随后采用NTxPred2的肽模式评价牙周炎标记BBB高分集合。该模型在神经毒性肽序列上微调ESM2-t30蛋白质语言模型[@rathore2025ntxpred2]。分析限于文献所述7–50 aa适用范围，较短候选记为超出模型覆盖，而不是阴性。Cu、Fe和Zn相关结合潜力采用mebipred评价。该无比对方法把氨基酸组成、理化描述符和金属结合5-mer频率整合到两级人工神经网络框架中，包括一般金属结合网络及离子特异性分类器[@aptekmann2022mebipred]，判定阈值为0.50。

抗氧化相关性质采用多任务深度卷积神经网络AnOxPePred评价。经one-hot编码的序列依次通过一维卷积层、平均池化和256单元全连接层，分别产生自由基清除（FRS）和螯合（CHEL）输出[@olsen2020anoxpepred]。分析三个操作性终点：CHEL≥0.25；CHEL≥0.25且FRS<0.50；CHEL≥0.25且FRS<0.45。本研究未重新训练任何模型。由于缺少逐行输出和NTxPred2至mebipred的候选交接表，多模型一致仅解释为串行计算分流，不构成相互独立的生物学确认。

### 序列表征与对接评分分析

另一张表包含12条被描述为CHEL/FRS主集合的肽序列。因缺少稳定标识符和序列层面的CHEL/FRS值，无法确认这些序列是否对应汇总漏斗终点的12行。我们直接依据序列字符串重算长度，以及组氨酸、半胱氨酸、碱性残基（Arg+Lys）和芳香残基（Phe+Tyr+Trp）数量，并要求序列互不重复且仅由标准氨基酸构成。

现有对接汇总称，12条肽使用AutoDock Vina 1.2.5对接人AChE结构PDB 4EY6，搜索盒为以外周阴离子位点为中心的40×40×40 Å³区域[@cheung2012ache; @trott2010vina; @eberhardt2021vina]。本研究转录均值和标准差并检查数值范围及排序，仅进行描述性分析。由于缺少制备后的受体和配体结构、PDBQT文件、精确盒中心、质子化和电荷设置、配置、exhaustiveness、运行次数、随机种子、原始分数、日志、构象及相互作用表，本研究未重跑对接。Vina数值仅视为筛选评分，不解释为结合亲和力或自由能。在缺少逐次运行信息时，标准差也无法对应已知的重复单位。

### 前瞻性分子动力学方案

前瞻性100 ns MD方案用于游离人AChE以及标记为ALLLHRC、FLLHTTR和YLSLLQR的AChE复合物。计划采用GROMACS[@abraham2015gromacs]、Amber99SB-ILDN力场[@lindorfflarsen2010amber]、TIP3P水模型、溶质至盒边界1.0 nm的三斜周期盒，并在中和后加入0.15 mol/L NaCl。能量最小化设定为2,000步最速下降，并对重原子施加1,255 kJ mol⁻¹ nm⁻²位置约束。平衡过程包括1.0 ns约束NVT升温（10至300 K）、1.0 ns约束NPT平衡，以及300 K、1 bar条件下1.0 ns无约束NPT平衡。

前瞻性生产阶段为100 ns，步长2 fs；含氢键采用LINCS约束，实空间截断为1.2 nm，范德华相互作用在1.0 nm后采用力切换，静电作用采用粒子网格Ewald法，温度耦合采用velocity-rescale方法，压力耦合采用Berendsen方法。坐标每20 ps保存一次，即每条轨迹计划得到5,000帧。预设分析包括复合物、AChE和肽层面的RMSD与RMSF、回转半径、溶剂可及表面积、径向分布函数、DSSP二级结构、氢键、残基接触及桥连水。完整起始坐标、末端与质子化状态、拓扑、随机种子、重复设计、运行日志、轨迹、检查点、能量和最终坐标是接纳轨迹分析的必要条件。轨迹处理与质量控制正在进行；稳定性、收敛性、接触及体系间比较结果将在预设分析完成后补充。

### 统计分析

所有分析均为描述性分析。比例按100×n/N并使用各转换阶段的明确分母计算。候选序列是嵌套于样本、组装、基因组和同源序列组的计算单位，而不是独立生物学重复。在缺少受试者或样本—候选逐行数据时，对汇总肽计数进行Fisher或χ²检验会造成伪重复。因此，本研究不计算健康与牙周炎比较的p值、置信区间、效应量、ROC、功效或多重校正。分支求和、分子≤分母约束、已评估/未评估分区、下游单调性、8/12阈值敏感性、序列组成和评分排序均采用确定性方式核对。

## 结果

### 序列证据过滤使两个smORF库均缩减99.7%以上

健康标记分支和牙周炎标记分支分别始于11,269,961条和11,721,988条smORF。经序列证据过滤和去冗余后，分别保留31,510条（0.2796%）和33,786条（0.2882%）候选（表1）。短肽与长肽分支之和均等于相应过滤后总数。这些比例描述计算保留率，不代表参与者患病率或疾病富集。

**表1. 汇总候选库及BBB高分输出。**

| 分支 | 原始smORF | 证据过滤后 | 短肽背景（5–30 aa） | 短肽BBB高分，n（%） | 长肽背景（31–50 aa） | 长肽BBB高分，n（%） |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 健康标记 | 11,269,961 | 31,510 | 30,557 | 3,359（10.99） | 953 | 40（4.20） |
| 牙周炎标记 | 11,721,988 | 33,786 | 32,754 | 3,446（10.52） | 1,032 | 72（6.98） |

两个分支的短肽BBB高分率分别为10.99%和10.52%，长肽分支分别为4.20%和6.98%。牙周炎标记分支包含3,446条短肽和72条长肽BBB高分输出，总计3,518条，其中97.95%属于短肽分支。所提供的短肽长度汇总包括5–7 aa 547条、8–15 aa 2,893条和16–30 aa 6条，另有72条长肽为31–50 aa。由于缺少逐行身份，无法分析重叠、分类学归属和参与者分布。

广义抗菌输出几乎完全为阳性：健康标记短肽中30,537/30,557条（99.93%）、牙周炎标记短肽中32,721/32,754条（99.90%）超过共同0.80阈值。这种饱和现象不太可能反映具有实验活性的口腔抗菌肽比例，更可能提示序列域偏移、校准不足或该标签不适合采用共同阈值。

### 串行模型筛选形成12条和8条候选终点

NTxPred2评价了3,299/3,518条牙周炎标记BBB高分候选（93.77%），另有219/3,518条（6.23%）低于模型适用长度。在已评估候选中，923/3,299条（27.98%）为模型阳性。后续汇总计数依次为111条mebipred阳性、15条CHEL≥0.25、12条CHEL≥0.25且FRS<0.50，以及8条CHEL≥0.25且FRS<0.45（表2）。收紧FRS阈值后保留主集合的8/12（66.67%）。由于缺少逐行交接数据，不能把111/923解释为已验证转换率。

**表2. 牙周炎标记分支的汇总优选结果。**

| 阶段 | 操作规则 | n | 分母或限制 |
| --- | --- | ---: | --- |
| 短肽BBB高分 | UniDL4BioPep BBB输出≥0.80；5–30 aa | 3,446 | 32,754条短肽候选 |
| 长肽BBB高分 | UniDL4BioPep BBB输出≥0.80；31–50 aa | 72 | 1,032条长肽候选 |
| BBB高分总计 | 短肽+长肽 | 3,518 | 算术和 |
| NTxPred2已评估 | 规定范围7–50 aa | 3,299 | 3,518条BBB高分候选 |
| NTxPred2未评估 | 低于规定范围 | 219 | 3,518条BBB高分候选 |
| NTxPred2阳性 | 模型阳性标签 | 923 | 3,299条已评估候选 |
| 金属结合阳性 | Mebipred输出≥0.50 | 111 | 缺少逐行交接 |
| CHEL优先 | CHEL≥0.25 | 15 | 111条金属阳性候选 |
| 主集合 | CHEL≥0.25且FRS<0.50 | 12 | 111条金属阳性候选 |
| 严格子集 | CHEL≥0.25且FRS<0.45 | 8 | 序列成员未知 |

### 12条所提供序列具有可区分的组成特征

另一张序列表包含12条互不重复、仅由标准氨基酸组成的肽，长度为7–9个残基（表3）。其中11条含组氨酸，6条含半胱氨酸，每条均至少含一个Arg或Lys。这些特征可用于合成规划和假设设计，但不能证明金属结合、BBB转运、毒性、分类学归属，也不能证明其对应汇总终点的12行。由于缺少序列层面FRS标签，严格8/12子集的身份仍未知。

**表3. 12条序列及重算组成。**

| Vina均值排序 | 序列 | 长度 | His | Cys | Arg+Lys | Phe+Tyr+Trp |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | FLLHTTR | 7 | 1 | 0 | 1 | 1 |
| 2 | YLSLLQR | 7 | 0 | 0 | 1 | 1 |
| 3 | ALLLHRC | 7 | 1 | 1 | 1 | 0 |
| 4 | FCLHLQLR | 8 | 1 | 1 | 1 | 1 |
| 5 | YHHLLCRR | 8 | 2 | 1 | 2 | 1 |
| 6 | LLHLPKRTT | 9 | 1 | 0 | 2 | 0 |
| 7 | LLHPLRL | 7 | 1 | 0 | 1 | 0 |
| 8 | WLLVHLKK | 8 | 1 | 0 | 2 | 1 |
| 9 | LLHPLRC | 7 | 1 | 1 | 1 | 0 |
| 10 | HLLTLKKHV | 9 | 2 | 0 | 2 | 0 |
| 11 | HLPLLHRCC | 9 | 1 | 2 | 1 | 0 |
| 12 | HVLLLRQCA | 9 | 1 | 1 | 1 | 0 |

### 现有Vina汇总仅提供描述性排序

对接表中的Vina均值范围为−9.60至−8.25 kcal/mol，标准差范围为0.04至0.12（表4）。FLLHTTR、YLSLLQR和ALLLHRC的均值最低，HLPLLHRCC和HVLLLRQCA的均值最高。约1.35 kcal/mol的范围仅描述该评分表。缺少制备输入、运行定义、构象和相互作用文件时，无法评价残基接触、靶位点偏好、亲和力或功能活性。

**表4. 人AChE PDB 4EY6的现有AutoDock Vina汇总。**

| 排名 | 序列 | 平均评分（kcal/mol） | SD |
| ---: | --- | ---: | ---: |
| 1 | FLLHTTR | −9.60 | 0.08 |
| 2 | YLSLLQR | −9.49 | 0.05 |
| 3 | ALLLHRC | −9.29 | 0.11 |
| 4 | FCLHLQLR | −9.27 | 0.09 |
| 5 | YHHLLCRR | −9.03 | 0.07 |
| 6 | LLHLPKRTT | −9.01 | 0.06 |
| 7 | LLHPLRL | −8.94 | 0.10 |
| 8 | WLLVHLKK | −8.94 | 0.04 |
| 9 | LLHPLRC | −8.91 | 0.08 |
| 10 | HLLTLKKHV | −8.88 | 0.05 |
| 11 | HLPLLHRCC | −8.35 | 0.12 |
| 12 | HVLLLRQCA | −8.25 | 0.09 |

## 讨论

### 主要发现

本次纯计算分析把庞大的口腔smORF搜索空间缩减为两个边界明确的后续对象：一个12条候选的汇总终点及其8条严格计数，以及一份包含12条明确7–9 aa序列和描述性AChE对接评分的独立清单。汇总算术、预测器适用范围、序列组成和评分排序均可核对，但无法建立漏斗与明确肽清单之间的序列层面对应关系。因此，本研究的主要价值是优选候选并明确后续验证所需信息，而不是证明肽介导的AD机制。

筛选级联不能解释为独立证据的累积。ESM序列表征、序列组成特征和任务特异性训练集可能产生相关误差。短肽分支近乎普遍的抗菌阳性突出显示了这一问题。高于阈值的评分可用于排序，但不能证明BBB转运、神经毒性、金属结合、抗氧化活性或生物暴露。

### 与当前smORF和肽发现标准的关系

当前smORF发现越来越重视编码证据、转录组学、核糖体关联、靶向蛋白质组学、保守性及功能实验的组合[@sberro2019smallgenes; @durrant2021sorf; @davin2026multiomics; @couso2017sorfs; @vanheesch2019heart]。本研究的精确匹配过滤可缩小序列空间，并可能支持某条肽或相关序列曾被观察，但跨异质口腔资源的匹配不能证明其在所提供疾病标记分支中表达。对短肽而言，分类学模糊尤其突出，因为同一短序列可能映射到多个菌种、同源序列或翻译框。

合理的后续研究需要建立候选层面矩阵，把每条序列连接到基因组坐标、组装、样本、临床标签、分类学归属、肽谱证据、预测器评分、适用性标记和最终集合。缺少这一结构时，两个起始库相近的汇总保留率不能解释为富集或缺失，也不能把牙周炎标签转移到单条肽。

### AChE对接假设的解释

AChE外周区域与Aβ组装相关，并可受到配体调节，因此可作为生成结构假设的合理靶点[@inestrosa1996ache; @deferrari2001motif; @bartolini2003pas; @kryger1999e2020; @cheung2012ache]。AutoDock Vina可提供高效的初步评分[@trott2010vina; @eberhardt2021vina]，但7–9 aa柔性肽是困难的对接配体。质子化、末端状态、初始构象、受体柔性、搜索盒位置、exhaustiveness及随机采样均可能改变排序。因此，现有均值仅定义了一个待独立重现的清单，不能作为结合证据。

在未知重复单位时，所列标准差无法得到明确解释。单一靶点和单一方案的评分不能证明选择性、外周位点偏好、催化抑制、Aβ调节或细胞活性。独立重现应使用公开的制备结构、精确参数、多种肽构象和随机种子、全部原始评分与构象，并采用适合肽的柔性精修。FlexPepDock或同类方法可检验排序经柔性精修后是否稳定[@london2011flexpepdock]。MD只能从记录完整且经过检查的起始复合物开始，不能补救不确定的对接构象。

### 金属结合与神经毒性假设

高比例组氨酸和半胱氨酸提供潜在配位基团，但组成和mebipred评分不能确定金属亲和力、选择性、化学计量、几何结构、氧化态或氧化还原后果。金属—肽体系研究表明，这些性质需要直接结构和生物物理测量[@bush2013metal; @lei2021elements; @dinatale2018tau; @perini2019tau]。同样，NTxPred2阳性是序列分类结果，而不是神经元损伤证据。

最低限度的验证应采用互补光谱和热力学方法定量Cu(II)、Fe(II/III)及Zn(II)相互作用，并检测金属依赖的活性氧和脂质过氧化。对照应包括仅肽、仅金属、打乱序列、组成匹配及明确阳性和阴性条件。毒理学研究应在神经元和非神经元细胞中采用浓度—反应设计，并设置膜完整性和非特异性聚集对照。预测结果只能决定实验顺序，不能预先决定实验解释。

### 牙周炎与AD仍是生成假设的研究背景

观察性和纵向研究支持继续考察牙周炎—AD关系，但异质性、混杂、反向因果和阴性遗传因果分析限制了解释[@larvin2023periodontalcognition; @kaliamoorthy2022periodontitisad; @liu2023oralbacteriaad; @kim2025periodontitisdementia; @ide2016periodontitis; @jiang2021periodontitis; @hu2024mendelian; @zhao2026mendelian; @chalmers2025primer]。*P. gingivalis*相关研究支持牙龈蛋白酶、炎症、感染或囊泡相关路径的合理性[@dominy2019pgingivalis; @poole2013pg; @ilievski2018oral; @ho2015omv; @guo2010gingipain; @haditsch2020cor388; @nara2021omv]。这些发现均不能把12条肽归属于*P. gingivalis*，也不能证明其存在于口腔以外。

因此，当前结果不能证明候选具有牙周炎特异性、来源于*P. gingivalis*、在相关口腔群落中被翻译、存在于血液或脑组织，或与AD存在因果关系。建立这条链需要序列—组装—样本映射、队列匹配的表达证据、系统暴露测量、BBB转运实验、靶点作用测定和疾病相关表型。

### 统计解释、验证顺序与局限

候选计数不能替代参与者层面的独立观察。数百万smORF可能在同一样本、组装、基因组或同源序列家族内相关。有效的健康—牙周炎比较需要参与者或样本层面的特征矩阵、预设结局、一致分母、同源性处理，以及考虑聚类和相关协变量的模型。因此，对现有汇总数据而言，描述性比例是可支持的最高分析强度。

验证应按顺序推进。首先，把12条明确序列连接到12条候选终点及8条严格子集，并使用固定模型版本重新生成全部预测器输出。其次，采用队列匹配的宏转录组、条件允许时的核糖体图谱以及具有肽层面错误发现率控制的靶向蛋白质组学检验翻译和表达。再次，对合成肽开展身份、纯度、溶解性、聚集及血清/蛋白酶稳定性测试。只有通过前序步骤的候选才应进入BBB转运、细胞毒性、金属化学、AChE/BChE活性、直接结合和Aβ测定。仅当分子身份、暴露、可重复生化活性及生物学重复表型均得到确认后，才适合进入复杂疾病模型。

本研究的主要局限包括：缺少漏斗逐行数据，汇总终点与明确肽清单之间的关系未解决，缺少原始对接输入和构象，MD轨迹分析仍在进行，以及完全缺少实验测量。候选分类学归属、翻译、队列表达、BBB转运、毒性、金属化学、AChE结合或功能、Aβ效应和疾病关联均未测量。这些限制决定了本研究属于计算优选，而不是机制验证。

## 结论

汇总计算数据支持一条透明的候选优选漏斗，终点为12条主集合和8条严格子集计数。另一张表提供12条明确的7–9 aa肽及AChE Vina评分排序，但无法根据现有材料重建其与漏斗的序列层面连接，也无法重现对接执行。预设MD扩展将在分析和质量控制完成后补充轨迹稳定性与接触结果。当前候选清单适合用于独立计算重现和分阶段实验检验，但不能证明肽表达、*P. gingivalis*来源、BBB通过、神经毒性、金属依赖活性、AChE结合、AD相关性或因果关系。

## 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease. *Lancet*. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4.
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer’s disease at 25 years. *EMBO Mol Med*. 2016;8(6):595–608. doi:10.15252/emmm.201606210.
3. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
4. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
5. Chalmers JC, Hernandez-Kapila YL. The role of the oral microbiome, host response, and periodontal disease treatment in Alzheimer’s disease: a primer. *Periodontol 2000*. 2025;98(1):220–227. doi:10.1111/prd.12631.
6. Belstrøm D, Constancias F, Drautz-Moses DI, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. *npj Biofilms Microbiomes*. 2021;7:76. doi:10.1038/s41522-021-00247-y.
7. Ovsepian A, Kardaras FS, Skoulakis A, Hatzigeorgiou AG. Microbial signatures in human periodontal disease: a metatranscriptome meta-analysis. *Front Microbiol*. 2024;15:1383404. doi:10.3389/fmicb.2024.1383404.
8. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors. *Periodontol 2000*. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x.
9. Ho MH, Chen CH, Goodwin JS, et al. Functional advantages of *Porphyromonas gingivalis* vesicles. *PLoS One*. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448.
10. Larvin H, Gao C, Kang J, et al. The impact of study factors in the association of periodontal disease and cognitive disorders. *Age Ageing*. 2023;52(2):afad015. doi:10.1093/ageing/afad015.
11. Kaliamoorthy S, Nagarajan M, Sethuraman V, et al. Association of Alzheimer’s disease and periodontitis. *Med Pharm Rep*. 2022;95(2):144–151. doi:10.15386/mpr-2278.
12. Liu S, Dashper SG, Zhao R. Association between oral bacteria and Alzheimer’s disease. *J Alzheimers Dis*. 2023;91(1):129–150. doi:10.3233/JAD-220627.
13. Kim J, Han DH. Periodontitis as a risk factor for dementia. *J Evid Based Dent Pract*. 2025;25:102094. doi:10.1016/j.jebdp.2025.102094.
14. Ide M, Harris M, Stevens A, et al. Periodontitis and cognitive decline in Alzheimer’s disease. *PLoS One*. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081.
15. Jiang Z, Shi Y, Zhao W, et al. Association between chronic periodontitis and the risk of Alzheimer’s disease. *BMC Oral Health*. 2021;21:466. doi:10.1186/s12903-021-01827-2.
16. Hu C, Li H, Huang L, et al. Periodontal disease and risk of Alzheimer’s disease: a two-sample Mendelian randomization. *Brain Behav*. 2024;14(4):e3486. doi:10.1002/brb3.3486.
17. Zhao Y, Zhang C, Chang X, et al. Causal association between periodontitis and systemic diseases: a systematic review and meta-analysis of Mendelian randomization studies. *BMC Oral Health*. 2026;26:383. doi:10.1186/s12903-026-07725-9.
18. Dominy SS, Lynch C, Ermini F, et al. *Porphyromonas gingivalis* in Alzheimer’s disease brains. *Sci Adv*. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333.
19. Poole S, Singhrao SK, Kesavalu L, et al. Determining the presence of *Porphyromonas gingivalis* in Alzheimer’s disease brain. *J Alzheimers Dis*. 2013;33(3):665–678. doi:10.3233/JAD-2012-121149.
20. Ilievski V, Zuchowska PK, Green SJ, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. *PLoS One*. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941.
21. Haditsch U, Roth T, Rodriguez L, et al. Alzheimer’s disease-like neurodegeneration in *Porphyromonas gingivalis* infected neurons with persistent expression of active gingipains. *J Alzheimers Dis*. 2020;75(4):1361–1376. doi:10.3233/JAD-200393.
22. Nara PL, Sindelar D, Penn MS, et al. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis. *J Alzheimers Dis*. 2021;82(4):1417–1450. doi:10.3233/JAD-210448.
23. Sberro H, Fremin BJ, Zlitni S, et al. Large-scale analyses of human microbiomes reveal thousands of small, novel genes. *Cell*. 2019;178(5):1245–1259.e14. doi:10.1016/j.cell.2019.07.016.
24. Durrant MG, Bhatt AS. Automated prediction and annotation of small open reading frames in microbial genomes. *Cell Host Microbe*. 2021;29(1):121–131.e4. doi:10.1016/j.chom.2020.11.002.
25. Davin ME, Ortís Sunyer J, Delgado LF, et al. High-resolution multi-omics enhances prediction and detection of smORF-encoded proteins in the human gut microbiome. *Nat Commun*. 2026. doi:10.1038/s41467-026-72762-5.
26. Couso JP, Patra P. Short ORFs: finding gems in hidden places. *Curr Opin Genet Dev*. 2017;45:14–21. doi:10.1016/j.gde.2017.04.002.
27. van Heesch S, Wit F, Botter J, et al. The translational landscape of the human heart. *Cell*. 2019;178(1):236–251.e24. doi:10.1016/j.cell.2019.05.010.
28. Chen T, Yu WH, Izard J, et al. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. *Database (Oxford)*. 2010;2010:baq013. doi:10.1093/database/baq013.
29. Belstrøm D, Jersie-Christensen RR, Lyon D, et al. Metaproteomics of saliva identifies human protein markers specific for individuals with periodontitis and dental caries compared to orally healthy controls. *PeerJ*. 2016;4:e2433. doi:10.7717/peerj.2433.
30. Jiang X, Zhang Y, Wang H, et al. In-depth metaproteomics analysis of oral microbiome for lung cancer. *Research*. 2022;2022:9781578. doi:10.34133/2022/9781578.
31. Yuan J, Sun B, Li M, et al. OSaMPle workflow for salivary metaproteomics analysis reveals dysbiosis in inflammatory bowel disease patients. *npj Biofilms Microbiomes*. 2025;11:63. doi:10.1038/s41522-025-00692-z.
32. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. *Brief Bioinform*. 2023;24(3):bbad135. doi:10.1093/bib/bbad135.
33. Gu ZF, Hao YD, Wang TY, et al. Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur. *BMC Biol*. 2024;22:86. doi:10.1186/s12915-024-01883-4.
34. Liu X, Zhao Z, Guan J, et al. Prediction of blood-brain barrier-penetrating peptides using B3BPFN. *Front Mol Biosci*. 2026;13:1858506. doi:10.3389/fmolb.2026.1858506.
35. Rathore AS, Jain S, Choudhury S, Raghava GPS. A large language model for predicting neurotoxic peptides and neurotoxins. *Protein Sci*. 2025;34(8):e70200. doi:10.1002/pro.70200.
36. Aptekmann AA, Buongiorno J, Giovannelli D, et al. mebipred: identifying metal-binding potential in protein sequence. *Bioinformatics*. 2022;38(14):3532–3540. doi:10.1093/bioinformatics/btac358.
37. Olsen TH, Yesiltas B, Marin FI, et al. AnOxPePred: using deep learning for the prediction of antioxidative properties of peptides. *Sci Rep*. 2020;10:21471. doi:10.1038/s41598-020-78319-w.
38. Torres MDT, Brooks EF, Cesaro A, et al. Mining human microbiomes reveals an untapped source of peptide antibiotics. *Cell*. 2024;187(19):5453–5467.e15. doi:10.1016/j.cell.2024.07.027.
39. De Ferrari GV, Canales MA, Shin I, et al. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. *Biochemistry*. 2001;40(35):10447–10457. doi:10.1021/bi0101392.
40. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. *Biochem Pharmacol*. 2003;65(3):407–416. doi:10.1016/s0006-2952(02)01514-9.
41. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept). *Structure*. 1999;7(3):297–307. doi:10.1016/s0969-2126(99)80040-9.
42. Cheung J, Rudolph MJ, Burshteyn F, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. *J Med Chem*. 2012;55(23):10282–10286. doi:10.1021/jm300871x.
43. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function. *J Comput Chem*. 2010;31(2):455–461. doi:10.1002/jcc.21334.
44. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203.
45. London N, Raveh B, Cohen E, et al. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. *Nucleic Acids Res*. 2011;39:W249–W253. doi:10.1093/nar/gkr326.
46. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
47. Lushchekina SV, Kots ED, Novichkova DA, et al. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. *BioNanoScience*. 2017;7:396–402. doi:10.1007/s12668-016-0375-x.
48. Bush AI. The metal theory of Alzheimer’s disease. *J Alzheimers Dis*. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011.
49. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer’s disease. *J Biol Chem*. 2021;296:100105. doi:10.1074/jbc.REV120.008207.
50. Di Natale G, Bellia F, Sciacca MFM, et al. Tau-peptide fragments and their copper(II) complexes: effects on amyloid-β aggregation. *Inorg Chim Acta*. 2018;472:82–92. doi:10.1016/j.ica.2017.09.061.
51. Perini G, Ciasca G, Minelli E, et al. Dynamic structural determinants underlie the neurotoxicity of the N-terminal tau 26–44 peptide. *Int J Biol Macromol*. 2019;141:278–289. doi:10.1016/j.ijbiomac.2019.08.220.
52. Chen SG, Stribinskis V, Rane MJ, et al. Exposure to the functional bacterial amyloid protein curli enhances alpha-synuclein aggregation. *Sci Rep*. 2016;6:34477. doi:10.1038/srep34477.
53. Escapa IF, Chen T, Huang Y, et al. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database. *mSystems*. 2018;3(6):e00187-18. doi:10.1128/mSystems.00187-18.
54. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
55. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
