# 10 多组学、网络与系统整合

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m077"></a>
## M077 多组学因子分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 解释跨层次差异并发现亚型 |
| 基本原理 | 将不同模态分解为共享/特有的低维变异因子 |
| 输入数据 / 上游实验 | 同一或重叠样本的RNA/蛋白/甲基化等矩阵 |
| 核心处理 | 模态标准化；因子模型；方差解释；因子关联 |
| 可以得到的结果 | 样本因子、特征负载、跨模态解释比例 |
| 常用术语 | latent factor：潜因子；loading：负载；variance explained：解释方差 |
| 代表工具 | MOFA+；MEFISTO；NMF/CCA |
| 前提、QC与证据边界 | 高方差因子可能是批次；相关因子不自动代表因果通路 |
| 代表来源与延伸阅读 | [mofa](../../references/index.md#mofa) |


<a id="m078"></a>
## M078 配对与非配对多模态整合

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 连接无法完全共同测量的数据 |
| 基本原理 | 通过共同细胞、共同特征或先验图对齐模态 |
| 输入数据 / 上游实验 | 配对/部分配对/非配对RNA、ATAC、蛋白矩阵 |
| 核心处理 | WNN、CCA、生成模型或图对齐；配对一致性评估 |
| 可以得到的结果 | 联合表征、跨模态映射或预测 |
| 常用术语 | CCA：典型相关；WNN：加权近邻；alignment：对齐 |
| 代表工具 | Seurat；totalVI/MultiVI；GLUE；muon |
| 前提、QC与证据边界 | 非配对对齐可能存在多个同样合理解；补全不是新测量 |
| 代表来源与延伸阅读 | [wnn](../../references/index.md#wnn) · [scvi](../../references/index.md#scvi) · [mofa](../../references/index.md#mofa) |


<a id="m079"></a>
## M079 共表达网络与模块分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 找共同程序、候选枢纽和表型相关模块 |
| 基本原理 | 根据协同变化构建基因模块和代表性分数 |
| 输入数据 / 上游实验 | 多样本表达/蛋白矩阵；协变量 |
| 核心处理 | 相关/稳健相关；网络；模块；eigengene关联 |
| 可以得到的结果 | 模块、枢纽候选、模块—表型关系 |
| 常用术语 | module：模块；hub：枢纽；eigengene：模块代表分量 |
| 代表工具 | WGCNA；MEGENA；igraph |
| 前提、QC与证据边界 | 共表达可能由细胞比例/批次驱动；hub不等于因果主调控者 |
| 代表来源与延伸阅读 | [mofa](../../references/index.md#mofa) · [scenic](../../references/index.md#scenic) |


<a id="m080"></a>
## M080 基因调控网络GRN推断

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 提出细胞状态调控机制候选 |
| 基本原理 | 联合表达依赖、motif与开放区域推断TF靶基因 |
| 输入数据 / 上游实验 | RNA；可选ATAC/motif/扰动数据 |
| 核心处理 | 共表达/树模型；motif约束；增强子链接；regulon打分 |
| 可以得到的结果 | TF—靶基因或TF—增强子—基因网络 |
| 常用术语 | GRN：调控网络；regulon：调控子集合；eRegulon：含增强子的调控单元 |
| 代表工具 | SCENIC；SCENIC+；GENIE3；CellOracle |
| 前提、QC与证据边界 | 网络边常是统计/先验推断；方向和直接性需干预验证 |
| 代表来源与延伸阅读 | [scenic](../../references/index.md#scenic) · [celloracle](../../references/index.md#celloracle) |


<a id="m081"></a>
## M081 虚拟扰动与反事实预测

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 优先排序候选扰动和组合 |
| 基本原理 | 在学习到的网络/潜空间内修改目标变量并预测响应 |
| 输入数据 / 上游实验 | 表达及调控网络；或已有扰动训练数据 |
| 核心处理 | 定义干预；预测状态/表达位移；外部扰动测试 |
| 可以得到的结果 | 候选扰动效应、状态转移和不确定性 |
| 常用术语 | in silico perturbation：虚拟扰动；counterfactual：反事实 |
| 代表工具 | CellOracle；scGen；CPA；GEARS |
| 前提、QC与证据边界 | 模型干预不等于真实CRISPR干预；未见细胞类型/组合可能失效 |
| 代表来源与延伸阅读 | [celloracle](../../references/index.md#celloracle) · [scperturb](../../references/index.md#scperturb) · [sklearn](../../references/index.md#sklearn) |


<a id="m082"></a>
## M082 知识图谱与证据整合

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 检索关系、靶点优先级与可解释假设 |
| 基本原理 | 以实体和关系整合基因、疾病、化合物、通路和文献证据 |
| 输入数据 / 上游实验 | 标准化实体ID、数据库关系、原始证据和出处 |
| 核心处理 | 实体消歧；关系类型；证据加权；图查询/学习 |
| 可以得到的结果 | 证据网络、候选关系、可追溯优先级 |
| 常用术语 | knowledge graph：知识图谱；ontology：本体；evidence provenance：证据来源 |
| 代表工具 | Neo4j；RDF/SPARQL；Open Targets类资源 |
| 前提、QC与证据边界 | 重复引用同一研究不算独立证据；文献热度会偏置排序 |
| 代表来源与延伸阅读 | [scenic](../../references/index.md#scenic) · [gsea](../../references/index.md#gsea) · [rdkit](../../references/index.md#rdkit) |
