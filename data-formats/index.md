# 数据格式与数据对象

[知识导航](../atlas/index.md) · [实验怎样产生数据](../docs/instruments-and-data.md) · [矩阵与统计](../docs/statistics-basics.md)

文件后缀提示存储方式，但不完整说明生物学含义。一个表格里的数可能是分子计数、光强、概率或模型得分；同一个格式也可能保存不同处理阶段的数据。先看下面几个小片段，再查后面的28类格式。**本页所有小片段均为教学构造，不是真实实验数据，也不是完整的分析数据集。**

## 1. FASTA与FASTQ：序列和质量

FASTA可以保存一条带名称的序列：

```text
>example_sequence
ACGT
```

以`>`开始的行是标识和可选说明，后面是序列。这里四个字符代表四个DNA碱基；蛋白FASTA使用氨基酸字母，需要看文件所描述的对象。

常见的FASTQ一条记录有四行：

```text
@read01
ACGT
+
IIII
```

第一行标识read，第二行是碱基序列，第三行是分隔行，第四行用字符编码逐碱基质量。第四行不是又一条生物序列；在这种四行表示中，序列和质量字符数应匹配。质量值与后续比对质量不是同一个量。[HTSlib与SAMtools文档](https://www.htslib.org/doc/samtools-fasta.html)

`R1`和`R2`常表示配对读取，但哪一端存条码、哪一端存生物序列取决于实验设计。不能仅凭文件名决定如何解释。

## 2. 计数表要和样本表一起读

```text
gene_id   sample_1   sample_2
gene_A          10         20
gene_B          30         60
```

这一示例是一行一个基因、一列一个样本。`gene_A`只是教学标识，不指实际基因。`20`说明在指定计数定义下该样本记录了20次对应信号，不自动表示组织中恰好有20个RNA分子。

```text
sample_id   subject_id   condition   batch
sample_1    subject_A    control     batch_1
sample_2    subject_B    treated     batch_1
```

第二张表才说明样本来自谁、条件是什么。两张表按`sample_id`对应，而不是凭行顺序拼接。只有两个示例样本不能提供充分的生物重复来支撑一般组间推断；这里仅展示数据结构。[DESeq2输入与设计](../references/index.md#deseq)

**稀疏矩阵**主要保存非零位置和数值，以减少存储；它不意味着零值都是缺失。**转置**交换行列；它不会改变对象本身，但若忘记标签含义，可能把基因当样本。

## 3. 基因组坐标：从0开始和从1开始

假设想记录某条染色体最前面的三个碱基。BED的0-based半开区间示意是：

```text
chr1    0    3
```

它包含起点0，不包含终点3，长度为3−0=3。在1-based闭区间表示中，同样的位置是1到3，长度为3−1+1=3。GTF/GFF通常使用后一种坐标规则，具体字段需按格式定义读取。[UCSC格式说明](https://genome.ucsc.edu/FAQ/FAQformat.html#format1)

因此，BED中的`0 3`与GTF中的`1 3`可以描述同一段位置；相同的数字在不同约定中未必是同一区间。还必须说明参考版本、染色体名称和链方向，不能只看起止数字。

## 4. AnnData/H5AD：一个对象里有多种数据层

AnnData不仅保存矩阵，还保存与行列对应的注释。H5AD是保存这种对象的常见文件形式。

| 部分 | 常见含义 |
| --- | --- |
| `X` | 观测×特征的主矩阵；具体数值层由分析流程决定 |
| `obs` | 每个观测的注释，例如细胞所属样本和条件 |
| `var` | 每个特征的注释，例如基因ID |
| `layers` | 与主矩阵行列对应的其他数值层 |
| `obsm` | 与观测对应的多维表示，例如PCA或UMAP坐标 |
| `obsp` | 观测之间的图或其他两两关系 |

`X`不保证一定是原始counts；一个名为`counts`的层也应核对生成过程；`.raw`是保存某时点矩阵和特征注释的机制，名称本身不保证其中从未做过变换。UMAP坐标是模型表示，不是基因计数。[AnnData官方定义](https://anndata.readthedocs.io/en/stable/generated/anndata.AnnData.html)

## 5. 图像：先认识轴、尺度与对象

一个图像对象可能有以下维度：

```text
T：时间点
Z：深度层
C：通道，例如不同标记
Y、X：图像中的两个位置方向
```

这不是规定所有文件的轴顺序，实际必须读取元数据。256个像素的距离需要乘相应像素尺寸，才能变成微米等物理距离；Z方向的采样间距也可能不同。[OME-TIFF官方说明](https://ome-model.readthedocs.io/en/stable/ome-tiff/)

原始强度图与分割掩膜不同。掩膜中的`1、2、3`可能是细胞编号，而不是细胞亮度；修改掩膜会改变“哪些像素属于谁”。缩略图和带伪彩色的截图适合展示，不应默认替代定量用的原始强度及元数据。[CellProfiler](../references/index.md#cellprof)

## 6. 质谱、结构与轨迹：看坐标代表哪一种空间

质谱中的横轴常是质荷比，色谱相关轴是保留时间，纵向数值可能是强度；它们不是分子在组织里的空间坐标。空间质谱则额外保存样本位置。[质谱原理](../docs/instruments-and-data.md)

PDB/mmCIF描述原子等实体及坐标；MRC等密度图描述体素信号；分子动力学轨迹描述同一组原子在多个时间帧的位置。模型、密度和轨迹各包含不同信息；轨迹必须和正确的拓扑及原子顺序对应。[Phenix](../references/index.md#phenix)、[GROMACS](../references/index.md#md)

## 28类格式与对象速查

下表保留知识库的跨领域查阅范围。每组可能包含数种相关格式，不意味着同组文件可以直接互换。

| 格式/对象 | 内容 | 主要应用 | 字段/术语 | 注意事项 |
| --- | --- | --- | --- | --- |
| 样本表 / metadata TSV/CSV | 一行一个明确的样本/实验单位，列出处理与协变量 | 所有组学、图像、队列 | sample_id、subject_id、condition、batch、time、assay | 没有样本层级和对照信息，矩阵本身往往不足以可靠分析 |
| FASTQ | 序列及逐碱基质量 | 测序原始/中间输入 | read、paired-end、Phred、barcode/UMI | R1/R2及条码规则依实验而异；碱基质量不是比对质量 |
| FASTA | DNA/RNA/蛋白序列与标识符 | 参考、组装、序列模型 | header、sequence、alphabet | 序列ID、版本和物种必须匹配 |
| SAM / BAM / CRAM | 比对后读段及质量、标志和位置 | DNA/RNA/表观测序 | CIGAR、MAPQ、FLAG、BAI/CSI | CRAM通常依赖正确参考；多重比对和副本不应任意丢弃 |
| VCF / BCF / gVCF | 位点、等位基因、基因型和质量；gVCF可含非变异区信息 | 变异分析与群体遗传 | REF/ALT、GT、DP、GQ、VAF | 参考版本、等位方向、左对齐和多等位拆分影响合并 |
| BED / narrowPeak / broadPeak | 基因组区间及可选peak信号 | 调控区域和基因组注释 | chrom、start、end、peak summit | BED通常0-based半开区间；不可直接当GTF坐标 |
| GTF / GFF3 | 基因、转录本、外显子等注释及层级关系 | RNA定量、基因模型 | gene_id、transcript_id、feature、strand | GTF/GFF通常1-based闭区间；注释版本影响基因ID与长度 |
| bedGraph / bigWig | 沿基因组位置的连续信号轨道 | 覆盖、富集、可及性等展示 | coverage、bin、normalization | 单位可能是CPM、富集倍数等，不是一律原始counts |
| MTX / TSV / HDF5 counts | 稀疏或稠密的特征与观测计数矩阵 | bulk/单细胞与多组学 | feature、barcode、sparse、raw counts | 确认方向、索引顺序和是否已归一化/取对数 |
| H5AD / AnnData | 矩阵及obs、var、layers、嵌入和图 | Python单细胞/空间 | X、obs、var、layers、obsm | X并不总是原始counts；确认每层语义 |
| RDS / Seurat / SingleCellExperiment | R对象及矩阵、注释、模型、嵌入 | R单细胞生态 | assay、counts/data/scale.data、metadata | 对象需兼容软件版本；不同assay不应混用 |
| H5MU / MuData | 多模态数据及其细胞/样本映射 | RNA、ATAC、蛋白等联合分析 | mod、paired、shared obs | 多模态观测未必完全配对，不能只按行号拼接 |
| fragments.tsv.gz | 带细胞条码的基因组片段 | scATAC和multiome | chrom、start、end、barcode、count | 需要索引和准确条码；与peak矩阵不是同一对象 |
| pairs / .cool / .mcool / .hic | 染色质接触对或多分辨率接触矩阵 | Hi-C/Micro-C | bin、contact、balanced、resolution | 平衡后的数值不是原始接触数；坐标与分辨率要一致 |
| FCS | 流式逐事件多通道值及仪器元数据 | 流式、光谱流式、CyTOF | event、channel、compensation、transform | 这里FCS是文件标准，不是荧光相关光谱技术 |
| OME-TIFF / OME-Zarr / WSI | 显微/病理图像及相应尺度元数据 | 成像、空间和高内涵 | X/Y/Z/C/T、pixel size、pyramid | WSI指全切片图像这一对象类别；保留尺度和通道顺序 |
| mzML / mzXML / RAW | 质谱扫描、m/z、强度和时间元数据 | 蛋白质/代谢质谱 | MS1/MS2、RT、charge、precursor | 厂商RAW需要合适读取/转换；profile和centroid不同 |
| mzIdentML / mzTab / 蛋白肽表 | 鉴定、定量与置信信息 | 蛋白组分析结果 | PSM、peptide、protein group、q-value | PSM、肽和蛋白的FDR及汇总层级要区分 |
| imzML | 空间坐标关联质谱 | 质谱成像 | pixel、spectrum、m/z | 相同m/z不保证唯一化合物；空间归一不等于浓度校准 |
| PDB / mmCIF | 原子坐标、链、残基、配体及元数据 | 实验/预测结构 | chain、residue、occupancy、B-factor | 预测文件B-factor栏可能存置信度；不要当实验温度因子 |
| MRC / CCP4 map | 三维密度体数据 | cryo-EM/ET、结构拟合 | voxel、map、origin、half-map | 密度图不是原子模型；体素大小和坐标变换需正确 |
| DCD / XTC / TRR + topology | 时间帧中的原子坐标及拓扑 | 分子动力学 | frame、time、PBC、atom index | 原子顺序必须匹配；周期边界要正确处理 |
| SMILES / SDF / MOL | 分子连接、手性及可选三维坐标 | 化学信息、对接、QSAR | bond、stereochemistry、charge、conformer | 质子化、盐、手性和互变异构体影响去重及建模 |
| NWB / NIX / EDF / BIDS相关文件 | 神经电生理/影像、时间戳、行为和元数据 | 神经科学与脑成像 | sampling rate、electrode、timestamps、events | BIDS是组织规范，不是单一文件后缀；保留原始相关信息 |
| Newick / Nexus / tree sequence | 树拓扑、枝长或多段遗传谱系 | 系统发育、群体遗传 | tip、branch、root、node support | 枝长可能是替换数或时间；树根与支持度定义要说明 |
| SBML / SBOL | 反应系统模型或生物设计描述 | 系统/合成生物学 | species、reaction、parameter、component | SBML偏模型，SBOL偏设计表示；单位与边界仍需检查 |
| GMT / OBO / ontology IDs | 基因集或本体关系及标识 | 富集与功能知识 | gene set、term、parent、evidence | 物种、ID、版本、背景和集合重叠影响解释 |
| GeoTIFF / Shapefile / GeoPackage | 地理坐标关联的栅格或矢量 | 生态、遥感、空间环境 | CRS、projection、raster、resolution | 不同投影/分辨率不应直接叠加；经纬度不是等距平面坐标 |

## 看到陌生文件时，先解释它而不是急着转换

需要知道对象是谁、每个轴是什么、数值单位是什么、经过哪些处理、样本和参考如何对应。格式转换可能改变压缩或存储，却不会自动解决这些语义问题。

上述文件与具体分析的联系见[计算方法](../docs/computation-basics.md)；跨领域实现的来源见[参考资料](../references/index.md)。本表是概念速查，不替代各格式完整规范及软件版本说明。
