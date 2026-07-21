# Terascale Query Processing in the Browser: Rethinking GPU Acceleration

- arXiv ID: `2607.17571v1`
- Authors: Jiaxin Lu, Landon Dyken, Yihao Sun, Kristopher Micinski, Thomas Gilray, Sidharth Kumar
- Published: 2026-07-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.17571v1) | [pdf](https://arxiv.org/pdf/2607.17571v1)

## Abstract

Recursive query computation, central to graph algorithms and relational databases, demands GPU acceleration due to its inherent computational intensity. While substantial prior work addresses GPU implementations of recursive queries that require fixed-point evaluation, existing systems are restricted to native execution environments. We introduce WGLog, the first web-browser-native GPU engine for compute-bound recursive database queries. WGLog is built entirely on WebGPU compute shaders, a cross-platform API that enables GPU acceleration in web browsers. WGLog leverages two key technical innovations. First, we replace hash-table-based joins with atomic-free sorted-array joins, eliminating the serialization bottleneck that hash tables suffer on skewed graphs. Second, we develop an asynchronous execution pipeline using WebGPU's indirect dispatch capability, which eliminates GPU-host synchronizations that would otherwise dominate per-iteration overhead. On representative workloads, WGLog delivers a 1.48--4.68x speedup over native GPU systems and orders-of-magnitude improvement over CPU and WebAssembly implementations.
