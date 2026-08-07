# LEARNT: A Practical Estimator for Cardinality of LIKE Queries with Formal Accuracy Guarantees

- arXiv ID: `2605.24308v1`
- Authors: Hai Lan, Zhifeng Bao, Divesh Srivastava, Shixun Huang, Yuwei Peng, Yang Yu
- Published: 2026-05-23
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.24308v1) | [pdf](https://arxiv.org/pdf/2605.24308v1)

## Abstract

We study the problem of cardinality estimation for LIKE queries on string data, focusing on the most common patterns in real workloads: prefix, suffix, and substring queries. We propose LEARNT, a LIKE query Estimator with Accuracy, Robustness, Negligible overhead, Tunability, and Theoretical guarantees. LEARNT formulates estimation as a bucket-classification problem, and upon correct classification, it yields formal bounds on Q-error for the queries with non-empty answer. It employs a memory-efficient bucketed layered-filter architecture with Bloom filters and compact auxiliary tables, together with optimizations that exploit query skew to reduce storage. For the queries that have empty answer, LEARNT incorporates dedicated filter-based and prefix-walk strategies, providing probabilistic guarantees on correct identification. Furthermore, to support arbitrarily long query strings, we extend LEARNT with Markov modeling scheme that composes short-query statistics into estimates for longer queries. A theoretical framework guides parameter selection to minimize storage under accuracy and robustness constraints. Extensive experiments on four real-world datasets show that LEARNT consistently outperforms state-of-the-art methods such as CLIQUE and LPLM, achieving 1.3-1.7x lower mean Q-error, significantly lower tail errors, and up to 70x faster construction with comparable memory usage.
