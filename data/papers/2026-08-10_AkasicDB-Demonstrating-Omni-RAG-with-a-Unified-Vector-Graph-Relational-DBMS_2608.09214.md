# AkasicDB: Demonstrating Omni RAG with a Unified Vector-Graph-Relational DBMS

- arXiv ID: `2608.09214v1`
- Authors: Geonho Lee, Jeongho Park, Donghyoung Han, Min-Soo Kim
- Published: 2026-08-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.09214v1) | [pdf](https://arxiv.org/pdf/2608.09214v1)

## Abstract

Recent Retrieval-Augmented Generation (RAG) systems increasingly combine vector retrieval with structured knowledge, such as Graph RAG and Filtered vector search. However, existing database architectures struggle to support such complex RAG workflows efficiently, as they rely on out-of-DB pipelines or in-DB non-native integration, leading to high overhead. This demo paper presents AkasicDB, a database system that natively supports such RAG workflows by jointly executing vector similarity search, graph traversal, and relational filtering within a single execution framework. AkasicDB extends our prior work, Chimera, with native vector support to enable such unified execution. Based on AkasicDB, we demonstrate the first native integration of Vector-Graph-Relational RAG, which we refer to as Omni RAG. Through an interactive chat-style demonstration, users execute and visualize Omni RAG queries, directly experiencing its superior retrieval and reasoning over vector-only approaches while observing the practical limitations of existing database architectures in supporting Omni RAG. A demonstration video is available at https://youtu.be/8d09_dtrEIM
