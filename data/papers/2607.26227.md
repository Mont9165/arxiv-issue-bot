# Two-sided RDMA Striking Back for Disaggregated Memory Databaases

- arXiv ID: `2607.26227v1`
- Authors: Hokeun Cha, Aditya Akella, Xiangyao Yu
- Published: 2026-07-28
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.26227v1) | [pdf](https://arxiv.org/pdf/2607.26227v1)

## Abstract

RDMA has enabled high-speed data access and low-latency communication in disaggregated memory databases. While various optimization techniques have been proposed to accelerate transactions with RDMA in this setting, two-sided RDMA has been largely underexplored in favor of one-sided RDMA due to its remote CPU involvement. However, the heavy use of one-sided RDMA introduces fundamental limitations. Its limited APIs cannot express complex system functions such as starvation prevention, priority-based scheduling, and preemption, which are all critical functions in concurrency control protocols. Moreover, indexing requires multiple network round-trips, causing network amplification.
  In this work, we revisit the long-standing debate between one-sided RDMA and two-sided RDMA in the context of disaggregated memory databases. We present Lotus, which addresses the conventional limitation of two-sided RDMA, i.e., CPU bottlenecks in memory servers, by leveraging the rich functionality of two-sided RDMA with two key optimization techniques: (1) lightweight caching and (2) efficient batching. Lotus demonstrates that limited CPU resources in memory servers, when intelligently utilized, can transform a perceived weakness into a significant advantage. Our experimental study shows that Lotus achieves up to 8.2$\times$ higher throughput and 42.9$\times$ lower p999 tail latency than state-of-the-art one-sided RDMA-based approaches in YCSB benchmark.
