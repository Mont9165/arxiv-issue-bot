# BoomHQ: Learning to Boost Multiple Hybrid Queries on Vector DBMSs

- arXiv ID: `2604.24552v1`
- Authors: Ermu Qiu, Tianyi Chen, Jun Gao, Xing Wei, Yaofeng Tu, Yinjun Han, Yang Lin
- Published: 2026-04-27
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.24552v1) | [pdf](https://arxiv.org/pdf/2604.24552v1)

## Abstract

Hybrid queries, which combine vector nearest neighbor searches with scalar predicates, represent a fundamental challenge in managing vector databases. Existing methods often restrict the number of vector columns involved or the complexity of scalar predicates, thereby limiting their flexibility in handling diverse query patterns. Moreover, these approaches typically do not fully leverage the correlations between scalar and vector attributes, or the distributional patterns observed from query vector neighborhoods. To address these limitations, we introduce BoomHQ, a learning-based framework to boost multiple hybrid queries on vector DBMSs. First, BoomHQ models the correlation between vector and scalar attributes using an autoencoder-based architecture, which is also friendly to data updates. Second, BoomHQ captures prevailing query patterns, particularly using estimated selectivity of scalar predicates within the neighborhood of a query vector. Guided by these two key features, BoomHQ predicts the execution hints and rewrites the original query into an optimized version. Furthermore, we extend well-known benchmarks by introducing vector and scalar data with inherent correlations to better evaluate query execution. Experimental results demonstrate that for multiple hybrid queries at specified recall thresholds, our method achieves a 2x average and over 25x peak speedup compared to the state-of-the-art. Additionally, BoomHQ shows strong robustness against data updates and consistent optimization effectiveness across three representative vector database systems.
