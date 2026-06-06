# EMA: Approximate Nearest Neighbor Search with General Attribute Filtering and Dynamic Updates

- arXiv ID: `2606.00734v1`
- Authors: Mocheng Li, Baotong Lu, James Cheng, Chenhao Ma
- Published: 2026-05-30
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.00734v1) | [pdf](https://arxiv.org/pdf/2606.00734v1)

## Abstract

Filtering Approximate Nearest Neighbor (FANN) search is a critical and emerging task for strengthening the query capability of vector databases, supporting applications such as recommendation systems, retrieval-augmented generation (RAG), and agent memory. However, most existing methods are limited to range or label filtering, often incurring unacceptable index construction time and memory overhead. Predicate-agnostic approaches further struggle to handle a wide range of predicate selectivities effectively. In this paper, we propose EMA, a filtering ANN algorithm that supports multi-predicate queries over mixed numerical and categorical attributes, and efficient dynamic updates. EMA introduces Markers as compact summaries attached to graph edges, providing conservative predicate- and geometric-aware guidance with zero false negatives at the Marker level. During query processing, EMA performs Marker-augmented joint search with a bounded edge recovery mechanism, enabling efficient filtering while preserving graph navigability. Extensive experiments demonstrate that EMA achieves 1.68x--12.25x speedup over state-of-the-art general filtering ANN methods across diverse workloads.
