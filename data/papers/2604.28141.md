# Index-Assisted Stratified Sampling for Online Aggregation

- arXiv ID: `2604.28141v1`
- Authors: Yunnan Yu, Zhuoyue Zhao
- Published: 2026-04-30
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.28141v1) | [pdf](https://arxiv.org/pdf/2604.28141v1)

## Abstract

Ad-hoc queries over frequently updated data in a flat schema are common in real-time data analysis applications and often require very low latency. Online aggregation can achieve so by providing approximate aggregation answers with confidence bound guarantees. It relies on the ability to draw samples online in a linear time to sample size rather than database size, which can be supported by index-assisted Sampling-based Approximate Query Processing (S-AQP) systems. However, the query latencies of approximate queries in these systems can still suffer from excessive sampling cost required to achieve a desired confidence bound, due to increased sample size for data with high variance in value distribution and selectivity. Classic stratified sampling methods with Neyman allocation can minimize sample size in theory, but several challenges prevent it from being applicable in index-assisted S-AQP systems, including requiring apriori statistics, high optimization cost, and inaccurate sampling cost model based on sample size. Towards that, we design index-assisted stratified sampling for online aggregation, which features a two-phase sampling framework. Samples drawn from first phase are used for both online aggregation and optimizing future sampling cost, while the second phase continues the online aggregation using the optimized strata. We prove optimal stratification and sample size allocation strategies for index-based sampling cost model, and design several greedy and dynamic programming based optimization methods to balance optimization cost and effectiveness in cost reduction. We evaluate our methods on several real-world and synthetic datasets and queries, and the results show ours consistently achieve good speedup and, in extreme cases, up to 3x speedup and 98708x speedup, when compared to index-assisted uniform sampling and classic scan-based stratified sampling respectively.
