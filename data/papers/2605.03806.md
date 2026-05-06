# ConRAD: Conformal Risk-Aware Neural Databases

- arXiv ID: `2605.03806v1`
- Authors: Sonia Horchidan, Fabian Zeiher, Xiangyu Shi, Vasiliki Kalavri, Henrik Boström, Ioannis Kontoyiannis, Paris Carbone
- Published: 2026-05-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.03806v1) | [pdf](https://arxiv.org/pdf/2605.03806v1)

## Abstract

Querying incomplete knowledge graphs with neural predictors is powerful but dangerous. Errors compound across multi-hop pipelines with no formal bound on the completeness of results. We introduce ConRAD, the first framework to enforce declarative recall guarantees natively within a neural graph database query engine. Given a user-specified risk budget, ConRAD automatically derives per-operator prediction thresholds that satisfy the recall target with finite-sample, distribution-free statistical validity via Conformal Risk Control, while maximizing end-to-end precision. To scale calibration across multi-operator query topologies, we introduce a quantile-space scalarization that reduces intractable high-dimensional threshold searches to a single parameter. We further design the conformal gate, a novel physical operator that dynamically bypasses neural inference when local graph evidence suffices, eliminating unnecessary model inferences in dense graph regions. Evaluated across three benchmarks and three query topologies, ConRAD strictly satisfies all risk budgets, with empirical recall falling below the target by at most 0.046 across all settings. It reduces neural invocations to zero in near-complete graph regions, and achieves precision that matches or exceeds best-case static baselines that offer no guarantees and require manual threshold search.
