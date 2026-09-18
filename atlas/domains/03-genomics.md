# 03 基因组与变异

[返回领域导航](../index.md) · [学习方式](../../docs/learning-guide.md)

以下为方法家族的初始学习卡片；代表工具不是排名，模型输出需结合适用假设和实验设计解读。

<a id="m019"></a>
## M019 短读长生殖系变异检测

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 寻找遗传SNV/Indel |
| 基本原理 | 从参考比对及局部组装推断个体基因型 |
| 输入数据 / 上游实验 | WGS/WES/靶向FASTQ；参考；样本及家系信息 |
| 核心处理 | 比对QC；variant calling；联合分型；过滤与注释 |
| 可以得到的结果 | VCF、基因型、质量及功能注释 |
| 常用术语 | SNV：单碱基变异；Indel：插缺；GQ：基因型质量 |
| 代表工具 | GATK；DeepVariant；BCFtools；nf-core/sarek |
| 前提、QC与证据边界 | 覆盖不足、参考偏倚、重复区和伪基因可漏检或误检 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [hts](../../references/index.md#hts) |


<a id="m020"></a>
## M020 体细胞变异与低频变异

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究肿瘤或嵌合突变 |
| 基本原理 | 区分肿瘤/特定组织新生变异和背景错误、遗传变异 |
| 输入数据 / 上游实验 | 肿瘤/正常配对reads；panel of normals；可选UMI |
| 核心处理 | 污染评估；体细胞calling；过滤；纯度与拷贝数联合解释 |
| 可以得到的结果 | 体细胞SNV/Indel及VAF、候选克隆信息 |
| 常用术语 | VAF：变异等位基因比例；PoN：正常背景库 |
| 代表工具 | Mutect2；Strelka；nf-core/sarek |
| 前提、QC与证据边界 | VAF不等于携带突变细胞比例；肿瘤纯度及CNV会改变它 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) |


<a id="m021"></a>
## M021 结构变异与拷贝数变异

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 检测缺失、重复、倒位、易位和复杂重排 |
| 基本原理 | 联合读深、断裂比对、成对距离和组装发现重排 |
| 输入数据 / 上游实验 | 短/长reads BAM；可选光学图谱和肿瘤正常对照 |
| 核心处理 | SV calling；CNV分段；合并验证；断点注释 |
| 可以得到的结果 | SV/CNV表、片段拷贝数、断点及图谱 |
| 常用术语 | SV：结构变异；CNV：拷贝数变异；BAF：B等位频率 |
| 代表工具 | Manta；Sniffles；CNVkit；GATK CNV |
| 前提、QC与证据边界 | 不同证据擅长不同尺寸；覆盖、倍性和纯度影响CNV推断 |
| 代表来源与延伸阅读 | [sarek](../../references/index.md#sarek) · [pangenome](../../references/index.md#pangenome) |


<a id="m022"></a>
## M022 单倍型分相与家系分析

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 区分cis/trans及遗传来源 |
| 基本原理 | 依据共现reads、群体LD或父母信息归属同一染色体 |
| 输入数据 / 上游实验 | 杂合VCF、长reads、亲子基因型 |
| 核心处理 | read-based/statistical phasing；孟德尔一致性检查 |
| 可以得到的结果 | 单倍型块、亲本来源、复合杂合候选 |
| 常用术语 | phasing：分相；phase block：单倍型块；cis/trans：同/异染色体 |
| 代表工具 | WhatsHap；SHAPEIT；Beagle |
| 前提、QC与证据边界 | 统计分相有switch error；罕见变异与复杂区域需额外证据 |
| 代表来源与延伸阅读 | [hifiasm](../../references/index.md#hifiasm) · [plink](../../references/index.md#plink) · [hts](../../references/index.md#hts) |


<a id="m023"></a>
## M023 从头组装与单倍型组装

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 研究非模式生物、复杂重复及参考遗漏序列 |
| 基本原理 | 将重叠reads或k-mer图拼成连续基因组 |
| 输入数据 / 上游实验 | HiFi/ONT/短reads；可选Hi-C和亲本reads |
| 核心处理 | 组装；去冗余/分相；scaffold；污染及完整性评估 |
| 可以得到的结果 | contig/scaffold、单倍型组装、组装图 |
| 常用术语 | N50：长度统计；BUSCO：保守基因完整性；QV：错误率质量 |
| 代表工具 | hifiasm；Flye；SPAdes；QUAST；BUSCO |
| 前提、QC与证据边界 | N50高不等于正确或完整；需检查misassembly和单倍型混杂 |
| 代表来源与延伸阅读 | [hifiasm](../../references/index.md#hifiasm) · [pangenome](../../references/index.md#pangenome) |


<a id="m024"></a>
## M024 泛基因组与图参考比对

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 减少单参考偏倚并发现复杂变异 |
| 基本原理 | 用多个单倍型路径表达群体序列多样性 |
| 输入数据 / 上游实验 | 多个高质量组装、变异或图参考及reads |
| 核心处理 | 图构建；图比对；路径/变异提取；评估偏倚 |
| 可以得到的结果 | 泛基因组图、复杂位点基因型、核心/可变序列 |
| 常用术语 | pangenome：泛基因组；path：图路径；reference bias：参考偏倚 |
| 代表工具 | Minigraph-Cactus；vg；minigraph |
| 前提、QC与证据边界 | 图复杂度、样本代表性和坐标体系仍影响解释 |
| 代表来源与延伸阅读 | [pangenome](../../references/index.md#pangenome) |


<a id="m025"></a>
## M025 基因预测与功能注释

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 方向核心 |
| 处理目的 | 把组装转成可解释的基因集 |
| 基本原理 | 综合ORF、同源、转录证据和结构域识别基因及功能 |
| 输入数据 / 上游实验 | 基因组FASTA；RNA/protein证据；功能数据库 |
| 核心处理 | 重复掩蔽；基因模型；结构域/同源注释；人工检查 |
| 可以得到的结果 | GFF/GTF、蛋白序列、候选功能及证据等级 |
| 常用术语 | ORF：开放阅读框；ortholog：直系同源；domain：结构域 |
| 代表工具 | BRAKER；MAKER；InterProScan；eggNOG-mapper |
| 前提、QC与证据边界 | 同源注释是推断；基因模型可能融合、断裂或遗漏 |
| 代表来源与延伸阅读 | [hifiasm](../../references/index.md#hifiasm) · [pangenome](../../references/index.md#pangenome) · [iqtree](../../references/index.md#iqtree) |


<a id="m026"></a>
## M026 重复序列、转座子与串联重复

| 项目 | 内容 |
| --- | --- |
| 学习层级 | 进阶专题 |
| 处理目的 | 分析基因组塑性、转座活性及重复扩增 |
| 基本原理 | 对重复家族或长度变化单独建模 |
| 输入数据 / 上游实验 | 基因组、DNA/RNA reads、重复注释 |
| 核心处理 | repeat annotation；多重比对建模；STR长度估计 |
| 可以得到的结果 | 重复图谱、家族表达、长度基因型 |
| 常用术语 | TE：转座元件；STR：短串联重复；LTR：长末端重复 |
| 代表工具 | RepeatMasker；EDTA；TEtranscripts；ExpansionHunter |
| 前提、QC与证据边界 | 家族表达不等于特定位点转座；短reads对长重复有限 |
| 代表来源与延伸阅读 | [pangenome](../../references/index.md#pangenome) · [sarek](../../references/index.md#sarek) · [rnaseq](../../references/index.md#rnaseq) |
