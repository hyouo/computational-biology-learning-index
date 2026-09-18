# 25 定量发育与合成生物学

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m189"></a>
## M189 形态发生与发育图谱量化

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究组织形成、分化与形态变化 |
| 基本原理 | 对齐发育时间与组织几何，联合细胞状态和运动 |
| 输入数据 / 上游实验 | 胚胎/类器官时序图像、空间或单细胞数据 |
| 核心处理 | 时空配准；分割追踪；形状/谱系；动态模型 |
| 可以得到的结果 | 发育图谱、细胞运动和形态转换规律 |
| 常用术语 | morphogenesis：形态发生；developmental stage：发育阶段；fate map：命运图 |
| 代表工具 | Fiji；CellProfiler；追踪工具；空间/轨迹模型 |
| 前提、QC与证据边界 | 不同个体阶段不同步；拟时序、真实年龄和谱系不可混为一谈 |
| 代表来源与延伸阅读 | [cellprof](../../references/index.md#cellprof) · [cellrank](../../references/index.md#cellrank) · [squidpy](../../references/index.md#squidpy) |


<a id="m190"></a>
## M190 单分子生物物理与状态切换

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 研究折叠、结合、转运及过程性 |
| 基本原理 | 从离散事件或连续轨迹推断分子的状态和转换 |
| 输入数据 / 上游实验 | 单分子FRET、力谱、荧光轨迹与标定 |
| 核心处理 | 去噪；HMM/change-point；驻留分布；动力学模型 |
| 可以得到的结果 | 状态、转换率、步长、等待时间分布 |
| 常用术语 | dwell time：驻留时间；processivity：过程性；change point：变化点 |
| 代表工具 | hmmlearn；专用单分子工具；自定义模型 |
| 前提、QC与证据边界 | 光物理闪烁可能被误当构象切换；时间分辨率限制快过程 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) · [md](../../references/index.md#md) |


<a id="m191"></a>
## M191 细胞周期、增殖与死亡动力学

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 区分增殖变慢、死亡增加和周期阻滞 |
| 基本原理 | 结合标记、DNA含量、计数和时间模型分解群体变化 |
| 输入数据 / 上游实验 | EdU/BrdU、DNA染色、Annexin/活死、活细胞计数或谱系 |
| 核心处理 | gating/图像；周期分布；增长/死亡模型；重复统计 |
| 可以得到的结果 | 周期比例、分裂/死亡率、时间依赖变化 |
| 常用术语 | EdU：核苷类似物掺入；doubling time：倍增时间；apoptosis：凋亡 |
| 代表工具 | FlowKit；CellProfiler；COPASI；统计模型 |
| 前提、QC与证据边界 | 代谢活性读数不等于活细胞数；单点周期比例不是进入/离开速率 |
| 代表来源与延伸阅读 | [flow](../../references/index.md#flow) · [cellprof](../../references/index.md#cellprof) · [copasi](../../references/index.md#copasi) |


<a id="m192"></a>
## M192 合成基因线路建模与表征

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 理解逻辑、开关、振荡与宿主负担 |
| 基本原理 | 用调控元件及反馈构建输入—输出和动态模型 |
| 输入数据 / 上游实验 | 启动子/调控元件表征、时间荧光、宿主生长 |
| 核心处理 | 动力学/随机模拟；参数拟合；负担和稳健性分析 |
| 可以得到的结果 | 传递函数、动态曲线、噪声和设计候选 |
| 常用术语 | transfer function：传递函数；bistability：双稳态；burden：负担 |
| 代表工具 | COPASI；Tellurium；SBOL相关工具；定制模型 |
| 前提、QC与证据边界 | 元件在新宿主/拷贝数中不一定模块化；模型需实测校准 |
| 代表来源与延伸阅读 | [copasi](../../references/index.md#copasi) · [addgene](../../references/index.md#addgene) |


<a id="m193"></a>
## M193 代谢工程、酶约束与路径设计

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 寻找提升目标产物或理解产率限制的候选改造 |
| 基本原理 | 将代谢网络、酶容量和资源成本纳入设计 |
| 输入数据 / 上游实验 | 宿主代谢模型、酶参数、蛋白组、交换通量 |
| 核心处理 | FBA/酶约束；knockout/调节情景；稳健性/权衡 |
| 可以得到的结果 | 产率边界、限制步骤、候选路径或调节方案 |
| 常用术语 | enzyme-constrained：酶约束；yield：产率；trade-off：权衡 |
| 代表工具 | COBRApy；GECKO；OptKnock类方法 |
| 前提、QC与证据边界 | 模型可行不保证宿主能实现；酶参数、毒性、调控和负担需验证 |
| 代表来源与延伸阅读 | [cobra](../../references/index.md#cobra) · [copasi](../../references/index.md#copasi) · [msstats](../../references/index.md#msstats) |


<a id="m194"></a>
## M194 设计—构建—测试—学习闭环

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 前沿选读 |
| 处理目的 | 提高蛋白、线路或细胞系统的可预测性 |
| 基本原理 | 把实验结果反馈给下一轮计算设计 |
| 输入数据 / 上游实验 | 候选设计、标准化实验、效应与失败记录 |
| 核心处理 | 批次设计；测量QC；模型更新；主动学习；独立复验 |
| 可以得到的结果 | 迭代候选、学习曲线、可追溯成功/失败证据 |
| 常用术语 | DBTL：设计构建测试学习；design space：设计空间；reproducibility：可复现性 |
| 代表工具 | 工作流/LIMS；贝叶斯优化；领域预测与设计工具 |
| 前提、QC与证据边界 | 不能只保留成功结果；实验批次泄漏和选择偏倚会虚增模型能力 |
| 代表来源与延伸阅读 | [rfdiff](../../references/index.md#rfdiff) · [copasi](../../references/index.md#copasi) · [sklearn](../../references/index.md#sklearn) · [nf](../../references/index.md#nf) |
