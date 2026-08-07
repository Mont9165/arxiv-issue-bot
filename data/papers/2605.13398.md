# FPGA-Accelerated Lock Management and Transaction Processing: Architecture, Optimization, and Design Space Exploration

- arXiv ID: `2605.13398v1`
- Authors: Shien Zhu, Gustavo Alonso
- Published: 2026-05-13
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2605.13398v1) | [pdf](https://arxiv.org/pdf/2605.13398v1)

## Abstract

Online Transaction Processing (OLTP) is a classic application with a growing business. CPU-based OLTP has low lock serving efficiency. The main reason is that most locks are cold, and the lock agent must issue frequent memory accesses to retrieve the lock details to determine whether to grant it. This motivates us to propose dedicated hardware-based lock agents with integrated lock tables to remove the DRAM access overhead.
  In this paper, we propose hardware-accelerated lock management and transaction processing for database systems. First, we propose a low-latency lock agent optimized for both lock acquiring and releasing requests. Second, we design a scalable transaction agent that executes the full transaction lifecycle. We present the architecture, optimizations, and design-space exploration of the proposed lock management and transaction processing system. The experiment results show up to 51X higher transaction throughput over the CPU baseline on the TPC-C benchmark.
