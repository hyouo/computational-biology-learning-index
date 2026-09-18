# 12 免疫组库与肿瘤演化

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m090"></a>
## M090 TCR/BCR组库重建与克隆分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究免疫克隆扩增、共享及多样性 |
| 基本原理 | 重建V(D)J重排受体序列并定义克隆 |
| 输入数据 / 上游实验 | bulk或单细胞V(D)J reads；可配对scRNA |
| 核心处理 | V/D/J注释；CDR3提取；链配对；克隆和多样性统计 |
| 可以得到的结果 | 受体序列、clonotype、扩增及细胞状态关系 |
| 常用术语 | CDR3：互补决定区3；clonotype：克隆型；V(D)J：可变重排片段 |
| 代表工具 | MiXCR；IgBLAST；Scirpy；immunarch |
| 前提、QC与证据边界 | 序列相似不必然识别同抗原；克隆定义和取样深度影响多样性 |
| 代表来源与延伸阅读 | [scirpy](../../references/index.md#scirpy) |


<a id="m091"></a>
## M091 BCR体细胞高突变与抗体谱系

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究抗体成熟、克隆分化和类别转换 |
| 基本原理 | 把受体序列相对胚系变化组织为进化关系 |
| 输入数据 / 上游实验 | BCR序列、胚系参考、同种型及样本时间 |
| 核心处理 | SHM注释；克隆聚类；谱系树；选择分析 |
| 可以得到的结果 | 抗体谱系、突变负荷、同种型组成 |
| 常用术语 | SHM：体细胞高突变；CSR：类别转换；germline：胚系参考 |
| 代表工具 | Immcantation；Change-O；IgPhyML |
| 前提、QC与证据边界 | 胚系等位基因缺失会假增突变；抗体序列树不等于完整细胞历史 |
| 代表来源与延伸阅读 | [immcant](../../references/index.md#immcant) · [hyphy](../../references/index.md#hyphy) |


<a id="m092"></a>
## M092 HLA分型与抗原呈递预测

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 筛选抗原呈递或肿瘤新抗原候选 |
| 基本原理 | 从reads推断HLA等位基因，再预测肽—MHC相容性 |
| 输入数据 / 上游实验 | DNA/RNA reads、HLA型、变异及肽序列 |
| 核心处理 | HLA typing；变异转肽；结合/呈递预测；表达过滤 |
| 可以得到的结果 | HLA型、候选呈递肽、新抗原排序 |
| 常用术语 | HLA/MHC：主要组织相容性复合体；neoantigen：新抗原 |
| 代表工具 | OptiType；arcasHLA；NetMHCpan；MHCflurry；pVACtools |
| 前提、QC与证据边界 | 预测结合≠天然呈递≠T细胞免疫原性；需质谱和功能验证 |
| 代表来源与延伸阅读 | [scirpy](../../references/index.md#scirpy) · [af3](../../references/index.md#af3) · [sarek](../../references/index.md#sarek) |


<a id="m093"></a>
## M093 肿瘤纯度、倍性与亚克隆重建

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 解释肿瘤异质性和进化次序 |
| 基本原理 | 联合等位基因比例、拷贝数和突变共变推断细胞组成 |
| 输入数据 / 上游实验 | 肿瘤正常DNA、CNV/SNV、可选多区域/多时点 |
| 核心处理 | 纯度倍性拟合；CCF校正；克隆聚类；树约束 |
| 可以得到的结果 | 纯度、倍性、克隆比例、候选演化树 |
| 常用术语 | CCF：癌细胞比例；subclone：亚克隆；LOH：杂合性丢失 |
| 代表工具 | ASCAT；FACETS；PyClone；PhyloWGS |
| 前提、QC与证据边界 | 多个树可同样解释数据；纯度和CNV误差会传给克隆结果 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [stats](../../references/index.md#stats) |


<a id="m094"></a>
## M094 突变特征与突变过程分解

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 提出DNA损伤、修复缺陷或暴露相关过程 |
| 基本原理 | 按碱基上下文/变异类型分解突变谱 |
| 输入数据 / 上游实验 | 体细胞变异及上下文；足够突变数 |
| 核心处理 | SBS/DBS/Indel谱；NMF或参考拟合；稳定性评估 |
| 可以得到的结果 | signature暴露量、过程候选及置信度 |
| 常用术语 | SBS：单碱基替换谱；signature：特征；exposure：特征贡献 |
| 代表工具 | SigProfiler；MutationalPatterns |
| 前提、QC与证据边界 | 相似特征可混淆；低突变数不稳；特征关联不等于锁定单一病因 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [mofa](../../references/index.md#mofa) |


<a id="m095"></a>
## M095 液体活检与cfDNA片段组学

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究组织来源、肿瘤负荷及动态监测 |
| 基本原理 | 利用循环DNA突变、甲基化或片段模式识别来源信号 |
| 输入数据 / 上游实验 | cfDNA测序、片段端点/长度、甲基化、对照队列 |
| 核心处理 | 错误抑制；片段统计；来源/分类模型；独立验证 |
| 可以得到的结果 | ctDNA候选信号、来源概率、动态指标 |
| 常用术语 | cfDNA：游离DNA；ctDNA：肿瘤来源DNA；fragmentomics：片段组学 |
| 代表工具 | UMI共识流程；专用片段/甲基化模型 |
| 前提、QC与证据边界 | 造血克隆、前处理与低肿瘤比例可干扰；研究分类器非临床确诊 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [hts](../../references/index.md#hts) · [sklearn](../../references/index.md#sklearn) |
