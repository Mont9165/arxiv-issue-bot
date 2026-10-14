# IORM: Hierarchical I/O Governance for Thousands of Consolidated Databases on Oracle Exadata

- arXiv ID: `2605.29006v1`
- Authors: Rajarshi Chowdhury, Akshay Shah, Zakaria Alrmaih, Chenhao Guo, Anubhav Singh, Sue Lee
- Published: 2026-05-27
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`, `cs.OS`
- Links: [abs](http://arxiv.org/abs/2605.29006v1) | [pdf](https://arxiv.org/pdf/2605.29006v1)

## Abstract

Oracle Exadata consolidates thousands of tenant databases onto shared storage infrastructure deployed at hundreds of customer sites worldwide. Oracle Multitenant architecture enables this extreme density, with thousands of tenant databases sharing a single Exadata storage system -- but this creates a multi-level resource hierarchy (container databases, tenant databases, and workloads within tenants) that commodity block-layer schedulers cannot govern, as they lack visibility into database semantics and tenant boundaries. This paper presents the I/O Resource Manager (IORM), a storage-side scheduler built on three mechanisms: I/O Tagging, which propagates semantic context from the database kernel to the storage scheduler; Hierarchical Resource Profiles, which express compositional allocation policies across consolidation tiers using shares and limits; and Unified Storage Governance, which applies these policies consistently across all tiers of the storage hierarchy -- persistent memory, flash, and hard disk -- including cache placement decisions. IORM enables successful cloud deployments where thousands of tenants coexist on shared storage: production OLTP workloads run alongside concurrent analytical workloads from the same or different databases without noisy-neighbor interference. Evaluation on production Exadata systems demonstrates that IORM dramatically improves latency consistency, virtually eliminating tail latency outliers and delivering several-fold improvements in average read latency under mixed workloads. Hierarchical limits compose correctly across all three levels, and proportional share allocation tracks configured ratios closely even under highly skewed demand.
