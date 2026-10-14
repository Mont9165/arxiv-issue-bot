# Chimera: Efficient Multi-Vector Retrieval via GPU-CPU Co-Processing

- arXiv ID: `2608.23553v1`
- Authors: Yanqi Chen, Juelin Liu, Alexandra Meliou, Xiao Yan
- Published: 2026-08-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.23553v1) | [pdf](https://arxiv.org/pdf/2608.23553v1)

## Abstract

Multi-vector retrieval has become a core primitive in semantic search applications that require fine-grained matching, such as information retrieval, recommender systems and bioinformatics. However, its high computational complexity and memory costs make low-latency retrieval difficult. Prior systems have attempted to optimize query latency, but their designs remain CPU-centric. While GPUs offer substantial computational advantages, their limited memory capacity necessitates a heterogeneous architecture in which the dataset resides in host memory and the GPU serves as an accelerator. Existing GPU-based system, PLAID, is bottlenecked by CPU-GPU data movement, as vector data must be transferred from host memory to the GPU at query time. We propose Chimera, a GPU-CPU co-processing system for multi-vector retrieval that eliminates this transfer bottleneck. Chimera stores highly compressed, low-precision quantization codes on the GPU while maintaining high-precision data in CPU memory. At query time, it leverages GPU-resident data for efficient candidate generation and filtering, and further refines results through a GPU-CPU collaborative scoring scheme that completely avoids vector data transfer while enabling computation overlap. Experiments on real-world datasets demonstrate that Chimera significantly outperforms existing approaches, achieving up to 16.0x higher QPS at the same recall level.
