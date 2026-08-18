# Building An Integrated Vector Database System in PostgreSQL

- arXiv ID: `2608.15994v1`
- Authors: Jiayi Liu, Te Guo, Jianguo Wang
- Published: 2026-08-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.15994v1) | [pdf](https://arxiv.org/pdf/2608.15994v1)

## Abstract

This paper presents PostgreSQL-V 2.0, a scalable integrated vector database system inside PostgreSQL. Existing PostgreSQL-based vector search systems such as pgvector embed vector indexes into PostgreSQL's page-oriented storage engine, incurring significant overhead that leads to a huge performance gap with specialized vector databases. In our earlier work, we introduced PostgreSQL-V 1.0, which addresses this issue by separating vector index structures from PostgreSQL's storage engine, enabling vector search performance close to that of native vector index libraries while preserving SQL compatibility. However, we find that PostgreSQL-V 1.0 has three limitations that matter for real-world workloads: it only supports a single connection (without concurrency), recovery time grows with index size, and physical replication is unsupported.
  We further present PostgreSQL-V 2.0, which closes all three gaps. PostgreSQL-V 2.0's concurrency support enables fully concurrent vector searches and updates across PostgreSQL's multi-process backends, delivering up to 36.4x the throughput of PostgreSQL-V 1.0 while serving 32 concurrent clients. PostgreSQL-V 2.0's fast crash recovery keeps cost independent of total index size, remaining near 20 ms while PostgreSQL-V 1.0's grows into seconds-scale. PostgreSQL-V 2.0's physical replication support extends physical replication to the decoupled index, preserving index consistency on standbys without burdening the primary node. Together, these advances make PostgreSQL-V 2.0 a fully concurrent, crash-resilient, and replication-ready vector database inside PostgreSQL.
