# GRBench: A Comprehensive Benchmark Evaluation for Graph-relational Data Management

- arXiv ID: `2608.31027v1`
- Authors: Zepeng Liu, Xinxin Huang, Xuanming Liu, Sheng Wang, Zhiyong Peng
- Published: 2026-08-31
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.31027v1) | [pdf](https://arxiv.org/pdf/2608.31027v1)

## Abstract

Modern data-intensive applications increasingly require database systems to manage structured records and graph data. This demand gives rise to graph-relational data management, spanning storage, query processing, and optimization across relational and graph data. In response, relational database extensions, multi-model databases, and dedicated graph-relational systems have emerged with diverse architectures. However, evaluation methodologies have not kept pace. Existing relational and graph benchmarks assess the two models largely in isolation, while multi-model benchmarks provide limited coverage of graph-relational workloads. Available graph-relational workloads mainly support functional validation and end-to-end latency measurement, revealing little about how storage, operator, and optimization designs affect performance. To evaluate system capabilities in graph-relational data management, we present GRBench. First, GRBench constructs a linked graph-relational schema from the real-world SciSciNet-v2 dataset and derives scalable instances through consistency-preserving subset extraction. Second, it organizes purpose-built query series for controlled evaluation of query processing and system components. Third, GRBench provides semantically equivalent native query formulations and evaluates representative system architectures through a unified, multidimensional methodology. Based on this evaluation, we analyze design trade-offs and identify open challenges to guide future system design and optimization.
