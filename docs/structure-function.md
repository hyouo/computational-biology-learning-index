# 蛋白、结构、相互作用与代谢

[知识导航](../atlas/index.md) · [分子调控](molecular-regulation.md) · [技术关系](technique-relations.md)

## 1. 为什么知道RNA仍然不够？

蛋白的数量、亚细胞位置、修饰、复合物组成和构象都可能影响功能。蛋白质组、空间成像、相互作用测定和结构分析分别观察这些变量。RNA为蛋白产生提供相关信息，却不直接给出其稳态量、所在位置或活性。[DIA-NN](../references/index.md#diann)、[TurboID](../references/index.md#turbo)、[DVP](../references/index.md#dvp)

功能也不是一个单一指标。某蛋白能结合底物、能催化反应、能进入细胞器、能改变细胞表型，是不同层面的性质。把它们拆开，才能解释突变后究竟改变了哪一个环节。

## 2. 从质谱信号到蛋白知识

常见bottom-up蛋白组先把蛋白转为肽段，再记录离子信号及碎片谱。分析需要把谱图指认为肽，之后处理共享肽带来的蛋白归属，并在合适层级汇总定量。[MaxQuant](../references/index.md#maxquant)

| 层次 | 输入 → 输出 | 对理解生物学的意义 |
| --- | --- | --- |
| 谱图鉴定 | 碎片谱+序列/谱库 → PSM和肽候选 | 哪些序列有证据存在 |
| DDA / DIA数据处理 | 不同采集方案的谱 → 鉴定与定量 | DDA偏向选择前体；DIA需要解混合片段信号 |
| 蛋白推断 | 肽证据 → 蛋白或蛋白组 | 同源蛋白共享肽时不总能唯一归属 |
| 相对/靶向定量 | 峰强、标签或标准 → 丰度变化/校准量 | 比较什么分子、用什么分母 |
| PTM定位与比较 | 修饰肽谱 → 位点及其变化 | 区分总蛋白量、修饰位点信号和占比 |
| 互作/邻近富集 | 富集样本与对照 → 候选伙伴 | 解释共同复合物、空间邻域或特定接触 |

DIA解卷积与定量见[DIA-NN](../references/index.md#diann)，定量层级见[MSstats](../references/index.md#msstats)，邻近读出见[TurboID](../references/index.md#turbo)。一条修饰肽增加，可能同时受蛋白总量与修饰程度影响；缺失鉴定也不自动等于蛋白不存在。

对应条目：[M096–M104](../atlas/domains/13-proteomics.md)。

## 3. 三种“相互作用”不是同一个意思

**共同富集**说明诱饵与其他分子在特定提取和富集条件下一起保留；**邻近标记**说明它们在给定时空范围内可被同一局部标记过程记录；**直接结合测定**则在指定体系中估计分子之间的结合行为。这几类证据可以互补，但不能互换。[TurboID](../references/index.md#turbo)、[实验读出 E008–E013](../experiments/index.md)

同样，接触位点、平衡亲和力、结合/解离速率和下游功能分别回答不同问题。界面预测帮助提出可能接触的残基；功能改变可能来自折叠、定位或稳定性改变，而不只来自界面改变。[AlphaFold 3](../references/nature-papers.md#n07)、[结构条目](../atlas/domains/15-structural-biology.md)

## 4. 实验结构怎样形成？

| 技术 | 原始约束 | 核心计算 | 主要结果 |
| --- | --- | --- | --- |
| 冷冻电镜单颗粒 | 不同取向的颗粒投影 | 运动与CTF处理、取向估计、分类、重建 | 三维密度和可支持的构象 |
| 冷冻电子断层 | 同一样本的倾转序列 | 对齐、三维重建、局部颗粒平均 | 原位三维组织与局部结构 |
| X射线晶体学 | 衍射强度及相位信息/约束 | 定标、相位求解、模型拟合与精修 | 电子密度与原子模型 |
| NMR | 化学位移、NOE、耦合和弛豫等 | 指认、结构/动态约束拟合 | 结构集合及运动信息 |
| SAXS/SANS | 散射曲线 | 尺寸、距离分布与模型拟合 | 整体形状和兼容构象 |

这些是不同观测模型。分辨率、各向异性、构象异质性、模型偏差和取样条件，都会影响可解释的细节；一个原子坐标文件不能代替对其来源数据的理解。[CryoSPARC](../references/index.md#cryo)、[RELION](../references/index.md#relion)、[Phenix](../references/index.md#phenix)、[BioXTAS RAW](../references/index.md#saxs)

## 5. 预测、模拟、对接与设计分别做什么？

**结构预测**从序列、分子实体及训练得到的规律产生坐标假设。**分子对接**在指定体系中搜索相对姿势并用近似函数评价。**分子动力学**在给定势能、边界条件与采样方案下产生轨迹。**自由能计算**针对明确定义的状态差进行统计力学估计。**设计**则从功能或几何约束反向提出候选序列/结构。[AlphaFold 3](../references/nature-papers.md#n07)、[AutoDock Vina](../references/index.md#vina)、[GROMACS](../references/index.md#md)、[RFdiffusion](../references/nature-papers.md#n05)

因此，“预测结构→对接→跑一段MD”不天然构成独立验证链：三者可能共享结构假设和近似。真正增加信息的是是否引入了不同的观测约束，以及模型能否解释未用于建模的数据。MD中的时间长度、结构波动和可重复轨迹，也要结合采样与模型适用性解释。[GROMACS](../references/index.md#md)、[MDAnalysis](../references/index.md#mdanalysis)

常见术语中，pLDDT描述预测局部可信度，PAE描述相对位置误差预测；RMSD描述选定对象对齐后的坐标差；自由能描述指定状态间的热力学差异。它们不属于同一尺度，不能用其中一个代替其他所有“好坏”。[AlphaFold 3](../references/nature-papers.md#n07)、[GROMACS](../references/index.md#md)

## 6. 平衡、速率与测定效应

在简单的P+L↔PL结合体系中，可定义：

$$K_D=\frac{[P][L]}{[PL]}.$$

在简化的酶反应E+S↔ES→E+P中，Michaelis–Menten假设下有：

$$v=\frac{V_{max}[S]}{K_m+[S]},\qquad K_m=\frac{k_{-1}+k_{cat}}{k_1}.$$

这些公式说明Kd与Km不是一般意义上的同一个常数。IC50是指定实验条件下达到某个抑制程度的浓度，也不是不依赖测定条件的分子常数。解释参数前，需要知道模型、反应条件、测量量和识别它们所需的数据。[COPASI](../references/index.md#copasi)、[实验读出](../experiments/index.md)

## 7. 代谢组：化学身份、丰度与空间

非靶向质谱首先得到特征；同位素峰、加合物、碎片和异构体使“一个峰=一种代谢物”通常不成立。色谱、准确质量、离子迁移率、碎片谱和标准品提供不同鉴定约束。靶向定量与非靶向发现的目的也不同。[MS-DIAL](../references/index.md#msdial)

空间质谱为特征增加位置，单细胞代谢组为特征增加细胞身份。它们提高对异质性的观察能力，但身份注释、定量尺度和检测偏倚仍然需要单独解释。2026年的离子迁移率质谱与MetCell研究是这种“测量提升+特征提取”关系的实例。[N16](../references/nature-papers.md#n16)

## 8. 浓度与通量：状态和过程的区别

设代谢物浓度向量为c，反应通量为v，化学计量矩阵为S，则简化质量守恒可写为dc/dt=Sv；稳态近似为Sv=0。这是模型约束，不是对每条反应速率的直接测量。FBA进一步加上边界和目标函数求解；FVA描述约束下的可行范围。[COBRApy](../references/index.md#cobra)

稳定同位素示踪约束原子来源与路径使用，结合时间、摄取/分泌及网络模型后可估计通量。浓度高可能因为产生增加，也可能因为消耗减少；仅凭高浓度不能区分。这是守恒方程的直接推论。[代谢条目](../atlas/domains/14-metabolomics.md)、[COPASI](../references/index.md#copasi)

**这一层的知识主线是：序列决定可能性，结构限制几何，物理和化学决定过程，实验观测约束状态与速率，而细胞背景决定这些过程怎样共同形成表型。**
