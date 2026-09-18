# 22 生物物理与数学建模

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m167"></a>
## M167 反应动力学与常微分方程ODE

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 解释信号反馈、振荡及剂量时间响应 |
| 基本原理 | 用反应速率方程描述分子浓度随时间变化 |
| 输入数据 / 上游实验 | 反应网络、速率式、时间浓度或活性测量 |
| 核心处理 | ODE求解；参数拟合；残差；独立条件预测 |
| 可以得到的结果 | 动力学曲线、参数区间、反馈机制候选 |
| 常用术语 | ODE：常微分方程；rate constant：速率常数；feedback：反馈 |
| 代表工具 | COPASI；Tellurium；deSolve；AMICI |
| 前提、QC与证据边界 | 不同参数组合可同样拟合；拟合不是机制唯一性证明 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) |


<a id="m168"></a>
## M168 随机反应、噪声与单细胞波动

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究表达噪声、开关和罕见事件 |
| 基本原理 | 以概率反应事件而非连续均值模拟低拷贝体系 |
| 输入数据 / 上游实验 | 反应网络、分子数、单细胞/单分子时序 |
| 核心处理 | SSA/Gillespie；master equation近似；参数推断 |
| 可以得到的结果 | 分布、波动、切换等待时间和罕见事件概率 |
| 常用术语 | SSA：随机模拟算法；burst：爆发；intrinsic/extrinsic noise：内/外源噪声 |
| 代表工具 | COPASI；GillesPy2；StochPy |
| 前提、QC与证据边界 | 技术噪声与生物噪声需区分；平均值正确不保证分布正确 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) |


<a id="m169"></a>
## M169 反应—扩散、偏微分方程与图案形成

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究形态发生、信号梯度和组织图案 |
| 基本原理 | 联合局部反应和空间运输描述浓度场 |
| 输入数据 / 上游实验 | 空间几何、扩散/反应参数、时空图像 |
| 核心处理 | PDE求解；边界条件；稳定性/分岔；与图像比较 |
| 可以得到的结果 | 时空浓度场、波/图案、参数范围 |
| 常用术语 | PDE：偏微分方程；Turing pattern：图灵图案；boundary condition：边界条件 |
| 代表工具 | FEniCS；COMSOL；FiPy；Morpheus |
| 前提、QC与证据边界 | 边界和几何假设可决定图案；外观相似不足以证明同一机制 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [cellprof](../../references/index.md#cellprof) · [stats](../../references/index.md#stats) |


<a id="m170"></a>
## M170 个体/细胞代理与组织力学模型

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究集体行为、组织形成与力学反馈 |
| 基本原理 | 让每个细胞按规则运动、分裂并相互作用 |
| 输入数据 / 上游实验 | 细胞规则、初始组织、力学/成像参数 |
| 核心处理 | agent-based/vertex/有限元；参数拟合；干预模拟 |
| 可以得到的结果 | 细胞轨迹、组织形态、应力/力学响应 |
| 常用术语 | ABM：基于个体模型；vertex model：顶点模型；FEM：有限元 |
| 代表工具 | PhysiCell；Chaste；Morpheus；SOFA |
| 前提、QC与证据边界 | 规则可能非唯一；组织宏观拟合不保证微观机制真实 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [cellpose](../../references/index.md#cellpose) · [stats](../../references/index.md#stats) |


<a id="m171"></a>
## M171 力谱、单分子轨迹与机械参数反演

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究结合断裂、分子马达和细胞材料性质 |
| 基本原理 | 从位移、力和响应曲线推断分子/组织力学参数 |
| 输入数据 / 上游实验 | AFM/光镊/磁镊力位移曲线、标定和几何 |
| 核心处理 | 基线/漂移；力学/动力学拟合；不确定性评估 |
| 可以得到的结果 | 弹性模量、刚度、断裂力、步进/驻留参数 |
| 常用术语 | AFM：原子力显微镜；optical tweezers：光镊；loading rate：加载速率 |
| 代表工具 | 仪器软件；自定义Python/R；力学模拟 |
| 前提、QC与证据边界 | 标定、接触模型和加载速率影响参数；断裂力不直接等于Kd |
| 代表来源与延伸阅读 | [stats](../../references/index.md#stats) · [copasi](../../references/index.md#copasi) · [md](../../references/index.md#md) |


<a id="m172"></a>
## M172 可辨识性、灵敏度与模型选择

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 共同基础 |
| 处理目的 | 避免过度解释漂亮拟合 |
| 基本原理 | 检验数据能否区分参数和竞争机制 |
| 输入数据 / 上游实验 | 候选模型、参数、噪声模型、观测数据 |
| 核心处理 | profile likelihood；全局/局部灵敏度；模型恢复；后验预测 |
| 可以得到的结果 | 可识别参数、最重要因素、竞争模型支持 |
| 常用术语 | identifiability：可辨识性；sensitivity：灵敏度；posterior predictive：后验预测 |
| 代表工具 | COPASI；PESTO；pyPESTO；PyMC；Stan |
| 前提、QC与证据边界 | 不可辨识参数不应作为精确机制常数；更复杂不自动更好 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) · [sklearn](../../references/index.md#sklearn) |


<a id="m173"></a>
## M173 信息论、网络科学与复杂系统

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 比较信息编码、网络模块和稳健性 |
| 基本原理 | 用熵、互信息和图拓扑概括依赖及组织结构 |
| 输入数据 / 上游实验 | 离散/连续变量、时间序列、结构或关联网络 |
| 核心处理 | 熵/MI估计；中心性/社区；零模型；稳健性分析 |
| 可以得到的结果 | 信息量、网络模块、连接/鲁棒性指标 |
| 常用术语 | MI：互信息；entropy：熵；centrality：中心性 |
| 代表工具 | NetworkX；igraph；信息论估计工具 |
| 前提、QC与证据边界 | 有限样本/离散化会偏置MI；网络中心性不是因果重要性的自动证据 |
| 代表来源与延伸阅读 | [stats](../../references/index.md#stats) · [microns](../../references/index.md#microns) · [scenic](../../references/index.md#scenic) |


<a id="m174"></a>
## M174 参数反演、实验设计与主动学习

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 用有限实验预算加快机制辨识和设计优化 |
| 基本原理 | 选择最能区分假设或减少预测不确定性的下一实验 |
| 输入数据 / 上游实验 | 候选参数/模型、已有实验、成本和可行范围 |
| 核心处理 | 贝叶斯优化；信息增益；设计模拟；迭代测量 |
| 可以得到的结果 | 推荐实验条件、候选排序、预期信息增益 |
| 常用术语 | active learning：主动学习；Bayesian optimization：贝叶斯优化；acquisition：采集函数 |
| 代表工具 | BoTorch；Ax；Optuna；PyMC；COPASI |
| 前提、QC与证据边界 | 推荐依赖模型与搜索空间；需保留探索和实验可行性限制 |
| 代表来源与延伸阅读 | [sklearn](../../references/index.md#sklearn) · [copasi](../../references/index.md#copasi) · [rfdiff](../../references/index.md#rfdiff) |
