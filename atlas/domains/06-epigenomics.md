# 06 表观组与三维基因组

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m046"></a>
## M046 ATAC-seq与DNase-seq

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位候选开放调控区域 |
| 基本原理 | 转座酶插入或核酸酶切割偏好暴露DNA |
| 输入数据 / 上游实验 | ATAC/DNase FASTQ；参考；生物重复 |
| 核心处理 | 比对；线粒体与黑名单检查；TSS/FRiP QC；peak calling |
| 可以得到的结果 | 开放区域、可及性轨道、差异peak |
| 常用术语 | TSS enrichment：起始位点富集；FRiP：峰内读段比例；peak：富集区 |
| 代表工具 | MACS；Genrich；nf-core/atacseq |
| 前提、QC与证据边界 | 开放不等于增强子活跃；Tn5偏好、细胞混合和深度影响信号 |
| 代表来源与延伸阅读 | [atac](../../references/index.md#atac) · [atacpaper](../../references/index.md#atacpaper) |


<a id="m047"></a>
## M047 ChIP-seq、CUT&RUN与CUT&Tag

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 描绘结合或染色质修饰分布 |
| 基本原理 | 抗体靶向蛋白/组蛋白标记，再富集或原位切割/转座附近DNA |
| 输入数据 / 上游实验 | 测序reads；input/IgG等适配对照；可选spike-in |
| 核心处理 | 目标特异QC；窄/宽峰；重复一致性；差异结合 |
| 可以得到的结果 | 结合峰、宽修饰域、轨道及变化 |
| 常用术语 | input：背景输入；IgG：抗体对照；spike-in：外源校准 |
| 代表工具 | MACS；SEACR；DiffBind；nf-core/chipseq |
| 前提、QC与证据边界 | 三类实验背景机制不同；抗体质量关键；不能一套参数套所有标记 |
| 代表来源与延伸阅读 | [chip](../../references/index.md#chip) · [cuttag](../../references/index.md#cuttag) |


<a id="m048"></a>
## M048 DNA甲基化与羟甲基化

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位表观状态与差异甲基化区域 |
| 基本原理 | 用化学/酶转化或直接测序信号区分修饰碱基 |
| 输入数据 / 上游实验 | WGBS/RRBS/EM-seq或ONT/PacBio信号；覆盖及对照 |
| 核心处理 | 转化/信号模型；位点比例；DMR统计；细胞组成处理 |
| 可以得到的结果 | CpG甲基化比例、DMR、修饰分布 |
| 常用术语 | β值：甲基化比例；DMR：差异甲基化区；5mC/5hmC：修饰类型 |
| 代表工具 | Bismark；DSS；methylKit；modkit |
| 前提、QC与证据边界 | 普通亚硫酸氢盐法通常不能区分5mC/5hmC；低覆盖比例不稳 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [hts](../../references/index.md#hts) · [alphagenome](../../references/index.md#alphagenome) |


<a id="m049"></a>
## M049 基序富集、TF足迹与偏差评分

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 寻找开放/结合区域的调控因子 |
| 基本原理 | 序列概率模型与切割模式推断候选TF调控 |
| 输入数据 / 上游实验 | DNA peak序列；motif库；ATAC/DNase切割或单细胞counts |
| 核心处理 | motif扫描/富集；GC背景；酶偏好校正；footprint/chromVAR |
| 可以得到的结果 | 候选TF、基序分数、足迹和细胞级偏差 |
| 常用术语 | PWM：位置权重矩阵；footprint：足迹；motif：基序 |
| 代表工具 | MEME/FIMO；HOMER；TOBIAS；chromVAR |
| 前提、QC与证据边界 | 同家族TF常共享motif；有motif不等于真实结合 |
| 代表来源与延伸阅读 | [meme](../../references/index.md#meme) · [wnn](../../references/index.md#wnn) · [atacpaper](../../references/index.md#atacpaper) |


<a id="m050"></a>
## M050 染色质状态分段

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 归纳启动子、增强子、抑制域等候选状态 |
| 基本原理 | 联合多个组蛋白/开放标记学习基因组状态 |
| 输入数据 / 上游实验 | 多种ChIP/ATAC信号轨道与基因组bin |
| 核心处理 | 二值化/连续建模；HMM；状态注释 |
| 可以得到的结果 | 染色质状态分段、跨条件转换 |
| 常用术语 | HMM：隐马尔可夫；chromatin state：染色质状态 |
| 代表工具 | ChromHMM；Segway |
| 前提、QC与证据边界 | 状态名称来自标记组合解释；不能代替功能扰动验证 |
| 代表来源与延伸阅读 | [chip](../../references/index.md#chip) · [cuttag](../../references/index.md#cuttag) · [stats](../../references/index.md#stats) |


<a id="m051"></a>
## M051 Hi-C、Micro-C与靶向染色质接触

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究区室、边界、环和调控接触 |
| 基本原理 | 交联、连接和配对测序记录空间近邻DNA接触 |
| 输入数据 / 上游实验 | 成对reads；参考；酶切/核小体方案；可选捕获靶点 |
| 核心处理 | 有效pairs；距离衰减和偏倚QC；矩阵平衡；结构检测 |
| 可以得到的结果 | 接触矩阵、A/B区室、TAD/边界、loops |
| 常用术语 | TAD：拓扑关联域；loop：环；O/E：观测/期望接触 |
| 代表工具 | HiC-Pro；Juicer；cooler/cooltools；HiCExplorer |
| 前提、QC与证据边界 | 接触频率不是欧氏距离；分辨率依赖深度；接触不等于调控 |
| 代表来源与延伸阅读 | [pangenome](../../references/index.md#pangenome) · [alphagenome](../../references/index.md#alphagenome) |


<a id="m052"></a>
## M052 增强子—靶基因链接

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 将非编码区域指向可能受调控基因 |
| 基本原理 | 联合距离、接触、活性与表达共变给候选链接打分 |
| 输入数据 / 上游实验 | ATAC/ChIP、Hi-C/HiChIP、RNA、可选CRISPR扰动 |
| 核心处理 | 相关/ABC类模型；跨模态网络；独立扰动验证 |
| 可以得到的结果 | 增强子—基因候选边、分数与证据 |
| 常用术语 | ABC：活性×接触模型；co-accessibility：共可及性 |
| 代表工具 | ABC；Cicero；SCENIC+；Signac |
| 前提、QC与证据边界 | 最近基因不一定靶基因；相关或接触只能产生候选联系 |
| 代表来源与延伸阅读 | [scenic](../../references/index.md#scenic) · [wnn](../../references/index.md#wnn) · [alphagenome](../../references/index.md#alphagenome) |


<a id="m053"></a>
## M053 DNA复制、损伤与染色体分离读出

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究复制起始/时序、损伤分布及稳定性 |
| 基本原理 | 结合复制时间、断裂端、标记或单分子轨迹分析DNA过程 |
| 输入数据 / 上游实验 | Repli-seq、END/BLISS类reads；DNA fiber图像 |
| 核心处理 | 特征定位；时序分箱；断裂富集；轨迹长度/速度统计 |
| 可以得到的结果 | 复制时序图、损伤热点、复制叉速度估计 |
| 常用术语 | replication timing：复制时序；DSB：双链断裂；fork：复制叉 |
| 代表工具 | 专用测序流程；图像分析；统计建模 |
| 前提、QC与证据边界 | 信号受细胞周期分布、捕获和修复阶段影响；不同读出不能直接替代 |
| 代表来源与延伸阅读 | [hts](../../references/index.md#hts) · [cellpose](../../references/index.md#cellpose) · [stats](../../references/index.md#stats) |
