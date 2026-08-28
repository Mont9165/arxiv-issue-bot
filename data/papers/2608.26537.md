# IBLTs Measure Before They Decode: Self-Sizing Set Reconciliation from Pre-Peeling Counts

- arXiv ID: `2608.26537v1`
- Authors: Min Wu, Ji Qi, Chengdui Luo, Shudong Lu, Zhengsheng Ye, Zhengyang Wei
- Published: 2026-08-27
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2608.26537v1) | [pdf](https://arxiv.org/pdf/2608.26537v1)

## Abstract

Set reconciliation recovers the symmetric difference $A\triangle B$ with communication far below the data volume. Invertible Bloom Lookup Tables (IBLTs) are a standard tool, but their capacity must match the unknown difference cardinality~$d$. In database deployments, $d$ spans orders of magnitude, so undersizing causes rescans or replays while oversizing wastes network and memory.
  We show that an IBLT measures $d$ before decoding. Each cell count records how many difference elements map to it; a quadratic statistic over the count array gives an exactly unbiased estimate with no extra transmitted bytes. The estimate remains valid after decoding failure because it is read from the same sketch. For standard IBLTs, we derive exact mean and variance formulas and chi-square confidence intervals. The same chi-square law governs failed instances in deep overload. A mapping-aware theorem extends the construction to Irregular, Rateless, and MET IBLTs through per-variant adapters.
  Our self-sizing protocol uses a first-round failure to compute the second-round capacity in one step, completing within two interaction rounds with an explicit success-probability guarantee. We profile 41{,}603 reconciliation runs over 90 days at NineData Cloud, compare end-to-end against Merkle-style localization in a cross-engine replay of production tables, and deploy across Redis and Pika in China Mobile. The first round therefore turns an unknown difference cardinality into a measurement it has already paid for.
