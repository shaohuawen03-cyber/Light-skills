# Abstract / intro / docking-methods replacements.
# Keys = paragraph prefixes in English_backup_pre-zotero.docx or current Chinese.docx.

EN_FRONT = {
    "Periodontitis has been tied to Alzheimer’s disease": (
        "Periodontitis has been tied to Alzheimer’s disease (AD) in clinical and "
        "experimental work, yet a peptide-level ligand that could act on a synaptic "
        "enzyme is still missing. Small open reading frames (sORFs) were predicted "
        "with EMBOSS getorf from PRJNA678453 metagenome-assembled genomes and scored "
        "with UniDL4BioPep. Both libraries were passed through 22 UniDL4BioPep "
        "classifiers; only the periodontitis branch was then matched to oral genomic "
        "and metaproteomic catalogues. NTxPred2, mebipred and AnOxPePred reduced the "
        "catalogue-supported list to twelve explicit peptides. All twelve are 7–9 "
        "residues, carry a net positive charge at pH 7.4, and are leucine-rich. The "
        "twelve ligands were docked into human acetylcholinesterase (AChE). Apo AChE "
        "and three complexes were then run for 100-ns molecular dynamics (MD). Local "
        "AutoDock Vina (three runs) placed FLLHTTR, YLSLLQR and LLHPLRL at the "
        "peripheral anionic site (PAS). Over 100 ns the FLLHTTR and YLSLLQR complexes "
        "stay more compact than apo AChE. FLLHTTR keeps a dense hydrogen-bond net; "
        "only YLSLLQR shrinks solvent-accessible surface area. These calculations "
        "outline a possible route in which oral micropeptides sit on the same PAS "
        "that accelerates amyloid-β (Aβ) assembly."
    ),
    "Microbiome smORFs encode a large pool of uncharted small proteins": (
        "Microbiome smORFs encode a large pool of uncharted small proteins [16–17]. "
        "Mining of human microbiomes for peptide antibiotics first scored millions of "
        "translated open reading frames and then applied experimental filters [18]. "
        "UniDL4BioPep supplies more than twenty binary bioactivity heads on ESM-2 "
        "embeddings [19]. Those tools can rank oral strings for bioactivity. They "
        "cannot show that a 7–9-aa periodontitis peptide occupies the Aβ-binding PAS, "
        "because occupancy is a geometric question on a protein surface, not a "
        "classifier output."
    ),
    "Accelerated MD places Aβ on the AChE surface": (
        "Molecular docking and MD are the usual next step once a ligand list exists. "
        "Accelerated MD places Aβ on the AChE surface and treats the enzyme as a "
        "nucleation centre [20]. A 1-μs PAS-centred AChE–Aβ trajectory remains bound, "
        "with the main residence at residues 344–361 [21]. PDB 4EY6 gives a 2.40 Å "
        "human AChE frame [22]. The aromatic gorge that joins the catalytic triad to "
        "the PAS was mapped on Torpedo AChE [23]. Docking can ask whether an oral "
        "heptapeptide contacts that same PAS; MD can ask whether the pose remains "
        "with the fold closed. What remains missing is that peptide-level test, drawn "
        "from oral smORFs rather than from Aβ itself."
    ),
    "Here we called sORFs with EMBOSS getorf": (
        "Here we called sORFs with EMBOSS getorf from PRJNA678453 MAGs, scored both "
        "libraries with 22 UniDL4BioPep heads, matched the periodontitis branch to "
        "oral genomic and metaproteomic catalogues, and reduced the list with "
        "NTxPred2, mebipred and AnOxPePred. Twelve 7–9-aa peptides were built with "
        "AlphaFold3 and docked into human AChE. Three complexes, together with apo "
        "enzyme, were simulated for 100 ns, tracking peptide residence at the PAS "
        "with the fold closed."
    ),
    "The work is computational. No new patients": (
        "The work is computational. No new patients, specimens, sequencing runs or "
        "wet assays were added. Healthy and periodontitis tags are library labels; "
        "they are not peptide-level clinical diagnoses. Ligand starting coordinates "
        "for docking were AlphaFold3 models of the twelve peptides. Docking used "
        "local three-run AutoDock Vina poses. MD used 100-ns GROMACS trajectories of "
        "apo AChE and three peptide complexes."
    ),
    "Human recombinant AChE (PDB 4EY6, 2.40 Å)": (
        "Ligand starting coordinates for the twelve peptides were predicted with "
        "AlphaFold3. Each model is a computed conformer for a short, flexible chain, "
        "not a crystal structure, and it was used only as the input geometry for "
        "docking. Human recombinant AChE (PDB 4EY6, 2.40 Å) was stripped of "
        "galantamine and crystal waters, chain breaks were repaired, and protonation "
        "was set at pH 7.4 [22]. The twelve ligands ALLLHRC, FCLHLQLR, FLLHTTR, "
        "HLLTLKKHV, HLPLLHRCC, HVLLLRQCA, LLHLPKRTT, LLHPLRC, LLHPLRL, WLLVHLKK, "
        "YHHLLCRR and YLSLLQR were docked with AutoDock Vina, exhaustiveness 32 "
        "[34–35]. The grid was centred on the PAS (Tyr72, Asp74, Thr75, Leu76, "
        "Trp286, His287, Tyr341) and covered the gorge neck (Phe295), the choline "
        "subsite (Trp86, Glu202, Tyr337) and the catalytic triad (Ser203, His447, "
        "Glu334). Each ligand was run three times. We report best-run affinity, "
        "three-run mean ± SD, hydrogen-bond count and PAS contact from the single "
        "best pose. Vina scores rank poses; they are not experimental free energies."
    ),
}

