# 群体、进化、生态、神经与系统建模

[知识导航](../atlas/index.md) · [技术关系](technique-relations.md) · [测量与推断](learning-guide.md)

## 1. 不同尺度的生物学，需要不同的观测单位

分子、细胞、个体、物种和生态群落不是同一种统计对象。它们还可能通过共同祖先、空间位置或重复时间点相关。跨领域共通的不是某套RNA流程，而是：定义对象，说明如何观测，建立适配的模型，再解释模型识别了什么。[statsmodels](../references/index.md#stats)、[IQ-TREE](../references/index.md#iqtree)、[vegan](../references/index.md#vegan)

## 2. 序列相似、共同祖先与功能相同

比对建立可比较的位置；同源关系涉及共同祖先；ortholog与paralog区分物种分化和基因复制相关的关系。相似性是证据，功能注释是进一步的推断。基因复制、功能分化和不同的选择压力使“序列相似”不能无条件转换成“功能完全相同”。[系统发育方法](../atlas/domains/20-evolution.md)、[IQ-TREE](../references/index.md#iqtree)、[HyPhy](../references/index.md#hyphy)

系统发育树描述在给定序列、模型和采样下支持的分化关系；支持度不是所有历史问题都已经解决。基因树和物种树可能不一致；枝长表示替换还是时间，需要看模型和校准。祖先重建、自然选择检验和人口史推断使用不同约束，不是同一种树图的装饰。[IQ-TREE](../references/index.md#iqtree)、[HyPhy](../references/index.md#hyphy)、[tskit](../references/index.md#tskit)

## 3. 群体遗传：现在的变异包含怎样的历史？

等位频率、连锁不平衡、单倍型共享和亲缘结构，分别包含不同尺度的遗传信息。GWAS关注性状关联；人口史模型关注有效群体大小、分化和迁移；选择分析关注偏离特定中性预期的模式。相同统计模式可能受到多个过程影响，所以任务及模型假设必须分开。[PLINK](../references/index.md#plink)、[tskit](../references/index.md#tskit)、[HyPhy](../references/index.md#hyphy)

泛基因组位于这些推断的上游：它改善不同遗传背景的序列表示，但不直接回答某个群体的历史或某个变异的功能。[N01](../references/nature-papers.md#n01)

古DNA还加入降解、损伤、污染和低覆盖的观测过程。古代样本的序列不应按无误差的现代完整基因型处理。[古DNA与进化条目](../atlas/domains/20-evolution.md)

## 4. 微生物组：有哪些、能做什么、正在做什么？

| 问题 | 数据与方法 | 输出及其含义 |
| --- | --- | --- |
| 群落有哪些标记序列？ | 16S/18S/ITS等扩增子、去噪与分类 | ASV和分类组成；受标记与参考限制 |
| 包含哪些物种/菌株？ | shotgun reads、标记或k-mer分类 | 来源及相对丰度估计 |
| 能重建哪些基因组？ | 宏基因组组装与分箱 | MAG及完整性/污染评估 |
| 编码什么功能潜力？ | 基因与通路注释 | 基因家族与候选功能 |
| 哪些功能正在表达？ | 宏转录/宏蛋白组 | RNA或蛋白活动层证据 |
| 群落间怎样交换物质？ | 代谢读出、环境条件、网络模型 | 交换与互作假设 |

扩增子去噪见[DADA2](../references/index.md#dada)；分类与组装参考的关系见[MetaPhlAn 4](../references/nature-papers.md#n06)；功能和群落模型见[微生物组条目](../atlas/domains/19-microbiome.md)。DNA中的功能基因是潜力证据，不是当时功能已经执行的直接记录。

群落比较还需要区分相对组成、绝对数量和多样性。共同增加可能由共同环境驱动，不必是直接互作；参考中不存在的微生物也不一定真的不存在于样本。[MetaPhlAn](../references/index.md#metaphlan)、[vegan](../references/index.md#vegan)

## 5. 生态与植物：观测缺失不是生物缺失

在一个简化占据模型中，z表示物种是否占据样地，y表示这次调查是否检出；可以设y|z服从Bernoulli(zp)，p为检测概率。没有检出时，既可能未占据，也可能占据但未检测到。重复调查和检测模型提供区分的额外信息。该式是解释“生态状态与观测过程不同”的简化模型，不是所有生态研究的唯一形式。[生态条目](../atlas/domains/21-ecology-plants.md)

物种分布模型把出现与环境联系起来，其输出是模型定义下的适生性或出现相关估计；遥感测到反射、温度或几何代理；eDNA测到环境中的遗传物质。这些都不是无条件的个体计数。空间自相关、采样偏倚、季节和检测过程，决定了结果能怎样外推。[biomod2](../references/index.md#biomod)、[vegan](../references/index.md#vegan)

植物遗传还经常面对田间区组、基因型×环境互作和多倍体。基因组选择预测的是定义好的目标性状；亚基因组表达要区分同源拷贝和剂量。它们不能直接照搬二倍体且唯一比对的假设。[植物与农业条目](../atlas/domains/21-ecology-plants.md)、[PLINK](../references/index.md#plink)

## 6. 神经科学：结构、活动、行为与计算

| 层次 | 测量/处理 | 主要结果 |
| --- | --- | --- |
| 结构连接 | 连续EM、分割、骨架与突触识别 | 神经元及连接图 |
| 电活动 | 电极信号与spike sorting | unit、spike时间、波形及质量 |
| 活动成像 | 钙/电压图像、运动校正与信号分离 | 空间成分、轨迹、事件或推断活动 |
| 行为 | 视频关键点与时序模型 | 姿态、运动和行为状态 |
| 编码/解码 | 活动与刺激/行为的统计模型 | 调谐、可预测信息、泛化性能 |
| 因果干预 | 指定细胞/回路的干预和功能读出 | 给定条件下的功能效应 |

Kilosort、CaImAn和DeepLabCut分别位于不同的数据处理层。[Kilosort4](../references/index.md#kilosort)、[CaImAn](../references/index.md#caiman)、[DeepLabCut](../references/index.md#dlc)

MICrONS通过配准把活动和EM结构对应到相同神经对象，使“哪些细胞怎样活动”和“它们怎样连接”可以联合研究。这里增加的关键是对象对应，而不是假定结构边就等于功能强度；相关响应、连接存在和行为因果作用仍然分开。[N11](../references/nature-papers.md#n11)

## 7. 数学模型如何解释机制？

机制模型把过程写成可计算规则。ODE描述连续量随时间变化；随机反应模型处理离散事件；反应—扩散模型加入空间运输；代理模型以细胞或个体为行动单元；网络模型组织相互作用结构。[COPASI](../references/index.md#copasi)、[生物物理与模型条目](../atlas/domains/22-biophysics-modeling.md)

模型可以用于从规则预测观测，也可以用于从观测估计参数。后者可能不可辨识：多组参数或多个机制都能生成近似相同的曲线。“拟合好”因此只表示与这些数据兼容，不单独保证机制唯一。灵敏度、参数范围、外部读出和新的干预会对不同解释增加限制。[COPASI](../references/index.md#copasi)

这套逻辑同样连接定量发育与合成生物学：前者问组织图案怎样出现，后者问指定的系统规则能否产生预期行为。反应、扩散、反馈、细胞生长和机械作用需要与实际读出相连，而不是只画网络箭头。[定量发育与合成生物学](../atlas/domains/25-development-synthetic-biology.md)

## 8. 转化与药理：把暴露、响应和结局分开

药物或其他干预的剂量、体内暴露、靶点结合、分子响应和个体结局不是同一变量。PK/PD、剂量响应、联合效应、生存分析和多变量预测分别处理不同关系。离体细胞效应不能不经论证就外推到个体结局。[转化研究与药理条目](../atlas/domains/24-translational-pharmacology.md)、[statsmodels](../references/index.md#stats)、[COPASI](../references/index.md#copasi)

## 共同的分析意义

不同尺度的技术之所以能互相连接，是因为它们为同一问题增加了不同约束：序列约束历史，成像约束位置和几何，时序约束过程，干预约束改变后的响应。知识整合应说明这些约束怎样相互支持或冲突，而不是把所有结果压缩成一个“综合评分”。
