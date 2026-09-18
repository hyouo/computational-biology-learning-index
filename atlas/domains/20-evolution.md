# 20 进化、比较与古基因组

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m151"></a>
## M151 多序列比对与同源推断

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 为功能、结构和系统发育提供同源框架 |
| 基本原理 | 对齐可比较的进化位置并区分复制/物种分化关系 |
| 输入数据 / 上游实验 | DNA/RNA/蛋白序列、质量和物种信息 |
| 核心处理 | 同源搜索；MSA；修剪；orthogroup定义 |
| 可以得到的结果 | 比对、同源群、保守位点 |
| 常用术语 | homolog：同源；ortholog：直系同源；paralog：旁系同源 |
| 代表工具 | BLAST；MMseqs2；MAFFT；MUSCLE；OrthoFinder |
| 前提、QC与证据边界 | 相似不是同源的完整证明；错误对齐会传递到选择与树分析 |
| 代表来源与延伸阅读 | [iqtree](../../references/index.md#iqtree) · [hyphy](../../references/index.md#hyphy) · [af3](../../references/index.md#af3) |


<a id="m152"></a>
## M152 系统发育树与物种树

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 重建亲缘、基因历史及种间关系 |
| 基本原理 | 在序列演化模型下推断共同祖先关系 |
| 输入数据 / 上游实验 | 多序列比对、多个基因、外群/时间信息 |
| 核心处理 | 替换模型；ML/Bayes树；支持度；多基因物种树 |
| 可以得到的结果 | 树拓扑、枝长、节点支持度 |
| 常用术语 | bootstrap：自举支持；ILS：不完全谱系分选；gene/species tree：基因/物种树 |
| 代表工具 | IQ-TREE；RAxML-NG；MrBayes；ASTRAL；BEAST |
| 前提、QC与证据边界 | 基因树可因ILS/杂交/水平转移不同于物种树；支持度不是树必真概率 |
| 代表来源与延伸阅读 | [iqtree](../../references/index.md#iqtree) · [tskit](../../references/index.md#tskit) |


<a id="m153"></a>
## M153 正选择、约束与适应性分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位选择作用的分支、位点或区域 |
| 基本原理 | 比较替换率或多态性模式与中性模型 |
| 输入数据 / 上游实验 | 高质量密码子比对、树、群体变异 |
| 核心处理 | dN/dS模型；分支/位点检验；多重校正；稳健性 |
| 可以得到的结果 | 选择/约束候选位点、分支或区域 |
| 常用术语 | dN/dS：非同义/同义替换率比；purifying selection：纯化选择 |
| 代表工具 | HyPhy；PAML；选择扫描工具 |
| 前提、QC与证据边界 | dN/dS高不自动证明特定适应性功能；对齐、重组和模型偏差要排查 |
| 代表来源与延伸阅读 | [hyphy](../../references/index.md#hyphy) · [iqtree](../../references/index.md#iqtree) |


<a id="m154"></a>
## M154 比较基因组、共线性与基因家族演化

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究复制、丢失、重排及物种特异变化 |
| 基本原理 | 跨物种比较基因顺序、同源和拷贝数 |
| 输入数据 / 上游实验 | 多个基因组、注释、同源群、物种树 |
| 核心处理 | 全基因组/共线性比对；家族大小模型；祖先重建 |
| 可以得到的结果 | 共线区、复制/丢失、家族扩张候选 |
| 常用术语 | synteny：共线性；WGD：全基因组复制；gene family：基因家族 |
| 代表工具 | MCScanX；OrthoFinder；CAFE；全基因组比对工具 |
| 前提、QC与证据边界 | 注释不一致可伪装家族扩张；基因拷贝数不直接说明功能增强 |
| 代表来源与延伸阅读 | [pangenome](../../references/index.md#pangenome) · [hifiasm](../../references/index.md#hifiasm) · [iqtree](../../references/index.md#iqtree) |


<a id="m155"></a>
## M155 群体结构、祖源与基因流

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究混合历史、亲缘和祖源片段 |
| 基本原理 | 用等位频率、单倍型和共享变异刻画群体差异 |
| 输入数据 / 上游实验 | 群体基因型、采样地/历史、参考群体 |
| 核心处理 | PCA；结构模型；F统计；局部祖源和基因流检验 |
| 可以得到的结果 | 群体结构、祖源比例/片段、混合证据 |
| 常用术语 | FST：群体分化；admixture：混合；introgression：渗入 |
| 代表工具 | PLINK；ADMIXTURE；ADMIXTOOLS；RFMix |
| 前提、QC与证据边界 | 成分数/参考影响祖源解释；统计簇不等于固定自然类别 |
| 代表来源与延伸阅读 | [plink](../../references/index.md#plink) · [tskit](../../references/index.md#tskit) |


<a id="m156"></a>
## M156 群体历史、共祖与祖先重组图

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 重建瓶颈、扩张、分化和重组历史 |
| 基本原理 | 利用谱系、频谱或连锁推断有效群体大小和事件 |
| 输入数据 / 上游实验 | SFS、相位基因组、多样本变异及模型 |
| 核心处理 | 共祖/前向模拟；似然或ABC；ARG/tree sequence推断 |
| 可以得到的结果 | Ne历史、分化/迁移参数、局部谱系 |
| 常用术语 | Ne：有效群体大小；SFS：位点频率谱；ARG：祖先重组图 |
| 代表工具 | msprime；tskit；SLiM；dadi；fastsimcoal；Relate |
| 前提、QC与证据边界 | 多种人口史可能同样拟合；突变率/世代时间影响绝对年代 |
| 代表来源与延伸阅读 | [tskit](../../references/index.md#tskit) · [plink](../../references/index.md#plink) |


<a id="m157"></a>
## M157 古DNA质量与遗传历史分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 从历史样本重建遗传和群体关系 |
| 基本原理 | 对高度降解和损伤序列做概率处理 |
| 输入数据 / 上游实验 | 古DNA FASTQ、空白、参考、年代信息 |
| 核心处理 | 片段/末端损伤；污染估计；低深度基因型似然；群体模型 |
| 可以得到的结果 | 真实性QC、遗传关系、祖源与人口史候选 |
| 常用术语 | aDNA：古DNA；deamination：脱氨；pseudo-haploid：伪单倍体 |
| 代表工具 | mapDamage；ANGSD；EAGER；ADMIXTOOLS |
| 前提、QC与证据边界 | 现代污染与参考偏倚重要；低深度不能用普通高深度基因型逻辑替代 |
| 代表来源与延伸阅读 | [hts](../../references/index.md#hts) · [tskit](../../references/index.md#tskit) · [plink](../../references/index.md#plink) |


<a id="m158"></a>
## M158 比较性状与系统发育校正

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究性状演化、趋同和生态关联 |
| 基本原理 | 在共享祖先导致的相关性下比较物种性状 |
| 输入数据 / 上游实验 | 物种树、性状/生态数据、测量误差 |
| 核心处理 | PGLS；独立对比；祖先状态；演化速率模型 |
| 可以得到的结果 | 校正后关联、祖先状态和速率差异 |
| 常用术语 | phylogenetic signal：系统发育信号；PGLS：系统发育广义最小二乘 |
| 代表工具 | ape；phytools；caper；BayesTraits |
| 前提、QC与证据边界 | 物种不是完全独立样本；树误差及缺失性状需传播 |
| 代表来源与延伸阅读 | [iqtree](../../references/index.md#iqtree) · [stats](../../references/index.md#stats) · [tskit](../../references/index.md#tskit) |
