# Beyond Similarity Search: A Unified Data Layer for Production RAG Systems

- arXiv ID: `2605.03275v1`
- Authors: Venkata Krishna Prasanth Budigi, Siri Chandana Sirigiri
- Published: 2026-05-05
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.03275v1) | [pdf](https://arxiv.org/pdf/2605.03275v1)

## Abstract

Retrieval-Augmented Generation (RAG) systems have become the standard architecture for grounding large language models in organizational knowledge. Yet production deployments consistently expose a gap between clean prototype performance and real-world reliability. This paper identifies three root causes of that gap: data staleness, tenant data leakage, and query composition explosion. All three trace back to the conventional split-system data layer. We propose and evaluate a unified data layer built on PostgreSQL with native vector search (pgvector) and HNSW indexing. Controlled benchmarks on 50,000 documents show 92% latency reduction for date-filtered queries, 74% for tenant-scoped queries, zero synchronization inconsistency, and complete elimination of cross-tenant data leakage with 93% less synchronization code. We additionally discuss a recommended hybrid tier architecture
