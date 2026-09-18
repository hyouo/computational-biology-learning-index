# 05 转录组与RNA机制

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m035"></a>
## M035 bulk RNA-seq定量与差异表达

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 找表达改变及转录程序 |
| 基本原理 | 用测序计数表征样本平均RNA丰度，负二项模型比较条件 |
| 输入数据 / 上游实验 | RNA-seq FASTQ或gene counts；设计与注释 |
| 核心处理 | QC；比对/定量；低表达过滤；归一化；模型对比 |
| 可以得到的结果 | 基因表达矩阵、log2FC、FDR、富集候选 |
| 常用术语 | counts：计数；TPM：相对转录本丰度；dispersion：离散度 |
| 代表工具 | STAR/Salmon；DESeq2；edgeR；limma-voom |
| 前提、QC与证据边界 | RNA变化≠蛋白变化；DESeq2通常不用logTPM；细胞比例可驱动bulk差异 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [deseq](../../references/index.md#deseq) |


<a id="m036"></a>
## M036 异构体与长读长转录组

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 识别isoform、融合和新转录本 |
| 基本原理 | 跨完整转录本读段解析外显子连接及起止组合 |
| 输入数据 / 上游实验 | Iso-Seq/ONT cDNA或直接RNA reads；参考注释 |
| 核心处理 | 剪接比对；纠错；转录本collapse；结构QC；定量 |
| 可以得到的结果 | 异构体目录、结构及使用比例 |
| 常用术语 | isoform：转录异构体；FSM：完全剪接匹配；NMD：无义介导降解 |
| 代表工具 | FLAIR；TALON；SQANTI3；IsoQuant |
| 前提、QC与证据边界 | 截短、内部引物和测序错误会产生假异构体；需结合独立证据 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [hts](../../references/index.md#hts) |


<a id="m037"></a>
## M037 可变剪接与差异转录本使用

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 发现条件相关RNA加工变化 |
| 基本原理 | 比较外显子/剪接连接使用比例，而非总表达 |
| 输入数据 / 上游实验 | RNA BAM/junction counts或转录本计数；重复样本 |
| 核心处理 | 事件定义；PSI/DTU估计；统计对比 |
| 可以得到的结果 | 外显子跳跃等事件、ΔPSI、差异异构体 |
| 常用术语 | PSI：包含比例；DTU：转录本使用差异；IR：内含子保留 |
| 代表工具 | rMATS；LeafCutter；DEXSeq；DRIMSeq |
| 前提、QC与证据边界 | 基因总量不变也可剪接改变；低覆盖和注释影响结果 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [deseq](../../references/index.md#deseq) |


<a id="m038"></a>
## M038 APA与转录起始位点分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究UTR、启动子选择及调控 |
| 基本原理 | 比较RNA的3′切割加尾位点或5′起始分布 |
| 输入数据 / 上游实验 | 3′端测序、CAGE/RAMPAGE、常规或长读长RNA |
| 核心处理 | 定位端点；内部引物过滤；位点使用比较 |
| 可以得到的结果 | APA/TSS位点、UTR长短变化及使用比例 |
| 常用术语 | APA：可变多聚腺苷化；TSS：转录起始；UTR：非翻译区 |
| 代表工具 | DaPars；QAPA；CAGEr |
| 前提、QC与证据边界 | 常规3′单细胞与专用3′端实验分辨力不同；端点偏倚需排查 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [alphagenome](../../references/index.md#alphagenome) |


<a id="m039"></a>
## M039 融合转录本与RNA编辑

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 分析重排表达产物和转录后编辑 |
| 基本原理 | 识别异常跨基因连接或RNA相对DNA的碱基变化 |
| 输入数据 / 上游实验 | RNA reads；可选匹配DNA、正常对照 |
| 核心处理 | 嵌合比对；重复/伪基因过滤；DNA变异排除 |
| 可以得到的结果 | 融合候选及断点、编辑位点和比例 |
| 常用术语 | fusion：融合；A-to-I：腺苷到肌苷编辑；chimeric read：嵌合读段 |
| 代表工具 | STAR-Fusion；Arriba；REDItools |
| 前提、QC与证据边界 | 比对错误、read-through和遗传SNP可伪装成融合或编辑 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [sarek](../../references/index.md#sarek) |


<a id="m040"></a>
## M040 小RNA与非编码RNA分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究miRNA、piRNA、tRNA片段等调控 |
| 基本原理 | 按长度、序列和生物发生特征定量非编码RNA |
| 输入数据 / 上游实验 | small RNA-seq reads；专用接头和注释 |
| 核心处理 | 长度/接头QC；多重比对；家族及位点定量 |
| 可以得到的结果 | 小RNA表达、候选新miRNA、差异家族 |
| 常用术语 | miRNA：微RNA；isomiR：miRNA异构体；tRF：tRNA片段 |
| 代表工具 | miRDeep2；sRNAbench；专用比对流程 |
| 前提、QC与证据边界 | 修饰阻断逆转录及多拷贝可造成偏差；预测靶点不是验证靶点 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [meme](../../references/index.md#meme) |


<a id="m041"></a>
## M041 新生转录与RNA合成/降解动力学

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 分离合成速率、稳定性和转录暂停 |
| 基本原理 | 用延伸中的聚合酶或代谢标记区分新旧RNA |
| 输入数据 / 上游实验 | PRO/GRO/NET-seq；TT/SLAM-seq；时间与标记信息 |
| 核心处理 | 链特异比对；转换/标记识别；动力学拟合 |
| 可以得到的结果 | 新生转录、暂停指数、合成/降解或半衰期估计 |
| 常用术语 | nascent RNA：新生RNA；pause index：暂停指数；half-life：半衰期 |
| 代表工具 | 专用PRO-seq流程；GRAND-SLAM；kinetic models |
| 前提、QC与证据边界 | 标记效率、毒性、稳态及时间窗影响估计；不能用单点表达替代速率 |
| 代表来源与延伸阅读 | [velocity](../../references/index.md#velocity) · [copasi](../../references/index.md#copasi) · [rnaseq](../../references/index.md#rnaseq) |


<a id="m042"></a>
## M042 核糖体测序Ribo-seq

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位翻译ORF和估计相对翻译效率 |
| 基本原理 | 测定核糖体保护RNA片段及阅读框周期性 |
| 输入数据 / 上游实验 | RPF FASTQ；匹配RNA-seq；注释 |
| 核心处理 | rRNA过滤；P-site定位；三核苷酸周期性；ORF及TE分析 |
| 可以得到的结果 | 核糖体占据图、翻译ORF、TE变化 |
| 常用术语 | RPF：核糖体保护片段；P-site：肽酰位点；TE：翻译效率 |
| 代表工具 | RiboTISH；RiboCode；nf-core/riboseq |
| 前提、QC与证据边界 | 占据受停顿和延伸影响；不是直接测得蛋白稳态量 |
| 代表来源与延伸阅读 | [ribo](../../references/index.md#ribo) |


<a id="m043"></a>
## M043 CLIP/eCLIP/iCLIP与RBP结合

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 定位RBP结合区域和序列偏好 |
| 基本原理 | 交联并富集RNA结合蛋白所接触的RNA |
| 输入数据 / 上游实验 | CLIP reads、input/control、交联信息 |
| 核心处理 | UMI/QC；crosslink/peak calling；背景和motif分析 |
| 可以得到的结果 | RBP结合位点、富集RNA及基序 |
| 常用术语 | RBP：RNA结合蛋白；crosslink：交联；CLIP：交联免疫沉淀 |
| 代表工具 | PureCLIP；CLIPper；专用流程 |
| 前提、QC与证据边界 | 交联/抗体和RNA丰度带来偏倚；结合不必然产生调控效应 |
| 代表来源与延伸阅读 | [eclip](../../references/index.md#eclip) · [meme](../../references/index.md#meme) |


<a id="m044"></a>
## M044 RNA修饰与表观转录组

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 定位m6A等RNA修饰及条件差异 |
| 基本原理 | 用富集、化学/酶处理或直接RNA信号检测修饰 |
| 输入数据 / 上游实验 | MeRIP/m6A-CLIP、位点法或直接RNA数据；input |
| 核心处理 | 背景及表达校正；peak/位点识别；独立验证 |
| 可以得到的结果 | 修饰候选区域/位点、富集或修饰比例估计 |
| 常用术语 | m6A：N6-甲基腺苷；stoichiometry：修饰占比 |
| 代表工具 | exomePeak2；专用直接RNA模型 |
| 前提、QC与证据边界 | 抗体富集峰通常非单碱基及绝对占比；信号模型需校准 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [meme](../../references/index.md#meme) |


<a id="m045"></a>
## M045 RNA二级结构与互作结构

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究RNA折叠与远程相互作用 |
| 基本原理 | 化学探测反应性约束配对模型，或交联记录RNA接近 |
| 输入数据 / 上游实验 | SHAPE/DMS-MaP、PARIS/SPLASH等reads或RNA序列 |
| 核心处理 | 反应性估计；约束折叠；互作连接检测 |
| 可以得到的结果 | 结构概率、反应性轨道、RNA-RNA互作候选 |
| 常用术语 | SHAPE：选择性2′羟基酰化；DMS：二甲基硫酸探测；MFE：最小自由能 |
| 代表工具 | RNAstructure；ViennaRNA；专用流程 |
| 前提、QC与证据边界 | 细胞中可能有多个构象；低能量预测不是唯一真实结构 |
| 代表来源与延伸阅读 | [dms](../../references/index.md#dms) · [af3](../../references/index.md#af3) |
