# 13 蛋白质组与蛋白状态

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m096"></a>
## M096 DDA质谱鉴定与蛋白推断

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 确定样本中检测到哪些蛋白 |
| 基本原理 | 把MS/MS碎片谱匹配候选肽，再归属蛋白 |
| 输入数据 / 上游实验 | LC-MS/MS原始谱、蛋白FASTA、酶切/修饰设置 |
| 核心处理 | 峰处理；数据库搜索；target-decoy；肽到蛋白推断 |
| 可以得到的结果 | PSM、肽段、蛋白组及层级FDR |
| 常用术语 | PSM：谱图—肽段匹配；DDA：依赖数据采集；protein group：蛋白组 |
| 代表工具 | MaxQuant；MSFragger；Proteome Discoverer |
| 前提、QC与证据边界 | 共享肽无法唯一归属蛋白；PSM-FDR不自动等于蛋白FDR |
| 代表来源与延伸阅读 | [maxquant](../../references/index.md#maxquant) · [msstats](../../references/index.md#msstats) |


<a id="m097"></a>
## M097 DIA质谱定量

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 提高跨样本定量一致性和蛋白覆盖 |
| 基本原理 | 宽窗口系统采集混合碎片谱，再分离目标肽信号 |
| 输入数据 / 上游实验 | DIA原始谱；可选实测/预测谱库 |
| 核心处理 | 色谱峰提取；碎片解卷积；干扰校正；FDR控制 |
| 可以得到的结果 | 肽/蛋白强度矩阵、定量QC |
| 常用术语 | DIA：非依赖数据采集；library-free：无外部实测谱库；RT：保留时间 |
| 代表工具 | DIA-NN；Spectronaut；OpenSWATH |
| 前提、QC与证据边界 | 混合谱和批次仍影响结果；无谱库不等于不需要序列/模型先验 |
| 代表来源与延伸阅读 | [diann](../../references/index.md#diann) · [msstats](../../references/index.md#msstats) |


<a id="m098"></a>
## M098 LFQ、SILAC与TMT比较定量

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 比较条件间蛋白表达和重复变化 |
| 基本原理 | 利用离子强度、代谢质量标记或同量异位标签比较丰度 |
| 输入数据 / 上游实验 | 定量谱图、标签通道、样本表和参考通道 |
| 核心处理 | 标签校正；蛋白汇总；归一化；批次/重复统计 |
| 可以得到的结果 | 蛋白丰度、logFC、差异及QC |
| 常用术语 | LFQ：无标记定量；SILAC：稳定同位素标记；TMT：串联质量标签 |
| 代表工具 | MaxQuant；MSstats；MSstatsTMT；limma |
| 前提、QC与证据边界 | TMT共分离可压缩比值；缺失和归一化不能机械处理 |
| 代表来源与延伸阅读 | [maxquant](../../references/index.md#maxquant) · [msstats](../../references/index.md#msstats) |


<a id="m099"></a>
## M099 靶向蛋白组与绝对定量

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 精确验证候选蛋白或特定修饰 |
| 基本原理 | 选择特定肽/碎片并借助标准物定量 |
| 输入数据 / 上游实验 | PRM/SRM/MRM谱；标准肽；校准曲线 |
| 核心处理 | 峰界定；碎片离子比；内标校准；LOD/LOQ和重复性 |
| 可以得到的结果 | 目标蛋白/肽相对或绝对浓度 |
| 常用术语 | PRM：平行反应监测；SRM：选择反应监测；LOQ：定量限 |
| 代表工具 | Skyline；厂商软件；MSstats |
| 前提、QC与证据边界 | 肽作为蛋白代理需要消化/回收校准；无标准不能直接报绝对浓度 |
| 代表来源与延伸阅读 | [msstats](../../references/index.md#msstats) · [maxquant](../../references/index.md#maxquant) |


<a id="m100"></a>
## M100 磷酸化及其他PTM组学

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究信号转导、泛素化、乙酰化等 |
| 基本原理 | 富集或定位带修饰肽，分析位点及占据变化 |
| 输入数据 / 上游实验 | PTM富集LC-MS/MS；总蛋白组；修饰数据库 |
| 核心处理 | 修饰搜索；位点定位概率；蛋白量校正；激酶底物富集 |
| 可以得到的结果 | 修饰位点、变化、候选酶活性 |
| 常用术语 | PTM：翻译后修饰；localization probability：位点定位概率；occupancy：占据率 |
| 代表工具 | MaxQuant；FragPipe；MSstatsPTM；KSEA |
| 前提、QC与证据边界 | 修饰信号增加可能由总蛋白增加；富集强度通常不是占据率 |
| 代表来源与延伸阅读 | [maxquant](../../references/index.md#maxquant) · [msstats](../../references/index.md#msstats) |


<a id="m101"></a>
## M101 糖蛋白组与糖组学

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究糖基化异质性及分子功能 |
| 基本原理 | 解析肽骨架、糖基化位点与糖链组成/碎片 |
| 输入数据 / 上游实验 | 糖肽/释放糖链MS、酶学处理信息和标准 |
| 核心处理 | 糖肽搜索；位点/糖型归属；定量与结构置信度分级 |
| 可以得到的结果 | 糖型、位点、糖肽丰度及候选结构 |
| 常用术语 | glycoform：糖型；glycan：糖链；isomer：异构体 |
| 代表工具 | Byonic；pGlyco；MSFragger-Glyco；MS-DIAL |
| 前提、QC与证据边界 | 相同质量可对应多个糖异构体；组成鉴定不等于完整连接结构 |
| 代表来源与延伸阅读 | [maxquant](../../references/index.md#maxquant) · [msdial](../../references/index.md#msdial) |


<a id="m102"></a>
## M102 AP-MS与邻近标记互作组

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位候选互作、复合物和亚细胞邻域 |
| 基本原理 | 纯化诱饵复合物或标记空间邻近蛋白后进行MS |
| 输入数据 / 上游实验 | Co-IP/AP-MS或BioID/TurboID/APEX蛋白强度；对照 |
| 核心处理 | 背景蛋白过滤；富集统计；重复一致性；网络注释 |
| 可以得到的结果 | 候选互作伙伴、邻近蛋白和复合物 |
| 常用术语 | bait/prey：诱饵/猎物；PL：邻近标记；contaminant：污染背景 |
| 代表工具 | SAINT；MSstats；网络分析工具 |
| 前提、QC与证据边界 | 邻近、同一复合物和直接结合是三种不同证据；需要合适空间/标签对照 |
| 代表来源与延伸阅读 | [turbo](../../references/index.md#turbo) · [maxquant](../../references/index.md#maxquant) |


<a id="m103"></a>
## M103 结构蛋白组：交联、HDX与有限酶解

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究构象、界面及配体引发的改变 |
| 基本原理 | 把距离约束、溶剂暴露或局部可切性转换成结构信息 |
| 输入数据 / 上游实验 | XL-MS交联谱、HDX时间质谱或LiP-MS肽量 |
| 核心处理 | 位点鉴定；交换/保护曲线；差异与结构映射 |
| 可以得到的结果 | 残基距离约束、保护区域、构象变化候选 |
| 常用术语 | XL-MS：交联质谱；HDX：氢氘交换；LiP：有限蛋白水解 |
| 代表工具 | XlinkX；pLink；HDX专用软件；结构整合工具 |
| 前提、QC与证据边界 | 交联长度是软约束；交换/酶解变化可受动力学和环境影响 |
| 代表来源与延伸阅读 | [phenix](../../references/index.md#phenix) · [maxquant](../../references/index.md#maxquant) · [af3](../../references/index.md#af3) |


<a id="m104"></a>
## M104 热蛋白组、蛋白周转与免疫肽组

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 寻找药物结合候选、周转速率或天然呈递肽 |
| 基本原理 | 利用稳定性、标记时间或MHC富集等专用设计读取蛋白功能状态 |
| 输入数据 / 上游实验 | TPP/CETSA-MS、pulse-SILAC或免疫肽MS与相应对照 |
| 核心处理 | 按实验拟合熔解/周转；或非特异酶肽搜索与呈递分析 |
| 可以得到的结果 | 稳定性位移、半衰期或呈递肽清单 |
| 常用术语 | TPP：热蛋白组；turnover：周转；immunopeptidome：免疫肽组 |
| 代表工具 | TPP；MaxQuant；FragPipe；MSstats |
| 前提、QC与证据边界 | 这是三类专用实验；稳定性变化不一定直接结合，检测到肽不保证免疫原性 |
| 代表来源与延伸阅读 | [maxquant](../../references/index.md#maxquant) · [msstats](../../references/index.md#msstats) · [copasi](../../references/index.md#copasi) |
