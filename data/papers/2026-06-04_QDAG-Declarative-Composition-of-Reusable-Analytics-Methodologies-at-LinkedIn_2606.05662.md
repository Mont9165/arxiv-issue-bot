# QDAG: Declarative Composition of Reusable Analytics Methodologies at LinkedIn

- arXiv ID: `2606.05662v1`
- Authors: Peter Ho, Praveen Chaganlal, Tianle Zhang, Endong Zhu
- Published: 2026-06-04
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.05662v1) | [pdf](https://arxiv.org/pdf/2606.05662v1)

## Abstract

Production analytics products often depend on reusable methodologies: multi-step definitions such as headcount growth, top-skill growth, or differentially-private impression distributions. Although these methodologies define business-critical numbers, they are commonly implemented as imperative glue around OLAP queries, service calls, joins, transformations, and conditional logic. As a result, teams duplicate orchestration code, definitions drift across products, and methodologies are difficult to test or analyze.
  We present QDAG, a production system at LinkedIn that represents an analytics methodology as a declarative directed acyclic graph of typed steps. Nodes may execute Apache Pinot queries, downstream service calls, in-memory SQLite joins, jq transformations, conditionals, differentially-private aggregations, or calls to other QDAGs. The engine evaluates graphs demand-driven, memoized, pruned, and parallelized in the per-request analytics mid-tier. QDAG is deployed across more than 500 hosts and over 100 production use cases, adding roughly 10 ms median orchestration overhead and under 50 ms at the 99th percentile. Our experience shows that making methodologies declarative improves reuse, testability, and cross-product consistency while preserving interactive latency.
