# UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval

- arXiv ID: `2611.20758v1`
- Authors: Keyu Chen, Xiaoyao Zhong, Jiabao Jin, Peng Cheng, Wangze Ni, Jingkuan Song, Heng Tao Shen
- Published: 2026-11-16
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.20758v1) | [pdf](https://arxiv.org/pdf/2611.20758v1)

## Abstract

Hybrid dense-sparse vector retrieval combines semantic signals from dense representations with lexical signals from sparse representations, typically ranking items by a query-dependent weighted sum of dense and sparse vector distances. Existing systems commonly search separate dense and sparse vector indexes and rerank the union of their candidates, incurring two retrieval passes and potentially discarding items that rank highly only after the semantic and lexical signals are combined. Constructing a graph-based index directly under a hybrid distance can mitigate this premature candidate loss. However, because varying the hybrid weight alters the underlying neighborhood relationships, a single static graph built at a fixed weight cannot accommodate dynamic query-specific weights. Therefore, we propose a Unified Hybrid Graph (UniGraph), which merges neighbor sets computed at multiple hybrid weights into a single bounded-degree graph index, enabling hybrid vector retrieval with different query-specific weights without index reconstruction. We further develop an adaptive weight-guided search framework that chooses between sparse- and dense-guided entry points according to the query weight, together with a dense-first hybrid distance pruning strategy that avoids unnecessary exact sparse distance computations. Extensive experiments show that UniGraph provides a favorable Recall-QPS trade-off across different query weights. In the mixed-weight setting, UniGraph delivers 27.6%~52.3% higher QPS than the fastest baseline on each dataset at Recall@100 greater than or equal to 0.95. UniGraph has been deployed at scale in Ant Group's production environment, where hybrid retrieval with query-dependent weights is in strong demand.
