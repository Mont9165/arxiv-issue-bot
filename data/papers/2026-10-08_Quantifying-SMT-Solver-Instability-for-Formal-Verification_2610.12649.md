# Quantifying SMT Solver Instability for Formal Verification

- arXiv ID: `2610.12649v1`
- Authors: Daniel Evans, Rylie Hansen, John Shorter
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.12649v1) | [pdf](https://arxiv.org/pdf/2610.12649v1)

## Abstract

Program verification has become commonplace in software development projects, and much of its feasibility can be attributed to the potential of SMT solvers to automate model checking and other verification techniques. However, SMT instability, a phenomenon where semantically equivalent permutations of source code take much longer to solve or timeout, has been found to interrupt workflows and make software engineers more likely to avoid verification. Previous efforts to measure SMT instability have had difficulty quantifying it due to the abnormal runtime distributions it produces. In this paper, we use the coefficient of variation to model instability across an extensive dataset of SMT queries from three software domains. Our results show that SMT instability is significant in each area, and that it increases for queries that take longer on average. However, using a novel method to quantify instability, we show that a different approach is possible: if a solution were to optimize the structure of queries for runtime, rather than variance, instability could be mitigated while also improving overall solver performance.
