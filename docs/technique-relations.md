# 技术之间的逻辑与分析意义

[知识导航](../atlas/index.md) · [测量与推断](learning-guide.md)

技术之间的关系不是“一个软件接着另一个软件”。下面把方法组织成问题之间的联系。箭头仅在明确写成数据传递时表示输出进入下一步；其他关系可能是平行测量、候选解释或独立检验，不是固定的实验套餐。

## 五种需要区分的关系

| 关系 | 例子 | 增加了什么信息 |
| --- | --- | --- |
| 数据传递 | RNA reads → 比对/定量 → 计数模型 | 将信号转换为可比较的特征和效应 |
| 平行互补 | RNA-seq与蛋白质组 | 从不同分子层观测同一系统，不保证变化一致 |
| 测量范围或分辨率不同 | bulk、单细胞、空间表达 | 分别强调群体平均、细胞差异和组织位置；不是无条件升级 |
| 假设与检验 | 调控网络候选与基因/元件扰动 | 区分相关结构和干预后的响应 |
| 同任务的不同实现 | 同一类数据的不同定量或重建算法 | 比较模型假设、误差与适用条件，而非只比较软件新旧 |

RNA定量、长读长异构体重建和空间细胞映射分别展示了上述不同关系：[DESeq2](../references/index.md#deseq)、[IsoQuant](../references/nature-papers.md#n02)、[空间脑图谱](../references/nature-papers.md#n04)。

## 1. 基因组差异为什么可能影响表型？

序列分析首先发现或重建遗传差异；GWAS比较遗传变异与性状的统计关系；精细定位在连锁的候选变异中分配支持；分子QTL和共定位帮助连接分子层；元件或基因扰动检验特定条件下的效应。它们不是五种等价的“找关键基因”方法。[PLINK](../references/index.md#plink)、[SuSiE](../references/index.md#susie)、[coloc](../references/index.md#coloc)

**缺失的环节是什么？**关联位点不等于已确认的效应变异，效应变异不等于已确认的靶基因，靶基因也不等于机制已经完成。泛基因组改进变异表示；AlphaGenome预测功能读出；二者都不会自动补齐整条因果链。[N01](../references/nature-papers.md#n01)、[N14](../references/nature-papers.md#n14)

详见[分子调控](molecular-regulation.md)与[群体遗传](../atlas/domains/04-population-genetics.md)。

## 2. DNA相同，细胞为何表现不同？

染色质开放程度、调控蛋白占据、RNA合成与加工、蛋白丰度与修饰，从不同层面限制细胞的状态。ATAC关注可及性，ChIP/CUT&RUN/CUT&Tag关注指定靶标相关富集，RNA分析关注转录本，蛋白组关注肽和蛋白信号。它们相互补充，而不是从ATAC出发就能自动计算出其他所有层。[CUT&Tag](../references/index.md#cuttag)、[DESeq2](../references/index.md#deseq)、[DIA-NN](../references/index.md#diann)

SCENIC+是这些信息如何形成调控网络假设的具体例子。其意义在于缩小候选空间，不在于把每条预测边都变成已验证的生物学事实。[N03](../references/nature-papers.md#n03)

详见[分子调控](molecular-regulation.md)。

## 3. RNA增加，究竟增加了什么？

基因总量、异构体比例、转录起始、RNA半衰期和核糖体占据是不同变量。常规RNA-seq、长读长RNA、端点测序、新生RNA/代谢标记及Ribo-seq分别补充不同信息。一个基因总量不变，仍可能发生剪接改变；同样的RNA丰度也可能由不同的合成—降解组合产生。[IsoQuant](../references/nature-papers.md#n02)、[Ribo-seq](../references/index.md#ribo)、[CellRank 2](../references/nature-papers.md#n08)

**分析意义：**从“有差异”转向“差异属于哪个生物过程”，而不是给同一份表达矩阵再换几种降维算法。

详见[转录组方法](../atlas/domains/05-transcriptomics.md)。

## 4. 组织改变，是细胞变了，还是细胞组成变了？

单细胞身份注释、类型内差异状态、细胞组成比较和空间邻域分析回答不同问题。组织平均信号把这些信息混合在一起；拆解它们需要合适的样本层级和独立重复，不能只看UMAP上是否分开。[muscat](../references/index.md#muscat)、[空间脑图谱](../references/nature-papers.md#n04)

空间技术增加位置，但分割、捕获单位及参考映射影响结果。细胞间通信分析再引入配体—受体等先验；空间相邻仅缩小可能关系，不单独证明通信发生。[Cell2location](../references/index.md#cell2loc)、[LIANA+](../references/nature-papers.md#n09)

详见[细胞、空间与时间](cells-space-time.md)。

## 5. 状态顺序、变化方向和共同祖先是什么关系？

拟时序描述状态在推断路径上的相对位置；RNA velocity和其他方向信息用于估计状态转移；谱系标记记录共同来源；活细胞追踪在时间上匹配同一对象。这些技术增加的是不同的约束，不应把四种图上的“箭头”读成同一件事。[RNA velocity](../references/index.md#velocity)、[CellRank 2](../references/nature-papers.md#n08)、[动态与谱系](../atlas/domains/08-dynamics-lineage.md)

**分析意义：**区分细胞现在相似、未来可能趋向相同状态、过去来自同一祖先，以及真实经历了某个变化。

## 6. 一个蛋白为何具有某种功能？

蛋白质组回答量与部分状态，结构方法回答几何，结合测定约束相互作用，动力学描述反应或转换速率，扰动检验系统中的后果。结构预测、分子对接和MD是不同模型，不是互相自动验证的三步流水线。[AlphaFold 3](../references/nature-papers.md#n07)、[GROMACS](../references/index.md#md)、[AutoDock Vina](../references/index.md#vina)

设计则反过来从约束提出候选，再回到物理和功能读出。RFdiffusion说明了生成与实验表征如何分工，不说明任何计算候选都天然有预期功能。[N05](../references/nature-papers.md#n05)

详见[结构、功能与代谢](structure-function.md)。

## 7. 代谢物多了，是否说明通路更活跃？

代谢物丰度描述池大小；同位素标记提供原子来源和路径约束；摄取、分泌与时间信息进一步限制通量；FBA则从化学计量守恒和边界条件计算可行或优化解。它们不是同一量的不同展示方式。[COBRApy](../references/index.md#cobra)、[COPASI](../references/index.md#copasi)

单细胞代谢组把代谢状态异质性带入细胞尺度，却仍不自动把一次丰度测量转换为每个反应的速率。[N16](../references/nature-papers.md#n16)

详见[代谢组与通量](../atlas/domains/14-metabolomics.md)。

## 8. 微生物群落和进化历史怎样从序列中推断？

物种分类、功能注释、基因组组装和系统发育分别回答“有哪些”“编码什么”“序列怎样连接”“有哪些共同历史”。宏转录/宏蛋白分析再增加活动层信息；生态模型还需要环境、空间和检测过程。[MetaPhlAn 4](../references/nature-papers.md#n06)、[IQ-TREE](../references/index.md#iqtree)、[vegan](../references/index.md#vegan)

**分析意义：**避免把物种列表当作机制，把功能基因当作已发生的反应，把一个可拟合的历史模型当作唯一历史。

详见[群体、生态与系统](populations-systems.md)。

## 9. 神经结构、活动和行为如何连接？

EM重建连接，电生理和钙/电压成像提供活动，行为视频提供运动与行为特征，编码/解码模型分析这些变量的关系。跨模态配准建立对象对应；干预再检验特定回路的功能作用。[MICrONS](../references/nature-papers.md#n11)、[CaImAn](../references/index.md#caiman)、[DeepLabCut](../references/index.md#dlc)

“能解码某个行为”表示数据含有可预测信息，不自动说明脑使用了该解码算法；结构边也不是突触效力的直接数值。

详见[神经科学](../atlas/domains/18-neuroscience-behavior.md)。

## AI位于哪里？

AI不是以上所有问题之上的一个统一解释层。它可以用于信号识别、表征、结构预测、轨道预测或候选生成。CellSAM、Nicheformer、AlphaGenome和Evo 2的输入、训练目标和输出并不相同，因此需要按所做的任务理解，而不是统称为“模型理解了生物学”。[N13](../references/nature-papers.md#n13)、[N12](../references/nature-papers.md#n12)、[N14](../references/nature-papers.md#n14)、[N15](../references/nature-papers.md#n15)

这些关系共同构成知识库的主线：**先明确生物变量，再明确如何观察它，最后解释分析增加了什么、没有增加什么。**
