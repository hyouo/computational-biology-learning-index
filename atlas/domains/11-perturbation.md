# 11 扰动筛选与功能基因组

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m083"></a>
## M083 CRISPR pooled筛选

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 筛选必需基因、药物响应或表型调控因子 |
| 基本原理 | 比较处理前后sgRNA丰度，估计靶基因对适应度/表型的影响 |
| 输入数据 / 上游实验 | sgRNA计数、文库设计、条件与生物重复 |
| 核心处理 | 文库覆盖QC；计数归一化；guide到gene聚合；统计 |
| 可以得到的结果 | 正/负选择基因、效应大小与FDR |
| 常用术语 | sgRNA：单导向RNA；dropout：筛选中耗竭；hit：候选命中 |
| 代表工具 | MAGeCK；BAGEL；drugZ |
| 前提、QC与证据边界 | guide效率、脱靶、CNV切割毒性影响命中；筛选命中需独立验证 |
| 代表来源与延伸阅读 | [mageck](../../references/index.md#mageck) · [addgene](../../references/index.md#addgene) |


<a id="m084"></a>
## M084 CRISPRi/a、碱基/先导编辑与编辑结局分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 区分基因剂量、区域功能及等位变异效应 |
| 基本原理 | 抑制/激活转录或定点改写序列，并定量编辑产物 |
| 输入数据 / 上游实验 | guide设计；扩增子reads；表型；对照 |
| 核心处理 | 编辑率/产物谱；guide有效性；表型与编辑状态联合 |
| 可以得到的结果 | 编辑效率、indel/碱基变化、功能候选 |
| 常用术语 | CRISPRi/a：抑制/激活；base/prime editing：碱基/先导编辑 |
| 代表工具 | CRISPResso2；BE-Analyzer；设计工具 |
| 前提、QC与证据边界 | 不同编辑技术不是等价KO；旁观编辑、脱靶和异质性需评价 |
| 代表来源与延伸阅读 | [addgene](../../references/index.md#addgene) · [sarek](../../references/index.md#sarek) |


<a id="m085"></a>
## M085 Perturb-seq / CROP-seq等单细胞扰动

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 识别多维效应、状态特异响应和机制分组 |
| 基本原理 | 同一细胞关联扰动身份与全转录组/多模态读出 |
| 输入数据 / 上游实验 | 单细胞counts、guide捕获、非靶向对照、重复 |
| 核心处理 | guide分配；效应细胞识别；协变量模型；差异与扰动嵌入 |
| 可以得到的结果 | 扰动—表达效应矩阵、表型簇、状态依赖效应 |
| 常用术语 | MOI：感染复数；guide assignment：导向分配；perturbation signature：扰动特征 |
| 代表工具 | scPerturb资源；Mixscape；SCEPTRE；定制模型 |
| 前提、QC与证据边界 | 分配了guide不等于成功扰动；每个条件需足够独立重复和细胞 |
| 代表来源与延伸阅读 | [scperturb](../../references/index.md#scperturb) · [addgene](../../references/index.md#addgene) |


<a id="m086"></a>
## M086 组合扰动与遗传互作

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 发现上位性、补偿及合成致死候选 |
| 基本原理 | 比较双/多扰动结果和预设无互作期望 |
| 输入数据 / 上游实验 | 单/双扰动及对照的适应度或多维表型 |
| 核心处理 | 定义加法/乘法零模型；互作残差；统计与复验 |
| 可以得到的结果 | 互作分数、上位关系候选、协同/拮抗图 |
| 常用术语 | epistasis：上位性；synthetic lethality：合成致死；synergy：协同 |
| 代表工具 | 双guide筛选模型；scPerturb数据；定制回归 |
| 前提、QC与证据边界 | 互作取决于读出尺度及零模型；药物协同不必等同遗传互作 |
| 代表来源与延伸阅读 | [scperturb](../../references/index.md#scperturb) · [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) |


<a id="m087"></a>
## M087 MPRA与饱和调控元件分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 量化非编码序列的调控活性与变异效应 |
| 基本原理 | 将大量候选序列条码化并比较报告RNA/DNA比 |
| 输入数据 / 上游实验 | 报告文库DNA/RNA条码counts；序列与细胞条件 |
| 核心处理 | 条码QC；DNA校正；重复建模；序列效应比较 |
| 可以得到的结果 | 序列活性、等位效应、调控语法候选 |
| 常用术语 | MPRA：大规模平行报告；STARR-seq：自转录报告测序 |
| 代表工具 | MPRAnalyze；MPRAsnakeflow；专用模型 |
| 前提、QC与证据边界 | 外源报告与内源染色质背景不同；片段长度和载体影响活性 |
| 代表来源与延伸阅读 | [alphagenome](../../references/index.md#alphagenome) · [addgene](../../references/index.md#addgene) |


<a id="m088"></a>
## M088 深度突变扫描DMS

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 绘制序列—功能关系与关键残基 |
| 基本原理 | 对大量序列变体施加选择并量化前后丰度 |
| 输入数据 / 上游实验 | 变体文库NGS；选择前后counts；可选多表型 |
| 核心处理 | 变体解析；错误校正；富集/适应度模型；重复一致性 |
| 可以得到的结果 | 变异效应图、容忍度、互作残基候选 |
| 常用术语 | DMS：深度突变扫描；fitness：适应度；enrichment：富集 |
| 代表工具 | dms_tools2；Enrich2；DiMSum |
| 前提、QC与证据边界 | 读出可能混合表达、折叠和结合；选择条件限定效应外推 |
| 代表来源与延伸阅读 | [rfdiff](../../references/index.md#rfdiff) · [af3](../../references/index.md#af3) · [sklearn](../../references/index.md#sklearn) |


<a id="m089"></a>
## M089 高内涵/光学池化筛选

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 用形态、定位和动力学筛选机制 |
| 基本原理 | 将成像表型与扰动ID或孔位相连 |
| 输入数据 / 上游实验 | 多通道图像、原位barcode或孔位、扰动表 |
| 核心处理 | 分割；barcode解码；表型提取；批次归一；hit分析 |
| 可以得到的结果 | 扰动—形态指纹、表型簇、细胞异质性 |
| 常用术语 | HCS：高内涵筛选；optical pooled screen：光学池化筛选 |
| 代表工具 | CellProfiler；Cellpose；pycytominer；定制解码 |
| 前提、QC与证据边界 | 批次和细胞密度可主导形态；高维相似不直接证明相同靶点 |
| 代表来源与延伸阅读 | [cellpose](../../references/index.md#cellpose) · [scperturb](../../references/index.md#scperturb) · [sklearn](../../references/index.md#sklearn) |
