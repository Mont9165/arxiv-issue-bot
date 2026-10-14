# SemJoin: Semantic Join Optimization

- arXiv ID: `2606.29532v1`
- Authors: Christopher Gou, Aditya Banerjee, Jiaxuan Wang, Chunwei Liu
- Published: 2026-06-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.29532v1) | [pdf](https://arxiv.org/pdf/2606.29532v1)

## Abstract

Integrating unstructured data into relational database systems is increasingly important as demand grows for natural language querying and analysis. A semantic join, joining two tables under a natural-language predicate, can be evaluated with a large language model (LLM), but comparing every pair of tuples requires O(M x N) LLM invocations and is cost-prohibitive at scale. Existing systems reduce this cost but typically commit to a single fixed strategy (e.g., embedding similarity or one batched scheme) regardless of the data or the join predicate. We propose an LLM-agent-based decision pipeline that optimizes semantic joins by matching the execution strategy to the characteristics of the underlying tables. An LLM advisor routes each join to one of two strategies: a Cluster Join, which prunes candidates via unsupervised embedding clustering and sample-based filtering, or a Classifier strategy for predicates that reduce to a shared discrete label set. Across three diverse datasets (IMDb reviews, email contradictions, and Stack Overflow tags), the advisor consistently identifies the optimal execution strategy for each workload. This dynamic routing proves decisive: it outperforms adaptive block join (ABJ) by 20-33 F1 points across all datasets while consuming fewer tokens on two of the three, and achieves higher F1 scores than featurized-decomposition join (FDJ) at one to two orders of magnitude lower token cost.
