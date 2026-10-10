# Abstract / intro / methods. Keys = prefixes in English backup or current Chinese.

EN_FRONT = {
    "Periodontitis has been tied to Alzheimer’s disease": (
        "Periodontitis has been linked to Alzheimer’s disease (AD) in epidemiological "
        "and experimental studies, but it remains unclear whether oral microbial "
        "molecules could take part in processes related to amyloid-β (Aβ) assembly. "
        "This study aimed to screen oral microbe-derived short peptides that may "
        "interact with the peripheral anionic site (PAS) of human acetylcholinesterase "
        "(AChE), and to assess possible modes of interaction by molecular simulation. "
        "sORFs were predicted with EMBOSS getorf from PRJNA678453 metagenome-assembled "
        "genomes and scored with UniDL4BioPep. Periodontitis-labelled candidates were "
        "then matched to oral genomic and metaproteomic catalogues and reduced with "
        "NTxPred2, mebipred and AnOxPePred to twelve explicit peptides. All twelve are "
        "7–9 residues, net-positive at pH 7.4, and leucine-rich. The twelve ligands "
        "were docked into human AChE; apo enzyme and three representative complexes "
        "were then run for 100-ns MD. Docking placed FLLHTTR, YLSLLQR and LLHPLRL near "
        "the PAS. Relative to apo AChE, the FLLHTTR and YLSLLQR complexes adopted more "
        "compact overall conformations; FLLHTTR showed a richer intermolecular "
        "hydrogen-bond network, and YLSLLQR a reduced solvent-accessible surface. These "
        "features are conformational and contact descriptors, not proof of tighter "
        "binding. The calculations suggest that some oral micropeptides may interact "
        "with AChE-PAS. They supply computational evidence for a possible peptide-level "
        "link between periodontitis and AD-related AChE–Aβ biology, and they nominate "
        "candidates for later binding and Aβ-aggregation assays."
    ),
    "Alzheimer’s disease (AD) combines amyloid deposition": (
        "Alzheimer’s disease (AD) combines amyloid deposition, tau pathology, synaptic "
        "failure, immune activation and vascular injury over a long preclinical course "
        "[1]. Sequential cleavage of APP by β- and γ-secretases releases Aβ40 and Aβ42; "
        "soluble oligomers injure synapses; familial APP/PSEN mutations change peptide "
        "length and amount [2]. Amyloid load does not explain the spatial or clinical "
        "heterogeneity of the disease, so peripheral inflammatory exposures have been "
        "examined as possible modifiers of vulnerability rather than as single "
        "sufficient causes. Clarifying possible molecular links between peripheral "
        "chronic inflammation and AD-related pathology is therefore one route into that "
        "heterogeneity. Beyond inflammatory signalling itself, whether microbial "
        "products can take part in protein interactions related to Aβ generation, "
        "assembly or synaptic failure remains an open question."
    ),
    "Gingipains and outer-membrane vesicles of Porphyromonas gingivalis": (
        "Gingipains and outer-membrane vesicles of Porphyromonas gingivalis supply one "
        "mapped virulence pair [12–13]. The organism and gingipains have been reported "
        "in AD brains [14], and repeated oral infection in mice produces "
        "neuroinflammation and Aβ-related changes [15]. Those observations justify "
        "looking at oral products. They do not, by themselves, name a peptide that "
        "occupies AChE. Existing work has mainly tracked named pathogens, virulence "
        "factors and inflammatory responses. Whether short peptides encoded by the oral "
        "microbiome could themselves take part in AD-related protein interactions is "
        "still poorly defined. Short microbial peptides are a candidate class because "
        "they are compact and chemically diverse. Nominating such peptides and testing "
        "them against an AD-related target would move the periodontitis–AD association "
        "onto a more specific molecular footing."
    ),
    "Microbiome smORFs encode a large pool of uncharted small proteins": (
        "Microbiome smORFs encode a large pool of uncharted small proteins [16–17]. "
        "Mining of human microbiomes for peptide antibiotics first scored millions of "
        "translated open reading frames and then applied experimental filters [18]. "
        "UniDL4BioPep supplies more than twenty binary bioactivity heads on ESM-2 "
        "embeddings [19]. Sequence-based scores can only rank candidates; they cannot "
        "prove a protein-binding activity or locate a pose on a target surface. After a "
        "shortlist exists, docking and MD are needed to ask whether an interaction with "
        "AChE-PAS is geometrically plausible and what conformational features it would "
        "have. Combining sequence filters with that structural step narrows a large "
        "oral-encoded set to a smaller list that later assays can test."
    ),
    "Molecular docking and MD are the usual next step once a ligand list exists.": (
        "Molecular docking and MD are the usual next step once a ligand list exists. "
        "Accelerated MD places Aβ on the AChE surface and treats the enzyme as a "
        "nucleation centre [20]. A 1-μs PAS-centred AChE–Aβ trajectory remains bound, "
        "with the main residence at residues 344–361 [21]. PDB 4EY6 gives a 2.40 Å "
        "human AChE frame [22]. The aromatic gorge that joins the catalytic triad to "
        "the PAS was mapped on Torpedo AChE [23]. Docking can assess whether oral short "
        "peptides may interact with that same PAS; MD can assess conformational "
        "features of the complex. What remains missing is that peptide-level test, "
        "drawn from oral smORFs rather than from Aβ itself."
    ),
    "Here we called sORFs with EMBOSS getorf": (
        "On that background, this study aimed to screen oral microbiome-encoded short "
        "peptides that may interact with the PAS of AChE, and to assess possible modes "
        "of interaction by computation. We hypothesise that some oral-encoded short "
        "peptides have sequence and physicochemical features compatible with AChE-PAS "
        "occupancy, and that those peptides therefore deserve to be examined for a "
        "possible role in AChE-related Aβ assembly. sORFs were predicted with EMBOSS "
        "getorf from PRJNA678453 MAGs and scored with 22 UniDL4BioPep heads; "
        "periodontitis-labelled candidates were matched to oral genomic and "
        "metaproteomic catalogues and reduced with NTxPred2, mebipred and AnOxPePred. "
        "Twelve short peptides were then modelled with AlphaFold3 and docked into human "
        "AChE. Apo AChE and three representative complexes—the two strongest PAS poses "
        "(FLLHTTR, YLSLLQR) and the strongest catalytic-site pose (ALLLHRC)—were "
        "simulated for 100 ns to inspect conformational change, intermolecular contacts "
        "and apparent stability on that window. The aim is to nominate peptide-level "
        "candidates and computational evidence for a possible oral–AD molecular link, "
        "not to prove pathogenicity, and to set up later peptide–AChE binding and "
        "Aβ-aggregation assays."
    ),
    "The work is computational. No new patients": (
        "The work is computational. No new patients, specimens, sequencing runs or wet "
        "assays were added. Healthy and periodontitis tags are library labels; they are "
        "not peptide-level clinical diagnoses. Ligand starting coordinates for docking "
        "were AlphaFold3 models of the twelve peptides. All twelve were docked with "
        "local three-run AutoDock Vina. MD was restricted to apo AChE and three "
        "complexes taken from the best-run poses, as described below."
    ),
    "Four explicit-solvent systems were built in GROMACS": (
        "Four explicit-solvent systems were built in GROMACS with Amber99SB-ILDN and "
        "TIP3P water at 0.15 M NaCl [36–37]: apo AChE (chain A) and the ALLLHRC, "
        "FLLHTTR and YLSLLQR complexes. These three ligands were taken from the twelve "
        "docked peptides as the best-run Vina poses: FLLHTTR and YLSLLQR as PAS "
        "contacts, ALLLHRC as a high-scoring catalytic-site occupant without outer PAS "
        "aromatics, so that PAS geometry could be compared with a strong non-PAS score. "
        "Each box was triclinic with a 1.0 nm solute-to-wall buffer. Equilibration was "
        "2,000 steps of steepest descent, 1.0 ns restrained NVT to 300 K, 1.0 ns "
        "restrained NPT, and 1.0 ns free NPT. Production was 100 ns (dt = 2.0 fs) at "
        "300 K and 1.0 bar with LINCS, 1.2 nm cut-offs and particle-mesh Ewald. Frames "
        "were stored every 20 ps."
    ),
}

