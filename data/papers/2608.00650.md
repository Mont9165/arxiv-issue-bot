# TEngineDB-V: An OLAP-Native Vector Search System for Large-$k$ Workloads at Tencent

- arXiv ID: `2608.00650v1`
- Authors: Xufei Wu, Pengcheng Zhang, Yitong Song, Xiaobo Zhang, Anqi Liang, Kai Wang, Jijun Du, Yidi Xiong, Guangxu Cheng, Zhe Chen, Peng Chen, Guoliang Li, Xuanhe Zhou, Fan Wu
- Published: 2026-08-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.00650v1) | [pdf](https://arxiv.org/pdf/2608.00650v1)

## Abstract

Vector search systems are essential infrastructure for modern data-driven applications. Large-$k$ analytical vector search, which retrieves $k=10^3$--$10^5$ results for analytics (e.g., aggregation, filtering, joins), is increasingly important for emerging workloads, including LLM data management and advertising analysis at Tencent. Existing systems remain inadequate: specialized vector databases often cap $k$ (e.g., $k \leq 10^4$) to satisfy tail-latency constraints and offer limited analytical support, while OLAP systems typically embed per-segment vector indexes as black boxes, causing severe read/compute amplification and preventing native query optimization.
  This paper presents TEngineDB-V, an OLAP-native vector search system for large-$k$ workloads. TEngineDB-V makes vector search a first-class analytical primitive in Tencent's OLAP engine through a global segment-decoupled index materialized as relational tables, eliminating scatter-gather execution, reducing amplification, and enabling native storage optimizations. It decomposes IVFPQ-based search into relational operators, integrates OLAP optimizations, and introduces DPPQ, which combines direction-aware quantization with hierarchical residual refinement to improve recall while preserving relational efficiency. TEngineDB-V further incorporates index-aware query rewriting and a distributed-aware cost model for efficient distributed execution. Experiments show that TEngineDB-V achieves up to a $145\times$ speedup over competitive systems such as StarRocks, and up to a $52\times$ improvement in 10-billion-scale production deployments.
