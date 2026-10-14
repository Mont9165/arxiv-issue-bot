# Heuristic Search Space Partitioning for Low-Latency Multi-Tenant Cloud Queries

- arXiv ID: `2604.19057v1`
- Authors: Prashant Kumar Pathak, Chandra Biksheswaran Mouleeswaran, Rama Teja Repaka
- Published: 2026-04-21
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2604.19057v1) | [pdf](https://arxiv.org/pdf/2604.19057v1)

## Abstract

Large-scale cloud security platforms must continuously query millions of structured cloud resource records distributed across thousands of tenant accounts. Broad, account-spanning queries saturate database infrastructure, producing P95 latencies exceeding 60 seconds. We identify buffer cache pressure as the dominant latency driver: in a controlled experiment, the same query executing with the same plan completed in 3.7 seconds when its working set was memory-resident and 94 seconds when concurrent load had evicted those pages. No query plan optimization can address this; the only effective intervention is reducing the number of pages each query must touch. We present the Heuristic Search Space Partitioning System (HSSPS), a query-time optimization layer that logically partitions the search space through dynamic predicate injection, without schema modification. A two-phase heuristic engine selects partition key values and scores candidate query plans before execution. A client-side page token maintains cross-partition traversal state without server-side sessions, enabling horizontal scalability. Controlled evaluation across representative query types demonstrates 50-97% P95 latency reduction (95-97% on high-cardinality queries), 8-10x throughput improvement, and 41x reduction in average active sessions. Production rollout across live multi-tenant traffic reduced P95 latency from 61s to 2s across successive releases, sustained over 14,000 eligible queries per measurement window. The technique generalizes to any multi-tenant system where broad queries execute against large shared databases and physical schema modification is impractical.
