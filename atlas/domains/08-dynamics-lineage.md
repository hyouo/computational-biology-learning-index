# 08 细胞动态与谱系

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m063"></a>
## M063 拟时序与轨迹分支

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 提出分化、激活和状态转换假设 |
| 基本原理 | 在表达/表观流形上构建连续路径并相对排序 |
| 输入数据 / 上游实验 | 单细胞矩阵或潜变量；根/时间等先验 |
| 核心处理 | 图学习；根选择；分支与平滑基因趋势 |
| 可以得到的结果 | pseudotime、分支、动态基因 |
| 常用术语 | pseudotime：相对状态次序；trajectory：轨迹 |
| 代表工具 | Monocle；Slingshot；PAGA；tradeSeq |
| 前提、QC与证据边界 | 不是实际时间，也不是谱系；根、缺失状态和采样密度可改变轨迹 |
| 代表来源与延伸阅读 | [cellrank](../../references/index.md#cellrank) · [scanpy](../../references/index.md#scanpy) |


<a id="m064"></a>
## M064 RNA velocity

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 补充状态转换方向信息 |
| 基本原理 | 用未剪接/已剪接RNA及动力学模型估计局部变化方向 |
| 输入数据 / 上游实验 | spliced/unspliced counts；单细胞状态 |
| 核心处理 | 动力学拟合；velocity估计；高维图投影和置信度评估 |
| 可以得到的结果 | 局部向量、方向一致性、动力学候选基因 |
| 常用术语 | spliced/unspliced：已/未剪接；latent time：模型潜在时间 |
| 代表工具 | velocyto；scVelo |
| 前提、QC与证据边界 | 依赖转录/剪接/降解假设；二维箭头不是直接追踪到的细胞迁移 |
| 代表来源与延伸阅读 | [velocity](../../references/index.md#velocity) · [cellrank](../../references/index.md#cellrank) |


<a id="m065"></a>
## M065 命运概率与细胞状态转移

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 量化趋向各终末状态的模型概率 |
| 基本原理 | 将邻居关系和方向信息构成随机转移过程 |
| 输入数据 / 上游实验 | 邻居图；velocity、时间或其他方向信息 |
| 核心处理 | Markov转移；宏状态；吸收概率；驱动基因相关 |
| 可以得到的结果 | 初始/终末状态、命运概率、候选驱动因子 |
| 常用术语 | transition matrix：转移矩阵；absorption：吸收；fate probability：命运概率 |
| 代表工具 | CellRank |
| 前提、QC与证据边界 | 模型命运概率不是同一细胞实际未来频率的直接测量 |
| 代表来源与延伸阅读 | [cellrank](../../references/index.md#cellrank) |


<a id="m066"></a>
## M066 时间序列与最优传输

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 重建群体迁移、分化及增殖过程 |
| 基本原理 | 在不同时间群体之间寻找代价较小的分布对应 |
| 输入数据 / 上游实验 | 多时间点单细胞；可选生长率/标签 |
| 核心处理 | 距离/成本定义；OT耦合；动态和灵敏度分析 |
| 可以得到的结果 | 时间间状态对应、质量流、候选祖先后代关系 |
| 常用术语 | OT：最优传输；coupling：耦合矩阵；mass：分布质量 |
| 代表工具 | Waddington-OT；moscot；POT |
| 前提、QC与证据边界 | 采样时间不等于单细胞纵向追踪；成本、生长和死亡假设关键 |
| 代表来源与延伸阅读 | [cellrank](../../references/index.md#cellrank) · [mofa](../../references/index.md#mofa) |


<a id="m067"></a>
## M067 条形码谱系追踪与克隆重建

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 追踪来源、克隆扩增与命运限制 |
| 基本原理 | 以可遗传条码、突变记录或内源变异标记共同祖先 |
| 输入数据 / 上游实验 | 条码/记录位点序列；细胞表达；时间信息 |
| 核心处理 | 纠错；条码分组；树推断；映射细胞状态 |
| 可以得到的结果 | 克隆谱系树、克隆大小、跨状态后代分布 |
| 常用术语 | lineage：谱系；barcode collision：条码碰撞；homoplasy：同形变异 |
| 代表工具 | Cassiopeia；LineageOT；定制分析 |
| 前提、QC与证据边界 | 条码丢失、碰撞和记录饱和会误导；真实谱系仍含重建不确定性 |
| 代表来源与延伸阅读 | [cellrank](../../references/index.md#cellrank) · [scperturb](../../references/index.md#scperturb) |


<a id="m068"></a>
## M068 活细胞追踪与状态空间模型

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 直接观察分裂、运动及状态变化 |
| 基本原理 | 跨帧匹配同一细胞并建模隐藏状态 |
| 输入数据 / 上游实验 | 时间序列显微图像；荧光报告信号 |
| 核心处理 | 分割；轨迹关联；分裂检测；HMM/状态空间拟合 |
| 可以得到的结果 | 细胞轨迹、分裂树、驻留时间、转换率 |
| 常用术语 | tracking：追踪；dwell time：驻留时间；state space：状态空间 |
| 代表工具 | TrackMate；btrack；CellProfiler；自定义模型 |
| 前提、QC与证据边界 | 跟踪ID错误会制造假转变；荧光动力学与真实分子变化可能不同 |
| 代表来源与延伸阅读 | [cellpose](../../references/index.md#cellpose) · [copasi](../../references/index.md#copasi) · [stats](../../references/index.md#stats) |
