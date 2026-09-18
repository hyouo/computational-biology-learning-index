# 数据格式与数据对象

文件后缀只能提示数据类型。分析前还要核对样本身份、维度、单位、参考版本、坐标体系和每个数据层的语义。

| 格式/对象 | 内容 | 主要应用 | 字段/术语 | 注意事项 |
| --- | --- | --- | --- | --- |
| 样本表 / metadata TSV/CSV | 一行一个明确的样本/实验单位，列出处理与协变量 | 所有组学、图像、队列 | sample_id、subject_id、condition、batch、time、assay | 没有样本层级和对照信息，矩阵本身往往不足以可靠分析 |
| FASTQ | 序列及逐碱基质量 | 测序原始/中间输入 | read、paired-end、Phred、barcode/UMI | R1/R2链及条码规则依实验而异；质量值不是比对质量 |
| FASTA | DNA/RNA/蛋白序列与标识符 | 参考、组装、序列模型 | header、sequence、alphabet | 序列ID、版本和物种必须匹配 |
| SAM / BAM / CRAM | 比对后读段及质量、标志和位置 | DNA/RNA/表观测序 | CIGAR、MAPQ、FLAG、BAI/CSI | CRAM通常依赖正确参考；多重比对和副本不应任意丢弃 |
| VCF / BCF / gVCF | 位点、等位基因、基因型和质量；gVCF可含非变异区信息 | 变异分析与群体遗传 | REF/ALT、GT、DP、GQ、VAF | 参考版本、等位方向、左对齐和多等位拆分影响合并 |
| BED / narrowPeak / broadPeak | 基因组区间及可选peak信号 | 调控区域和基因组注释 | chrom、start、end、peak summit | BED通常0-based半开区间；不可直接当GTF坐标 |
| GTF / GFF3 | 基因、转录本、外显子等注释及层级关系 | RNA定量、基因模型 | gene_id、transcript_id、feature、strand | GTF/GFF通常1-based闭区间；注释版本影响基因ID与长度 |
| bedGraph / bigWig | 沿基因组位置的连续信号轨道 | 覆盖、富集、可及性等展示 | coverage、bin、normalization | 轨道单位可能是CPM、fold enrichment等；不是一律原始counts |
| MTX / TSV / HDF5 counts | 稀疏或稠密特征×观测计数矩阵 | bulk/单细胞与多组学 | feature、barcode、sparse、raw counts | 确认方向、索引顺序和是否已归一/取对数 |
| H5AD / AnnData | 矩阵及obs、var、layers、嵌入和图 | Python单细胞/空间 | X、obs、var、layers、obsm | X并不总是原始counts；分析前确认layer语义 |
| RDS / Seurat / SingleCellExperiment | R对象及矩阵、注释、模型、嵌入 | R单细胞生态 | assay、counts/data/scale.data、metadata | 序列化对象需兼容软件版本；不同assay不应混用 |
| H5MU / MuData | 多模态数据及其细胞/样本映射 | RNA+ATAC+蛋白等 | mod、paired、shared obs | 多模态观测未必完全配对，不能只按行号拼接 |
| fragments.tsv.gz | 带细胞条码的基因组片段 | scATAC和multiome | chrom、start、end、barcode、count | 需要索引和准确条码；与peak矩阵不是同一对象 |
| pairs / .cool / .mcool / .hic | 染色质接触对或分辨率不同的接触矩阵 | Hi-C/Micro-C | bin、contact、balanced、resolution | 平衡后的数值不是原始接触数；坐标与分辨率要一致 |
| FCS | 流式逐事件多通道值及仪器元数据 | 流式、光谱流式、CyTOF | event、channel、compensation、transform | 这里FCS是文件标准，不是荧光相关光谱技术 |
| OME-TIFF / OME-Zarr / WSI | 含维度、物理尺度等元数据的显微/病理图像 | 成像、空间和高内涵 | X/Y/Z/C/T、pixel size、pyramid | 必须保留物理单位、通道顺序和缩放；缩略图不可替代定量原图 |
| mzML / mzXML / RAW | 质谱扫描、m/z、强度和时间元数据 | 蛋白质/代谢质谱 | MS1/MS2、RT、charge、precursor | 厂商RAW需要合适读取/转换；profile和centroid不同 |
| mzIdentML / mzTab / 蛋白肽表 | 鉴定、定量与置信信息 | 蛋白组分析结果 | PSM、peptide、protein group、q-value | PSM、肽和蛋白的FDR及汇总层级要区分 |
| imzML | 空间坐标关联质谱 | 质谱成像 | pixel、spectrum、m/z | 相同m/z不保证唯一化合物；空间归一不等于浓度校准 |
| PDB / mmCIF | 原子坐标、链、残基、配体及部分元数据 | 实验/预测结构 | chain、residue、occupancy、B-factor | 预测文件B-factor栏可能存置信度；不要直接当实验温度因子 |
| MRC / CCP4 map | 三维电镜/密度体数据 | cryo-EM/ET、结构拟合 | voxel、map、origin、half-map | 密度图不是原子模型；体素大小和坐标变换需正确 |
| DCD / XTC / TRR + topology | 随时间变化的原子坐标及拓扑 | 分子动力学 | frame、time、PBC、atom index | 轨迹必须与拓扑原子顺序匹配；跨边界要正确unwrap |
| SMILES / SDF / MOL | 分子连接、手性及可选三维坐标 | 化学信息、对接、QSAR | bond、stereochemistry、charge、conformer | 质子化、盐、手性和互变异构体影响去重及建模 |
| NWB / NIX / EDF / BIDS相关文件 | 神经电生理/影像、时间戳、行为和元数据 | 神经科学与脑成像 | sampling rate、electrode、timestamps、events | NWB主要神经数据标准，BIDS是组织规范；不能只保存处理后的曲线 |
| Newick / Nexus / tree sequence | 树拓扑、枝长及可选多段遗传谱系 | 系统发育、群体遗传 | tip、branch、root、node support | 枝长可能是替换数或时间；树根与支持度定义要说明 |
| SBML / SBOL | 反应系统模型或生物设计的结构化描述 | 系统/合成生物学 | species、reaction、parameter、component | SBML偏动态模型，SBOL偏设计表示；单位和边界条件仍需检查 |
| GMT / OBO / ontology IDs | 基因集或结构化本体关系 | 富集与功能知识 | gene set、term、parent、evidence | 物种、ID、版本、背景与基因集重叠影响解释 |
| GeoTIFF / Shapefile / GeoPackage | 带地理坐标的栅格或矢量数据 | 生态、遥感、空间环境 | CRS、projection、raster、resolution | 不同投影/分辨率不应直接叠加；经纬度距离不是等距平面距离 |

[返回领域导航](../atlas/index.md) · [参考资料](../references/index.md)
