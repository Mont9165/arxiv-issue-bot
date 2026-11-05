# Optimizing Geo-replicated Deterministic Databases

- arXiv ID: `2611.05882v1`
- Authors: Yunhao Mao, Shiquan Zhang, Gengrui Zhang, Hans-Arno Jacobsen
- Published: 2026-11-04
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.05882v1) | [pdf](https://arxiv.org/pdf/2611.05882v1)

## Abstract

In transactional databases, achieving active-active replication among geo-distributed replicas is challenging due to the high coordination cost in ensuring the serializability of concurrent cross-node transactions. Deterministic concurrency control (DCC) has emerged as a promising alternative: it establishes a global order for a batch of transactions before execution and thereby amortizes this coordination cost across the batch. To better understand the performance characteristics of DCC, we conduct a theoretical analysis of traditional two-phase locking and optimistic concurrency control to account for geo-replication and introduce a model for DCC. We compare the three paradigms and identify the conditions under which DCC is advantageous. Guided by the insights from this analysis, we then present Quirinus, a DCC-based geo-replicated database that optimizes transaction execution through speculative execution, transaction reordering, integration of conflict-free replicated data types (CRDTs), and fast-path commit. Even without these optimizations, Quirinus achieves up to 6.2x the TPC-C throughput of Tiga under our configuration.
