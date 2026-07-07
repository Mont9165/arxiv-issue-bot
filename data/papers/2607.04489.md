# Eiger: An Efficient Library for GPU-based Data Analytics

- arXiv ID: `2607.04489v1`
- Authors: Bowen Wu, Marko Kabić, Sven Hepkema, Vasilis Mageirakos, Christos Kozyrakis, Gustavo Alonso
- Published: 2026-07-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.04489v1) | [pdf](https://arxiv.org/pdf/2607.04489v1)

## Abstract

GPUs have become an increasingly attractive platform for accelerating analytical workloads due to their massive parallelism and high memory bandwidth. Recent studies show that in systems with fast CPU-GPU interconnects and networks, query processing within the GPU, rather than data movement, is the dominant bottleneck. This highlights the need for more efficient relational operators on GPUs than the widely used library, cuDF. While offering rich functionality, cuDF commits to a single, statically chosen implementation for most operators and barely uses runtime information about the data, limiting performance across diverse workloads and GPUs. We present Eiger, a high-performance library for GPU-based data analytics that improves single-GPU query processing through runtime workload adaptivity. Adaptivity in Eiger rests on two principles. First, Eiger provides multiple implementation variants and tunable knobs for most operators, covering not only joins and group-bys but also expensive yet often overlooked operations, such as expression evaluation, string processing, and multi-key sorting, for which it contributes new optimization techniques. Second, Eiger profiles intermediate data during query execution using lightweight statistics, such as value ranges and HyperLogLog++ sketches, and uses them to select implementations, tune knobs, and compress data on the fly, overcoming the limitations of traditional static query optimization. The breadth of operators and variants also enables a more comprehensive performance analysis, covering more operations and workloads than previous work. We evaluate Eiger with operator microbenchmarks on two GPU architectures and the complete TPC-H benchmark (up to scale factor 100). Across the 22 queries, Eiger reduces total runtime by up to 1.8x compared to the state-of-the-art cuDF library; for individual queries, Eiger achieves up to 6.1x better performance.
