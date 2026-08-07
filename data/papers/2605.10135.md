# ScaleGANN: Accelerate Large-Scale ANN Indexing by Cost-effective Cloud GPUs

- arXiv ID: `2605.10135v1`
- Authors: Lan Lu, Peiqi Yin, Isaac Yang, Tao Luo, Hua Fan, Wenchao Zhou, Feifei Li, Boon Thau Loo
- Published: 2026-05-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.10135v1) | [pdf](https://arxiv.org/pdf/2605.10135v1)

## Abstract

Graph-based ANNS algorithms have gained increasing research interest and market adoption due to their efficiency and accuracy in retrieval. Existing approaches primarily rely on CPUs for graph index construction and retrieval, but this often requires significant time, especially for large-scale and high-dimensional datasets. Some studies have explored GPU-based solutions. However, GPUs are costly and their limited memory makes handling large datasets challenging.
  In this paper, we propose a novel end-to-end system ScaleGANN that enables users to efficiently construct graph indexes for large-scale, high-dimensional datasets by leveraging low-cost spot GPU resources in a distributed cloud system. ScaleGANN utilized the idea of divide-and-merge, with an optimized vector partitioning algorithm to further improve the indexing time and space efficiency while guaranteeing good index quality. Its novel resource allocation strategy realized multi-GPU indexing parallelism and overall cost-effectiveness for both build and query. Besides, we designed a task scheduler and cost model for better spot instance management and evaluation.
  We tested our system on large real-world datasets. Experiment results show that our approach can significantly accelerate the index build time to up to 9x times at even 6x lower price compared with the state-of-the-art extendable ANNS benchmark DiskANN.
