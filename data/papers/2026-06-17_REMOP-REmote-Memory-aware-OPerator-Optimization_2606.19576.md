# REMOP: REmote-Memory-aware OPerator Optimization

- arXiv ID: `2606.19576v1`
- Authors: Shiquan Zhang, Yunhao Mao, Yuqiu Zhang, Gengrui Zhang, Jeyhun Karimov, Hans-Arno Jacobsen
- Published: 2026-06-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2606.19576v1) | [pdf](https://arxiv.org/pdf/2606.19576v1)

## Abstract

Remote and disaggregated memory tiers expand the effective memory capacity of analytical database engines, but they also reshape the cost structure of out-of-memory query processing. When an operator spills beyond local DRAM, moving pages to remote memory incurs both data-transfer time and a fixed round-trip latency per transfer. Classical operator analyses and buffer-allocation heuristics primarily target disk spilling by minimizing total I/O volume. Under remote memory, these strategies can be suboptimal because they may trigger excessive transfer rounds. We present REMOP, a remote-memory-aware operator optimization framework that uses transfer-round-aware intra-operator memory policies to improve out-of-memory execution under tight memory budgets. REMOP introduces the number of transfer rounds into the latency cost model and derives operator-specific buffer-partitioning strategies, instantiating the approach for blocked nested-loop join, external merge sort, and external hash join in DuckDB. Our evaluation on a two-node compute-memory testbed shows that REMOP reduces transfer rounds by up to 97% and operator runtime by up to 48% on spill-heavy microbenchmarks, and lowers the average runtime of spilling TPC-H and TPC-DS queries by 22.7% and 26.4% end-to-end.
