# DBRepro: Automated Database Synthesis via a Hybrid Constraint-Solving Approach for Reproducing Slow Queries

- arXiv ID: `2608.27822v1`
- Authors: Zhaoyang Zhang, Shuang Liu, Dengfeng Xu, Wei Lu, Jianquan Leng, Sheng Du, Xiaoyong Du
- Published: 2026-08-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.27822v1) | [pdf](https://arxiv.org/pdf/2608.27822v1)

## Abstract

Slow queries frequently cause severe performance bottlenecks in database management systems. Diagnosing their root causes online risks exacerbating resource contention, while data privacy regulations often prohibit copying production data to test environments. Synthesizing a proxy database from non-intrusive metadata that induces the query optimizer to generate the same physical execution plans is therefore critical for offline diagnosis. High-fidelity reproduction requires preserving global statistical distributions while enforcing exact local cardinalities. Existing data-driven and workload-aware approaches cannot satisfy both requirements simultaneously.
  We present DBRepro, an automated end-to-end framework that formulates database generation as a constrained distribution synthesis problem. DBRepro initializes a global distribution from lightweight column statistics, extracts execution constraints from target queries, and progressively adjusts the distribution to satisfy these constraints while preserving the global distribution. Experiments on TPC-H and SSB show that DBRepro reduces cardinality error by up to 20.3% over a data-driven baseline while maintaining identical plan consistency. Compared with a workload-aware baseline, it reproduces 15% more consistent execution plans and reduces latency proportion error by 21.5%. We further validate DBRepro on a nearly 1 TB real-world dataset managed by KingbaseES, where it reproduces the execution performance of complex slow queries with high fidelity.
