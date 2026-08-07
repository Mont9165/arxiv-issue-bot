# Query-aware Routing for Filtered Approximate Nearest Neighbors Search

- arXiv ID: `2606.19898v1`
- Authors: Qianqian Xiong, Mengxuan Zhang
- Published: 2026-06-18
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2606.19898v1) | [pdf](https://arxiv.org/pdf/2606.19898v1)

## Abstract

Filtered ANN search, which combines vector similarity with attribute predicates, is a core primitive in modern vector databases and retrieval-augmented generation. We benchmark all major categorical filtered ANN methods across multiple datasets under three predicates and find that no single method dominates. Moreover, even within a single dataset and predicate type, the best method for a query can vary. Therefore, we propose a query-aware routing framework. A lightweight ML model predicts each candidate method's recall on the query, and the router consults an offline benchmark table that maps every method and parameter setting to its measured recall and QPS, then selects the method with the best recall--QPS trade-off. Our ablation study narrows 22 candidate features to a minimal set of three and we adopt regression rather than classification as the prediction target to sharpen accuracy. Our model is trained on six real-world datasets and applied to five unseen validation datasets. The final result shows that our router achieves state-of-the-art recall and QPS balance across all five validation datasets compared to existing filtered ANN baselines, while incurring negligible latency overhead.
