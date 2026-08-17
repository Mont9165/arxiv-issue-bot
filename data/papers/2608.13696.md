# Over the Memory Wall, Into the Instruction Wall: The New Bottleneck in GPU Data Processing

- arXiv ID: `2608.13696v1`
- Authors: Sven Hepkema, Bowen Wu, Christos Kozyrakis, Yannis Chronis, Gustavo Alonso
- Published: 2026-08-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.13696v1) | [pdf](https://arxiv.org/pdf/2608.13696v1)

## Abstract

Datacenter GPUs have seen an order-of-magnitude increase in memory bandwidth with the adoption of newer generations of HBM. Meanwhile, GPU database systems are gaining traction, many building on cuDF, an open-source library of GPU relational operators. Previously, query performance was bound by memory bandwidth, but the increase in memory bandwidth has not resulted in a proportional speedup of cuDF kernels. To investigate why performance has not kept up, we built Valk, a performance analysis tool that combines data from multiple profilers. We profile cuDF running TPC-H in-memory on two extremes of hardware capability, the L4 and GH200 GPUs. The GH200 has 13.4$\times$ the memory bandwidth and 2.5$\times$ the instruction throughput of the L4, yet is only 5.2$\times$ faster in running TPC-H. Our analysis shows that when memory bandwidth is increased, kernels become compute bound. From our analysis, we make three recommendations to fully utilize the GPUs' potential for relational workloads when the memory wall is removed: kernels need to 1) make more efficient use of caches, and 2) increase occupancy and/or instruction level parallelism, and 3) execute fewer instructions per memory access.
