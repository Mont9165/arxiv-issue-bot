# ReSequel: Robust LLM-assisted Query Rewriting and Optimization using Templatization and Sampling

- arXiv ID: `2606.20853v1`
- Authors: Saeed Fathollahzadeh, Essam Mansour, Matthias Boehm
- Published: 2026-06-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.20853v1) | [pdf](https://arxiv.org/pdf/2606.20853v1)

## Abstract

Heuristic query rewriting has long complemented cost-based optimization to improve performance. Such rewrites transform SQL queries into semantically equivalent forms that are easier or faster to execute. Examples are standardizing expressions, eliminating redundancy, propagating constants, pushing down selections and projections, unnesting queries, and utilizing constraints. Modern DBMSs implement hundreds to thousands of such rules, but maintaining them is notoriously difficult. The interactions among rules are complex, and their static nature and application order prevent adaptation to specific query and database characteristics. Recent approaches that use large language models (LLMs) for query rewriting show promise but face challenges regarding the large search space, reliable query verification, and exploitation of metadata. We present ReSequel, an outer optimization layer on top of existing DBMSs to rewrite SQL queries using LLMs. ReSequel leverages catalog and statistical metadata to infer template-specific rules that guide the LLM toward effective query transformations. We generate, verify, and rank rewritten query variants on sampled data to ensure result correctness and runtime improvements. Our experiments cover eight benchmarks: JOB, TPC-H, Stats(-CEB), Public BI, IMDB, DSB, and StackOverflow; multiple DBMSs: PostgreSQL, MySQL, and DuckDB; as well as LLM-based query rewriting baselines. ReSequel yields workload-level speedups of up to 16x over native DBMSs and 22x over LLM-based systems, with individual queries exceeding 600x, across eight benchmarks and three DBMSs.
