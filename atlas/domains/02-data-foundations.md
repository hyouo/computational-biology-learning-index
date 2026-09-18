# 02 数据工程与共用分析

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m011"></a>
## M011 可复现工作流与计算环境

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 让分析可重跑、可审计、可移植 |
| 基本原理 | 把依赖和数据转换写为有向任务图并固定环境 |
| 输入数据 / 上游实验 | 原始数据、样本表、参数、软件与参考版本 |
| 核心处理 | Git；环境锁定；容器；流程调度；日志和校验和 |
| 可以得到的结果 | 可复现pipeline、运行报告、版本与数据谱系 |
| 常用术语 | DAG：任务图；container：容器；provenance：数据来源链 |
| 代表工具 | Nextflow；Snakemake；nf-core；Docker/Apptainer |
| 前提、QC与证据边界 | 能重跑不等于生物学设计正确；参考基因组版本也是依赖 |
| 代表来源与延伸阅读 | [nf](../../references/index.md#nf) |


<a id="m012"></a>
## M012 测序拆样与碱基质量控制

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 从仪器输出得到可信reads |
| 基本原理 | 根据信号/索引生成序列并诊断错误、接头和污染 |
| 输入数据 / 上游实验 | BCL/POD5等仪器数据或FASTQ；sample sheet |
| 核心处理 | basecalling/demultiplexing；接头处理；FastQC/MultiQC |
| 可以得到的结果 | FASTQ、质量报告、样本与条码对应关系 |
| 常用术语 | Phred：碱基错误概率质量；index hopping：索引跳跃 |
| 代表工具 | 厂商basecaller；fastp；Cutadapt；FastQC；MultiQC |
| 前提、QC与证据边界 | 过滤阈值取决于平台与实验；不要对所有文库机械去重复 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [nf](../../references/index.md#nf) · [hts](../../references/index.md#hts) |


<a id="m013"></a>
## M013 序列比对、定量与坐标处理

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 获得读段来源及信号强度 |
| 基本原理 | 将reads匹配参考序列，或对转录本候选分配概率 |
| 输入数据 / 上游实验 | FASTQ、参考FASTA、GTF/GFF和索引 |
| 核心处理 | 比对；排序索引；多重比对处理；特征计数 |
| 可以得到的结果 | BAM/CRAM、counts、coverage轨道 |
| 常用术语 | MAPQ：比对置信度；CIGAR：比对结构；multi-mapping：多重比对 |
| 代表工具 | STAR；BWA-MEM2；minimap2；Salmon；featureCounts |
| 前提、QC与证据边界 | 基因ID、链方向、0/1-based坐标错误可毁掉后续结论 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [sarek](../../references/index.md#sarek) · [hts](../../references/index.md#hts) |


<a id="m014"></a>
## M014 UMI纠错与分子去重复

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 降低PCR重复计数及低频错误 |
| 基本原理 | 用随机分子标签区分扩增副本和独立分子 |
| 输入数据 / 上游实验 | reads、UMI序列、比对位置或细胞条码 |
| 核心处理 | 标签纠错；聚类；分子共识；必要时双链共识 |
| 可以得到的结果 | 分子计数、共识reads、纠错变异 |
| 常用术语 | UMI：唯一分子标识；duplex：双链共识 |
| 代表工具 | UMI-tools；fgbio；平台分析软件 |
| 前提、QC与证据边界 | 同坐标reads未必是PCR重复；UMI碰撞和纠错过度需检查 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [sarek](../../references/index.md#sarek) |


<a id="m015"></a>
## M015 样本身份、污染与批次诊断

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 发现样本混淆、污染、离群和批次 |
| 基本原理 | 利用性别、基因型、标记及整体信号检测不一致 |
| 输入数据 / 上游实验 | 元数据、测序QC、基因型或表达矩阵 |
| 核心处理 | 相关性/PCA；指纹比较；污染估计；追溯样本表 |
| 可以得到的结果 | 异常样本清单、QC依据、协变量建议 |
| 常用术语 | sample swap：样本交换；batch：批次；outlier：离群 |
| 代表工具 | MultiQC；VerifyBamID；PCA；领域QC工具 |
| 前提、QC与证据边界 | 不能仅因与假设不符而删除样本；批次与组别完全重合无法辨别 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [rnaseq](../../references/index.md#rnaseq) · [deseq](../../references/index.md#deseq) |


<a id="m016"></a>
## M016 PCA、聚类与非线性可视化

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 探索异质性、离群与候选群体 |
| 基本原理 | 压缩特征或按相似性发现结构 |
| 输入数据 / 上游实验 | 经过合理预处理的样本×特征矩阵 |
| 核心处理 | PCA/NMF；距离/邻居图；聚类；UMAP/t-SNE |
| 可以得到的结果 | 主成分、簇标签、低维图及负载 |
| 常用术语 | PC：主成分；KNN：近邻；Leiden：图聚类 |
| 代表工具 | Scanpy；Seurat；scikit-learn |
| 前提、QC与证据边界 | UMAP间距、岛大小和朝向不直接对应生物距离、数量或发育时间 |
| 代表来源与延伸阅读 | [scanpy](../../references/index.md#scanpy) · [sklearn](../../references/index.md#sklearn) · [cellrank](../../references/index.md#cellrank) |


<a id="m017"></a>
## M017 功能富集与基因集打分

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 从长基因表归纳过程与功能假设 |
| 基本原理 | 检验候选/排序中基因集偏聚，或汇总集合信号 |
| 输入数据 / 上游实验 | 基因列表或全基因排序；基因集；背景集 |
| 核心处理 | ORA或GSEA；多重校正；单样本打分；检查重叠基因 |
| 可以得到的结果 | 富集条目、NES、leading edge、样本分数 |
| 常用术语 | GO：本体；ORA：过度代表；NES：标准化富集分数 |
| 代表工具 | clusterProfiler；fgsea；GSEA；GSVA；AUCell |
| 前提、QC与证据边界 | 背景、基因集版本与方向影响结果；富集≠直接测得通路活性 |
| 代表来源与延伸阅读 | [gsea](../../references/index.md#gsea) · [scenic](../../references/index.md#scenic) |


<a id="m018"></a>
## M018 分类、回归与模型评估

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 预测表型、响应、类别或数值 |
| 基本原理 | 从训练样本学习特征到标签的映射 |
| 输入数据 / 上游实验 | 特征矩阵、标签、个体/时间/同源分组 |
| 核心处理 | 嵌套交叉验证；管道内预处理；调参；独立验证 |
| 可以得到的结果 | 预测值、校准、AUROC/AUPRC或误差、置信度 |
| 常用术语 | CV：交叉验证；leakage：泄漏；calibration：校准 |
| 代表工具 | scikit-learn；XGBoost；PyTorch |
| 前提、QC与证据边界 | 按患者/同源家族等分割；AUC高不能证明机制或跨域可靠 |
| 代表来源与延伸阅读 | [sklearn](../../references/index.md#sklearn) |
