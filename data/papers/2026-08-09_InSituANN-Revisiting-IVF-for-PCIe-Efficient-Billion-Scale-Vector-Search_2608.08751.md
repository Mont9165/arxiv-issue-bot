# InSituANN: Revisiting IVF for PCIe-Efficient Billion-Scale Vector Search

- arXiv ID: `2608.08751v1`
- Authors: Yuemeng Xu, Zongxi Liu, Junyu Long, Yiming Huang, Jiarui Guo, Yangyujia Wang, Jiachen Xu, Dongyuan Yu, Zongwei Lv, Tong Yang
- Published: 2026-08-09
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.08751v1) | [pdf](https://arxiv.org/pdf/2608.08751v1)

## Abstract

Approximate nearest neighbor search (ANNS) over billion-scale vector datasets has become a foundational operator for modern retrieval systems, powering large-scale recommendation, semantic search, and LLM/RAG workloads. Although GPUs offer massive parallelism and high-bandwidth memory for batched vector search, their limited VRAM capacity makes fully GPU-resident billion-scale indexes difficult to deploy. In CPU-GPU heterogeneous designs, keeping the base vectors in host memory avoids this capacity limit, but naively offloading fine search to the GPU introduces a new bottleneck: large volumes of base-vector data must be streamed over PCIe.
  We present InSituANN, an IVF-based ANNS engine that enables billion-scale vector search on a single commodity GPU. InSituANN keeps original base vectors in host memory, performs fine search in situ, and uses the GPU for compact routing and optional pruning. As a result, query processing avoids PCIe transfers of high-dimensional base vectors while retaining the simplicity of IVF. Beyond query performance, we further design an ultra-fast IVF construction path for InSituANN. On SIFT-1B, InSituANN builds the IVF index in 5.2 minutes, about 350x faster than the measured 30.4-hour HNSW build. At matched recall on billion-scale datasets, InSituANN improves end-to-end throughput by 104.9x-4298.2x over the PCIe-bound Rummy baseline and by 2.4x-4.6x over DiskANN on SIFT-1B and DEEP-1B. Together with strong recall-throughput trade-offs and lower index space than graph-based alternatives, these gains make billion-scale retrieval practical on cost-efficient hardware.
  We open-source InSituANN at https://github.com/mindtravel/InSituANN-OpenSource.
