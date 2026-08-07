# GORIO: GPU-Centered Remote I/O for Graph ANNS over NVMe-oF

- arXiv ID: `2607.04415v1`
- Authors: Gen Zhang, Wenhao Gu
- Published: 2026-07-05
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.04415v1) | [pdf](https://arxiv.org/pdf/2607.04415v1)

## Abstract

Graph-based approximate nearest neighbor search (ANNS) is increasingly used in vector databases and retrieval-augmented generation services, but large vector indexes often exceed the memory capacity of a single GPU server. NVMe over Fabrics (NVMe-oF) provides an attractive storage-disaggregation substrate, yet existing remote storage paths are still largely CPU-centered: the CPU forms I/O requests, drives transport progress, and determines when GPU computation can resume. This organization is poorly matched to graph ANNS, where the next data access is discovered inside GPU graph traversal.
  This paper presents GORIO, a system study that extends GPU-centered local I/O to remote storage and specializes the resulting substrate for graph ANNS over NVMe-oF. GORIO keeps query evolution, page-miss generation, pending-query state, and resume decisions on the GPU, while the CPU acts only as an NVMe-oF transport and completion proxy. The design has two layers: a GPU-direct remote I/O path that turns local page-cache misses into split-phase remote operations, and ANNS-specific scheduling mechanisms that overlap graph traversal with remote page service. On a SIFT1M DiskANN-style graph workload over an RDMA NVMe-oF path, GORIO is 1.31$\times$ faster than the state-of-the-art remote-I/O reference path and 3.73$\times$ faster than the direct remote page-cache path. These results demonstrate a concrete GPU-centered remote I/O substrate for graph ANNS.
