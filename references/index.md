# 概念入口与基础来源

[知识导航](../atlas/index.md) · [近年Nature系列原始论文](nature-papers.md)

百科用于厘清名称、别名和相邻概念；原始研究用于理解技术的观测与推断关系；官方文档用于核对具体实现。正文采用独立归纳，不复制百科或论文全文。

本页保留原有方法条目的资料键，供交叉引用。通用文档和领域背景不一定覆盖一个方法家族的全部子方法，不能把“有参考链接”当作每项说明均已逐条核实。近期专题正文的直接论文依据见各段链接与[论文解析](nature-papers.md)。动态文档应按实际使用版本阅读；本页不宣称软件推荐排名或完整方法评测。

## encyclopedia

百科概念导航，查阅日期2026-09-18；不作为具体算法性能或实验结论的唯一依据。

| 概念 | 入口 | 用于厘清什么 |
| --- | --- | --- |
| 分子生物学中心法则 | [Central dogma of molecular biology](https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology) | 序列信息传递与调控反馈的区别；直接依据见[Crick](#crick) |
| 基因表达 | [Gene expression](https://en.wikipedia.org/wiki/Gene_expression) | 从转录到功能产物的相关过程；具体读出见[分子调控](../docs/molecular-regulation.md) |
| 系统生物学 | [Systems biology](https://en.wikipedia.org/wiki/Systems_biology) | 多层次相互作用与系统建模的概念范围；实现见[COPASI](#copasi)和[COBRApy](#cobra) |

## crick

[Crick. Central dogma of molecular biology. Nature, 1970. DOI: 10.1038/227561a0](https://www.nature.com/articles/227561a0)

概念原始论述：序列信息传递；不是禁止蛋白对转录、染色质或代谢反馈。

## slam

[Herzog et al. Thiol-linked alkylation of RNA to assess expression dynamics. Nature Methods, 2017. DOI: 10.1038/nmeth.4435](https://www.nature.com/articles/nmeth.4435)

原始方法：RNA代谢标记与表达动态；不要将静态RNA量直接当成合成或降解速率。

## rmats

[Shen et al. rMATS: robust and flexible detection of differential alternative splicing from replicate RNA-Seq data. PNAS, 2014. DOI: 10.1073/pnas.1419161111](https://pubmed.ncbi.nlm.nih.gov/25480548/)

原始方法：重复样本中的差异可变剪接；与基因总量差异不是同一检验。

## dvp

[Mund et al. Deep Visual Proteomics defines single-cell identity and heterogeneity. Nature Biotechnology, 2022. DOI: 10.1038/s41587-022-01302-5](https://www.nature.com/articles/s41587-022-01302-5)

原始方法：图像定义对象并指导空间取样质谱。图像中识别单细胞不意味着每一份质谱样本均为单个细胞。

## miqe

[The MIQE 2.0 Guidelines: Minimum Information for Publication of Quantitative Real-Time PCR Experiments. Clinical Chemistry, 2025. DOI: 10.1093/clinchem/hvaf043](https://pubmed.ncbi.nlm.nih.gov/40272429/)

实验报告与解释依据：qPCR设计、分析和报告；不是用RNA-seq流程文档替代qPCR原理。

## stats

[statsmodels：统计模型用户指南](https://www.statsmodels.org/stable/user-guide.html) — 官方文档。

## sklearn

[scikit-learn：常见陷阱与推荐实践](https://scikit-learn.org/stable/common_pitfalls.html) — 官方文档。

## nf

[nf-core：计算流程目录](https://nf-co.re/pipelines) — 官方流程入口，不是所有方法原理的统一来源。

## hts

[HTSlib / SAMtools / BCFtools](https://www.htslib.org/doc/) — 官方格式与软件文档。

## rnaseq

[nf-core/rnaseq](https://nf-co.re/rnaseq) — RNA测序预处理和定量流程文档。

## deseq

[DESeq2分析指南](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) — 计数模型、设计、差异表达与输入要求。

## sarek

[nf-core/sarek](https://nf-co.re/sarek) — 生殖系与体细胞变异流程文档。

## atac

[nf-core/atacseq](https://nf-co.re/atacseq) — 可及性数据流程文档。

## chip

[nf-core/chipseq](https://nf-co.re/chipseq) — ChIP-seq数据流程文档。

## ribo

[nf-core/riboseq](https://nf-co.re/riboseq) — 核糖体足迹数据流程文档。

## hifiasm

[Haplotype-resolved de novo assembly using phased assembly graphs with hifiasm. Nature Methods, 2021](https://www.nature.com/articles/s41592-020-01056-5) — 原始方法。

## pangenome

[A draft human pangenome reference. Nature, 2023](https://www.nature.com/articles/s41586-023-05896-x) — 原始研究；[技术关系解析](nature-papers.md#n01)。

## atacpaper

[Transposition of native chromatin for fast and sensitive epigenomic profiling. Nature Methods, 2013](https://www.nature.com/articles/nmeth.2688) — ATAC-seq原始方法。

## cuttag

[CUT&Tag for efficient epigenomic profiling of small samples and single cells. Nature Communications, 2019](https://www.nature.com/articles/s41467-019-09982-5) — 原始方法。

## meme

[MEME Suite：序列基序分析](https://meme-suite.org/meme/doc/overview.html) — 官方文档。

## plink

[PLINK 2](https://www.cog-genomics.org/plink/2.0/) — 基因型处理与关联分析官方文档。

## susie

[SuSiE / susieR](https://stephenslab.github.io/susieR/) — 精细定位与稀疏回归官方文档。

## coloc

[coloc](https://chr1swallace.github.io/coloc/) — 共定位官方文档。

## mr

[TwoSampleMR](https://mrcieu.github.io/TwoSampleMR/) — 孟德尔随机化实现文档。

## scanpy

[Scanpy教程](https://scanpy.readthedocs.io/en/stable/tutorials/index.html) — 单细胞数据处理官方教程。

## scvi

[scvi-tools](https://scvi-tools.org/) — 概率模型与多模态分析官方文档。

## muscat

[muscat detects subpopulation-specific state transitions from multi-sample multi-condition single-cell transcriptomics data. Nature Communications, 2020](https://www.nature.com/articles/s41467-020-19894-4) — 原始方法。

## velocity

[Generalizing RNA velocity to transient cell states through dynamical modeling. Nature Biotechnology, 2020](https://www.nature.com/articles/s41587-020-0591-3) — scVelo原始方法。

## cellrank

[CellRank for directed single-cell fate mapping. Nature Methods, 2022](https://www.nature.com/articles/s41592-021-01346-6) — 原始方法；[CellRank 2解析](nature-papers.md#n08)。

## cell2loc

[Cell2location maps fine-grained cell types in spatial transcriptomics. Nature Biotechnology, 2022](https://www.nature.com/articles/s41587-021-01139-4) — 原始方法。

## cellchat

[Inference and analysis of cell-cell communication using CellChat. Nature Communications, 2021](https://www.nature.com/articles/s41467-021-21246-9) — 原始方法；[LIANA+解析](nature-papers.md#n09)。

## squidpy

[Squidpy: a scalable framework for spatial omics analysis. Nature Methods, 2022](https://www.nature.com/articles/s41592-021-01358-2) — 原始方法。

## scenic

[SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks. Nature Methods, 2023](https://www.nature.com/articles/s41592-023-01938-4) — 原始方法；[技术关系解析](nature-papers.md#n03)。

## celloracle

[Dissecting cell identity via network inference and in silico gene perturbation. Nature, 2023](https://www.nature.com/articles/s41586-022-05688-9) — CellOracle原始方法。

## scperturb

[scPerturb: harmonized single-cell perturbation data. Nature Methods, 2024](https://www.nature.com/articles/s41592-023-02144-y) — 数据资源与分析研究。

## wnn

[Seurat：Weighted Nearest Neighbor Analysis](https://satijalab.org/seurat/articles/weighted_nearest_neighbor_analysis) — 官方多模态分析教程。

## mofa

[MOFA2](https://biofam.github.io/MOFA2/) — 多组学因子分析官方文档。

## scirpy

[Scirpy](https://scirpy.scverse.org/en/latest/) — 免疫组库分析官方文档。

## diann

[DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput. Nature Methods, 2020](https://www.nature.com/articles/s41592-019-0638-x) — 原始方法。

## maxquant

[MaxQuant enables high peptide identification rates, individualized p.p.b.-range mass accuracies and proteome-wide protein quantification. Nature Biotechnology, 2008](https://www.nature.com/articles/nbt.1511) — 原始方法。

## msdial

[MS-DIAL: data-independent MS/MS deconvolution for comprehensive metabolome analysis. Nature Methods, 2015](https://www.nature.com/articles/nmeth.3393) — 原始方法。

## cobra

[COBRApy](https://cobrapy.readthedocs.io/en/latest/) — 约束型代谢模型官方文档。

## copasi

[COPASI用户手册](https://copasi.org/Support/User_Manual/) — 反应动力学、随机模拟、参数估计和分析官方文档。

## af3

[Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature, 2024](https://www.nature.com/articles/s41586-024-07487-w) — 原始方法；[技术关系解析](nature-papers.md#n07)。

## rfdiff

[De novo design of protein structure and function with RFdiffusion. Nature, 2023](https://www.nature.com/articles/s41586-023-06415-8) — 原始方法；[技术关系解析](nature-papers.md#n05)。

## cryo

[CryoSPARC指南](https://guide.cryosparc.com/) — 冷冻电镜计算官方文档。

## relion

[RELION](https://relion.readthedocs.io/en/latest/) — 冷冻电镜重建官方文档。

## md

[GROMACS reference manual](https://manual.gromacs.org/current/reference-manual/index.html) — 分子模拟理论与实现文档。

## vina

[AutoDock Vina](https://autodock-vina.readthedocs.io/en/latest/) — 分子对接官方文档。

## rdkit

[RDKit入门](https://www.rdkit.org/docs/GettingStartedInPython.html) — 化学信息学官方文档。

## cellpose

[Cellpose: a generalist algorithm for cellular segmentation. Nature Methods, 2021](https://www.nature.com/articles/s41592-020-01018-x) — 原始方法；[CellSAM解析](nature-papers.md#n13)。

## kilosort

[Spike sorting with Kilosort4. Nature Methods, 2024](https://www.nature.com/articles/s41592-024-02232-7) — 原始方法。

## dlc

[DeepLabCut: markerless pose estimation of user-defined body parts with deep learning. Nature Neuroscience, 2018](https://www.nature.com/articles/s41593-018-0209-y) — 原始方法。

## microns

[Functional connectomics spanning multiple areas of mouse visual cortex. Nature, 2025](https://www.nature.com/articles/s41586-025-08790-w) — 原始研究；[技术关系解析](nature-papers.md#n11)。

## qiime

[QIIME 2 amplicon documentation](https://amplicon-docs.qiime2.org/en/latest/) — 扩增子数据官方文档。

## dada

[DADA2: High-resolution sample inference from Illumina amplicon data. Nature Methods, 2016](https://www.nature.com/articles/nmeth.3869) — 原始方法。

## metaphlan

[Extending and improving metagenomic taxonomic profiling with uncharacterized species using MetaPhlAn 4. Nature Biotechnology, 2023](https://www.nature.com/articles/s41587-023-01688-w) — 原始方法；[技术关系解析](nature-papers.md#n06)。

## iqtree

[IQ-TREE](https://iqtree.github.io/doc/) — 系统发育分析官方文档。

## hyphy

[HyPhy selection methods](https://hyphy.org/methods/selection-methods/) — 选择分析官方文档。

## biomod

[biomod2](https://biomodhub.github.io/biomod2/) — 物种分布建模官方文档。

## vegan

[vegan](https://vegandevs.github.io/vegan/) — 群落生态分析官方文档。

## addgene

[Addgene技术指南](https://www.addgene.org/guides/) — 分子生物学技术背景；不能替代每个实验专门的验证依据。

## spatial2024

[Method of the Year 2024: spatial proteomics. Nature Methods, 2024](https://www.nature.com/articles/s41592-024-02565-3) — 编辑部专题背景，非原始方法论文。

## em2025

[Method of the Year 2025专题](https://www.nature.com/articles/s41592-025-02988-6) — 编辑部专题背景，非原始方法论文。

## alphagenome

[Advancing regulatory variant effect prediction with AlphaGenome. Nature, 2026](https://www.nature.com/articles/s41586-025-10014-0) — 原始方法；[技术关系解析](nature-papers.md#n14)。

## evo2

[Genome modelling and design across all domains of life with Evo 2. Nature, 2026](https://www.nature.com/articles/s41586-026-10176-5) — 原始方法；[技术关系解析](nature-papers.md#n15)。

## nicheformer

[Nicheformer: a foundation model for single-cell and spatial omics. Nature Methods, 2025](https://www.nature.com/articles/s41592-025-02814-z) — 原始方法；[技术关系解析](nature-papers.md#n12)。

## gsea

[GSEA / MSigDB documentation](https://docs.gsea-msigdb.org/) — 基因集与富集分析官方文档。

## eclip

[Robust transcriptome-wide discovery of RNA-binding protein binding sites with enhanced CLIP (eCLIP). Nature Methods, 2016](https://www.nature.com/articles/nmeth.3810) — 原始方法。

## dms

[DMS-MaPseq for genome-wide or targeted RNA structure probing in vivo. Nature Methods, 2017](https://pubmed.ncbi.nlm.nih.gov/27819661/) — 原始方法。

## caiman

[CaImAn](https://caiman.readthedocs.io/en/latest/) — 钙成像分析官方文档。

## flow

[FlowKit](https://flowkit.readthedocs.io/en/latest/) — 流式数据处理官方文档。

## phenix

[Phenix documentation](https://www.phenix-online.org/documentation/) — 实验结构解析与验证官方文档。

## cellprof

[CellProfiler](https://cellprofiler.org/) — 生物图像定量官方工具与文档。

## tskit

[tskit tutorials](https://tskit.dev/tutorials/intro.html) — 遗传谱系与tree sequence官方文档。

## turbo

[Efficient proximity labeling in living cells and organisms with TurboID. Nature Biotechnology, 2018](https://www.nature.com/articles/nbt.4201) — 原始方法。

## mdanalysis

[MDAnalysis](https://docs.mdanalysis.org/stable/) — 分子轨迹分析官方文档。

## msstats

[MSstats](https://bioconductor.org/packages/release/bioc/html/MSstats.html) — 质谱定量统计分析官方文档。

## mageck

[MAGeCK](https://sourceforge.net/p/mageck/wiki/Home/) — pooled CRISPR筛选分析官方文档。

## saxs

[BioXTAS RAW](https://bioxtas-raw.readthedocs.io/en/latest/) — 小角散射分析官方文档。

## immcant

[Immcantation](https://immcantation.readthedocs.io/en/stable/) — 抗体组库、克隆和谱系分析官方文档。
