# Tailwind: A Practical Framework for Query Accelerators

- arXiv ID: `2604.28079v1`
- Authors: Geoffrey X. Yu, Ryan Marcus, Tim Kraska
- Published: 2026-04-30
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.28079v1) | [pdf](https://arxiv.org/pdf/2604.28079v1)

## Abstract

Relational database management systems (RDBMSes) can process general-purpose queries, but often have lower performance compared to custom-built solutions for specific queries. For example, consider a group-by query over a few known groups (e.g., grouping by country). While an RDBMS would likely use a hash map to do the grouping, a faster method could hard-code the expected groups into the query executor. But such workload-specific techniques, which we call query accelerators, are not widely used in practice because the engineering effort (optimizer and engine changes, potential bugs) does not justify the isolated performance gains (speedup on a single specific query). We propose Tailwind: an external query planner that brings accelerators into any RDBMS that supports data import/export. Users define their accelerators using abstract logical plans (ALPs): a new mostly-declarative abstraction over relational operators built on regular tree expressions. ALPs allow Tailwind to automatically build customized neural network models to estimate when using a particular accelerator is beneficial. At runtime, Tailwind sits atop an RDBMS and transparently rewrites queries to run across one or more accelerators when predicted to be beneficial, falling back to the underlying RDBMS when not. On Redshift and DuckDB with a library of four diverse accelerators, Tailwind accelerates TPC-H queries by 1.38x on average (up to 29x).
