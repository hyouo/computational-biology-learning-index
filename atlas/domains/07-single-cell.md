# 07 单细胞与细胞图谱

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m054"></a>
## M054 scRNA-seq / snRNA-seq原始定量

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 得到细胞/细胞核级RNA矩阵 |
| 基本原理 | 细胞条码分隔细胞，UMI近似计数被捕获分子 |
| 输入数据 / 上游实验 | 液滴、板式或组合索引FASTQ；条码规则；参考 |
| 核心处理 | 拆条码；比对；UMI去重；empty droplet处理 |
| 可以得到的结果 | 细胞×基因counts及细胞QC |
| 常用术语 | barcode：细胞条码；UMI：分子标签；snRNA：单核RNA |
| 代表工具 | Cell Ranger；STARsolo；kallisto-bustools；alevin-fry |
| 前提、QC与证据边界 | 捕获效率不完全；核/整细胞及3′/全长方案的偏倚不同 |
| 代表来源与延伸阅读 | [scanpy](../../references/index.md#scanpy) · [scvi](../../references/index.md#scvi) · [rnaseq](../../references/index.md#rnaseq) |


<a id="m055"></a>
## M055 单细胞QC、双细胞与环境RNA处理

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 防止假细胞类型和污染信号 |
| 基本原理 | 用复杂度、背景模型和混合表达识别技术异常 |
| 输入数据 / 上游实验 | raw/filtered矩阵、空液滴、基因注释、样本标签 |
| 核心处理 | nGenes/nUMI/线粒体分布；doublet与ambient估计；人工检查 |
| 可以得到的结果 | 保留细胞、双细胞评分、校正矩阵和QC报告 |
| 常用术语 | doublet：双细胞；ambient RNA：环境RNA；dropout：未检出 |
| 代表工具 | scDblFinder；Scrublet；SoupX；CellBender |
| 前提、QC与证据边界 | 不要使用跨组织固定阈值；真实过渡细胞可能被误判 |
| 代表来源与延伸阅读 | [scanpy](../../references/index.md#scanpy) · [scvi](../../references/index.md#scvi) |


<a id="m056"></a>
## M056 单细胞归一化、聚类与标记

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 发现细胞群及标记表达 |
| 基本原理 | 提取可解释的生物变异并在近邻图上分群 |
| 输入数据 / 上游实验 | counts与细胞/样本元数据 |
| 核心处理 | 归一化；HVG；PCA；neighbors；Leiden；markers |
| 可以得到的结果 | 细胞簇、表达图谱、标记表 |
| 常用术语 | HVG：高变基因；resolution：聚类分辨参数；marker：标记 |
| 代表工具 | Scanpy；Seurat；SCTransform |
| 前提、QC与证据边界 | 簇数由参数和数据共同决定；marker不是绝对专一身份 |
| 代表来源与延伸阅读 | [scanpy](../../references/index.md#scanpy) · [wnn](../../references/index.md#wnn) |


<a id="m057"></a>
## M057 批次整合与参考映射

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 联合不同样本、平台和图谱 |
| 基本原理 | 对齐共享生物结构，同时尽量保留条件特异变化 |
| 输入数据 / 上游实验 | 多个表达/特征矩阵、批次标签、参考标注 |
| 核心处理 | anchors/MNN/潜变量；映射；生物与批次指标验证 |
| 可以得到的结果 | 整合嵌入、参考坐标、标签及置信度 |
| 常用术语 | integration：整合；label transfer：标签迁移；overcorrection：过度校正 |
| 代表工具 | Harmony；Seurat；scVI/scANVI；Scanorama |
| 前提、QC与证据边界 | 不能为了混匀消除真实疾病/物种差异；差异分析需适当原始计数模型 |
| 代表来源与延伸阅读 | [scvi](../../references/index.md#scvi) · [scanpy](../../references/index.md#scanpy) |


<a id="m058"></a>
## M058 细胞类型注释与状态识别

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 区分细胞身份、激活/应激状态与异常群 |
| 基本原理 | 结合标记、参考分类和领域知识解释簇 |
| 输入数据 / 上游实验 | 表达矩阵、参考图谱、marker知识 |
| 核心处理 | 多标记交叉验证；参考映射；稀有/未知标签检查 |
| 可以得到的结果 | 细胞注释、状态分数、不确定或新群体候选 |
| 常用术语 | cell type：类型；cell state：状态；ontology：本体 |
| 代表工具 | CellTypist；SingleR；Azimuth；手工验证 |
| 前提、QC与证据边界 | 参考缺失的新状态不应强行分到已有类；表达相似不等于同来源 |
| 代表来源与延伸阅读 | [scanpy](../../references/index.md#scanpy) · [scvi](../../references/index.md#scvi) |


<a id="m059"></a>
## M059 单细胞差异状态与差异丰度

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 避免把组成改变混成细胞内变化 |
| 基本原理 | 分别检验同类型细胞的表达变化及群体比例变化 |
| 输入数据 / 上游实验 | 多生物重复单细胞数据、个体及条件标签 |
| 核心处理 | 按个体×类型pseudobulk；混合模型；邻域/组成丰度模型 |
| 可以得到的结果 | 类型特异差异基因、状态变化、丰度差异 |
| 常用术语 | pseudobulk：伪汇总；DS：差异状态；DA：差异丰度 |
| 代表工具 | muscat；DESeq2；Milo；scCODA |
| 前提、QC与证据边界 | 独立样本通常是个体；相对比例增加可能仅由另一类型减少 |
| 代表来源与延伸阅读 | [muscat](../../references/index.md#muscat) · [deseq](../../references/index.md#deseq) |


<a id="m060"></a>
## M060 scATAC-seq与单细胞表观图谱

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位细胞特异调控元件和状态 |
| 基本原理 | 以条码记录每个细胞开放片段或表观信号 |
| 输入数据 / 上游实验 | fragments、peak×cell矩阵；可选scCUT&Tag/sc甲基化 |
| 核心处理 | TSS/FRiP QC；TF-IDF/LSI；聚类；motif；链接RNA |
| 可以得到的结果 | 表观细胞群、差异开放区域、候选调控因子 |
| 常用术语 | LSI：潜在语义索引；gene activity：基因活性代理分数 |
| 代表工具 | Signac；ArchR；SnapATAC2；chromVAR |
| 前提、QC与证据边界 | gene activity不等于测得RNA；稀疏性会限制单细胞单峰判断 |
| 代表来源与延伸阅读 | [wnn](../../references/index.md#wnn) · [cuttag](../../references/index.md#cuttag) · [scenic](../../references/index.md#scenic) |


<a id="m061"></a>
## M061 CITE-seq、Multiome与其他共测量

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 降低跨样本对齐歧义并连接分子层次 |
| 基本原理 | 在同一细胞联合记录RNA、抗体标签、ATAC等模态 |
| 输入数据 / 上游实验 | 配对RNA+ADT、RNA+ATAC等counts及条码 |
| 核心处理 | 各模态QC；背景处理；WNN/totalVI/MultiVI整合 |
| 可以得到的结果 | 联合嵌入、细胞身份、跨模态关系 |
| 常用术语 | ADT：抗体衍生标签；multiome：多组共测；WNN：加权近邻 |
| 代表工具 | Seurat WNN；totalVI；MultiVI；muon |
| 前提、QC与证据边界 | 同细胞共测不等于无技术噪声；抗体标签一般仅覆盖预设panel |
| 代表来源与延伸阅读 | [wnn](../../references/index.md#wnn) · [scvi](../../references/index.md#scvi) |


<a id="m062"></a>
## M062 单细胞DNA、CNV与克隆图谱

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究嵌合、肿瘤异质性与克隆演化 |
| 基本原理 | 按细胞基因型或拷贝数差异推断遗传亚群 |
| 输入数据 / 上游实验 | scDNA测序；可选scRNA及bulk DNA |
| 核心处理 | 扩增偏倚QC；CNV/SNV calling；克隆聚类 |
| 可以得到的结果 | 细胞遗传克隆、CNV谱、候选进化关系 |
| 常用术语 | ADO：等位基因脱落；clone：克隆；ploidy：倍性 |
| 代表工具 | 专用scDNA流程；inferCNV；CopyKAT |
| 前提、QC与证据边界 | RNA推断CNV不是DNA测量；正常激活状态可能造成假阳性 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [muscat](../../references/index.md#muscat) |
