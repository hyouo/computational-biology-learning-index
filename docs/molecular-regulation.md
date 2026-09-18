# 基因组、染色质、RNA与调控

[知识导航](../atlas/index.md) · [技术关系](technique-relations.md) · [细胞层次](cells-space-time.md)

## 1. 先分清信息、调控与分子数量

DNA保存可传递的序列信息；转录产生RNA；部分RNA经翻译形成蛋白。中心法则讨论的是序列信息的转移，不是说所有生物学影响都只能单向传递。蛋白对转录、染色质或代谢的反馈，不等于蛋白序列被逆向翻译成DNA。[Crick, 1970](../references/index.md#crick)

基因表达也不只是“开”或“关”。起始、延伸、剪接、末端加工、运输、降解和翻译，都能改变我们观察到的RNA或蛋白。测量稳态RNA、测量新合成RNA和测量核糖体占据，所约束的是不同变量。[SLAM-seq](../references/index.md#slam)、[Ribo-seq](../references/index.md#ribo)

## 2. 基因组分析先建立对象与坐标

**比对**把读段放到参考序列的位置；**组装**从重叠等信息重建较长序列；**变异检测**在给定参考和误差模型下比较差异；**分相**确定变异属于哪条单倍型；**注释**解释变异处于什么基因或功能区域。一个VCF记录因此既包含生物差异，也依赖参考版本、坐标、等位表示和检测能力。[HTSlib](../references/index.md#hts)、[hifiasm](../references/index.md#hifiasm)

短变异、结构变异、拷贝数和重复区域不是同一检测问题。长读段与单倍型组装提供跨越复杂区域的序列证据；泛基因组把多个个体的路径纳入参考，降低“一条参考代表所有序列”的限制。[N01](../references/nature-papers.md#n01)

对应条目：[M019–M026](../atlas/domains/03-genomics.md)。

## 3. 顺式元件、反式因子与染色质

**顺式调控元件**是与目标基因处于同一DNA分子上的调控序列，例如启动子及增强子；**反式因子**是可作用于其他位点的调控分子，例如转录因子。启动子涉及转录起始，增强子可在特定细胞条件下影响转录。motif是序列偏好的模型，不是一个转录因子真实占据某位置的记录。[MEME Suite](../references/index.md#meme)、[SCENIC+](../references/nature-papers.md#n03)

染色质测量从多个侧面限制调控解释：

| 技术或分析 | 测量/计算原理 | 输入 → 结果 | 生物学意义 |
| --- | --- | --- | --- |
| ATAC-seq / DNase-seq | 利用酶接近暴露DNA的性质 | 片段或切割信号 → 可及区域 | 哪些区域处于可接近状态 |
| ChIP-seq | 富集目标蛋白相关染色质片段 | 富集与背景数据 → 目标相关峰或域 | 指定因子/修饰在哪里富集 |
| CUT&RUN / CUT&Tag | 抗体把切割酶或转座酶引至靶标附近 | 靶向片段 → 占据/修饰相关图谱 | 以不同实验机制观察特定染色质成分 |
| 甲基化分析 | 转化、酶或直接信号区分碱基修饰 | 位点信号 → 修饰比例、差异区域 | 某类DNA修饰怎样分布 |
| motif / footprint | 序列偏好及切割模式建模 | 序列/切割图谱 → 候选因子信息 | 提出可能的调控者 |
| Hi-C / Micro-C | 记录邻近连接产生的片段对 | read pairs → 接触矩阵及结构特征 | 基因组区域在群体中如何接近 |

前几类实验的关键差异见[ATAC原始论文](../references/index.md#atacpaper)与[CUT&Tag原始论文](../references/index.md#cuttag)；各模态的处理与限定见[表观组条目](../atlas/domains/06-epigenomics.md)。它们不是必须串联的一套流程。某区域开放，不代表某个TF已经结合；接触频率也不是直接测得的物理距离或调控强度。

## 4. 从候选增强子到靶基因，为什么需要多种信息？

一个开放区域可能接近多个基因；序列motif可能对应同一家族多个TF；基因与区域共变也可能来自共同细胞状态。增强子—靶基因链接需要明确其依据是距离、接触、表达共变、序列先验还是扰动。不同依据约束的是不同解释。[SCENIC+](../references/nature-papers.md#n03)

**报告实验和内源扰动也不等价。**MPRA/STARR-seq询问序列在报告体系中的输出；内源元件扰动在原有基因组背景中检验功能。Perturb-tracing则把遗传干预与三维染色质读出相连。结果不一致时，应先检查所问的对象和环境是否一致，而不是简单认定某一种技术“错了”。[扰动方法](../atlas/domains/11-perturbation.md)、[N10](../references/nature-papers.md#n10)

## 5. 转录组的几种“变化”

| 待解释的变量 | 相应方法 | 主要结果 |
| --- | --- | --- |
| 一个基因的RNA总量 | bulk或单细胞RNA定量、差异表达 | 条件效应及不确定性 |
| 外显子怎样组合 | 长读长转录本重建、可变剪接分析 | 转录本结构、PSI或异构体使用 |
| 从哪里开始、在哪里结束 | CAGE/RAMPAGE、3′端/APA分析 | 起始与加尾位点使用 |
| RNA合成与消失有多快 | 新生转录、代谢标记与时间模型 | 合成、降解或暂停的相关参数 |
| 哪些区域被翻译 | Ribo-seq | 核糖体占据、阅读框及相对翻译信息 |
| 哪些RNA与蛋白接触 | CLIP/eCLIP/iCLIP | RBP接触相关位点或区域 |
| RNA的化学与配对状态 | 修饰分析、DMS/SHAPE、互作结构分析 | 修饰候选、反应性或结构约束 |

异构体重建和剪接比例比较分别见[IsoQuant](../references/nature-papers.md#n02)及[rMATS](../references/index.md#rmats)；动态与分子接触见[SLAM-seq](../references/index.md#slam)、[eCLIP](../references/index.md#eclip)及[DMS-MaPseq](../references/index.md#dms)。这些输出不能只用一个“差异基因列表”概括。

在最简单的一阶RNA模型中，设R为RNA量，k_syn为合成速率，k_deg为降解常数：

$$\frac{dR}{dt}=k_{syn}-k_{deg}R.$$

若达到稳态，则R=k_syn/k_deg。这个推导说明：相同的RNA量可以对应不同的合成和降解组合；一个静态表达值通常不能同时确定两者。真实体系还可能有加工、运输、反馈与非稳态过程。标记和时间信息增加了对这些过程的约束。[SLAM-seq](../references/index.md#slam)、[COPASI](../references/index.md#copasi)

对应条目：[M035–M045](../atlas/domains/05-transcriptomics.md)。

## 6. 遗传关联怎样进入分子机制解释？

GWAS把变异与性状联系起来，分子QTL把变异与表达/剪接等分子性状联系起来。精细定位处理LD下多个候选变异的问题；共定位检验两个性状是否兼容共享信号。它们对“可能由什么分子过程介导”提供不同支持，但共定位本身不证明中介方向，也不保证候选基因是唯一因果基因。[SuSiE](../references/index.md#susie)、[coloc](../references/index.md#coloc)

从序列预测调控读出的模型处于另一个位置：它为未测量变异提供功能假设。训练目标是功能轨道、序列概率还是特定表型，决定了分数的语义；不能把不同模型的分数都称为“致病程度”。[AlphaGenome](../references/nature-papers.md#n14)、[Evo 2](../references/nature-papers.md#n15)

## 7. 这一层与其他层怎样连接？

调控网络解释细胞状态的候选控制关系，见[细胞、空间与时间](cells-space-time.md)；RNA并不直接等于蛋白数量、活性或反应通量，见[结构、功能与代谢](structure-function.md)；不同个体的变异和共同祖先还引入群体结构，见[群体、生态与系统](populations-systems.md)。这些是同一生物系统的不同观测层，不是某一组学天然解释其他所有组学。
