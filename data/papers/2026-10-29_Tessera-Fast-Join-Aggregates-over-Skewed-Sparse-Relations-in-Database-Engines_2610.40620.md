# Tessera: Fast Join-Aggregates over Skewed Sparse Relations in Database Engines

- arXiv ID: `2610.40620v1`
- Authors: Gyuyeong Kim
- Published: 2026-10-29
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.40620v1) | [pdf](https://arxiv.org/pdf/2610.40620v1)

## Abstract

Join-aggregate queries count or sum matching rows for each pair of values, often over skewed sparse relations in which a few values are frequent and most pairs of values never co-occur. Conventional execution plans materialize billions of intermediate join rows, taking minutes to tens of minutes per query. Recent matrix-based solutions reformulate these queries as matrix multiplication to reduce or avoid this materialization. However, they remain slow because they either store result cells for non-matching pairs or still materialize intermediate join rows for infrequent values. We present Tessera, a skew-aware join-aggregate operator for database engines that avoids both sources of overhead. Specifically, Tessera computes a sparse matrix product directly over the engine's rows, emits only nonzero cells as result rows, and prunes values that cannot meet the query's threshold before multiplication begins. It also offloads the dense block formed by pairs of the most frequent values to a CPU matrix accelerator when that block is dense enough. Experimental results show that Tessera is faster than the fastest existing system by 2.8x to 18.8x. In addition, Tessera outperforms DuckDB's execution plans by up to 1,802x.
