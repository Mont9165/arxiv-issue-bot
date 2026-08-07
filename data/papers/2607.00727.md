# Approximate Nearest Neighbor Search with Graph Range Filters

- arXiv ID: `2607.00727v1`
- Authors: Qian Tao, Yuntao Jiang, Yongxin Tong, Yu Sun
- Published: 2026-07-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.00727v1) | [pdf](https://arxiv.org/pdf/2607.00727v1)

## Abstract

Vector databases have become a fundamental component for high-dimensional vector retrieval in artificial intelligence applications. Recent research has focused on filtered approximate nearest neighbor search (filtered ANN), which involves retrieving the nearest vectors that satisfy a given attribute-based filter. However, existing filters are generally limited to numerical range constraints or categorical existence checks, which restricts their applicability in more complex, real-world scenarios. In this paper, we investigate filtered ANN using graph range filters, where the retrieved vectors must be within a specified distance from the query node in a predefined filter graph. To address this problem, we propose DLH, a Distance-aware Labeling index with Hashing compression. DLH creates distance-aware labeling sets to enable efficient graph range filters via the simplified set intersection operations. Large labeling sets are further compressed into Bloom filters to improve query efficiency in DLH. Furthermore, recognizing that the query node is always involved in in-range queries of the graph range filters, we enhance DLH by memoizing the intermediate hashing index for the query node, yielding an optimized version called DLH-M. Experimental evaluations on diverse datasets demonstrate that DLH and DLH-M improve throughput by up to 70.3%, and could maintain recall rates over 98.5% with limited extra storage, validating the practical availability of the proposed solution.
