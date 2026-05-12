# Data Path Fusion in GPU for Analytical Query Processing

- arXiv ID: `2605.10511v1`
- Authors: Tsuyoshi Ozawa, Kazuo Goda
- Published: 2026-05-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.10511v1) | [pdf](https://arxiv.org/pdf/2605.10511v1)

## Abstract

One major technical challenge for modern analytical database systems is how to leverage GPU to exploit their massive parallelism and high bandwidth. Yet, existing GPU-driven database engines suffer from inefficiencies caused by frequent host-device interactions and fragmented execution across multiple GPU kernels, limiting their ability to fully utilize GPU's computational and IO capabilities. This paper proposes Data Path Fusion (DPF), a novel GPU-driven data processing architecture that integrates a sequence of data path operations -- including IOs, decompression, and query operations -- into a single GPU kernel. By fusing the data path, DPF reduces host-device communication overheads and enables more efficient utilization of GPU resources for analytical query workloads. DPF seamlessly integrates GPU-friendly optimization techniques, including type-specific compression/decompression, variable-length attribute support, and state-of-the-art GPU-driven IO mechanism, to work in concert, enabling efficient end-to-end query execution directly on GPU. Through extensive experimental evaluation using a prototyped DPF-based GPU-driven database engine (DPFProto) with analytical benchmark workloads, this paper demonstrates that DPF achieves speedups of 2.66 to 6.22 on TPC-H and 3.84 to 16.81 on SSB over the state-of-the-art approach in the representative configuration. Our results show that DPF effectively unlocks the computational and IO potential of modern GPU, providing a promising direction for next-generation analytical database systems.
