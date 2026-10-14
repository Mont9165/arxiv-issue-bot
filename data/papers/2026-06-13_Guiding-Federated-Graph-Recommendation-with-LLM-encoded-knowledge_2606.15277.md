# Guiding Federated Graph Recommendation with LLM-encoded knowledge

- arXiv ID: `2606.15277v1`
- Authors: Thi Minh Chau Nguyen, Hien Trang Nguyen, Duc Anh Nguyen, Van Ho-Long, Thanh Trung Huynh, Zhao Ren
- Published: 2026-06-13
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.AI`, `cs.DB`, `cs.ET`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.15277v1) | [pdf](https://arxiv.org/pdf/2606.15277v1)

## Abstract

Graph-based recommender systems are highly effective at extracting collaborative signals from user--item interactions, and federated learning (FL) allows these models to be trained while preserving user privacy. However, aggregating graph representations across distributed, non-IID clients remains a challenge; structural embeddings learned locally often misalign, and naive averaging fails to capture meaningful cross-client relationships. Most existing federated graph methods rely exclusively on structural aggregation, neglecting the rich, global semantic context available in large language models (LLMs). In this paper, we propose a novel framework that uses LLM-encoded knowledge to guide federated graph recommendation. Specifically, clients learn structural representations from local graphs while simultaneously summarizing their typical interaction patterns into compact semantic vectors via a frozen LLM. The central server then uses these LLM-encoded semantic signals to discover related preference patterns across clients, guiding the selective aggregation of their structural representations. This enables semantically informed cross-client collaboration without exposing raw data. Extensive experiments on standard benchmarks show that guiding structural alignment with LLM-encoded knowledge consistently improves recommendation accuracy over existing federated graph baselines.
