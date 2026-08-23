## 摘要

本研究采用已发表AChE–β-淀粉样肽研究的分析指标，对一条归属于乙酰胆碱酯酶（acetylcholinesterase，AChE）–ALLLHRC复合物的100 ns分子动力学（molecular dynamics，MD）输出进行解读，但不迁移该文献的肽特异结果。配置的GROMACS流程采用Amber99SB-ILDN、显式水、生理盐浓度、分阶段平衡和100 ns产物阶段。AChE骨架RMSD为0.1803 ± 0.0220 nm。肽自拟合RMSD形成三个平台：0.0–22.6 ns为0.0582 ± 0.0091 nm，23.4–55.6 ns为0.1432 ± 0.0161 nm，57.0–100.0 ns为0.2694 ± 0.0148 nm。肽–AChE质心距离分布在约1.2和1.4 nm处出现峰值；复合物与肽的溶剂可及表面积分别大致保持在210–223和10–12 nm²。分子间氢键数在0–11之间变化，轨迹后段通常较少。现有输出未提供独立重复、经核实的残基接触、结合自由能、AChE活性实验或完整原始轨迹档案。

**关键词：** ALLLHRC；乙酰胆碱酯酶；分子动力学；肽–蛋白相互作用；RMSD；氢键

## 引言

乙酰胆碱酯酶（AChE）水解乙酰胆碱，并且仍是阿尔茨海默病（AD）对症治疗的药物靶点[@hampel2018cholinergic]。其外周区域也被认为与β-淀粉样蛋白（Aβ）组装加速有关[@inestrosa1996ache]。这些发现支持对AChE相互作用分子进行结构研究，但计算肽轨迹本身不能证明酶抑制、Aβ聚集改变或疾病相关性。

Atanasova等采用RMSD、RMSF、径向分布、溶剂暴露、二级结构、接触、氢键和水桥，对AChE–Aβ复合物进行了1 μs分析[@atanasova2020md]。本研究使用这些指标类别组织另一个独立的100 ns结果，其研究对象是七残基肽ALLLHRC。参考文献中的任何Aβ特异接触、驻留区域或机制均未被赋予ALLLHRC。

## 材料与方法

可用结果包括与`md_alllhrc`目录关联的一张六面板轨迹汇总图和一份RMSD诊断导出。根据目录及随附说明，体系被归属于ALLLHRC；但图中仍保留继承的“AChE–Aβ”标题。该标注差异仍需通过相匹配的拓扑和轨迹标识符解决。

上游流程指定采用GROMACS[@abraham2015gromacs]、Amber99SB-ILDN[@lindorfflarsen2010amber]、与TIP3P兼容的水、中和离子、0.15 mol/L NaCl、1.0 nm溶质至盒边距离、能量最小化、1 ns受限NVT升温、1 ns受限NPT平衡和1 ns无约束NPT平衡。产物阶段配置为100 ns、300 K和1 bar，时间步长2 fs，采用LINCS、粒子网格Ewald静电处理，并每20 ps保存坐标。由于完整输入、日志、能量、检查点和原始轨迹不可用，这些内容被视为配置参数，而不是经独立核实的实际运行参数。

RMSD诊断将AChE定义为残基1–530，将ALLLHRC定义为残基531–537。肽RMSD在肽骨架自拟合后计算，因此表示内部构象偏差，而不是整条肽的平移。RMSD汇总来自对数字化曲线的诊断计算，属于描述性估计，不能替代原始坐标分析；其他数值均从现有图中保守读取。未依据图像重建推断统计量。

## 结果

AChE骨架RMSD为0.1803 ± 0.0220 nm，最大值0.2320 nm，说明本条轨迹中的受体骨架偏差有限（表1）。ALLLHRC自拟合RMSD约在23和56 ns发生两次转变，之后进入较高但较窄的末段平台。全肽序列为0.1789 ± 0.0870 nm，范围0.0151–0.3141 nm。由于肽自拟合去除了平移和旋转，这些阶跃反映相对于起始构象的内部重排，不能证明解离或重新结合。

