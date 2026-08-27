# PolyMemDB: A Polyglot Database System for AI Memory Management

- arXiv ID: `2608.25577v1`
- Authors: Yu Wang, Jiaheng Lu
- Published: 2026-08-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.25577v1) | [pdf](https://arxiv.org/pdf/2608.25577v1)

## Abstract

With the widespread adoption of personal intelligent agents, users generate massive, heterogeneous data during long-term interactions. Leveraging this data as long-term memory helps reduce token overhead and deliver personalized experiences. However, existing memory systems face two primary limitations: they rely on single-storage paradigms that fragment multi-dimensional data, and they lack fine-grained data provenance to resolve long-term factual conflicts, thereby worsening LLM hallucinations.
  In this demonstration, we introduce PolyMemDB, a novel system tailored for managing agent memory. PolyMemDB has a polyglot storage architecture designed to track and manage various memory types, including graph, vector, probability and spatial-temporal data. To ensure factual consistency and reduce hallucinations, it features a probabilistic inference engine that integrates temporal decay with semiring aggregation, resolving long-term factual conflicts, providing detailed data provenance, and enabling users to trace reasoning chains transparently.
