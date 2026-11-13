# VecDBLens: An Evaluatology-Based Framework for Vector Database Diagnosis

- arXiv ID: `2611.15105v1`
- Authors: Yutong Zhou, Guoxin Kang, Wenxin Zhou, Haoyu He, Yuedong Zhu, Lei Wang, Wanling Gao, Fanda Fan, Jianfeng Zhan
- Published: 2026-11-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.15105v1) | [pdf](https://arxiv.org/pdf/2611.15105v1)

## Abstract

Vector databases are increasingly deployed as retrieval pipelines in which representation, indexing, and query-time execution jointly determine accuracy, throughput, and cost. Existing vector database evaluations primarily focus on indexing while treating embeddings as fixed inputs and ignoring the role of query-time execution, making it difficult to decide whether a bottleneck should be addressed by changing the embedding model, the index, or the query-processing functions. To address the above limitation, we introduce VecDBLens, an Evaluatology-based framework that treats the function under diagnosis as an evaluated object and all remaining dataset, workload, parameter, and runtime factors as matched evaluation conditions. VecDBLens attributes performance differences to individual evaluated objects through comparisons under matched evaluation conditions, summarizing their performance and stability across multiple datasets and workloads. It further analyzes interactions among objects using analysis of variance (ANOVA), thereby turning vector database benchmarking from leaderboard ranking into a reproducible diagnostic procedure. VecDBLens reveals two key insights. First, retrieval performance is fundamentally upper-bounded by embedding quality, revealing that many apparent indexing failures are therefore representation-side limitations. Second, stronger index parameterization is not always beneficial: overly aggressive configurations can reshape neighborhood topology and cause recall regression. These results challenge the common practice of evaluating vector databases primarily through indexing and show that real-world limitations arise from constraints across retrieval functions rather than any single function alone. VecDBLens provides a principled basis for identifying the true performance drivers of vector databases and for guiding their design in practical applications.