大多数AChE RMSF低于约0.10 nm，但局部存在较高峰，末端数值接近0.60 nm。大多数肽RMSF约为0.05–0.10 nm，一个端点接近0.21 nm。质心RDF在约1.2 nm处出现主峰，在约1.4 nm处出现次峰，与两个优选间距范围相符，但不能解释为测得的亲和力或残基接触。

复合物SASA大致保持在210–223 nm²，肽SASA约为10–12 nm²。图示二级结构比例相对稳定，其中螺旋最高，约为0.33–0.37；但分析选择未提供，若按全复合物计算，数值将由AChE主导。AChE–ALLLHRC氢键数在0–11之间波动。轨迹前段和中段通常约为3–7个，约65–70 ns后更多为1–4个，与肽末段平台期间发生界面重排相容。

**表1. AChE–ALLLHRC现有轨迹的简洁汇总。**

| 指标 | 结果 | 解释边界 |
| --- | --- | --- |
| AChE骨架RMSD | 0.1803 ± 0.0220 nm；最大0.2320 nm | 单条轨迹内偏差有限，不代表功能性稳定 |
| ALLLHRC RMSD平台1 | 0.0582 ± 0.0091 nm，0.0–22.6 ns | 初始内部构象状态 |
| ALLLHRC RMSD平台2 | 0.1432 ± 0.0161 nm，23.4–55.6 ns | 第一次重排状态 |
| ALLLHRC RMSD平台3 | 0.2694 ± 0.0148 nm，57.0–100.0 ns | 持续的第二次重排状态 |
| 质心RDF | 峰约1.2和1.4 nm | 优选间距，而非原子接触或亲和力 |
| SASA | 复合物约210–223 nm²；肽约10–12 nm² | 未见较大的整体暴露转变 |
| 分子间氢键 | 0–11；后段通常较少 | 间歇极性接触，而非生化抑制 |

## 讨论

综合模式支持AChE骨架较为受限，而肽具有构象适应性。持续出现的氢键和优选质心间距与动态关联相容；肽RMSD阶跃和后段较低的氢键数则不支持把轨迹描述为单一刚性结合姿势。要判断肽是在一个表面区域内移动、转移至其他位点还是部分脱离，还需要受体拟合后的肽位置RMSD、最小距离、残基接触、代表性结构和轨迹目视检查。

参考AChE–Aβ模拟表明需要结合多个轨迹指标，但其Aβ接触残基、AChE 344–361驻留区域、PAS移动和1 μs稳定性结论不能迁移到ALLLHRC[@atanasova2020md]。源图中继承的Aβ标题应予更正，并通过拓扑和轨迹哈希核实体系身份。

主要局限包括只有一条100 ns轨迹、缺少独立种子和apo对照、原始文件不完整、二级结构选择不确定，以及缺少残基分辨率相互作用。本研究未测量结合自由能、驻留时间、催化抑制、配体竞争、Aβ聚集、BBB转运、细胞毒性或AD表型。因此，现有输出不能证明ALLLHRC结合外周阴离子位点、抑制AChE、改变淀粉样生物学、进入脑内或参与疾病。

## 参考文献

1. Hampel H, Mesulam MM, Cuello AC, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer’s disease. *Brain*. 2018;141(7):1917–1933. doi:10.1093/brain/awy132.
2. Inestrosa NC, Alvarez A, Pérez CA, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer’s fibrils. *Neuron*. 1996;16(4):881–891. doi:10.1016/s0896-6273(00)80108-7.
3. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. *Cybern Inf Technol*. 2020;20(6):140–154. doi:10.2478/cait-2020-0068.
4. Abraham MJ, Murtola T, Schulz R, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. *SoftwareX*. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001.
5. Lindorff-Larsen K, Piana S, Palmo K, et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field. *Proteins*. 2010;78(8):1950–1958. doi:10.1002/prot.22711.
