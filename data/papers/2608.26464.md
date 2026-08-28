# VoS: Variate Ordering Strategies for Skyline Query Optimization

- arXiv ID: `2608.26464v1`
- Authors: Abhinav Gorantla, Pratanu Mandal, K. Selçuk Candan, Maria Luisa Sapino
- Published: 2026-08-26
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.26464v1) | [pdf](https://arxiv.org/pdf/2608.26464v1)

## Abstract

Efficiency of skyline algorithms is highly influenced by the underlying data characteristics. Traditionally, optimization efforts have focused on minimizing the total number of tuple-pair dominance checks to improve query performance. However, in practice, a dominance check between two tuples does not necessarily require evaluating dominance relationships for each and every preference attribute of the data and this creates a disconnect between dominance checks optimization and query execution performance. In this paper, we argue that skyline algorithms need to optimize total per-attribute dominance checks, along with per-tuple dominance checks and that, for both of these goals, the ordering of the attributes (or variates) can have a substantial impact on the efficiency of skyline computation. Based on this premise, we present several strategies for identifying an effective variate order to minimize redundant attribute comparisons. Extensive experiments on both synthetic and real-world datasets, and on both scalar and SIMD architectures, confirm the effectiveness of the proposed approach in reducing computational overhead and improving skyline query performance.
