# Hollywood: Towards a Large Movie Dataset for Database Benchmarking

- arXiv ID: `2607.19666v1`
- Authors: Ivan Iachnyk, Mihail Stoian, Andreas Kipf
- Published: 2026-07-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.19666v1) | [pdf](https://arxiv.org/pdf/2607.19666v1)

## Abstract

The IMDb real-world dataset of the JOB benchmark has been extensively used in the last decade as part of the research line on cardinality estimation, given its ability to stress test both traditional and learned estimators. However, unlike the synthetic TPC family, it does not come with a scale factor, being a simple dump. We introduce Hollywood, a synthetic IMDb-compatible benchmark generator that combines LLM-generated semantic dictionaries with deterministic temporal-graph-based relational data generation. We analyze a preliminary Hollywood-200K, which contains 200,000 primary movies, generated series and episode title rows, 19.7M IMDb-style rows, and 213 nonzero JOB-Light, JOB, and JOB-Complex queries. Experiments with two open systems demonstrate that Hollywood induces cardinality estimation errors comparable to or exceeding those observed on the original IMDb dataset. The release includes generation settings and prompt/LLM-output provenance together with adapted SQL and labels, enabling tests of whether cardinality estimators generalize beyond a fixed movie snapshot and distribution.
