# Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting

- arXiv ID: `2607.19679v1`
- Authors: Xinjie Hu, Zhengjie Miao
- Published: 2026-07-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.19679v1) | [pdf](https://arxiv.org/pdf/2607.19679v1)

## Abstract

Materialized views (MVs) accelerate OLAP and data-warehouse workloads by precomputing reusable subexpressions, but practical MV-based query acceleration is a multi-stage pipeline: candidate enumeration, view selection under storage budgets, and query rewriting inside the optimizer. Existing evaluations typically study only parts of this pipeline and within a single system, leaving end-to-end trade-offs and cross-system behavior unclear.
  In this paper, we benchmark MV-based query rewriting by jointly evaluating enumeration, selection, and rewriting with a modular evaluation framework and by using controlled ablations. We also introduce a cross-engine protocol allowing us to compare systems that expose only execution plans by contrasting native optimizer-level rewriting with portable SQL rewriting baselines when available. Across representative academic methods and modern open-source and commercial systems, we find strong interaction effects across stages and large variability in MV usage and realized savings. We identify recurring failure modes that explain performance regressions after rewriting. Our results highlight which pipeline stages most often limit performance and provide evidence to guide future MV enumeration, selection, and rewriting designs.
