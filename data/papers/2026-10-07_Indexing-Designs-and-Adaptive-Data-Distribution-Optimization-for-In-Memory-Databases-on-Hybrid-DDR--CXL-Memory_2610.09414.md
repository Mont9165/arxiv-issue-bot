# Indexing Designs and Adaptive Data Distribution Optimization for In-Memory Databases on Hybrid DDR--CXL Memory

- arXiv ID: `2610.09414v1`
- Authors: Huijie Cao, Shun Yang, Yinan Zhang, Huiqi Hu, Xuan Zhou, Weining Qian
- Published: 2026-10-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.09414v1) | [pdf](https://arxiv.org/pdf/2610.09414v1)

## Abstract

CXL memory expands single-node memory capacity for in-memory databases but has higher latency and lower bandwidth than local DDR. Hybrid DDR--CXL databases require joint indexing and data distribution design. Indexing designs differ in access and migration paths and constrain the placement of indexes and tuples, creating trade-offs in runtime performance, DDR memory efficiency, and system integration complexity. Their performance impact is thus difficult to determine. Indexes and tuples may differ in access characteristics: placing them in the same tier may reduce DDR efficiency, while separate management adds tracking and decision overhead.
  We propose five indexing designs based on two approaches: treating the two tiers as a unified data space or managing them separately. We analyze their trade-offs and underlying causes and develop adaptive data distribution optimization for single-index designs in which the database explicitly manages distribution. The method manages index objects and tuples separately, reduces metadata overhead through hierarchical hotness tracking and an index object residency policy, and extends benefit-aware admission and randomized eviction to determine and adjust their placement according to each type's expected benefits and memory footprints.
  We implemented the designs in a hybrid DDR--CXL database prototype and evaluated them using YCSB. The single-index design with direct addressing achieves the best performance under most workloads and system configurations. The dual-index design performs better mainly when DDR capacity is limited or accesses are highly concentrated, and has relatively low integration complexity. Adaptive distribution optimization improves DDR memory efficiency and system performance, enabling single-index designs to achieve up to $1.59\times$ the throughput of their counterparts with non-separated management.
