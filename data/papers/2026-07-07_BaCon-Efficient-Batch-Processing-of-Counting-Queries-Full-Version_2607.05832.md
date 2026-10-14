# BaCon: Efficient Batch Processing of Counting Queries [Full Version]

- arXiv ID: `2607.05832v1`
- Authors: Yuxi Liu, Xiao Hu, Pankaj K. Agarwal, Jun Yang
- Published: 2026-07-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.05832v1) | [pdf](https://arxiv.org/pdf/2607.05832v1)

## Abstract

Counting queries are ubiquitous in database systems, particularly for driving internal system optimization. Learned models for cardinality estimation rely heavily on large-scale training data, yet generating such data by executing massive batches of counting queries is expensive. We propose BaCon, an efficient algorithm for batch evaluation of counting queries on top of a database system, without modifying its internals. BaCon integrates the idea of factorized databases with a workload-aware domain quantization strategy, allowing it to evaluate batches of counting queries using compact data structures rather than materializing massive join results. BaCon's design is compatible with most database management system, and we have implemented it as a client-side application on PostgreSQL with a lightweight C-language UDF (user-defined function). This implementation delivers speedups between 2$\times$ and 178$\times$ over baselines and good performance across various workloads, making training and maintenance of learned cardinality estimation models significantly more practical.