CN_FRONT = {
    "牙周炎与阿尔茨海默病（AD）在临床和实验中有关联": (
        "牙周炎与阿尔茨海默病（AD）在临床和实验中有关联，但仍缺少能够作用于突触酶的肽水平配体。"
        "用 EMBOSS getorf 从 PRJNA678453 宏基因组组装基因组预测小开放阅读框（sORF），再用 UniDL4BioPep 打分。"
        "两库均跑完 22 个分类头；随后仅对牙周炎分支与口腔基因组、宏蛋白质组目录做精确匹配。"
        "经 NTxPred2、mebipred 与 AnOxPePred 将目录支持的名单收至 12 条明示序列。"
        "12 条均为 7–9 残基、pH 7.4 带净正电荷且富亮氨酸。这 12 条配体对接到人源乙酰胆碱酯酶（AChE）。"
        "apo AChE 与三种复合物随后做 100 ns 分子动力学（MD）。"
        "本地 AutoDock Vina（三次）把 FLLHTTR、YLSLLQR 与 LLHPLRL 放到外周阴离子位点（PAS）。"
        "100 ns 内 FLLHTTR 与 YLSLLQR 复合物比 apo 更紧凑。FLLHTTR 氢键网最密；仅 YLSLLQR 收缩溶剂可及面积。"
        "计算勾勒出口腔微肽占据促 Aβ 成纤同一 PAS 的可能路径。"
    ),
    "微生物组 smORF 编码大量尚未绘图的小蛋白": (
        "微生物组 smORF 编码大量尚未绘图的小蛋白[16–17]。"
        "人体微生物组抗菌肽挖掘先对数百万条翻译开放阅读框打分，再做实验过滤[18]。"
        "UniDL4BioPep 在 ESM-2 嵌入上提供二十余个二分类活性头[19]。"
        "这些工具可以给口腔字符串排生物活性。它们不能表明 7–9 aa 牙周炎肽占据 Aβ 结合 PAS，"
        "因为占据是蛋白表面上的几何问题，不是分类器输出。"
    ),
    "加速 MD 把 Aβ 放到 AChE 表面": (
        "有了配体名单之后，下一步通常是分子对接和 MD。"
        "加速 MD 把 Aβ 放到 AChE 表面，并把该酶视为成核中心[20]。"
        "1 μs、以 PAS 为中心的 AChE–Aβ 轨迹保持结合，主驻留区为残基 344–361[21]。"
        "PDB 4EY6 给出 2.40 Å 人源 AChE 框架[22]。连接催化三联体与 PAS 的芳香峡部早先在电鳗 AChE 上被定位[23]。"
        "对接可以问口腔七肽是否碰到同一 PAS；MD 可以问构象是否在折叠闭合时留下。"
        "仍缺少的是这一肽水平检验，配体来自口腔 smORF，而不是 Aβ 本身。"
    ),
    "本研究用 EMBOSS getorf 从 PRJNA678453 的 MAG 预测 sORF": (
        "本研究用 EMBOSS getorf 从 PRJNA678453 的 MAG 预测 sORF，对两库做 22 项 UniDL4BioPep 打分，"
        "将牙周炎分支与口腔基因组和宏蛋白质组目录匹配，再用 NTxPred2、mebipred 和 AnOxPePred 收窄名单。"
        "12 条 7–9 aa 肽用 AlphaFold3 建模后对接到人源 AChE。"
        "三个复合物与 apo 酶一起做 100 ns 模拟，跟踪肽在 PAS 上的驻留，折叠保持闭合。"
    ),
    "工作为纯计算。未新增患者、标本、测序或湿实验。": (
        "工作为纯计算。未新增患者、标本、测序或湿实验。健康与牙周炎标记是文库标签，不是肽水平临床诊断。"
        "对接配体的起始坐标为 12 条肽的 AlphaFold3 模型。对接使用本地三次 AutoDock Vina 构象。"
        "MD 使用 apo AChE 与三种肽复合物的 100 ns GROMACS 轨迹。"
    ),
    "人源重组 AChE（PDB 4EY6，2.40 Å）去除加兰他敏与结晶水": (
        "12 条肽的配体起始坐标用 AlphaFold3 预测。每个模型是短柔性链的计算构象，不是晶体结构，仅作为对接输入几何。"
        "人源重组 AChE（PDB 4EY6，2.40 Å）去除加兰他敏与结晶水，修复链断裂，并按 pH 7.4 分配质子化[22]。"
        "12 条配体 ALLLHRC、FCLHLQLR、FLLHTTR、HLLTLKKHV、HLPLLHRCC、HVLLLRQCA、LLHLPKRTT、LLHPLRC、"
        "LLHPLRL、WLLVHLKK、YHHLLCRR 和 YLSLLQR 用 AutoDock Vina 对接，exhaustiveness = 32[34–35]。"
        "网格以 PAS（Tyr72、Asp74、Thr75、Leu76、Trp286、His287、Tyr341）为中心，覆盖峡部颈（Phe295）、"
        "胆碱亚位点（Trp86、Glu202、Tyr337）和催化三联体（Ser203、His447、Glu334）。每条配体跑三次。"
        "报告最优单次亲和力、三次均值±SD、氢键数和最优构象的 PAS 接触。Vina 分数用于排序，不是实验自由能。"
    ),
}
