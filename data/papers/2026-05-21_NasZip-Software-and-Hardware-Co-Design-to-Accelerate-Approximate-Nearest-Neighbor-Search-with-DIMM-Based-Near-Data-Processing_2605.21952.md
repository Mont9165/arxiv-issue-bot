# NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing

- arXiv ID: `2605.21952v1`
- Authors: Cheng Zou, Shuo Yang, Chen Nie, Yu Zou, Yu He, Chao Jiang, Limin Xiao, Weifeng Zhang, Zhezhi He
- Published: 2026-05-21
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2605.21952v1) | [pdf](https://arxiv.org/pdf/2605.21952v1)

## Abstract

As large language models (LLMs) continue to advance, retrieval-augmented generation (RAG) has become the key mechanism for expanding model knowledge and reducing hallucinations. Central to RAG is approximate nearest neighbor search (ANNS), which retrieves database vectors most similar to a given query. However, distance calculation over high-dimensional vectors is inherently memory-bound, causing retrieval performance to be constrained by I/O bandwidth on mainstream platforms such as CPUs and GPUs. Although many prior early exiting (EE) techniques attempt to reduce memory accesses by only computing partial dimensions, the partial distance converges too slowly to the EE threshold, which ultimately limits their performance gains. To address these challenges, we propose NASZIP, a hardware-software co-designed framework that integrates near data processing (NDP) with a novel feature-level early exiting guided by statistics-based principal component analysis (PCA). Instead of relying solely on partial distances, NASZIP incorporates estimation and correction parameters to approximate full dimensional distances accurately, enabling earlier exiting without compromising accuracy. We further introduce a bit-level NDP-aware dynamic-float scheme that significantly reduces memory access for vector data. On the hardware side, we develop a data aware neighbor list mapping strategy that reduces neighbor retrieval latency and inter-channel communication overhead, complemented by a dedicated cache that exploits data locality and enhances prefetch efficiency. With these co-optimized techniques, NASZIP delivers speedups of up to $8.4\times$ / $1.4\times$ over CPU baseline and state-of-the-art GPU implementation at equal accuracy. Relative to the state-of-the-art NDP ANNS accelerator ANSMET, NASZIP achieves $1.69\times$ performance improvement.
