# 生物学技术与分析方法知识导航

这个知识库解释生物学对象、测量原理和计算意义：一个分子或细胞怎样变成数据，我们为什么要进行某种分析，又能据此理解什么。

## 从不熟悉的概念进入

不需要先懂代码或背缩写。下面四篇正文解释后续技术共同依赖的概念；数字示例均用于讲清含义，不冒充真实实验。

| 当前想弄明白的问题 | 对应正文 |
| --- | --- |
| 细胞、基因、染色体、RNA和蛋白是什么？基因表达是什么意思？ | [生物学基础](../docs/biology-basics.md) |
| 测序究竟读了什么？显微图、质谱和流式中的数字来自哪里？ | [实验怎样产生数据](../docs/instruments-and-data.md) |
| 什么是样本、计数和矩阵？怎样理解重复、归一化、P值和FDR？ | [数据与统计基础](../docs/statistics-basics.md) |
| 比对、组装、降维、聚类、富集、网络和AI分别在做什么？ | [计算方法基础](../docs/computation-basics.md) |

这些是相互连接的知识页，不是需要打卡的课程。遇到具体格式或缩写，可查[数据对象](../data-formats/index.md)和[语境化术语](../glossary/index.md)。

## 把技术连接到生物学问题

| 想理解的问题 | 知识正文 |
| --- | --- |
| 从实验到数据再到解释，中间发生了什么？ | [测量、数据、模型与生物学解释](../docs/learning-guide.md) |
| 同一个问题为什么需要多种技术？什么是互补、替代和验证？ | [技术之间的逻辑与分析意义](../docs/technique-relations.md) |
| 序列、染色质、转录和RNA加工怎样影响表达？ | [基因组、染色质、RNA与调控](../docs/molecular-regulation.md) |
| 细胞身份、状态、组成、位置、命运和谱系有何区别？ | [细胞、空间、时间与扰动](../docs/cells-space-time.md) |
| 蛋白量、结构、结合、活性、代谢物浓度和通量怎样联系？ | [蛋白、结构、相互作用与代谢](../docs/structure-function.md) |
| 共同祖先、环境、神经活动与系统行为怎样从数据研究？ | [群体、进化、生态、神经与系统建模](../docs/populations-systems.md) |

## 技术与方法查阅层

以下保留25个领域、194个方法家族条目与原有M编号。它们提供原理、目的、输入、处理、输出和边界的快速索引；同一条目可能归并多个子方法，不代表194个软件，也不是对全部论文方法的穷尽统计。

### 共用的数据与推断基础

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [01 统计与研究设计](domains/01-statistics.md) | 怎样区分变化、误差、效应与混杂？ | M001–M010 |
| [02 数据工程与共用分析](domains/02-data-foundations.md) | 数据怎样整理、比较、分组与概括？ | M011–M018 |

不熟悉矩阵和模型时，先看[统计基础](../docs/statistics-basics.md)和[计算任务解释](../docs/computation-basics.md)。

### 序列、遗传变异与分子调控

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [03 基因组与变异](domains/03-genomics.md) | 序列是什么，哪些位置和结构不同？ | M019–M026 |
| [04 群体遗传与因果优先级](domains/04-population-genetics.md) | 变异与性状怎样关联，如何缩小候选机制？ | M027–M034 |
| [05 转录组与RNA机制](domains/05-transcriptomics.md) | RNA的数量、加工、合成与降解如何改变？ | M035–M045 |
| [06 表观组与三维基因组](domains/06-epigenomics.md) | DNA怎样包装、开放、被占据和空间组织？ | M046–M053 |

基因、等位基因和转录本的区别见[生物学基础](../docs/biology-basics.md)；这些方法的内在联系见[分子调控](../docs/molecular-regulation.md)。

