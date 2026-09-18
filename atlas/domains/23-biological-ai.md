# 23 生物AI与基础模型

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m175"></a>
## M175 蛋白语言模型与序列嵌入

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 构建表示、预测功能或变异影响 |
| 基本原理 | 以自监督任务学习蛋白序列统计规律 |
| 输入数据 / 上游实验 | 蛋白序列、预训练权重、可选少量标签 |
| 核心处理 | token化；embedding/概率；下游训练；同源分组验证 |
| 可以得到的结果 | 序列表征、候选变异分数、功能预测 |
| 常用术语 | PLM：蛋白语言模型；embedding：嵌入；zero-shot：零样本 |
| 代表工具 | ESM；ProtT5；其他蛋白基础模型 |
| 前提、QC与证据边界 | 语言概率≠生化适应度；同源泄漏及训练集记忆需检查 |
| 代表来源与延伸阅读 | [af3](../../references/index.md#af3) · [rfdiff](../../references/index.md#rfdiff) · [sklearn](../../references/index.md#sklearn) |


<a id="m176"></a>
## M176 DNA序列到分子表型预测

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 优先评价非编码变异与调控序列 |
| 基本原理 | 从DNA上下文联合预测多类调控读出 |
| 输入数据 / 上游实验 | DNA序列、ref/alt变异、组织/任务定义 |
| 核心处理 | 序列模型；反事实等位输入；轨道差异；外部功能验证 |
| 可以得到的结果 | 表达/剪接/开放/结合等预测及变异分数 |
| 常用术语 | sequence-to-function：序列到功能；in silico mutagenesis：虚拟突变 |
| 代表工具 | AlphaGenome；Enformer；Basenji类模型 |
| 前提、QC与证据边界 | 出版信息以原始来源为准；输出是预测，不是临床或机制确证 |
| 代表来源与延伸阅读 | [alphagenome](../../references/index.md#alphagenome) |


<a id="m177"></a>
## M177 基因组基础模型与序列生成

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 序列表征、变异评分和受约束研究设计 |
| 基本原理 | 跨大规模DNA序列学习上下文与长程模式 |
| 输入数据 / 上游实验 | DNA序列、模型上下文、评估任务与约束 |
| 核心处理 | 自监督预训练/使用预训练模型；变异比较；独立评价 |
| 可以得到的结果 | 嵌入、概率、候选序列和预测效应 |
| 常用术语 | genome model：基因组模型；context window：上下文窗口；generative：生成式 |
| 代表工具 | Evo 2；其他DNA基础模型 |
| 前提、QC与证据边界 | 出版信息以原始来源为准；自然相似序列不保证实际生物功能 |
| 代表来源与延伸阅读 | [evo2](../../references/index.md#evo2) · [sklearn](../../references/index.md#sklearn) |


<a id="m178"></a>
## M178 单细胞与空间基础模型

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 迁移注释、整合和候选响应预测 |
| 基本原理 | 在大图谱中学习细胞及其空间上下文表示 |
| 输入数据 / 上游实验 | 表达/空间图谱、预训练模型、目标数据 |
| 核心处理 | 数据对齐/token化；嵌入/微调；外部组织评估 |
| 可以得到的结果 | 细胞/生态位表示、标签或响应预测 |
| 常用术语 | cell embedding：细胞表示；tokenization：编码；fine-tuning：微调 |
| 代表工具 | scGPT；Geneformer；Nicheformer；其他模型 |
| 前提、QC与证据边界 | 未必胜过简单基线；基因集/物种/平台偏移与数据泄漏需评估 |
| 代表来源与延伸阅读 | [nicheformer](../../references/index.md#nicheformer) · [scvi](../../references/index.md#scvi) · [sklearn](../../references/index.md#sklearn) |


<a id="m179"></a>
## M179 图神经网络与多尺度几何学习

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 预测结构、互作、组织状态及分子性质 |
| 基本原理 | 沿分子键、空间邻接或生物网络传播特征 |
| 输入数据 / 上游实验 | 分子图/空间图/知识图谱、节点边特征 |
| 核心处理 | GNN/几何等变网络；负样本设计；图划分验证 |
| 可以得到的结果 | 节点/边/图级预测、几何或嵌入 |
| 常用术语 | GNN：图神经网络；equivariance：等变性；message passing：消息传递 |
| 代表工具 | PyTorch Geometric；DGL；几何深度模型 |
| 前提、QC与证据边界 | 构图和负样本选择可决定结果；随机拆边可能泄漏共享实体 |
| 代表来源与延伸阅读 | [rdkit](../../references/index.md#rdkit) · [af3](../../references/index.md#af3) · [sklearn](../../references/index.md#sklearn) |


<a id="m180"></a>
## M180 自监督图像、分割基础模型与多模态对齐

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 减少标注成本并连接病理、空间和分子表型 |
| 基本原理 | 从大量无标签图像或跨模态对应学习表示 |
| 输入数据 / 上游实验 | 显微/病理图像、空间组学、可选标注/配对 |
| 核心处理 | 自监督预训练；域适配；分割/检索/预测；独立测试 |
| 可以得到的结果 | 图像嵌入、对象掩膜、跨模态预测 |
| 常用术语 | SSL：自监督学习；contrastive：对比学习；foundation model：基础模型 |
| 代表工具 | 领域图像模型；Cellpose；SAM衍生模型；多模态网络 |
| 前提、QC与证据边界 | 自然图像能力不自动迁移生物显微；重建细节需防幻觉 |
| 代表来源与延伸阅读 | [cellpose](../../references/index.md#cellpose) · [nicheformer](../../references/index.md#nicheformer) · [sklearn](../../references/index.md#sklearn) |


<a id="m181"></a>
## M181 可解释性、消融与模型可信度

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 诊断模型捷径并形成可检验假设 |
| 基本原理 | 扰动输入或模型组件，评估哪些信息支撑预测 |
| 输入数据 / 上游实验 | 模型、训练/测试集、特征和负对照 |
| 核心处理 | saliency/SHAP；ablation；基线比较；校准和OOD测试 |
| 可以得到的结果 | 重要特征、性能贡献、失败模式、不确定性 |
| 常用术语 | ablation：消融；shortcut：捷径；attribution：归因；OOD：分布外 |
| 代表工具 | SHAP；Captum；scikit-learn；专用解释方法 |
| 前提、QC与证据边界 | 注意力/归因不等于因果机制；强相关特征可互相替代 |
| 代表来源与延伸阅读 | [sklearn](../../references/index.md#sklearn) · [alphagenome](../../references/index.md#alphagenome) |


<a id="m182"></a>
## M182 虚拟细胞与跨尺度预测评估

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 研究可泛化的细胞响应与模型辅助实验闭环 |
| 基本原理 | 将状态、扰动、环境和多模态观测纳入可预测模型 |
| 输入数据 / 上游实验 | 细胞图谱、扰动数据、时空/蛋白/表观等模态 |
| 核心处理 | 训练与机制约束；跨细胞/扰动/实验室留出；前瞻验证 |
| 可以得到的结果 | 有限任务范围内的响应预测、模型失效边界 |
| 常用术语 | virtual cell：虚拟细胞；out-of-distribution perturbation：未见扰动；prospective validation：前瞻验证 |
| 代表工具 | 扰动基础模型；生成模型；机制—学习混合框架 |
| 前提、QC与证据边界 | 不是已存在可替代所有实验的万能数字细胞；必须按任务验证 |
| 代表来源与延伸阅读 | [scperturb](../../references/index.md#scperturb) · [celloracle](../../references/index.md#celloracle) · [nicheformer](../../references/index.md#nicheformer) · [sklearn](../../references/index.md#sklearn) |
