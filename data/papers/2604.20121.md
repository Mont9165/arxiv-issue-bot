# A GPU-Accelerated Framework for Multi-Attribute Range Filtered Approximate Nearest Neighbor Search

- arXiv ID: `2604.20121v1`
- Authors: Zhonggen Li, Haoran Yu, Yifan Zhu, Yunjun Gao
- Published: 2026-04-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.20121v1) | [pdf](https://arxiv.org/pdf/2604.20121v1)

## Abstract

Range-filtered approximate nearest neighbor search (RFANNS) is increasingly critical for modern vector databases. However, existing solutions suffer from severe index inflation and construction overhead. Furthermore, they rely exclusively on CPUs for the heavy indexing and query processing, failing to leverage the powerful computational capabilities of GPUs. In this paper, we present Garfield, a GPU-accelerated framework for multi-attribute range filtered ANNS that overcomes these bottlenecks through designing a lightweight index structure and hardware-aware execution pipeline. Garfield introduces the GMG index, which partitions data into cells and builds local graph indexes. By adding a constant number of cross-cell edges, it guarantees linear storage and indexing overhead. For queries, Garfield utilizes a cluster-guided ordering strategy that reorders query-relevant cells, enabling a highly efficient cell-by-cell traversal on the GPU that aggressively reuses candidates as entry points across cells. To handle datasets exceeding GPU memory, Garfield features a cell-oriented out-of-core pipeline. It dynamically schedules cells to minimize the number of active queries per batch and overlaps GPU computation with CPU-to-GPU index streaming. Extensive evaluations demonstrate that Garfield reduces index size by 4.4x, while delivering 119.8x higher throughput than state-of-the-art RFANNS methods.
