# BranchBench: Aligning Database Branching with Agentic Demands

- arXiv ID: `2604.17180v1`
- Authors: Elaine Ang, Sam Weldon, In Keun Kim, Kevin Durand, Kostis Kaffes, Eugene Wu
- Published: 2026-04-19
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2604.17180v1) | [pdf](https://arxiv.org/pdf/2604.17180v1)

## Abstract

Branchable databases are evolving from developer tools to infrastructure for agentic workloads characterized by speculative mutations and non-linear state exploration. Traditional RDBMS mechanisms such as nested transactions do not provide the persistent isolation and concurrent branch management required by autonomous agents, and recent "zero-copy" designs make different trade-offs whose impact on agentic workloads remains unclear.
  To clarify this space, we present BranchBench, a benchmark for evaluating branchable relational DBMSes under agentic exploration. We characterize five representative workloads-agentic software engineering, failure reproduction, data curation, MCTS, and simulation-and design parameterized macrobenchmarks that execute branch-mutate-evaluate loops to reflect these workloads, along with microbenchmarks that isolate branch lifecycle costs. We evaluate state of the art systems including Neon, DoltgreSQL, Tiger Data, Xata, and PostgreSQL baselines, and find a fundamental tension: systems optimized for fast branching suffer up to 5-4000x slower reads as branches deepen, while systems optimized for fast data operations incur 25-1500x higher branch creation and switching latency. Further, no current system supports the representative workloads at scale. These results highlight the need for branch-native DBMSes designed specifically for agentic exploration.
