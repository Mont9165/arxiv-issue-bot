# Time-Decayed Vector Search in the Rhythm of TANGO: Jointly Modeling Semantic Similarity and Temporal Freshness

- arXiv ID: `2609.00548v1`
- Authors: Jiuqi Wei, Qiyao Luo, Quanqing Xu, Chuanhui Yang, Themis Palpanas
- Published: 2026-09-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.00548v1) | [pdf](https://arxiv.org/pdf/2609.00548v1)

## Abstract

Vector search typically measures relevance through semantic similarity under a fixed scoring function. However, in a growing range of applications, relevance may evolve over time, making temporal freshness an additional signal beyond semantic similarity. In this paper, we formalize time-decayed vector search (TDVS), which incorporates continuous temporal decay into the search objective so that relevance is jointly determined by semantic similarity and temporal freshness. We design Score-Preserving Temporal Reduction (STR) that enables existing Maximum Inner Product Search indexes to directly support TDVS. We further present Chronos, a TDVS-native framework that derives an exact metric formulation and introduces Query-Orthogonal TimeLift to control data--data geometry while preserving all query--data scores and rankings. Building on Chronos, we propose TANGO, a hierarchical graph index that adopts layer-specific TimeLift geometries to preserve temporal locality at the base layer while strengthening long-range semantic connectivity in upper layers. TANGO traverses the hierarchy using the exact TDVS score, caches temporal factors to reduce computation, and supports efficient online insertion. Extensive experiments show that TANGO achieves up to 3.5$\times$ higher query throughput and 4.05$\times$ faster index construction than state-of-the-art graph-based competitors. TANGO also maintains its advantage over all competitors across diverse temporal settings and enables efficient online insertion, demonstrating its robustness and practicality.
