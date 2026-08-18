# Efficient Privacy-Preserving Range Filtered Approximate Nearest Neighbor Search

- arXiv ID: `2608.16488v1`
- Authors: Haoyu Wang, Yandi Zhang, Jiadong Xie, Yingfan Liu, Hui Li, Jeffrey Xu Yu, Jiangtao Cui
- Published: 2026-08-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.16488v1) | [pdf](https://arxiv.org/pdf/2608.16488v1)

## Abstract

Range-filtered approximate nearest neighbor search (RFANNS) is an important primitive for vector databases; it retrieves vectors that are similar to a query and satisfy a numerical range predicate, but existing RFANNS indexes expose vectors, attributes, and queries in plaintext. This assumption is unsuitable for outsourced vector databases, where sensitive data and queries must be protected from an honest-but-curious cloud server. To the best of our knowledge, this is the first study that systematically formulates and evaluates privacy-preserving RFANNS over outsourced encrypted vector databases. Our approach separates range localization from encrypted vector search: an authorized user maps the query range to a compact set of nodes in a local N-ary attribute tree, and the server searches only the corresponding proximity graph sub-indices over encrypted vectors. To reduce expensive encrypted comparisons, we use a filter-and-refine pipeline that first retrieves coarse candidates with approximate distance-comparison-preserving encryption and then reranks a small candidate set with exact distance-comparison encryption. We then analyze the computation, storage, communication, and leakage of the protocol. Experiments on four widely used vector datasets show that our method improves the QPS-Recall trade-off over representative secure adaptations of existing RFANNS approaches, scaling effectively to large datasets.
