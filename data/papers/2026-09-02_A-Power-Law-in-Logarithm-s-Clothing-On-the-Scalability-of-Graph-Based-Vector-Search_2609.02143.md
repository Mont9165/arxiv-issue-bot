# A Power Law in Logarithm's Clothing: On the Scalability of Graph-Based Vector Search

- arXiv ID: `2609.02143v1`
- Authors: Sajad Faghfoor Maghrebi, Navid Eslami, Niv Dayan
- Published: 2026-09-02
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.02143v1) | [pdf](https://arxiv.org/pdf/2609.02143v1)

## Abstract

Most vector databases rely on graph-based indexes, notably HNSW and Vamana, for approximate nearest neighbor search. With embedding models widely adopted, the datasets these databases store grow rapidly. At a fixed accuracy, how does search cost scale with dataset size? The prevailing answer is poly-logarithmic growth. Yet the claim is proven only under special conditions and asserted without proof for the indexes used in practice. It is also largely untested: standard benchmarks measure cost at one dataset size, not across sizes. We put the claim to the test. The answer depends on the scale itself. While the dataset size $N$ is small relative to the data's intrinsic dimensionality, search cost grows as $N^c$ for a constant $0<c<1$. We call this scaling the Sublinear Power Law. Once $N$ is large enough, growth slows to subpolynomial, consistent with the poly-logarithmic claim. The Sublinear Power Law appears on every dataset, mostly up to its full size, at every recall target, query hardness level, and index configuration we test. The transition to subpolynomial growth appears on the two datasets that grow large enough relative to their intrinsic dimensionality. One mechanism underlies both behaviors: a dataset's intrinsic dimensionality grows with its size until the data resolves its underlying distribution. Higher intrinsic dimensionality packs more vectors into the query neighborhood the search must examine. We present a unifying theory of beam-search cost that explains our observations. For exact and bounded-degree constructions, we prove the Sublinear Power Law and the eventual transition to poly-logarithmic scaling, and derive the scale at which it occurs. We also develop models that predict the power-law exponents for any recall target and index configuration. These models give a principled way to navigate trade-offs among search cost, insertion cost, and recall as data grows.
