# 近年 Nature 系列论文：技术怎样连接到生物学问题

这里按技术关系选取2023—2026年的16篇原始研究或技术报告，核对日期为2026-09-18。范围包括 Nature、Nature Methods、Nature Biotechnology 和 Nature Cell Biology；不是逐期穷尽检索，也不以期刊声望代替方法有效性。年份按正式发表信息记录，不从DOI中的数字推断年份。旧的奠基论文及工具文档见[基础来源](index.md)。

各项概括依据论文页面可取得的摘要与正文；N16使用公开摘要与图注，不声称核验了付费全文或全部补充方法。下文的“理解要点”是对方法用途和证据边界的解释，不是新增实验结论。

[知识导航](../atlas/index.md) · [技术关系](../docs/technique-relations.md)

<a id="n01"></a>
## N01 多个基因组怎样成为参考，而不是只依赖一条序列？

**A draft human pangenome reference. Nature, 2023.** DOI: [10.1038/s41586-023-05896-x](https://www.nature.com/articles/s41586-023-05896-x)。

多个人类单倍型组装被整合为泛基因组，使部分线性参考遗漏的序列和复杂结构变异能够被表示。它连接的是“组装—群体多样性—参考表示—变异检测”，不是从变异直接推导表型。理解要点：参考是分析中的测量坐标和先验，参考改变会改变可观察到的变异。

关联：[基因组与变异](../atlas/domains/03-genomics.md)；[群体与系统](../docs/populations-systems.md)。

<a id="n02"></a>
## N02 为什么表达量相同的基因可能产生不同转录本？

**Accurate isoform discovery with IsoQuant using long reads. Nature Biotechnology, 2023.** DOI: [10.1038/s41587-022-01565-y](https://www.nature.com/articles/s41587-022-01565-y)。

IsoQuant利用长RNA读段及内含子图重建转录本，并进行读段归属和定量。它连接“读段中的剪接结构—转录本模型—异构体使用”，与只比较基因总计数不是同一任务。重建出的新转录本仍需检查测序、比对和截短等替代解释。

关联：[M036](../atlas/domains/05-transcriptomics.md#m036)；[分子调控](../docs/molecular-regulation.md)。

<a id="n03"></a>
## N03 开放区域如何关联到转录因子和靶基因？

**SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks. Nature Methods, 2023.** DOI: [10.1038/s41592-023-01938-4](https://www.nature.com/articles/s41592-023-01938-4)。

将染色质可及性、表达及motif信息结合，推断TF—增强子—靶基因关系。其意义是把不同分子层组织成可检验的调控假设；网络边不是每一条都经过物理结合与干预验证的事实。

关联：[多组学与网络](../atlas/domains/10-multi-omics-networks.md)；[分子调控](../docs/molecular-regulation.md)。

<a id="n04"></a>
## N04 细胞身份怎样放回组织位置？

**Molecularly defined and spatially resolved cell atlas of the whole mouse brain. Nature, 2023.** DOI: [10.1038/s41586-023-06808-9](https://www.nature.com/articles/s41586-023-06808-9)。

研究将MERFISH测得的空间分子信息与scRNA-seq整合，再关联解剖坐标。要区分直接成像的基因、映射的细胞类型与补全的表达；空间接近和配体—受体模式支持通信假设，并不替代功能验证。

关联：[空间组学](../atlas/domains/09-spatial-omics.md)；[细胞、空间与时间](../docs/cells-space-time.md)。

<a id="n05"></a>
## N05 预测一个结构与设计一个分子有什么不同？

**De novo design of protein structure and function with RFdiffusion. Nature, 2023.** DOI: [10.1038/s41586-023-06415-8](https://www.nature.com/articles/s41586-023-06415-8)。

RFdiffusion通过结构去噪学习生成蛋白骨架，并在多类设计任务中结合实验表征。它的角色是提出满足约束的候选；骨架生成、序列选择、结构预测和实际功能测试是不同环节，计算筛选通过不是实验功能成立的同义词。

关联：[计算化学与设计](../atlas/domains/16-computational-chemistry.md)；[结构与功能](../docs/structure-function.md)。

<a id="n06"></a>
## N06 未培养的微生物如何进入群落分析？

**Extending and improving metagenomic taxonomic profiling with uncharacterized species using MetaPhlAn 4. Nature Biotechnology, 2023.** DOI: [10.1038/s41587-023-01688-w](https://www.nature.com/articles/s41587-023-01688-w)。

将分离株基因组与宏基因组组装基因组整合，构建物种水平基因组群及标记基因，再用标记覆盖估计群落组成。它连接“组装发现—参考数据库—新样本定量”；参考缺失和相对丰度的分母仍限制解释。

关联：[微生物组](../atlas/domains/19-microbiome.md)；[群体与系统](../docs/populations-systems.md)。

<a id="n07"></a>
## N07 分子组成怎样转化为三维结构假设？

**Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature, 2024.** DOI: [10.1038/s41586-024-07487-w](https://www.nature.com/articles/s41586-024-07487-w)。

从蛋白、核酸、配体等实体预测复合物坐标与置信度。应把几何预测、结合亲和力、反应速率和构象分布分开理解。论文自身讨论了构象覆盖等限制；不能把模型多次采样直接解释为实验热力学分布。

关联：[M117](../atlas/domains/15-structural-biology.md#m117)；[结构与功能](../docs/structure-function.md)。

<a id="n08"></a>
## N08 表达快照怎样用于推断细胞命运？

**CellRank 2: unified fate mapping in multiview single-cell data. Nature Methods, 2024.** DOI: [10.1038/s41592-024-02303-9](https://www.nature.com/articles/s41592-024-02303-9)。

在统一状态转移框架中利用表达、方向、实验时间或代谢标记等不同数据视角，推断终末状态与命运概率。这些视角可按数据选择，不是每次都必须齐全。命运概率是模型输出，与条码记录的共同祖先或活细胞追踪的真实轨迹不同。

关联：[动态与谱系](../atlas/domains/08-dynamics-lineage.md)；[细胞、空间与时间](../docs/cells-space-time.md)。

<a id="n09"></a>
## N09 细胞间通信怎样连接到细胞内响应？

**LIANA+ provides an all-in-one framework for cell–cell communication inference. Nature Cell Biology, 2024.** DOI: [10.1038/s41556-024-01469-w](https://www.nature.com/articles/s41556-024-01469-w)。

整合配体—受体先验、单细胞/空间与多条件信息，并关联细胞内信号。它有助于组织跨细胞假设，不会把转录本表达自动变成配体分泌、受体活化或已经测得的因果路径；结果依赖先验覆盖和输入模态。

关联：[M073](../atlas/domains/09-spatial-omics.md#m073)；[细胞、空间与时间](../docs/cells-space-time.md)。

<a id="n10"></a>
## N10 什么证据可以把染色质结构与基因功能联系起来？

**Perturb-tracing enables high-content screening of multi-scale 3D genome regulators. Nature Methods, 2025.** DOI: [10.1038/s41592-025-02652-z](https://www.nature.com/articles/s41592-025-02652-z)。

将pooled CRISPR扰动身份的原位读取与染色质追踪结合，在相同细胞内关联扰动和三维组织读出。其分析意义是从结构共变推进到干预后的结构改变；仍需区分直接结构作用与细胞周期、存活或其他下游变化。

关联：[表观组](../atlas/domains/06-epigenomics.md)；[扰动筛选](../atlas/domains/11-perturbation.md)。

<a id="n11"></a>
## N11 神经元的活动和连接怎样对应？

**Functional connectomics spanning multiple areas of mouse visual cortex. Nature, 2025.** DOI: [10.1038/s41586-025-08790-w](https://www.nature.com/articles/s41586-025-08790-w)。

MICrONS把钙成像的功能响应与电子显微镜重建的神经连接配准。关键不是分别获得两张大图，而是同一对象的结构与功能对应。连接存在、活动相关、突触功能强度和行为因果作用依然是不同问题。

关联：[神经科学](../atlas/domains/18-neuroscience-behavior.md)；[群体与系统](../docs/populations-systems.md)。

<a id="n12"></a>
## N12 无空间坐标的细胞可以获得怎样的空间信息？

**Nicheformer: a foundation model for single-cell and spatial omics. Nature Methods, 2025.** DOI: [10.1038/s41592-025-02814-z](https://www.nature.com/articles/s41592-025-02814-z)。

用解离单细胞与空间转录组共同学习细胞表征，用于空间相关预测。模型迁移来的空间语境不是原始实验新增的坐标；预测的可信范围应由任务、组织和留出数据上的验证来决定。

关联：[生物AI](../atlas/domains/23-biological-ai.md)；[细胞、空间与时间](../docs/cells-space-time.md)。

<a id="n13"></a>
## N13 为什么图像分割属于生物学测量的一部分？

**CellSAM: a foundation model for cell segmentation. Nature Methods, 2025.** DOI: [10.1038/s41592-025-02879-w](https://www.nature.com/articles/s41592-025-02879-w)。

以细胞检测和分割模型从图像产生对象边界。边界随后决定强度、形态及分子归属，因此分割不是纯展示步骤；跨成像域的性能仍需在目标数据上检查，不能从算法名称直接推断适用性。

关联：[显微图像](../atlas/domains/17-imaging-cytometry.md)；[测量与推断](../docs/learning-guide.md)。

<a id="n14"></a>
## N14 序列模型预测的“功能”具体是什么？

**Advancing regulatory variant effect prediction with AlphaGenome. Nature, 2026.** DOI: [10.1038/s41586-025-10014-0](https://www.nature.com/articles/s41586-025-10014-0)。

从DNA序列预测表达、起始、剪接、可及性及染色质相关读出，并用于变异效应预测。它学习的是序列与指定功能测量之间的映射；预测某条轨道改变不等于完成了该变异的个体表型或疾病因果验证。

关联：[分子调控](../docs/molecular-regulation.md)；[生物AI](../atlas/domains/23-biological-ai.md)。

<a id="n15"></a>
## N15 基因组语言模型与实验读出预测模型有什么不同？

**Genome modelling and design across all domains of life with Evo 2. Nature, 2026.** DOI: [10.1038/s41586-026-10176-5](https://www.nature.com/articles/s41586-026-10176-5)。

Evo 2从大规模DNA序列学习表征，用于序列评分、变异分析和受约束的生成研究。与直接学习特定功能轨道的模型相比，其训练目标和输出语义不同；序列概率、功能分数和真实生物功能不能直接互换。

关联：[生物AI](../atlas/domains/23-biological-ai.md)；[技术关系](../docs/technique-relations.md)。

<a id="n16"></a>
## N16 单细胞代谢异质性如何成为可计算的数据？

**Deep-coverage single-cell metabolomics enabled by ion mobility-resolved mass cytometry. Nature Methods, 2026.** DOI: [10.1038/s41592-025-02970-2](https://www.nature.com/articles/s41592-025-02970-2)。

论文将单细胞引入、离子迁移率质谱与MetCell分析结合，用于代谢状态表征。需区分峰检测、代谢物注释与单细胞定量；峰数不等于已唯一鉴定的代谢物数，丰度也不等于代谢通量。本条依据公开摘要及图注。

关联：[代谢组](../atlas/domains/14-metabolomics.md)；[结构与功能](../docs/structure-function.md)。
