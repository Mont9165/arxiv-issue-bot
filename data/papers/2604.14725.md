# RELOAD: A Robust and Efficient Learned Query Optimizer for Database Systems

- arXiv ID: `2604.14725v1`
- Authors: Seokwon Lee, Jaeyoung Sim, Sihyun Kim, Yuhsing Li, Yiwen Zhu, Kwanghyun Park
- Published: 2026-04-16
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.14725v1) | [pdf](https://arxiv.org/pdf/2604.14725v1)

## Abstract

Recent advances in query optimization have shifted from traditional rule-based and cost-based techniques towards machine learning-driven approaches. Among these, reinforcement learning (RL) has attracted significant attention due to its ability to optimize long-term performance by learning policies over query planning. However, existing RL-based query optimizers often exhibit unstable performance at the level of individual queries, including severe performance regressions, and require prolonged training to reach the plan quality of expert, cost-based optimizers. These shortcomings make learned query optimizers difficult to deploy in practice and remain a major barrier to their adoption in production database systems. To address these challenges, we present RELOAD, a robust and efficient learned query optimizer for database systems. RELOAD focuses on (i) robustness, by minimizing query-level performance regressions and ensuring consistent optimization behavior across executions, and (ii) efficiency, by accelerating convergence to expert-level plan quality. Through extensive experiments on standard benchmarks, including Join Order Benchmark, TPC-DS, and Star Schema Benchmark, RELOAD demonstrates up to 2.4x higher robustness and 3.1x greater efficiency compared to state-of-the-art RL-based query optimization techniques.
