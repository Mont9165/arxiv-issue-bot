# FROG: Efficient Range-Filtering Approximate Nearest Neighbor Search on GPUs

- arXiv ID: `2608.16491v1`
- Authors: Xiaokun Cui, Pengbo Liu, Jiadong Xie, Yingfan Liu, Hui Li, Jeffrey Xu Yu, Jiangtao Cui
- Published: 2026-08-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.16491v1) | [pdf](https://arxiv.org/pdf/2608.16491v1)

## Abstract

Range-filtering approximate nearest neighbor search (RFANNS) is a fundamental operation in modern vector databases. Given a query vector $q$ and a numerical range predicate, RFANNS returns the $k$-approximate nearest neighbors ($k$-ANN) of the query $q$ among the objects whose attributes satisfy the range predicate. However, existing RFANNS methods are not well suited to high-throughput GPU execution. CPU indexes offer limited parallel scalability, generic GPU filtering is highly selectivity-dependent, and GPU indexes built from locally optimized subgraphs can incur long search trajectories and redundant distance computations. To address these limitations, we present FROG, a GPU-oriented RFANNS index that replaces multiple locally optimal substructure building with a globally aware, vertex-centric design. It organizes diverse expansion neighbor candidates for each vertex in a GPU-friendly structure and rapidly identifies the expansion neighbors used for computation at query time. Moreover, GPU-oriented algorithms and implementations are developed for both index construction and query processing. Experiments on six datasets show that FROG improves mixed-selectivity query throughput by 14.7--37.7$\times$ over 44-core CPU baselines and 4.5--7.6$\times$ over the strongest GPU baseline. It also accelerates index construction by 2.4--14.8$\times$ over the GPU baseline.
