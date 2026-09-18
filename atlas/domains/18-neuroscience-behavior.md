# 18 神经活动、连接组与行为

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m135"></a>
## M135 电生理spike sorting

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 获得候选单神经元放电事件 |
| 基本原理 | 从多电极混合电位中分离神经元发放模板 |
| 输入数据 / 上游实验 | 多通道电压时间序列、采样率、电极几何 |
| 核心处理 | 滤波；检测；模板匹配；漂移处理；不应期/污染QC |
| 可以得到的结果 | unit波形、spike times、质量指标 |
| 常用术语 | unit：分离单元；refractory period：不应期；drift：漂移 |
| 代表工具 | Kilosort；SpikeInterface；MountainSort |
| 前提、QC与证据边界 | 分离unit不保证恰好一个稳定神经元；漂移和噪声需验证 |
| 代表来源与延伸阅读 | [kilosort](../../references/index.md#kilosort) |


<a id="m136"></a>
## M136 钙成像与电压成像分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 获得群体神经活动的光学代理 |
| 基本原理 | 分离细胞荧光信号并校正运动和背景 |
| 输入数据 / 上游实验 | 单/双光子movies、采样率、刺激/行为时间戳 |
| 核心处理 | 运动校正；ROI/source提取；neuropil去混；ΔF/F；可选反卷积 |
| 可以得到的结果 | 荧光时间序列、事件及推断活动 |
| 常用术语 | ΔF/F：相对荧光变化；neuropil：神经纤维背景；CNMF：约束分解 |
| 代表工具 | CaImAn；Suite2p；VolPy |
| 前提、QC与证据边界 | 钙信号是发放的滤波代理；不同指示器动力学影响时间精度 |
| 代表来源与延伸阅读 | [caiman](../../references/index.md#caiman) · [microns](../../references/index.md#microns) |


<a id="m137"></a>
## M137 膜片钳、膜电流与离子通道模型

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究细胞兴奋性、突触和通道动力学 |
| 基本原理 | 在控制电压或电流条件下记录膜响应 |
| 输入数据 / 上游实验 | 膜电压/电流轨迹、刺激方案、细胞参数 |
| 核心处理 | 伪迹/QC；事件检测；I–V/阈值；动力学拟合 |
| 可以得到的结果 | 输入电阻、动作电位参数、突触电流、通道参数 |
| 常用术语 | voltage/current clamp：电压/电流钳；I–V：电流电压关系 |
| 代表工具 | Clampfit；pClamp；Neo；Elephant；NEURON |
| 前提、QC与证据边界 | 串联电阻和空间钳制误差很重要；切片条件未必代表体内状态 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) · [kilosort](../../references/index.md#kilosort) |


<a id="m138"></a>
## M138 神经编码、解码与群体动力学

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究信息表示、调谐和状态变化 |
| 基本原理 | 将刺激/行为与活动建立统计或动态映射 |
| 输入数据 / 上游实验 | spike/荧光/LFP及同步刺激、行为和任务事件 |
| 核心处理 | PSTH/GLM；编码/解码；交叉验证；潜在动力学 |
| 可以得到的结果 | 感受野、调谐曲线、可解码信息、群体状态 |
| 常用术语 | PSTH：刺激对齐直方图；tuning：调谐；latent dynamics：潜动力学 |
| 代表工具 | Elephant；statsmodels；scikit-learn；LFADS |
| 前提、QC与证据边界 | 可解码不等于脑实际用此信号；时间自相关可能使随机CV泄漏 |
| 代表来源与延伸阅读 | [kilosort](../../references/index.md#kilosort) · [caiman](../../references/index.md#caiman) · [stats](../../references/index.md#stats) · [sklearn](../../references/index.md#sklearn) |


<a id="m139"></a>
## M139 电子显微连接组重建

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 绘制神经元形态和结构网络 |
| 基本原理 | 分割连续EM体中的细胞并识别突触连接 |
| 输入数据 / 上游实验 | 连续切片/块面EM体数据；可选光学活动 |
| 核心处理 | 配准；神经突起分割；突触检测；proofreading；图构建 |
| 可以得到的结果 | 神经元骨架、突触表、连接图及结构统计 |
| 常用术语 | connectome：连接组；proofreading：人工校订；synapse：突触 |
| 代表工具 | Neuroglancer；CloudVolume；CAVE；深度EM分割 |
| 前提、QC与证据边界 | 分割合并/断裂会改变拓扑；结构连接不等于突触强度或因果功能 |
| 代表来源与延伸阅读 | [microns](../../references/index.md#microns) · [em2025](../../references/index.md#em2025) |


<a id="m140"></a>
## M140 EEG/MEG、LFP与fMRI信号分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究节律、网络活动与任务关联 |
| 基本原理 | 分析电磁/血氧时间序列及其空间来源 |
| 输入数据 / 上游实验 | 传感器/影像时序、头动/生理记录、任务时间 |
| 核心处理 | 滤波/伪迹；ICA；频谱/时频；GLM；连接性和多重校正 |
| 可以得到的结果 | 功率/相位、激活图、来源估计、功能连接 |
| 常用术语 | BOLD：血氧水平依赖；ICA：独立成分；functional connectivity：功能连接 |
| 代表工具 | MNE；EEGLAB；FieldTrip；FSL；SPM；fMRIPrep |
| 前提、QC与证据边界 | 滤波/参考选择改变结论；血氧不是直接神经发放，功能连接不是解剖连接 |
| 代表来源与延伸阅读 | [stats](../../references/index.md#stats) · [sklearn](../../references/index.md#sklearn) · [microns](../../references/index.md#microns) |


<a id="m141"></a>
## M141 无标记姿态估计与行为量化

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 客观量化动作、社会行为和运动表型 |
| 基本原理 | 从视频定位身体关键点，再构造运动/行为特征 |
| 输入数据 / 上游实验 | 单/多视角视频、人工标注、标定信息 |
| 核心处理 | 关键点模型；遮挡/身份QC；3D三角化；轨迹与行为标注 |
| 可以得到的结果 | 姿态、速度、动作片段和行为统计 |
| 常用术语 | pose estimation：姿态估计；keypoint：关键点；ethogram：行为谱 |
| 代表工具 | DeepLabCut；SLEAP；Anipose；SimBA |
| 前提、QC与证据边界 | 关键点准确不保证行为标签有效；动物/场景应独立验证 |
| 代表来源与延伸阅读 | [dlc](../../references/index.md#dlc) · [sklearn](../../references/index.md#sklearn) |


<a id="m142"></a>
## M142 行为状态、决策模型与闭环分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究策略、学习率、反馈及干预响应 |
| 基本原理 | 用隐状态或强化学习模型解释连续行为和选择 |
| 输入数据 / 上游实验 | 行为事件、奖励、选择、姿态和神经信号 |
| 核心处理 | HMM/状态分割；RL参数拟合；模型恢复；干预比较 |
| 可以得到的结果 | 行为状态、转移率、决策参数和模型预测 |
| 常用术语 | RL：强化学习；model recovery：模型恢复；closed loop：闭环 |
| 代表工具 | MoSeq；Keypoint-MoSeq；PyMC；定制RL/HMM |
| 前提、QC与证据边界 | 参数可不可辨识需验证；模型拟合好不代表动物实现了同一算法 |
| 代表来源与延伸阅读 | [dlc](../../references/index.md#dlc) · [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) |
