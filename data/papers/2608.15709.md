# Logos: Certified Order-Sensitive SQL Rewrites with Mechanized Semantics and LLM Guidance

- arXiv ID: `2608.15709v1`
- Authors: Jingyu Ke, Jingyang Li, Guoqiang Li
- Published: 2026-08-16
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.15709v1) | [pdf](https://arxiv.org/pdf/2608.15709v1)

## Abstract

SQL rewrite verification must account for duplicate rows, observable row order, and typed value semantics. Existing verifiers have yet to combine proofs over database instances of arbitrary finite cardinality with an ordered-list semantics for nested, tie-sensitive top-k. Unbounded systems reason primarily over bags or handle ordering through syntax-directed restrictions, whereas bounded systems either support only restricted top-k forms or impose a deterministic ordering rather than retain all legal tie-induced outcomes. Support for typed expression and aggregate semantics, observable runtime errors, and integrity constraints also remains partial.
  In Rocq, we mechanize a compositional logical semantics for a typed SQL core with order-sensitive operators, capturing all possible ordered lists and observable SQL failures in the supported fragment. To our knowledge, this is the first mechanized SQL semantics to combine nested, tie-sensitive top-k with a closure-based lifting from bag equivalence to ordered-list equivalence, enabling sound reuse of bag-theoretic reasoning while preserving compositionality across order-sensitive and correlated contexts. The formalization further provides executable semantics for PostgreSQL-oriented scalar and aggregate evaluation and an explicit account of integrity constraints. Building on this semantics, we present Logos, an LLM-guided Rocq verifier for unbounded SQL rewrite equivalence. Its agent uses a verified SQL-specific lemma library to construct query-specific Rocq proofs. Our evaluation covers 389 query pairs from Apache Calcite optimizer tests, TPC-H and TPC-DS rewrites, and WeTune's real-application workloads. Logos solves 86.9% of them, compared with 64.0% for SQLSolver, the strongest baseline.
