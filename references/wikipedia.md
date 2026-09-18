# 百科概念与基础来源

[知识导航](../atlas/index.md) · [原始研究与实现文档](index.md) · [近年Nature系列论文](nature-papers.md)

本页将本轮查阅的维基百科概念与知识正文对应起来。百科入口署名为 Wikipedia contributors，链接到英文条目，中文列说明其在本知识库中的用途；可在百科页面切换语言。查阅日期：**2026-09-18**。这些是动态页面，不代表固定历史版本；未列出的条目不声称已核验。

正文是针对本知识库重新组织的中文解释，不复制百科原文、表格或图片。百科帮助厘清定义和相邻概念；具体统计含义、实验原理与方法能力还对应下方原始论文或官方说明。这里只说明来源范围，不表示全部194个既有方法条目已重新完成逐项文献审查。

<a id="biology"></a>
## 生物学对象：细胞、遗传信息和分子功能

对应正文：[生物学基础](../docs/biology-basics.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [Cell (biology)](https://en.wikipedia.org/wiki/Cell_%28biology%29) | 细胞、细胞结构和原核/真核背景 |
| [Gene](https://en.wikipedia.org/wiki/Gene) | 基因不是染色体，也不只指蛋白编码片段 |
| [Gene expression](https://en.wikipedia.org/wiki/Gene_expression) | 从遗传信息产生功能产物及其调节 |
| [Central dogma of molecular biology](https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology) | 序列信息转移与调控反馈的区别 |
| [Protein](https://en.wikipedia.org/wiki/Protein) | 氨基酸、蛋白结构和功能 |
| [Protein structure](https://en.wikipedia.org/wiki/Protein_structure) | 序列、局部结构、折叠与复合体层次 |
| [Enzyme](https://en.wikipedia.org/wiki/Enzyme) | 催化、底物、反应速率与平衡 |
| [Metabolism](https://en.wikipedia.org/wiki/Metabolism) | 合成、分解和代谢网络 |

基因、染色质、转录和翻译的基础定义同时参照[NHGRI术语表](https://www.genome.gov/genetics-glossary)。中心法则的解释以[Crick原文](https://doi.org/10.1038/227561a0)的序列信息含义为准，不把百科概括当成“所有生物作用都只能单向传递”。

<a id="molecular"></a>
## 核酸、测序与调控

对应正文：[测量原理](../docs/instruments-and-data.md)、[分子调控](../docs/molecular-regulation.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [DNA sequencing](https://en.wikipedia.org/wiki/DNA_sequencing) | 测序、读段、平台读出及序列信息 |
| [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment) | 对应位置、错配、插入缺失、局部/全局比对 |
| [RNA-Seq](https://en.wikipedia.org/wiki/RNA-Seq) | RNA测量与转录组分析的范围 |
| [Alternative splicing](https://en.wikipedia.org/wiki/Alternative_splicing) | 外显子组合与转录本异构体 |
| [Chromatin](https://en.wikipedia.org/wiki/Chromatin) | DNA包装与可接近性背景 |
| [Epigenetics](https://en.wikipedia.org/wiki/Epigenetics) | 不改变DNA序列的功能状态与遗传语境 |
| [Genome-wide association study](https://en.wikipedia.org/wiki/Genome-wide_association_study) | 基因型、性状和关联分析 |

比对和文件定义参照[HTSlib](https://www.htslib.org/doc/)；定量与比较参照[DESeq2](index.md#deseq)；长读长结构重建参照[IsoQuant](nature-papers.md#n02)；开放染色质与抗体靶向富集的差异参照[ATAC](index.md#atacpaper)和[CUT&Tag](index.md#cuttag)。

<a id="cells"></a>
## 细胞、空间与扰动

对应正文：[细胞、空间与时间](../docs/cells-space-time.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [Single-cell analysis](https://en.wikipedia.org/wiki/Single-cell_analysis) | 单细胞是测量尺度，不只是一种RNA技术 |
| [Spatial transcriptomics](https://en.wikipedia.org/wiki/Spatial_transcriptomics) | 位置与表达的结合 |
| [CRISPR gene editing](https://en.wikipedia.org/wiki/CRISPR_gene_editing) | 遗传干预与筛选的背景 |
| [Proteomics](https://en.wikipedia.org/wiki/Proteomics) | 系统测量蛋白及其状态 |
| [Metabolomics](https://en.wikipedia.org/wiki/Metabolomics) | 代谢分子集合与化学状态 |

单细胞样本层比较的依据见[muscat原始研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC7705760/)；多模态分析见[WNN](index.md#wnn)和[MOFA](index.md#mofa)；扰动读出见[MAGeCK](index.md#mageck)及[相关Nature研究](nature-papers.md)。

<a id="measurement"></a>
## 仪器与实验读出

对应正文：[实验怎样产生数据](../docs/instruments-and-data.md)、[实验读出表](../experiments/index.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [Polymerase chain reaction](https://en.wikipedia.org/wiki/Polymerase_chain_reaction) | 特定核酸扩增，不等于所有PCR都能直接绝对定量 |
| [Antibody](https://en.wikipedia.org/wiki/Antibody) | 分子识别与抗体检测 |
| [Hybridization probe](https://en.wikipedia.org/wiki/Hybridization_probe) | 互补核酸识别与标记探针 |
| [Fluorescence microscope](https://en.wikipedia.org/wiki/Fluorescence_microscope) | 激发、发射、图像通道与信号 |
| [Flow cytometry](https://en.wikipedia.org/wiki/Flow_cytometry) | 逐事件检测与分选的区别 |
| [Chromatography](https://en.wikipedia.org/wiki/Chromatography) | 混合物分离及保留时间 |
| [Mass spectrometry](https://en.wikipedia.org/wiki/Mass_spectrometry) | 离子、质荷比与碎片谱 |
| [Cryogenic electron microscopy](https://en.wikipedia.org/wiki/Cryogenic_electron_microscopy) | 冷冻电子显微测量与重建 |
| [Nuclear magnetic resonance spectroscopy](https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance_spectroscopy) | 核磁共振谱与分子环境 |
| [Molecular dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics) | 给定相互作用模型下的运动模拟 |

谱图到肽与蛋白的分析见[MaxQuant](index.md#maxquant)；DIA信号处理见[DIA-NN](https://www.nature.com/articles/s41592-019-0638-x)；细胞对象识别见[CellProfiler](index.md#cellprof)；流式数据处理见[FlowKit](index.md#flow)；结构与模拟分别见[CryoSPARC](index.md#cryo)、[Phenix](index.md#phenix)和[GROMACS](index.md#md)。它们只支持各自对应任务，不互相代替测量证据。

<a id="statistics"></a>
## 数据、统计与判断

对应正文：[数据与统计基础](../docs/statistics-basics.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [Statistical hypothesis test](https://en.wikipedia.org/wiki/Statistical_hypothesis_test) | 零假设、P值与检验错误 |
| [Confidence interval](https://en.wikipedia.org/wiki/Confidence_interval) | 区间估计与重复抽样解释 |
| [False discovery rate](https://en.wikipedia.org/wiki/False_discovery_rate) | 多重检验与发现集合的错误控制 |
| [Confounding](https://en.wikipedia.org/wiki/Confounding) | 关心因素与其他因素的混杂 |
| [Pseudoreplication](https://en.wikipedia.org/wiki/Pseudoreplication) | 观测数与独立重复数的区别 |
| [Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis) | 结果、解释变量、效应与残差 |

P值、区间和模型条件需同时阅读[NIST统计手册](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm)；FDR程序参照[BH原始论文](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)，不是给每个发现分配“为假的概率”。

<a id="computation"></a>
## 计算任务与知识表示

对应正文：[计算方法基础](../docs/computation-basics.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [Bioinformatics](https://en.wikipedia.org/wiki/Bioinformatics) | 生物数据组织、分析与方法背景 |
| [Computational biology](https://en.wikipedia.org/wiki/Computational_biology) | 用计算和模型研究生物问题 |
| [Principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) | 主要变异方向和低维线性表示 |
| [Cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis) | 根据相似性分组 |
| [Machine learning](https://en.wikipedia.org/wiki/Machine_learning) | 从数据学习映射与表示 |
| [Gene set enrichment analysis](https://en.wikipedia.org/wiki/Gene_set_enrichment_analysis) | 从单个基因到基因集合的统计概括 |
| [Gene Ontology](https://en.wikipedia.org/wiki/Gene_Ontology) | 功能概念、层级关系与注释 |
| [Flux balance analysis](https://en.wikipedia.org/wiki/Flux_balance_analysis) | 化学计量守恒、边界和目标约束 |

算法与评估参照[scikit-learn](https://scikit-learn.org/stable/user_guide.html)；单细胞处理参照[Scanpy](https://scanpy.readthedocs.io/en/stable/tutorials/basics/clustering.html)；GSEA参照[原始研究](https://www.broadinstitute.org/publications/broad3678)；FBA参照[COBRApy模型说明](https://cobrapy.readthedocs.io/en/latest/simulating.html)。

<a id="systems"></a>
## 历史、群落、神经与系统

对应正文：[群体、进化、生态、神经与系统建模](../docs/populations-systems.md)。

| 百科条目 | 本知识库用来解释什么 |
| --- | --- |
| [Metagenomics](https://en.wikipedia.org/wiki/Metagenomics) | 混合群落的遗传信息 |
| [Phylogenetics](https://en.wikipedia.org/wiki/Phylogenetics) | 共同祖先、树与演化关系 |
| [Population genetics](https://en.wikipedia.org/wiki/Population_genetics) | 等位频率、遗传变化与历史 |
| [Biodiversity](https://en.wikipedia.org/wiki/Biodiversity) | 多样性及其不同层次 |
| [Action potential](https://en.wikipedia.org/wiki/Action_potential) | 电活动及神经信号的基础 |
| [Systems biology](https://en.wikipedia.org/wiki/Systems_biology) | 组分相互作用与系统行为 |
| [Pharmacokinetics](https://en.wikipedia.org/wiki/Pharmacokinetics) | 暴露随时间的变化 |
| [Pharmacodynamics](https://en.wikipedia.org/wiki/Pharmacodynamics) | 暴露与作用之间的关系 |

方法原理分别连接[IQ-TREE](index.md#iqtree)、[HyPhy](index.md#hyphy)、[MetaPhlAn](index.md#metaphlan)、[vegan](index.md#vegan)、[Kilosort](index.md#kilosort)、[CaImAn](index.md#caiman)和[COPASI](index.md#copasi)。群体历史、神经活动与反应动力学不应套用同一套数据假设。

<a id="core-sources"></a>
## 基础定义、统计和计算的直接依据

| 来源 | 用途与适用范围 |
| --- | --- |
| [NHGRI Talking Glossary](https://www.genome.gov/genetics-glossary)；[Gene](https://www.genome.gov/genetics-glossary/Gene)、[Transcription](https://www.genome.gov/genetics-glossary/Transcription)、[Translation](https://www.genome.gov/genetics-glossary/Translation)、[Chromatin](https://www.genome.gov/genetics-glossary/Chromatin) | 基因及遗传过程的基础定义；不是完整方法教材 |
| Crick, 1970. [Central dogma of molecular biology](https://doi.org/10.1038/227561a0) | 中心法则的原始序列信息含义 |
| [HTSlib文档](https://www.htslib.org/doc/) | 序列比对、变异及相关文件的字段与坐标 |
| [NIST统计手册](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm)；[均值置信区间](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) | 假设检验、分布、区间与适用前提 |
| Benjamini & Hochberg, 1995. [Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) | FDR与多重检验的原始方法，需保留其假设 |
| [statsmodels GLM](https://www.statsmodels.org/stable/glm.html)、[混合模型](https://www.statsmodels.org/stable/mixed_linear.html)、[生存分析](https://www.statsmodels.org/stable/duration.html)、[多重检验](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) | 不同数据类型和模型族的实现说明 |
| Love et al., 2014. [DESeq2](https://doi.org/10.1186/s13059-014-0550-8)；[官方分析指南](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) | 计数建模、尺度估计、设计矩阵、效应与检验 |
| Crowell et al., 2020. [muscat](https://pmc.ncbi.nlm.nih.gov/articles/PMC7705760/) | 多样本单细胞差异状态、汇总和混合模型 |
| [scikit-learn常见陷阱](https://scikit-learn.org/stable/common_pitfalls.html)、[分解/PCA](https://scikit-learn.org/stable/modules/decomposition.html)、[聚类](https://scikit-learn.org/stable/modules/clustering.html) | 变换、模型验证、泄漏与计算任务的区分 |
| Subramanian et al., 2005. [Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles](https://www.broadinstitute.org/publications/broad3678) | 排序基因集合的富集，而不是直接测量通路活性；DOI 10.1073/pnas.0506580102 |
| [GROMACS分子动力学](https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html) | 在力场和积分规则下产生轨迹 |
| [COBRApy通量模拟](https://cobrapy.readthedocs.io/en/latest/simulating.html) | FBA与可行通量分析的约束和计算 |

<a id="assay-sources"></a>
## PCR与定量读出的直接依据

**Bustin et al., 2009，MIQE。** [The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments](https://pubmed.ncbi.nlm.nih.gov/19246619/)，DOI 10.1373/clinchem.2008.112797。用于理解样本、参考、效率、对照和定量解释为什么不可省略，不作为实验操作处方。

**Bustin et al., 2025，MIQE 2.0。** [MIQE 2.0: Revision of the Minimum Information for Publication of Quantitative Real-Time PCR Experiments Guidelines](https://pubmed.ncbi.nlm.nih.gov/40272429/)，DOI 10.1093/clinchem/hvaf043。作为已发表的更新版本补充效率、阈值、质量和可追溯分析信息；本页不声称对所有实验标准做了完整现行性审查。

**Huggett et al., 2020，dMIQE2020。** [The Digital MIQE Guidelines Update: Minimum Information for Publication of Quantitative Digital PCR Experiments for 2020](https://doi.org/10.1093/clinchem/hvaa125)。用于理解分区、阳性判断、分子分配模型和测量不确定性；数字PCR与qPCR的观测模型不同。

## 来源之间怎样分工

一个来源链接不自动支持某条目中的所有软件和子方法。正文中的直接链接定位具体依据；百科链接用于定义和概念关联；[Nature论文解析](nature-papers.md)说明研究中怎样组合技术。软件文档会更新，实际应用还应核对所用版本和数据条件。
