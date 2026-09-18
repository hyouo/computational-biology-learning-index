# 09 空间组学与组织生态位

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m069"></a>
## M069 捕获式空间转录组

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 保留表达与组织位置的联系 |
| 基本原理 | 将组织RNA赋予空间条码并测序 |
| 输入数据 / 上游实验 | 空间FASTQ、spot/bin坐标、组织图像 |
| 核心处理 | 比对定量；图像对齐；组织掩膜；空间QC |
| 可以得到的结果 | 空间表达矩阵、组织轨道、候选空间区域 |
| 常用术语 | spot/bin：捕获单元；capture efficiency：捕获效率 |
| 代表工具 | Space Ranger；Stereo-seq/Slide-seq分析流程；SpatialData |
| 前提、QC与证据边界 | spot可能混多个细胞；bin小不自动等于可信单细胞分辨率 |
| 代表来源与延伸阅读 | [squidpy](../../references/index.md#squidpy) · [cell2loc](../../references/index.md#cell2loc) |


<a id="m070"></a>
## M070 成像式空间转录组与原位测序

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 在原位得到分子坐标与细胞表达 |
| 基本原理 | 多轮探针成像或原位读序定位RNA分子 |
| 输入数据 / 上游实验 | 多轮多通道图像、barcode codebook、细胞边界 |
| 核心处理 | 配准；点检测；解码；背景/误码；分配细胞 |
| 可以得到的结果 | 分子×坐标表、细胞×基因矩阵 |
| 常用术语 | MERFISH/seqFISH：复用原位杂交；codebook：编码表 |
| 代表工具 | 平台软件；Baysor；Squidpy；SpatialData |
| 前提、QC与证据边界 | 基因panel有限时不能假装全转录组；分割和分子归属影响细胞信号 |
| 代表来源与延伸阅读 | [squidpy](../../references/index.md#squidpy) · [cell2loc](../../references/index.md#cell2loc) |


<a id="m071"></a>
## M071 空间解卷积与细胞类型定位

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 推断哪些细胞群在组织哪里出现 |
| 基本原理 | 用参考细胞表达解释混合空间单位 |
| 输入数据 / 上游实验 | spot×gene矩阵；scRNA参考；批次信息 |
| 核心处理 | 参考特征选择；混合/概率模型；空间验证 |
| 可以得到的结果 | 每spot细胞类型丰度及不确定性 |
| 常用术语 | deconvolution：解卷积；reference bias：参考偏倚 |
| 代表工具 | cell2location；RCTD；SPOTlight |
| 前提、QC与证据边界 | 输出是推断丰度，不是测量到的单细胞位置；缺失参考会误分 |
| 代表来源与延伸阅读 | [cell2loc](../../references/index.md#cell2loc) |


<a id="m072"></a>
## M072 空间域、邻域和自相关

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 发现组织结构、生态位与共定位模式 |
| 基本原理 | 利用空间邻接检验表达或细胞类型的局部聚集 |
| 输入数据 / 上游实验 | 坐标、表达、细胞类型、组织边界 |
| 核心处理 | 邻居图；Moran/Geary；邻域富集；空间域模型 |
| 可以得到的结果 | 空间变异基因、组织域、邻接富集 |
| 常用术语 | Moran's I：空间自相关；niche：局部生态位 |
| 代表工具 | Squidpy；SpatialDE；SPARK-X；BayesSpace |
| 前提、QC与证据边界 | 空间置换应保留合理结构；解剖邻近不等于功能互作 |
| 代表来源与延伸阅读 | [squidpy](../../references/index.md#squidpy) |


<a id="m073"></a>
## M073 配体—受体与细胞通信推断

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 提出发送者、接收者和信号路径候选 |
| 基本原理 | 将配体/受体表达映射到先验相互作用数据库 |
| 输入数据 / 上游实验 | 单细胞/空间表达；细胞类型；配体受体库 |
| 核心处理 | 筛选表达；打分/置换；可选靶基因或空间约束 |
| 可以得到的结果 | 候选通信边、通路网络、发送/接收分数 |
| 常用术语 | ligand/receptor：配体/受体；autocrine：自分泌；paracrine：旁分泌 |
| 代表工具 | CellChat；CellPhoneDB；NicheNet；LIANA |
| 前提、QC与证据边界 | RNA≠分泌蛋白或受体活性；必须结合空间、蛋白和扰动验证 |
| 代表来源与延伸阅读 | [cellchat](../../references/index.md#cellchat) · [squidpy](../../references/index.md#squidpy) |


<a id="m074"></a>
## M074 空间蛋白组与多重组织成像

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 连接细胞类型、蛋白状态和组织结构 |
| 基本原理 | 用循环荧光、金属标签或空间取样质谱定位蛋白 |
| 输入数据 / 上游实验 | CycIF/CODEX/IMC/MIBI图像或激光切割MS数据 |
| 核心处理 | 轮次配准；去背景；分割；细胞表型；空间统计 |
| 可以得到的结果 | 细胞×蛋白矩阵、亚细胞/组织蛋白地图 |
| 常用术语 | IMC：成像质谱流式；MIBI：多重离子束成像；DVP：深度视觉蛋白组 |
| 代表工具 | 平台软件；CellProfiler；QuPath；Squidpy |
| 前提、QC与证据边界 | 抗体panel与质谱发现式覆盖不同；蛋白定位有分辨率及抗体验证限制 |
| 代表来源与延伸阅读 | [spatial2024](../../references/index.md#spatial2024) · [squidpy](../../references/index.md#squidpy) |


<a id="m075"></a>
## M075 多切片配准与三维组织重建

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 从二维切片构建组织三维结构或跨样本对应 |
| 基本原理 | 匹配相邻切片的图像、表达及几何结构 |
| 输入数据 / 上游实验 | 连续切片坐标/图像/表达、可选解剖标志 |
| 核心处理 | 刚性/非刚性配准；OT；形变校验；重建 |
| 可以得到的结果 | 三维坐标、对齐空间图谱、跨切片域对应 |
| 常用术语 | registration：配准；deformation：形变；landmark：标志点 |
| 代表工具 | PASTE；STalign；ANTs；SpatialData |
| 前提、QC与证据边界 | 切片损失、旋转和形变可产生假结构；推断坐标需标识 |
| 代表来源与延伸阅读 | [squidpy](../../references/index.md#squidpy) · [microns](../../references/index.md#microns) |


<a id="m076"></a>
## M076 空间多模态预测与缺失模态补全

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 预测未直接测量的空间分子层 |
| 基本原理 | 学到空间RNA、蛋白、图像与表观信号的对应 |
| 输入数据 / 上游实验 | 空间组学、单细胞参考、图像、配对或非配对数据 |
| 核心处理 | 共享表示；跨模态预测；留出样本验证 |
| 可以得到的结果 | 预测蛋白/表达/可及性地图及误差 |
| 常用术语 | imputation：补全；paired/unpaired：配对/非配对；OOD：分布外 |
| 代表工具 | 多模态生成模型；Nicheformer；领域专用模型 |
| 前提、QC与证据边界 | 预测图不能在图例中伪装成实测；跨组织泛化需独立测试 |
| 代表来源与延伸阅读 | [nicheformer](../../references/index.md#nicheformer) · [scvi](../../references/index.md#scvi) · [mofa](../../references/index.md#mofa) |
