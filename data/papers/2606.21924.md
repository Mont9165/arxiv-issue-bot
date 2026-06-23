# Cache-Aware I/O Cost Modeling for Disk-Based Learned Indexes

- arXiv ID: `2606.21924v1`
- Authors: Zhanwei Shi, Meng Zhang, Guangyi Zhang, Sha Hu, Jianwei Liao, Jingshu Peng, Qiyu Liu, Yingxia Shao
- Published: 2026-06-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.21924v1) | [pdf](https://arxiv.org/pdf/2606.21924v1)

## Abstract

Learned indexes have shown attractive space-time trade-offs in main-memory settings, yet a principled I/O cost model for their disk-resident deployments is still missing, which is a prerequisite for index tuning and query optimization. The practically employed page buffer makes the problem even harder: under typical cache policies, many of the logical page references issued by the index are served by the buffer rather than reaching disk, so the effective physical I/O depends jointly on the workload, the cache policy, and the index configuration. In this paper, we propose CAM, the \textit{first} cache-aware I/O cost model for learned indexes that takes practical cache eviction policies into consideration. CAM is not tied to a particular learned index design: it estimates page access distributions without full trace replay for mainstream learned index designs, and then combines them with I/O cost models to estimate effective physical I/Os. This formulation enables principled knob tuning by explicitly modeling the trade-off between index footprint and buffer capacity. We instantiate CAM for disk-based PGM-index and RMI, and further apply the same modeling principle to learned-index-based joins through a hybrid strategy that adaptively chooses point or range probes based on local key density. Extensive experiments on real benchmarks show that CAM provides \textit{accurate and efficient} I/O estimation across diverse workloads: CAM-guided tuning improves PGM throughput by \textbf{1.17$\times$} over multicriteria PGM tuning and improves RMI throughput by \textbf{1.66$\times$} over CDFShop with I/O-related considerations. For learned-index-based joins, our hybrid strategy improves end-to-end performance by up to \textbf{8.8$\times$} over disk-based index nested-loop join.
