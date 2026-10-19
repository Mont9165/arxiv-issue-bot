# The Case for TPU-Accelerated Analytical Query Processing

- arXiv ID: `2610.22673v1`
- Authors: Yeounoh Chung, Jaehyun Ha, Helena Caminal, Fatma Ozcan, Aditya K Kamath, Arvind Krishnamurthy, Henry M. Levy
- Published: 2026-10-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.22673v1) | [pdf](https://arxiv.org/pdf/2610.22673v1)

## Abstract

Large-scale analytical query processing requires computing substrates capable of immense distributed scale-out. Tensor Processing Units (TPUs) perfectly embody this extreme-scale architecture, offering massive computational density and highly scalable optical pod-level interconnects. Despite these advantages, TPUs have so far remained largely unexplored for analytical database workloads. In this paper, we present the first comprehensive case for TPU-accelerated analytical query processing by running all the TPC-H queries entirely on the TPUs. We introduce Native TPU Accelerator (NTA) for analytical query processing, which provides hardware-conscious algorithm design and optimizations in JAX/XLA. By exposing the TPU's structural mechanics, we demonstrate how dynamic, memory-bound database operations can be rewritten into deterministic JAX programs. We engineer a suite of novel execution strategies that leverage both the TPU's TensorCore and SparseCore to trade sparse, unpredictable memory accesses for dense, hardware-aligned ones. At the core of NTA, a compiler uses catalog statistics to assign guarded static capacities and a hardware-calibrated local cost model to select a TPU-native implementation for each relational operator before JIT compilation.
  We evaluate our system using the TPC-H benchmark. Taking full advantage of TPU slices and JAX distributed computing, we seamlessly scale our execution environment to run TPC-H benchmark up to Scale Factor 1000 (SF1000). Evaluated against a rigorous CPU ground truth (DuckDB), our native TPU accelerator achieves state-of-the-art performance, achieving a 7.0x single-device speedup over DuckDB at SF100 and a 68.6x speedup with 16 TPUs at SF1000 (1TB). The results establish TPUs not merely as dense neural compute hardware, but as a highly competitive, massively scalable substrate for the next generation of analytical query processing.
