# 细胞身份、状态、空间、时间与扰动

[知识导航](../atlas/index.md) · [分子调控](molecular-regulation.md) · [技术关系](technique-relations.md)

## 1. 一个细胞不等于一个RNA向量

细胞具有序列、RNA、蛋白、染色质、代谢、形态和位置等多种属性。scRNA-seq观察其中RNA相关的一部分；单细胞ATAC观察可及性相关的一部分；多组共测尝试把同一细胞的不同测量连接起来。不同模态共同构成对状态的约束，但不会因为被整合到一个低维坐标中就变成完整的“细胞状态真值”。[WNN](../references/index.md#wnn)、[scvi-tools](../references/index.md#scvi)

“细胞类型”通常用于相对稳定、可重复的身份划分；“状态”描述条件、周期、刺激等相关变化。二者的边界依研究目的和证据而定。聚类只是从当前表示和相似性定义获得分组，注释还需要标记、参考和独立信息。[Scanpy](../references/index.md#scanpy)、[空间脑图谱](../references/nature-papers.md#n04)

## 2. 单细胞数据怎样生成？

条码把分子信号归属到捕获单位，UMI辅助区分原始分子与扩增副本；随后识别有效细胞、建立特征矩阵。空液滴、环境RNA、多个细胞进入同一捕获单位，以及低质量细胞会产生不同类型的混合或噪声。单核数据与完整细胞数据的可观察RNA范围也不同，因此质量判断应依据具体实验。[单细胞条目](../atlas/domains/07-single-cell.md)、[Scanpy](../references/index.md#scanpy)

处理通常包含归一化、特征选择、表示学习和邻接图，再进行聚类或参考映射。UMAP是表示的可视化，不是细胞的真实空间位置；用于整合的表征也不必是统计检验应使用的表达层。[Scanpy](../references/index.md#scanpy)、[scvi-tools](../references/index.md#scvi)

## 3. 身份、状态与组成对应三个分析问题

| 问题 | 需要比较的对象 | 典型结果 |
| --- | --- | --- |
| 样本中有哪些细胞？ | 细胞特征及参考定义 | 类型标签、未确定群体、标记 |
| 同一类细胞是否改变？ | 多个独立样本中对应类型的表达或其他读出 | 类型特异差异状态 |
| 各类细胞的构成是否改变？ | 每个独立样本的细胞数量或组成 | 类型/邻域丰度变化 |

pseudobulk的思想是按个体和细胞类型汇总，再在样本层比较。它不是把所有细胞混成一个无重复样本，也不是声称细胞内异质性不重要。[muscat](../references/index.md#muscat)

理解bulk信号时，可用简化混合关系B_g=sum_k w_k E_gk。E_gk表示各群体的表达，w_k表示其对总体信号的有效贡献。w_k不一定等于细胞数量比例，因为细胞RNA产量和捕获效率也会改变贡献。这个模型解释了为什么总体表达变化既可能来自类型内变化，也可能来自组成变化；解卷积是在参考和模型假设下估计这种混合。[Cell2location](../references/index.md#cell2loc)

## 4. 多组学整合究竟连接了什么？

**同细胞配对**有明确的模态对应；**不同细胞/不同切片**需要通过共同特征、参考或统计假设建立对应。联合嵌入回答共享结构的问题，补全回答未观测模态的预测问题，调控网络回答候选机制关系的问题。三者不等价。[MOFA](../references/index.md#mofa)、[WNN](../references/index.md#wnn)、[SCENIC+](../references/nature-papers.md#n03)

如果某基因没有在空间panel中测量，模型给出的值应称为预测或补全，而不是该细胞的新实测值。Nicheformer的空间语境迁移同样属于模型信息迁移。[N12](../references/nature-papers.md#n12)

## 5. 空间技术不是一类统一的数据

| 技术/任务 | 输入与基本机制 | 主要产物 | 必须保留的含义 |
| --- | --- | --- | --- |
| 捕获式空间RNA | 空间条码及测序 | 位置×基因矩阵 | 捕获单位可能混合多个细胞 |
| 成像式空间RNA | 多轮探针/原位读取图像 | 分子坐标、细胞归属 | 依赖探针集合、检测与分割 |
| 空间蛋白测量 | 多重抗体成像或空间取样MS | 位置与蛋白信号 | panel与非靶向MS覆盖并不相同 |
| 解卷积与映射 | 空间数据+细胞参考 | 类型丰度或映射概率 | 是参考约束下的估计 |
| 空间域与邻域 | 坐标、图和分子特征 | 区域、梯度、共现 | 需定义尺度和空间零模型 |
| 跨切片配准 | 图像、地标及组织几何 | 对应坐标与变换 | 变换误差影响距离和对应 |

空间脑图谱展示了成像、参考映射和解剖配准的组合；Deep Visual Proteomics展示了图像定义对象后进行空间取样质谱的另一条路径。[N04](../references/nature-papers.md#n04)、[DVP](../references/index.md#dvp)

分割掩膜决定“这个分子属于哪个细胞”和“这个细胞有多大”，因此会影响空间表达和邻域结果。图像算法提供对象边界，但对象是否对应实际生物实体仍需检查。[CellSAM](../references/nature-papers.md#n13)

## 6. 细胞间通信：从兼容性到响应

配体—受体分析通常把发送端与接收端的分子读出和已知相互作用集合结合，寻找候选通信。空间信息缩小哪些细胞可能接触或受到局部影响；下游信号与转录响应再增加功能方面的约束。[LIANA+](../references/nature-papers.md#n09)

这类分析需要区分四件事：分子是否存在、是否到达接收端、是否激活相关过程、改变该过程是否改变表型。只观测到表达与邻近时，合适的表述是“候选关系”；不同方向的独立读出才帮助排除共同环境或细胞组成等解释。[CellChat](../references/index.md#cellchat)、[N04](../references/nature-papers.md#n04)

## 7. 时间、方向与谱系是不同信息

| 方法 | 从什么约束推断什么 | 分析意义 |
| --- | --- | --- |
| 拟时序 | 状态相似性及图结构 → 相对顺序 | 组织连续变化，不直接给出真实时钟 |
| RNA velocity | 已/未剪接等动态信息 → 局部变化方向 | 在动力学假设下增加方向约束 |
| 命运概率 | 状态转移模型 → 终末状态趋向 | 量化模型中的可能结局 |
| 多时间点/最优传输 | 各时间点分布 → 群体耦合 | 利用采样时间，而非唯一追踪每个细胞 |
| 谱系记录 | 可遗传标记或编辑记录 → 共同来源 | 区分状态相似与祖先相同 |
| 活细胞追踪 | 连续图像 → 对象轨迹与分裂 | 提供实际时间观察，仍有匹配误差 |

RNA velocity与CellRank说明方向和命运建模的关系，但命运概率不是已经观察到的后代身份。[velocity](../references/index.md#velocity)、[N08](../references/nature-papers.md#n08)；其他方法见[动态与谱系条目](../atlas/domains/08-dynamics-lineage.md)。

## 8. 扰动怎样改变证据的性质？

pooled CRISPR筛选通过guide丰度变化寻找与选择表型有关的候选；Perturb-seq把扰动身份与单细胞转录状态联系起来；光学筛选连接形态；Perturb-tracing连接三维染色质。区别在于干预后的读出是什么，而不只是“都做了CRISPR”。[MAGeCK](../references/index.md#mageck)、[scPerturb](../references/index.md#scperturb)、[N10](../references/nature-papers.md#n10)

干预提供的证据仍具有条件性：实际改变是否成立，细胞是否因存活筛选而重新组成，观察到的是直接作用还是下游反应，都影响解释。回补、组合干预、独立读出和不同时间点可以针对不同替代解释增加信息，不应机械堆叠。[实验读出](../experiments/index.md)、[扰动方法](../atlas/domains/11-perturbation.md)

## 9. 对免疫、肿瘤与发育意味着什么？

免疫受体序列把克隆身份与细胞状态连接起来，但克隆相似不直接等于同一抗原特异性；肿瘤变异连接遗传克隆与状态，但需要纯度和拷贝数等信息；发育中的状态轨迹与真实谱系也可能分离。这些问题都要求同时区分“是什么”“处于什么状态”“从哪里来”。[Scirpy](../references/index.md#scirpy)、[Immcantation](../references/index.md#immcant)、[免疫与肿瘤](../atlas/domains/12-immunity-cancer.md)、[定量发育](../atlas/domains/25-development-synthetic-biology.md)
