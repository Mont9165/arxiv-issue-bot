# AgenticDB: Agentic Performance Reconfiguration for Database Workloads

- arXiv ID: `2606.20318v1`
- Authors: Xinyue Yang, Chaozheng Wang, Chen Zheng, Heng Zhang, Yanjun Wu
- Published: 2026-06-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.20318v1) | [pdf](https://arxiv.org/pdf/2606.20318v1)

## Abstract

Database configuration tuning is critical for workload performance, but practical tuning on real deployments remains difficult. Existing automatic tuners mostly formulate tuning as iterative search over DBMS knob values. This formulation leads to high execution cost, prematurely narrows the configuration space, and leaves practical requirements insufficiently addressed: diagnosing runtime bottlenecks from system feedback, exploring OS-level reconfiguration opportunities, executing changes robustly, and learning from previous trials and tasks.
  We propose AgenticDB, an agentic framework for database workload reconfiguration. AgenticDB implements a context-grounded harness that interacts with the target database environment by proposing DBMS- and OS-level changes, applying them under safety constraints, observing workload performance and runtime states, and using execution feedback to guide subsequent decisions. This runtime interaction enables AgenticDB to diagnose bottlenecks, explore a broader DBMS- and OS-level reconfiguration space, avoid unsafe or unsupported actions, and accumulate experience within and across reconfiguration tasks. As a result, AgenticDB turns database tuning into a self-refining reconfiguration process in which runtime feedback iteratively improves later decisions.
  We conduct extensive experiments on MySQL and PostgreSQL using YCSB, Sysbench, and TPC-H workloads. The results show that AgenticDB achieves the best final performance on all evaluated workloads, improving over the strongest baseline by 118.1% on average and reducing aggregate time-to-best by 22.6%. The results also demonstrate that its OS-level action space, robust execution lifecycle, and memory-enhanced planning contribute to more effective and practical database reconfiguration.
