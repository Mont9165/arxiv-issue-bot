# TraHist: Fast and Accurate Cardinality Estimation for Trajectory Data (Extended Version)

- arXiv ID: `2610.22310v1`
- Authors: Yujeong Jo, Incheol Baek, Changbeom Shim, Yon Dohn Chung
- Published: 2026-10-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.22310v1) | [pdf](https://arxiv.org/pdf/2610.22310v1)

## Abstract

Cardinality estimation is fundamental for query optimization in database systems. Histogram-based estimators are widely used for their simplicity and efficiency but rely on point-centric partitioning that assumes record independence. This assumption breaks in trajectory data, where records from the same moving object show strong spatiotemporal dependencies. Conventional axis-aligned histograms therefore fragment trajectories across partition boundaries, leading to overestimation through duplicate counting. This error reflects a structural limitation of partition boundaries that are misaligned with trajectory-induced density patterns. To this end, we propose TraHist, a histogram-based estimator approximating density-aligned partitioning via efficient grid-based propagation. TraHist builds density-adaptive rectilinear buckets to preserve trajectory continuity and local density coherence while keeping histogram efficiency. Experiments on large-scale real-world datasets show that TraHist reduces estimation error by over 20x relative to the strongest competing estimator in query regimes where trajectory fragmentation is a dominant source of estimation error, while maintaining sub-millisecond query latency and competitive construction cost.
