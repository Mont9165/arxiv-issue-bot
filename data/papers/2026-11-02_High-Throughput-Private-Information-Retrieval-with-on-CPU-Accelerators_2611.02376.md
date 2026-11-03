# High-Throughput Private Information Retrieval with on-CPU Accelerators

- arXiv ID: `2611.02376v1`
- Authors: Gyuyeong Kim
- Published: 2026-11-02
- Primary category: `cs.OS`
- Categories: `cs.OS`, `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.02376v1) | [pdf](https://arxiv.org/pdf/2611.02376v1)

## Abstract

Private information retrieval (PIR) hides which record a client retrieves by scanning the entire database, and batching is an effective technique to improve throughput by sharing this scan across queries. However, existing CPU-based solutions gain little from batching because each query still requires its own multiplications, and vector instructions perform only a few at a time. GPUs and other discrete accelerators can accelerate these computations, but require extra hardware and can constrain database size due to their limited memory capacity. In this paper, we present AltoPIR, the first PIR system that leverages on-CPU matrix accelerators such as Intel AMX. AltoPIR keeps the accelerator fed from the CPU caches, reading each database byte from memory once for all queries in a batch and never writing intermediate products to memory. This enables high-performance PIR through efficient batching without requiring discrete accelerators. Our evaluation shows that AltoPIR achieves up to 50.1x higher throughput than existing CPU-based solutions and serves databases larger than a GPU's memory.
