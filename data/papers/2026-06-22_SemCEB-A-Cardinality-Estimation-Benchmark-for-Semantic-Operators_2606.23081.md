# SemCEB: A Cardinality Estimation Benchmark for Semantic Operators

- arXiv ID: `2606.23081v1`
- Authors: Andreas Zimmerer, Claudius Kühn, Yang Li, Mihail Stoian, Renata Borovica-Gajic, Andreas Kipf
- Published: 2026-06-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.23081v1) | [pdf](https://arxiv.org/pdf/2606.23081v1)

## Abstract

Modern data systems increasingly expose multi-modal large language models as semantic operators: SQL operators, including filters and joins, whose predicates are defined by a natural-language instruction. Query optimization in these systems still rests on the same foundations as in traditional databases$\unicode{x2013}$plan enumeration and cost models$\unicode{x2013}$yet faces new challenges, e.g., a larger plan space and the lack of efficient cardinality estimates. The elevated per-tuple costs of semantic operators make bad plan choices worse by orders of magnitude. Therefore, precise$\unicode{x2013}$but also fast and cheap$\unicode{x2013}$cardinality estimates for semantic filters and joins are of high importance for optimizing query plans that include semantic operators.
  In this paper, we introduce SemCEB, the first benchmark for cardinality estimation over semantic operators, based on a real-world dataset of (semi-)structured text and images with 102 hand-curated, diverse queries spanning a wide range of selectivities, assessing cardinality estimation for semantic filters and joins in isolation. We evaluate sampling-based algorithms and Semantic Histograms, a state-of-the-art cardinality estimation algorithm for semantic operators, with respect to their accuracy, cost, latency, and memory overhead. We show that, while sampling is robust across different predicate categories, it does not scale and comes with high costs. Our adaptation of Semantic Histograms, on the other hand, is limited in its applicability, and its performance appears sensitive to the predicate category.
