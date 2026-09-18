# 17 显微图像与细胞表型

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m127"></a>
## M127 显微图像校正、去噪与反卷积

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 校正照明、漂移、模糊并提高测量可靠性 |
| 基本原理 | 用成像系统和噪声模型恢复更可分析的信号 |
| 输入数据 / 上游实验 | 多通道图像、暗场/平场、PSF、像素与曝光元数据 |
| 核心处理 | flat-field；漂移；去噪；PSF反卷积；保真检查 |
| 可以得到的结果 | 校正图像及残差、有效信噪比 |
| 常用术语 | PSF：点扩散函数；deconvolution：反卷积；SNR：信噪比 |
| 代表工具 | Fiji；DeconvolutionLab；CellProfiler；CARE |
| 前提、QC与证据边界 | AI增强可能制造/抹除结构；分析需保留原始图及独立验证 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [cellpose](../../references/index.md#cellpose) · [sklearn](../../references/index.md#sklearn) |


<a id="m128"></a>
## M128 细胞/细胞核/细胞器分割

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 让图像转为单对象定量数据 |
| 基本原理 | 识别每个对象的边界或像素类别 |
| 输入数据 / 上游实验 | 2D/3D显微图像；可选人工标注 |
| 核心处理 | 阈值/分水岭或深度分割；人工QC；跨域测试 |
| 可以得到的结果 | instance mask、对象计数、边界及误差 |
| 常用术语 | semantic/instance segmentation：语义/实例分割；IoU/Dice：重叠指标 |
| 代表工具 | Cellpose；StarDist；ilastik；U-Net；CellProfiler |
| 前提、QC与证据边界 | 预训练模型并非适用所有组织；融合/分裂错误传递到表达与形态统计 |
| 代表来源与延伸阅读 | [cellpose](../../references/index.md#cellpose) · [cellprof](../../references/index.md#cellprof) |


<a id="m129"></a>
## M129 形态学、定位与Cell Painting

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 量化药物/基因引发的多维细胞表型 |
| 基本原理 | 对分割对象提取强度、形状、纹理和相互位置特征 |
| 输入数据 / 上游实验 | 多染色图像、掩膜、孔位/批次和扰动标签 |
| 核心处理 | 特征提取；单细胞汇总；批次/密度校正；表型比较 |
| 可以得到的结果 | 形态指纹、亚细胞定位、相似机制候选 |
| 常用术语 | morphological profile：形态谱；texture：纹理；phenotypic similarity：表型相似 |
| 代表工具 | CellProfiler；pycytominer；深度图像嵌入 |
| 前提、QC与证据边界 | 形态相似只提示过程相似；细胞毒性及密度可能主导特征 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [cellpose](../../references/index.md#cellpose) · [sklearn](../../references/index.md#sklearn) |


<a id="m130"></a>
## M130 单细胞/粒子追踪与运动分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究迁移、运输、分裂及随机扩散 |
| 基本原理 | 跨时间关联同一对象并量化位移和转向 |
| 输入数据 / 上游实验 | 时序图像、粒子/细胞坐标、时间间隔 |
| 核心处理 | 检测；轨迹连接；漂移校正；MSD/速度/持久性 |
| 可以得到的结果 | 轨迹、扩散系数、迁移速率、分裂事件 |
| 常用术语 | MSD：均方位移；persistence：方向持久性；ID switch：身份交换 |
| 代表工具 | TrackMate；Trackpy；btrack；CellProfiler |
| 前提、QC与证据边界 | 定位误差、帧率和轨迹截断会偏置扩散/速度估计 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [cellpose](../../references/index.md#cellpose) · [stats](../../references/index.md#stats) |


<a id="m131"></a>
## M131 病理全切片分析与弱监督学习

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 识别组织区、细胞结构和候选表型关联 |
| 基本原理 | 将大切片分块，在区域或患者层级聚合形态信息 |
| 输入数据 / 上游实验 | WSI病理图像、染色信息、患者标签 |
| 核心处理 | 组织检测；stain处理；分割/patch编码；MIL；外部验证 |
| 可以得到的结果 | 组织/细胞地图、热图、患者级预测 |
| 常用术语 | WSI：全切片图；MIL：多实例学习；domain shift：域偏移 |
| 代表工具 | QuPath；TIAToolbox；MONAI；深度MIL |
| 前提、QC与证据边界 | 同患者切片必须同一数据划分；热图关注区域不自动是机制解释 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [sklearn](../../references/index.md#sklearn) · [squidpy](../../references/index.md#squidpy) |


<a id="m132"></a>
## M132 多色流式、光谱流式与CyTOF

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 表型鉴定、分群、频率和功能标记比较 |
| 基本原理 | 在单细胞层面记录荧光或金属标签强度 |
| 输入数据 / 上游实验 | FCS事件表、补偿/参考谱、FMO/单染、样本设计 |
| 核心处理 | 去碎片/双细胞；补偿或解混；变换；gating/聚类 |
| 可以得到的结果 | 细胞群、比例、MFI、状态及群体变化 |
| 常用术语 | FMO：缺一色对照；compensation：补偿；unmixing：光谱解混 |
| 代表工具 | FlowJo；FlowKit；flowCore；FlowSOM；CATALYST |
| 前提、QC与证据边界 | 补偿和光谱解混不是同一步骤；阳性门和批次影响比例，事件不是独立个体 |
| 代表来源与延伸阅读 | [flow](../../references/index.md#flow) · [scanpy](../../references/index.md#scanpy) |


<a id="m133"></a>
## M133 超分辨定位与分子聚集分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究纳米尺度组织和分子簇 |
| 基本原理 | 定位单荧光发射体或重建高频信息 |
| 输入数据 / 上游实验 | STORM/PALM/SIM等原始图像；标定与漂移记录 |
| 核心处理 | 定位/重建；闪烁合并；漂移；空间点统计 |
| 可以得到的结果 | 定位坐标、超分辨图、簇大小和密度 |
| 常用术语 | localization precision：定位精度；blinking：闪烁；Ripley's K：点聚集统计 |
| 代表工具 | ThunderSTORM；Picasso；Fiji；专用软件 |
| 前提、QC与证据边界 | 一次闪烁不等于一个分子；重建分辨率与定位精度不同 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [squidpy](../../references/index.md#squidpy) · [stats](../../references/index.md#stats) |


<a id="m134"></a>
## M134 FRAP、FRET与荧光相关定量

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究分子流动性、相互作用及局部浓度 |
| 基本原理 | 用恢复、能量转移或涨落曲线推断扩散/邻近/动力学 |
| 输入数据 / 上游实验 | 光漂白时间序列、供受体图像或荧光涨落 |
| 核心处理 | 背景/串色校正；恢复/寿命/相关曲线；物理模型拟合 |
| 可以得到的结果 | 移动分数、恢复时间、转移效率或扩散参数 |
| 常用术语 | FRAP：漂白后恢复；FRET：共振能量转移；FCS：荧光相关光谱 |
| 代表工具 | Fiji；专用寿命/相关软件；动力学拟合 |
| 前提、QC与证据边界 | 恢复同时受扩散和结合影响；FRET需合适距离取向及串色对照 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) |
