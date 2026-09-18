# 21 生态、植物与农业

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m159"></a>
## M159 群落多样性、排序与PERMANOVA

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究环境/处理对应的群落变化 |
| 基本原理 | 以物种组成距离及约束模型比较群落结构 |
| 输入数据 / 上游实验 | 样地×物种表、环境与实验区组 |
| 核心处理 | α/β多样性；PCoA/NMDS；RDA/CCA；置换检验 |
| 可以得到的结果 | 群落排序、效应、环境解释比例 |
| 常用术语 | Bray–Curtis：丰度差异距离；NMDS：非度量排序；PERMANOVA：置换方差分析 |
| 代表工具 | vegan；QIIME 2 |
| 前提、QC与证据边界 | 组间离散度不同会影响解释；置换应按区组或空间限制 |
| 代表来源与延伸阅读 | [vegan](../../references/index.md#vegan) · [qiime](../../references/index.md#qiime) |


<a id="m160"></a>
## M160 物种分布与生态位模型

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 预测适生范围和环境变化关联 |
| 基本原理 | 学习物种出现与环境的关系并投射空间 |
| 输入数据 / 上游实验 | 出现/缺失或presence-only数据、环境栅格 |
| 核心处理 | 采样偏倚处理；背景选择；模型；空间分块CV |
| 可以得到的结果 | 适生性地图、环境响应、预测不确定性 |
| 常用术语 | SDM：物种分布模型；niche：生态位；background：背景点 |
| 代表工具 | biomod2；MaxEnt；ENMeval |
| 前提、QC与证据边界 | 适生性不是实际占据概率的无条件保证；新环境外推需谨慎 |
| 代表来源与延伸阅读 | [biomod](../../references/index.md#biomod) · [sklearn](../../references/index.md#sklearn) |


<a id="m161"></a>
## M161 占据、检测概率与标志重捕

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 估计种群数量、出现和存活变化 |
| 基本原理 | 区分真实存在/存活和观测到的概率 |
| 输入数据 / 上游实验 | 重复调查、检测历史、标记个体记录 |
| 核心处理 | occupancy或capture-recapture层级模型；可识别性检查 |
| 可以得到的结果 | 占据率、检测率、存活率、数量估计 |
| 常用术语 | detectability：可检测性；occupancy：占据；capture-recapture：标志重捕 |
| 代表工具 | unmarked；RMark；NIMBLE；Bayesian模型 |
| 前提、QC与证据边界 | 未检测到不等于不存在；封闭性、标记丢失和调查设计影响估计 |
| 代表来源与延伸阅读 | [stats](../../references/index.md#stats) · [vegan](../../references/index.md#vegan) · [biomod](../../references/index.md#biomod) |


<a id="m162"></a>
## M162 环境DNA与生物多样性监测

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究难直接调查的群落和分布 |
| 基本原理 | 从环境样本的DNA条码或混合序列推断生物出现 |
| 输入数据 / 上游实验 | 水/土壤等eDNA reads；采样、空白、参考库 |
| 核心处理 | 去噪/分类；污染与检测阈值；时空/占据模型 |
| 可以得到的结果 | 物种检出、群落变化、分布候选 |
| 常用术语 | eDNA：环境DNA；metabarcoding：宏条形码；false absence：假缺失 |
| 代表工具 | QIIME 2；DADA2；OBITools；占据模型 |
| 前提、QC与证据边界 | DNA可被运输和残留；reads数不是通用个体数，参考库不全会漏检 |
| 代表来源与延伸阅读 | [qiime](../../references/index.md#qiime) · [dada](../../references/index.md#dada) · [vegan](../../references/index.md#vegan) |


<a id="m163"></a>
## M163 植物数量性状定位与基因组选择

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 定位农艺性状并提高选择效率 |
| 基本原理 | 利用遗传标记与表型关联或预测育种值 |
| 输入数据 / 上游实验 | 亲本/后代或种质基因型；田间表型；环境信息 |
| 核心处理 | QTL/GWAS；亲缘/区组校正；G×E；基因组预测 |
| 可以得到的结果 | QTL区间、候选基因、育种值和预测性能 |
| 常用术语 | QTL：数量性状位点；G×E：基因×环境；GEBV：基因组估计育种值 |
| 代表工具 | R/qtl2；GAPIT；rrBLUP；BGLR |
| 前提、QC与证据边界 | 群体结构、连锁及田间环境可混杂；跨环境/代际预测需独立验证 |
| 代表来源与延伸阅读 | [plink](../../references/index.md#plink) · [stats](../../references/index.md#stats) · [sklearn](../../references/index.md#sklearn) |


<a id="m164"></a>
## M164 高通量植物表型与遥感

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 量化生长、结构、胁迫与时空变化 |
| 基本原理 | 从图像、光谱、热信号和三维点云提取性状 |
| 输入数据 / 上游实验 | 地面/无人机图像、光谱、LiDAR、地理与环境元数据 |
| 核心处理 | 辐射/几何校正；分割；3D重建；性状反演；地面验证 |
| 可以得到的结果 | 株高/面积/生长曲线、胁迫代理、田间性状图 |
| 常用术语 | NDVI：归一化植被指数；LiDAR：激光雷达；phenomics：表型组学 |
| 代表工具 | PlantCV；OpenDroneMap；点云工具；ML模型 |
| 前提、QC与证据边界 | 光谱指数是代理信号；光照、冠层、土壤和季节可混杂 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [biomod](../../references/index.md#biomod) · [sklearn](../../references/index.md#sklearn) |


<a id="m165"></a>
## M165 多倍体、亚基因组与等位表达

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究多倍化、亚基因组优势与剂量效应 |
| 基本原理 | 区分同源染色体及不同起源的相似基因拷贝 |
| 输入数据 / 上游实验 | 高质量组装、相位变异、RNA及祖先/近缘参考 |
| 核心处理 | 同源/亚基因组分配；dosage；homeolog表达及选择 |
| 可以得到的结果 | 亚基因组结构、剂量、同源拷贝偏表达 |
| 常用术语 | homeolog：异源多倍体同源拷贝；dosage：剂量；subgenome：亚基因组 |
| 代表工具 | hifiasm类组装；专用多倍体分型；共线性与RNA流程 |
| 前提、QC与证据边界 | 高度相似拷贝的错配会制造表达优势；二倍体假设不能直接套用 |
| 代表来源与延伸阅读 | [hifiasm](../../references/index.md#hifiasm) · [pangenome](../../references/index.md#pangenome) · [rnaseq](../../references/index.md#rnaseq) |


<a id="m166"></a>
## M166 食物网、种群动力学与生态互作

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究稳定性、竞争、捕食和扰动响应 |
| 基本原理 | 以网络和微分/随机模型描述种群变化及作用 |
| 输入数据 / 上游实验 | 丰度时间序列、摄食/互作观测、环境与干预 |
| 核心处理 | 网络构建；Lotka–Volterra/状态空间；参数与敏感性 |
| 可以得到的结果 | 互作候选、稳定性、种群轨迹和情景预测 |
| 常用术语 | food web：食物网；carrying capacity：承载量；stability：稳定性 |
| 代表工具 | vegan；deSolve；COPASI；定制模型 |
| 前提、QC与证据边界 | 共现不等于直接互作；模型可识别性和观测误差限制参数解释 |
| 代表来源与延伸阅读 | [vegan](../../references/index.md#vegan) · [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) |
