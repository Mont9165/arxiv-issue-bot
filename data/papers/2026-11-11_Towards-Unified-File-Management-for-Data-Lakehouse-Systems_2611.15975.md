# Towards Unified File Management for Data Lakehouse Systems

- arXiv ID: `2611.15975v1`
- Authors: Keonwoo Oh, Akshay Mehra, Joshua Kimball, Amol Deshpande
- Published: 2026-11-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.15975v1) | [pdf](https://arxiv.org/pdf/2611.15975v1)

## Abstract

Data lakehouse systems have garnered widespread adoption, yet their metadata management systems face a fundamental architectural dilemma. File-based OTFs (Open Table Formats) scale well, but suffer from metadata bloat, high commit latencies, the absence of multi-table transactions, and unsafe garbage collection. On the other hand, catalogs relying entirely on a transactional database incur severe scalability bottlenecks due to analytic file-level metadata. To reconcile this tension, we present Raven, an operational catalog that stores transactional metadata within a database while offloading analytical metadata to underlying OTF structures. Based on this hybrid architecture, Raven introduces an extended Merge-on-Read (MoR) mechanism to reduce commit latency and mitigate metadata bloat, alongside multi-table transactions under snapshot isolation. Furthermore, Raven unifies core data lakehouse semantics including versioning and reference tracking under an extensible ER (Entity-Relationship) metadata model, enabling safe global garbage collection across diverse types of assets. Empirical evaluations demonstrate that Raven substantially reduces commit latency and metadata bloat when integrated with Apache Iceberg and Delta Lake, maintains a catalog storage footprint orders of magnitude smaller than database-only systems like DuckLake, and achieves scalable garbage collection with minimal disruption.
