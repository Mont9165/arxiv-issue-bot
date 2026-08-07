# SQL-RewriteBench: A Correctness-Gated, Full-Denominator Benchmark for Statement-Level SQL Rewriting [Experiment,Analysis & Benchmark]

- arXiv ID: `2607.09251v1`
- Authors: Jiang Long, Tianci Gao, Shiyuan Hao, Haochen Zhang, Shuncheng Liu, Jiang Zhang
- Published: 2026-07-10
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.09251v1) | [pdf](https://arxiv.org/pdf/2607.09251v1)

## Abstract

Statement-level SQL rewriting can improve query performance and maintainability without changing the DBMS kernel, but existing benchmarks do not evaluate rewrite methods as deployable systems. They typically focus on DBMS performance, rule regression, query equivalence, or dialect translation, while missing the full path from accepting an input query to producing an executable, result-consistent, and operationally useful rewrite. We present SQL-RewriteBench, a benchmark for statement-level SQL rewriting that applies correctness gating and full-denominator accounting. Its metric suite explicitly separates Source Acceptance, Generation Rate, Execution Coverage, Result Consistency, UnsafeRewrite Rate, and speedup distribution. It also defines SCS, a deterministic index of static SQL structure, and CGOQ, a correctness-gated optimization-quality score that gives optimization credit only after the case-specific Checker Contract is satisfied. CGOQ combines runtime improvement with structural simplification through a continuous scoring function, making it suitable for deployment-oriented rewrite assessment. As an artifact, SQL-RewriteBench provides 180 executable Benchmark Instances organized into EQUIV, PERF, ROBUST, and DIALECT pools, each packaged with SQL, schema metadata, provenance, evidence, and rewrite-opportunity documentation. Across seven representative academic and LLM-based methods, every full-benchmark CGOQ is negative. Existing methods often fail before rewriting, fail result checks, or return correct rewrites that are slower or no better than the input. These results show that deployable SQL rewrite requires broader input handling, result validation, and benefit-aware rewrite decisions.