### 细胞、组织、动态与功能检验

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [07 单细胞与细胞图谱](domains/07-single-cell.md) | 有哪些细胞，它们的状态和组成怎样不同？ | M054–M062 |
| [08 细胞动态与谱系](domains/08-dynamics-lineage.md) | 状态顺序、时间和共同祖先怎样区分？ | M063–M068 |
| [09 空间组学与组织生态位](domains/09-spatial-omics.md) | 细胞和分子在哪里，局部环境怎样组织？ | M069–M076 |
| [10 多组学、网络与系统整合](domains/10-multi-omics-networks.md) | 多种读出怎样共同约束状态和候选机制？ | M077–M082 |
| [11 扰动筛选与功能基因组](domains/11-perturbation.md) | 改变基因或元件，哪个读出受到影响？ | M083–M089 |
| [12 免疫组库与肿瘤演化](domains/12-immunity-cancer.md) | 受体、克隆、遗传背景和状态怎样对应？ | M090–M095 |
| [25 定量发育与合成生物学](domains/25-development-synthetic-biology.md) | 细胞行为、反馈和规则怎样形成组织或功能？ | M189–M194 |

条码、分割和混合信号的背景见[实验与数据](../docs/instruments-and-data.md)；从读出到细胞解释见[细胞、空间与时间](../docs/cells-space-time.md)。

### 分子组成、结构与化学过程

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [13 蛋白质组与蛋白状态](domains/13-proteomics.md) | 蛋白有多少，怎样修饰、定位和组装？ | M096–M104 |
| [14 代谢组、脂质组与通量](domains/14-metabolomics.md) | 化合物数量和反应流量是什么关系？ | M105–M111 |
| [15 结构生物学与实验重建](domains/15-structural-biology.md) | 三维结构如何从实验约束或模型中获得？ | M112–M119 |
| [16 计算化学、设计与药物分子](domains/16-computational-chemistry.md) | 分子怎样结合、运动，怎样提出新候选？ | M120–M126 |

质谱、密度图和坐标的区别见[测量原理](../docs/instruments-and-data.md)；数量、结合和活性的关系见[结构与功能](../docs/structure-function.md)。

### 图像、神经活动与行为

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [17 显微图像与细胞表型](domains/17-imaging-cytometry.md) | 图像和多通道信号怎样成为对象及定量？ | M127–M134 |
| [18 神经活动、连接组与行为](domains/18-neuroscience-behavior.md) | 结构、活动、刺激和行为怎样对应？ | M135–M142 |

像素、通道和事件见[实验与数据](../docs/instruments-and-data.md)；活动与结构连接的区别见[神经与系统](../docs/populations-systems.md)。

### 群落、历史与环境

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [19 微生物组与环境组学](domains/19-microbiome.md) | 有哪些微生物，编码什么，正在表达什么？ | M143–M150 |
| [20 进化、比较与古基因组](domains/20-evolution.md) | 序列怎样保存祖先、选择和历史信息？ | M151–M158 |
| [21 生态、植物与农业](domains/21-ecology-plants.md) | 分布、环境、检测过程与性状怎样联系？ | M159–M166 |

种群、群落、多样性与系统发育树见[群体、进化与生态](../docs/populations-systems.md)。

### 跨尺度模型与转化问题

| 领域 | 主要回答的问题 | 条目 |
| --- | --- | --- |
| [22 生物物理与数学建模](domains/22-biophysics-modeling.md) | 什么规则能产生观测，哪些机制可区分？ | M167–M174 |
| [23 生物AI与基础模型](domains/23-biological-ai.md) | 模型学了什么映射，预测怎样验证？ | M175–M182 |
| [24 转化研究与药理数据](domains/24-translational-pharmacology.md) | 剂量、暴露、响应和结局是什么关系？ | M183–M188 |

模型、拟合和预测见[计算基础](../docs/computation-basics.md)；过程、平衡和速率见[结构与代谢](../docs/structure-function.md)及[系统建模](../docs/populations-systems.md)。

## 查读出、文件、词义和依据

[实验读出](../experiments/index.md)解释对照和测量；[数据对象与格式](../data-formats/index.md)展示字段与单位；[术语词典](../glossary/index.md)区分同一缩写的不同语境。

[百科概念对应](../references/wikipedia.md)给出基础入口及核对来源；[原始研究与官方文档](../references/index.md)用于追溯具体方法；[Nature系列论文解析](../references/nature-papers.md)说明技术如何用于研究。各类来源承担不同角色，不能用一个百科链接代替某项方法全部能力的验证。