CN_FRONT = {
    "牙周炎与阿尔茨海默病（AD）在临床和实验中有关联": (
        "牙周炎与阿尔茨海默病（AD）在流行病学和实验研究中存在关联，但口腔微生物来源分子是否可能参与与淀粉样β蛋白（Aβ）聚集相关的分子过程，仍有待探索。"
        "本研究旨在筛选口腔微生物来源、可能与人源乙酰胆碱酯酶（AChE）外周阴离子位点（PAS）相互作用的短肽，并用分子模拟初步评估其潜在作用方式。"
        "用 EMBOSS getorf 从 PRJNA678453 宏基因组组装基因组预测小开放阅读框（sORF），再用 UniDL4BioPep 打分；"
        "牙周炎标记候选序列与口腔基因组及宏蛋白质组目录精确匹配，并结合 NTxPred2、mebipred 和 AnOxPePred 收至 12 条明示肽。"
        "12 条均为 7–9 残基，pH 7.4 净正电且富亮氨酸。12 条配体均对接到人源 AChE，再对 apo 酶与三个代表性复合物做 100 ns MD。"
        "对接显示 FLLHTTR、YLSLLQR 与 LLHPLRL 出现在 PAS 附近。"
        "相对 apo AChE，FLLHTTR 与 YLSLLQR 复合物整体更紧凑；FLLHTTR 分子间氢键更密，YLSLLQR 溶剂可及表面积下降。"
        "这些是构象与接触描述，不能单独证明结合更强。"
        "结果提示部分口腔微肽可能与 AChE-PAS 发生相互作用。"
        "本研究为探索口腔微肽参与 AChE 相关 Aβ 聚集过程的潜在机制提供计算依据，并为后续验证牙周炎与 AD 之间可能存在的肽介导分子联系提供候选分子。"
    ),
    "阿尔茨海默病（AD）在漫长临床前过程中同时出现淀粉样沉积": (
        "阿尔茨海默病（AD）在漫长临床前过程中同时出现淀粉样沉积、tau 病理、突触衰竭、免疫激活和血管损伤[1]。"
        "APP 经 β、γ 分泌酶依次切割，释放 Aβ40 和 Aβ42；可溶寡聚体损伤突触；家族性 APP/PSEN 突变改变肽长度和产量[2]。"
        "淀粉样负荷解释不了疾病的空间与临床异质性，因此外周炎症暴露被当作易感性的可能修饰因素，而不是单一充分病因。"
        "阐明外周慢性炎症与 AD 相关病理之间可能存在的分子联系，是理解这一异质性的方向之一。"
        "除炎症信号本身外，微生物来源产物能否直接参与与 Aβ 生成、聚集或突触功能障碍相关的蛋白质相互作用，也值得进一步研究。"
    ),
    "牙龈卟啉单胞菌的牙龈蛋白酶与外膜囊泡是一对已定位的毒力因子": (
        "牙龈卟啉单胞菌的牙龈蛋白酶与外膜囊泡是一对已定位的毒力因子[12–13]。"
        "AD 脑内曾检出该菌与牙龈蛋白酶[14]，小鼠反复口腔感染可产生神经炎症和 Aβ 相关改变[15]。"
        "这些观察支持检查口腔产物，但并不能单独指出占据 AChE 的肽。"
        "现有工作主要跟踪特定病原、毒力因子和炎症反应。口腔微生物编码的短肽是否可能直接参与 AD 相关蛋白质相互作用，认识仍然有限。"
        "短肽序列短、理化性质多样，在原则上可以结合蛋白表面，因而构成值得探索的候选类别。"
        "从口腔微生物组系统提名此类肽，并在 AD 相关靶蛋白上评估相互作用，有助于把牙周炎与 AD 的关联推进到更具体的分子层面。"
    ),
    "微生物组 smORF 编码大量尚未绘图的小蛋白": (
        "微生物组 smORF 编码大量尚未绘图的小蛋白[16–17]。"
        "人体微生物组抗菌肽挖掘先对数百万条翻译开放阅读框打分，再做实验过滤[18]。"
        "UniDL4BioPep 在 ESM-2 嵌入上提供二十余个二分类活性头[19]。"
        "基于序列的活性预测只能为筛选提供初步依据，不能证明特定蛋白质结合能力，也不能确定在靶蛋白表面的结合位置。"
        "获得候选序列后，还需要结合分子对接和分子动力学，评估其与 AChE-PAS 相互作用的可能性及相关构象特征。"
        "把序列筛选与结构分析衔接起来，可以从大量微生物编码序列中缩小范围，并为后续实验提供更有针对性的对象。"
    ),
    "有了配体名单之后，下一步通常是分子对接和 MD。": (
        "有了配体名单之后，下一步通常是分子对接和 MD。"
        "加速 MD 把 Aβ 放到 AChE 表面，并把该酶视为成核中心[20]。"
        "1 μs、以 PAS 为中心的 AChE–Aβ 轨迹保持结合，主驻留区为残基 344–361[21]。"
        "PDB 4EY6 给出 2.40 Å 人源 AChE 框架[22]。连接催化三联体与 PAS 的芳香峡部早先在电鳗 AChE 上被定位[23]。"
        "对接可以评估口腔来源短肽是否可能与同一 PAS 相互作用；MD 可以评估复合物的构象特征。"
        "仍缺少的是这一肽水平检验，配体来自口腔 smORF，而不是 Aβ 本身。"
    ),
    "本研究用 EMBOSS getorf 从 PRJNA678453 的 MAG 预测 sORF": (
        "基于上述背景，本研究旨在从口腔微生物宏基因组数据中筛选可能与 AChE 外周阴离子位点相互作用的短肽，并初步评估其潜在分子作用方式。"
        "我们提出，部分口腔微生物编码短肽可能具有与 AChE-PAS 相互作用的序列及理化特征，因而值得进一步考察其在 AChE 相关 Aβ 聚集过程中的潜在作用。"
        "为此，采用 EMBOSS getorf 从 PRJNA678453 的 MAG 预测 sORF，并用 UniDL4BioPep 做 22 项活性预测；"
        "随后将牙周炎相关候选与口腔基因组和宏蛋白质组目录精确匹配，并结合 NTxPred2、mebipred 和 AnOxPePred 进一步筛选。"
        "在此基础上选取 12 条短肽，用 AlphaFold3 建模并对接到人源 AChE。"
        "对 apo AChE 及三个代表性复合物——两个最强 PAS 构象（FLLHTTR、YLSLLQR）和一个最强催化位点构象（ALLLHRC）——做 100 ns 分子动力学，"
        "考察构象变化、相互作用特征和该时间窗口上的表观稳定性。"
        "本研究旨在从肽分子层面为探索口腔微生物与 AD 相关病理之间的潜在联系提供候选分子和计算证据，"
        "而不是证明这些肽具有致病性或牙周炎导致 AD，并为后续肽–AChE 结合验证及 Aβ 聚集实验奠定基础。"
    ),
    "工作为纯计算。未新增患者、标本、测序或湿实验。": (
        "工作为纯计算。未新增患者、标本、测序或湿实验。健康与牙周炎标记是文库标签，不是肽水平临床诊断。"
        "对接配体的起始坐标为 12 条肽的 AlphaFold3 模型。12 条均做本地三次 AutoDock Vina 对接。"
        "MD 限于 apo AChE 与按下述规则从最优单次构象中取出的三个复合物。"
    ),
    "四个显式溶剂体系在 GROMACS 中以 Amber99SB-ILDN 和 TIP3P、0.15 M NaCl 构建": (
        "四个显式溶剂体系在 GROMACS 中以 Amber99SB-ILDN 和 TIP3P、0.15 M NaCl 构建[36–37]："
        "apo AChE（A 链）以及 ALLLHRC、FLLHTTR、YLSLLQR 复合物。"
        "这三条取自 12 条已对接肽中最优单次 Vina 构象：FLLHTTR 与 YLSLLQR 为 PAS 接触，"
        "ALLLHRC 为不接触外侧 PAS 芳香残基的高分催化位点占据者，以便把 PAS 几何与强非 PAS 分数对照。"
        "盒子为三斜，溶质至壁缓冲 1.0 nm。平衡为 2,000 步最速下降、1.0 ns 受限 NVT 升至 300 K、1.0 ns 受限 NPT 和 1.0 ns 自由 NPT。"
        "生产相 100 ns（dt = 2.0 fs），300 K、1.0 bar，LINCS、1.2 nm 截断和粒子网格 Ewald。每 20 ps 存一帧。"
    ),
}
