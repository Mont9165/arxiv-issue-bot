# Federated Vector Retrieval across Heterogeneous VectorDBs

- arXiv ID: `2611.01514v1`
- Authors: Mintaek Lim, Sieun Hyeon, Geon Chio, Jaeyoung Do
- Published: 2026-11-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.01514v1) | [pdf](https://arxiv.org/pdf/2611.01514v1)

## Abstract

Vector databases are now core infrastructure for AI retrieval systems, yet many real deployments must serve queries over multiple independently constructed vectorDBs built with different embedding models. This creates a systems problem of federated retrieval over heterogeneous vectorDBs: vectors and similarity scores are not directly comparable across embedding spaces, while fully resolving this incompatibility through corpus-wide re-embedding and re-indexing is often operationally prohibitive. Existing methods therefore face a difficult trade-off between retrieval quality, construction cost, and query throughput. We present HVMap, a lightweight compatibility layer for federated retrieval across heterogeneous vectorDBs. Instead of rebuilding databases into a unified space, HVMap learns bidirectional mappings between embedding spaces using a fuzzy contrastive loss, enabling calibrated cross-database scoring without corpus migration or index reconstruction. HVMap is system-agnostic and further scales to multi-vectorDB settings while preserving ranking fidelity through a hub-based architecture. We evaluate HVMap in open-domain, cross-domain, and scale-out settings, and also construct a new benchmark for heterogeneous cross-domain federation. Across these settings, HVMap consistently achieves a better quality--cost--throughput trade-off than baselines, achieving up to 3.59X higher nDCG@10, up to 2.01X higher query throughput, and construction time as low as 0.3% of baseline methods. These results show that HVMap makes heterogeneous vectorDB federation practical at scale.
