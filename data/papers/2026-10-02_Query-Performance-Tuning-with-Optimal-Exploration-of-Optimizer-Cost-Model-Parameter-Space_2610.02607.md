# Query Performance Tuning with Optimal Exploration of Optimizer Cost Model Parameter Space

- arXiv ID: `2610.02607v1`
- Authors: Wentao Wu, Xiaoying Wang, Vivek Narasayya, Surajit Chaudhuri
- Published: 2026-10-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.02607v1) | [pdf](https://arxiv.org/pdf/2610.02607v1)

## Abstract

Modern query optimizers use analytical cost models to estimate the cost of a given query plan. Such cost models are typically functions of a set of "cost units" that specify unit CPU cost when processing a row or unit IO cost when accessing a disk page. These cost units are traditionally viewed as platform-dependent constants, that is, they require a one-shot calibration when a database is deployed on a hardware/software platform, but are fixed afterward regardless of the query being optimized for. Some very recent work has taken a different perspective by viewing these cost units as tunable parameters that we call "cost model parameters (CMPs)" in this paper. However, so far there is no approach that offers any optimality guarantee for the tuning results. We present a new approach to systematically explore the query plan space spanned by the CMPs and find the best plan in terms of execution time. Compared to alternative exploration approaches that use random search (RS) or Bayesian optimization (BO), our new approach is deterministic and, therefore, avoids the undesirable instability that is inevitable when applying RS or BO. Moreover, it is guaranteed to find all candidate plans in the query plan space without suffering from the overhead of an exhaustive enumeration. We also present a set of optimization techniques to reduce the overall evaluation time spent on executing the candidate plans found, a factor that is often overlooked by previous work but is critical from a practical point of view. Experimental evaluation on top of PostgreSQL and Microsoft SQL Server demonstrates the efficacy of tuning the CMPs, which can find query plans that are orders of magnitude faster in execution time than the ones found by RS or BO.
