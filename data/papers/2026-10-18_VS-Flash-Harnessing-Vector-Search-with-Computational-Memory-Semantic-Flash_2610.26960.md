# VS-Flash: Harnessing Vector Search with Computational Memory-Semantic Flash

- arXiv ID: `2610.26960v1`
- Authors: Donguk Kim, Sangjun Pae, Daeyoung Lee, Dong Kim
- Published: 2026-10-18
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2610.26960v1) | [pdf](https://arxiv.org/pdf/2610.26960v1)

## Abstract

As generative AI continues to evolve, retrieval-augmented generation (RAG) systems are driving rapid growth in vector database capacity requirements. As datasets outgrow host DRAM, vector databases rely on MMap-based serving over SSDs to extend capacity. However, high-fan-out ANN searches generate concurrent irregular accesses that contend for host memory and storage resources, degrading bulk throughput and inflating tail latency under mixed workloads. In this paper, we address these challenges through memory-semantic capacity and workload-aware compute placement. VS-Flash exposes flash as a large-capacity memory-semantic space and dynamically selects the execution engine according to runtime query and workload characteristics. It offloads throughput-oriented large-batch queries to a Computational Memory-Semantic Flash (CMS-Flash) device, while executing latency-sensitive small-batch queries on the host CPU. Both paths access the same resident segments, avoiding a separate host-DRAM replica. Across three billion-scale datasets, VS-Flash improves bulk-search throughput over vanilla Milvus by 36.8X on average, with up to a 57.4X improvement. Under mixed workloads, VS-Flash reduces the p99 latency of latency-sensitive requests by up to 24.8X while sustaining device-side bulk search. These results show that VS-Flash delivers scalable vector search beyond host DRAM capacity while jointly improving bulk throughput and small-request tail latency.
