# Navigating Runtime Dynamism in Semantic Query Serving

- arXiv ID: `2611.04248v1`
- Authors: Hengrui Zhang, Xupeng Miao
- Published: 2026-11-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.04248v1) | [pdf](https://arxiv.org/pdf/2611.04248v1)

## Abstract

LLM-powered semantic queries increasingly combine relational processing with multiple LLM-based operators over unstructured data. Efficiently serving such queries is challenging due to runtime dynamism at two coupled levels. Across queries, dynamic arrivals and heterogeneous resource demands continuously change scheduling priorities. Within a query, heterogeneous characteristics across fine-grained input batches cause operator costs and selectivities to vary throughout execution, making a statically optimized plan unreliable. These two forms of dynamism create a circular dependency: inter-query scheduling requires estimates of remaining LLM work, while the remaining work depends on runtime plan choices whose costs become observable only during execution.
  We present SeqoFlow, a runtime framework that jointly adapts query plans and schedules concurrent semantic queries. SeqoFlow enumerates equivalence-preserving plan alternatives under operator dependencies and decomposes queries into fine-grained units, enabling safe plan adaptation and query preemption at batch boundaries. To support both decisions without exhaustively profiling candidate plans on the target LLM, SeqoFlow uses lightweight speculative estimation to capture runtime costs. These estimates jointly guide plan adaptation and inter-query scheduling, closing the loop between query optimization and LLM inference. Experiments across diverse query structures, data distributions, and arrival rates show that SeqoFlow substantially reduces end-to-end latency compared to existing semantic query systems, adaptive query processing techniques, and conventional scheduling policies.
