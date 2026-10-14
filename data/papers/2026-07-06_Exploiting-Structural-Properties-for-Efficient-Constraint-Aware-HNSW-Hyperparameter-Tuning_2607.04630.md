# Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning

- arXiv ID: `2607.04630v1`
- Authors: Geon Choi, Hoeun Lee, Jaeyoung Do
- Published: 2026-07-06
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.04630v1) | [pdf](https://arxiv.org/pdf/2607.04630v1)

## Abstract

Vector databases (VectorDBs) are a core component of modern retrieval systems, including Retrieval-Augmented Generation (RAG), where efficient Approximate Nearest Neighbor Search (ANNS) is critical. Among ANNS algorithms, Hierarchical Navigable Small World (HNSW) graphs are widely adopted for their strong recalllatency trade-off. However, configuring HNSW remains challenging: its hyperparameters jointly affect search quality, latency, build time, and index size in nonlinear ways, while production deployments impose strict resource and tuning-time constraints.We study HNSW hyperparameter tuning from a systems perspective and show that its configuration space exhibits strong structural regularities. Specifically, we identify monotonic, dominant unimodal, and separable relationships among search-time and construction-time parameters, which induce feasibility boundaries under performance and resource constraints. Building on this insight, we propose CHAT, a constraint-aware tuning framework for HNSW. Unlike generic black-box optimizers, CHAT exploits HNSW-specific structure to perform deterministic, sample-efficient search and prune resource-infeasible configurations before full index construction. Across multiple datasets and HNSW-based vector search engines, CHAT identifies configurations that maximize recall or throughput while satisfying constraints on accuracy, latency, build time, index size, and tuning budget. Compared to strong baselines, CHAT achieves up to 45% higher throughput or 11% higher recall, and converges up to 44x faster. These results show that principled, structure-aware tuning enables efficient and robust HNSW deployment beyond generic black-box optimization.
