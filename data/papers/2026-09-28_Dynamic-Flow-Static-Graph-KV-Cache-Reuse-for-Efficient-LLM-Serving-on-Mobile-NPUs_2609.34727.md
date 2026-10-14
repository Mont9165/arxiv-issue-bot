# Dynamic Flow, Static Graph: KV Cache Reuse for Efficient LLM Serving on Mobile NPUs

- arXiv ID: `2609.34727v1`
- Authors: Zhengxiang Huang, Shengheng Chen, Chaoyue Niu, Yujie Sun, Zhaode Wang, Zeyu Zhao, Chengfei Lv, Fan Wu, Guihai Chen
- Published: 2026-09-28
- Primary category: `cs.OS`
- Categories: `cs.OS`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.34727v1) | [pdf](https://arxiv.org/pdf/2609.34727v1)

## Abstract

On-device large language model (LLM) serving is a cornerstone of local-first personal intelligence, offering users data sovereignty, strong privacy guarantees, and freedom from cloud API latency and cost. Although KV caching is widely used to reduce latency in long-context inference, existing designs were primarily optimized for cloud GPUs with dynamic execution environments and abundant memory bandwidth. These architectural assumptions do not hold on mobile NPUs, where computation graphs must be statically compiled and both memory capacity and I/O bandwidth are severely constrained. In this work, we present a compute-storage co-design for mobile-centric prefix and non-prefix KV reuse. We first propose an intra-graph mechanism that maps selective KV recomputation onto static NPU graphs, reconciling algorithmic dynamicity with NPU staticity. We further develop an inter-graph scheduler to optimize chunk merging and minimize padding with dynamic programming. To address mobile bandwidth limitations, we introduce a hierarchical KV manager featuring a tree-hash-semantic hybrid structure, along with cost-aware prefetching and eviction policies. We also build a two-dimensional pipeline that overlaps KV loading, rerotation, and storage with NPU execution, hiding data-movement latency. Experiments across representative on-device workloads and LLMs show that our design reduces time-to-first-token (TTFT) by $40-60\%$ compared with no reuse and prefix-only caching.
