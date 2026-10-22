# Building SQL Equivalence Proofs from Query Rewrite Rules

- arXiv ID: `2610.30100v1`
- Authors: Chunyu Chen, Xinyi Huang, Zhengjie Miao
- Published: 2026-10-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.30100v1) | [pdf](https://arxiv.org/pdf/2610.30100v1)

## Abstract

Query rewriting and semantic evaluation of text-to-SQL systems both depend on deciding whether two SQL queries return the same result on every database satisfying the schema constraints. Decades of equivalence-preserving optimizer rules provide a natural basis for constructive proofs: two queries are equivalent when admitted rewrites transform them to a common logical expression. Building on this observation, \sys{} organizes query-rewriting knowledge as a standalone proof-producing system. It separates rule validation from proof discovery, explicitly aligns alternative query representations, and returns the resulting rewrite derivation. Across three corpus classes, EquiTrace proves 648/1,106 expected-equivalent text-to-SQL pairs (58.6%), 229/266 curated pairs (86.1%), and 97/240 LLM-generated rewrites whose results agree under benchmark execution (40.4%). On the query rewrite corpus, EquiTrace proves 97 pairs, compared with 35 for QED and 38 for SQLSolver. An analysis of 1,242 recorded proofs shows that coverage depends on a small number of transformations, while many frequently used rules are individually substitutable. The resulting derivations make each proof replayable and expose the specific transformations on which it depends.
