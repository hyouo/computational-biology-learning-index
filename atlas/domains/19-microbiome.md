# 19 微生物组与环境组学

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m143"></a>
## M143 标记基因扩增子：16S/18S/ITS等

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 比较细菌/真核/真菌等群落组成 |
| 基本原理 | 用分类标记区序列近似表示样本群落 |
| 输入数据 / 上游实验 | 扩增子FASTQ、引物区、阴性对照、样本元数据 |
| 核心处理 | 去引物；去噪/ASV；去嵌合；分类；群落统计 |
| 可以得到的结果 | ASV表、分类注释、α/β多样性 |
| 常用术语 | ASV：精确扩增子变体；OTU：聚类单元；chimera：嵌合体 |
| 代表工具 | DADA2；QIIME 2；Cutadapt |
| 前提、QC与证据边界 | 引物与拷贝数偏倚明显；一般不能仅凭16S确定菌株及全部功能 |
| 代表来源与延伸阅读 | [qiime](../../references/index.md#qiime) · [dada](../../references/index.md#dada) |


<a id="m144"></a>
## M144 宏基因组物种与菌株组成

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 描绘更广的微生物物种及部分菌株差异 |
| 基本原理 | 用分类k-mer或标记基因匹配shotgun reads |
| 输入数据 / 上游实验 | shotgun FASTQ；宿主参考；分类数据库与阴性对照 |
| 核心处理 | 宿主去除；分类；丰度校正；物种/菌株比较 |
| 可以得到的结果 | 分类丰度、检测物种及菌株候选 |
| 常用术语 | shotgun：非靶向测序；marker：分类标记；strain：菌株 |
| 代表工具 | Kraken2/Bracken；MetaPhlAn；StrainPhlAn |
| 前提、QC与证据边界 | 数据库遗漏与污染影响检出；相对丰度不代表绝对菌量 |
| 代表来源与延伸阅读 | [metaphlan](../../references/index.md#metaphlan) · [qiime](../../references/index.md#qiime) |


<a id="m145"></a>
## M145 宏基因组组装与MAG分箱

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 重建未培养微生物的基因组 |
| 基本原理 | 将混合reads组装并按组成、覆盖和连锁分到基因组 |
| 输入数据 / 上游实验 | shotgun reads、多样本覆盖、可选长reads |
| 核心处理 | 组装；binning；去冗余；完整性/污染/分类评估 |
| 可以得到的结果 | MAG、基因目录、代谢潜力 |
| 常用术语 | MAG：宏基因组组装基因组；bin：分箱；completeness：完整性 |
| 代表工具 | MEGAHIT；metaSPAdes；MetaBAT2；CONCOCT；CheckM2；GTDB-Tk |
| 前提、QC与证据边界 | 高完整性不等于无混合；菌株异质性会导致嵌合和丢失 |
| 代表来源与延伸阅读 | [metaphlan](../../references/index.md#metaphlan) · [hifiasm](../../references/index.md#hifiasm) · [qiime](../../references/index.md#qiime) |


<a id="m146"></a>
## M146 微生物功能谱与代谢潜力

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 比较群落潜在功能与贡献物种 |
| 基本原理 | 把reads/基因映射至酶、基因家族和通路 |
| 输入数据 / 上游实验 | 宏基因组reads或MAG基因、功能数据库 |
| 核心处理 | 同源/家族注释；长度丰度校正；通路重建 |
| 可以得到的结果 | 基因家族、通路丰度及物种分层贡献 |
| 常用术语 | functional potential：功能潜力；KO/EC：功能/酶编号 |
| 代表工具 | HUMAnN；eggNOG-mapper；DRAM；METABOLIC |
| 前提、QC与证据边界 | DNA存在说明潜力，不等于表达或通量；预测功能受数据库覆盖限制 |
| 代表来源与延伸阅读 | [metaphlan](../../references/index.md#metaphlan) · [cobra](../../references/index.md#cobra) · [gsea](../../references/index.md#gsea) |


<a id="m147"></a>
## M147 宏转录组与宏蛋白组

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 更接近群落当时表达活动 |
| 基本原理 | 在混合群落中测定RNA或蛋白并分配物种/功能 |
| 输入数据 / 上游实验 | 混合RNA-seq或MS谱；匹配DNA/蛋白数据库 |
| 核心处理 | 去rRNA/宿主；分类+功能定量；共享肽处理；跨组整合 |
| 可以得到的结果 | 活跃基因/蛋白、物种贡献、表达变化 |
| 常用术语 | metatranscriptome：宏转录组；metaproteome：宏蛋白组 |
| 代表工具 | HUMAnN；RNAseq流程；MetaLab；MSFragger |
| 前提、QC与证据边界 | 表达不等于代谢速率；共享序列/肽使物种归属模糊 |
| 代表来源与延伸阅读 | [rnaseq](../../references/index.md#rnaseq) · [maxquant](../../references/index.md#maxquant) · [metaphlan](../../references/index.md#metaphlan) |


<a id="m148"></a>
## M148 微生物差异丰度与生态网络

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 识别条件相关物种及群落关联结构 |
| 基本原理 | 用组成性或计数模型比较菌群并推断共变 |
| 输入数据 / 上游实验 | 物种/ASV counts、个体、环境及批次 |
| 核心处理 | 污染/低丰度QC；组成模型；多重校正；稳健网络 |
| 可以得到的结果 | 差异丰度、效应及共变边 |
| 常用术语 | α/β diversity：样本内/间多样性；CLR：中心对数比；sparsity：稀疏性 |
| 代表工具 | ANCOM-BC；ALDEx2；MaAsLin；SPIEC-EASI；vegan |
| 前提、QC与证据边界 | 相关网络不等于互作；菌群比例变化和阴性对照需充分解释 |
| 代表来源与延伸阅读 | [qiime](../../references/index.md#qiime) · [vegan](../../references/index.md#vegan) · [metaphlan](../../references/index.md#metaphlan) |


<a id="m149"></a>
## M149 病毒组、移动元件与耐药基因注释

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 描述生态组成及功能基因分布 |
| 基本原理 | 从混合序列识别病毒、质粒或已知功能基因家族 |
| 输入数据 / 上游实验 | 宏基因组contig/reads、分类与功能参考库 |
| 核心处理 | 序列QC；分类/同源注释；宿主候选关联；覆盖验证 |
| 可以得到的结果 | 病毒/质粒候选、基因家族和宿主关联假设 |
| 常用术语 | virome：病毒组；MGE：移动遗传元件；AMR：抗微生物耐药 |
| 代表工具 | VirSorter2；CheckV；geNomad；CARD相关注释流程 |
| 前提、QC与证据边界 | 基因同源注释不等于已证实表型；宿主预测是推断，污染要排除 |
| 代表来源与延伸阅读 | [metaphlan](../../references/index.md#metaphlan) · [hifiasm](../../references/index.md#hifiasm) · [meme](../../references/index.md#meme) |


<a id="m150"></a>
## M150 群落代谢建模与宿主—微生物整合

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 提出营养互作与生态功能假设 |
| 基本原理 | 连接物种网络、交换代谢物和宿主分子表型 |
| 输入数据 / 上游实验 | 物种丰度、MAG代谢网络、培养基、宿主组学 |
| 核心处理 | 群落FBA；交换约束；纵向/多组整合；敏感性分析 |
| 可以得到的结果 | 交叉喂养候选、代谢交换、群落响应预测 |
| 常用术语 | cross-feeding：交叉喂养；community model：群落模型 |
| 代表工具 | MICOM；COBRApy；MOFA；定制动力学 |
| 前提、QC与证据边界 | 推断交换不是实测分泌；培养/同位素/干预证据可区分竞争解释 |
| 代表来源与延伸阅读 | [cobra](../../references/index.md#cobra) · [mofa](../../references/index.md#mofa) · [vegan](../../references/index.md#vegan) |
