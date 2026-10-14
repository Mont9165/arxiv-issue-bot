# A Structured Knowledge Infrastructure for Domain-Specific Data Asset Discovery

- arXiv ID: `2607.27748v1`
- Authors: Mengdi Chen, Yuanxin Huang, Yulin Jiang, Wei Sun
- Published: 2026-07-30
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.27748v1) | [pdf](https://arxiv.org/pdf/2607.27748v1)

## Abstract

Enterprise data analytics agents face two structural failures: generic RAG retrieves the wrong asset (Hit@10=19.1%) and delivers no usage knowledge to prevent metric misinterpretation---stemming from four root causes (C1--C4) ranging from semantic gap and entity ambiguity to schema drift and asset-usage gap. We present a two-layer solution deployed in the commercial advertising data warehouse at Xiaohongshu (5,300+ Hive tables, 14 domains). A three-tier dual-purpose knowledge base (179 documents, eight-section annotation template) serves both retrieval and generation, with a closed-loop refresh pipeline maintaining day-level freshness (one yes/no approval, 30s hot-reload). The Graph-Guided Retriever (GGR) uses a 2,859-node knowledge graph as a candidate gate with intent routing to deliver 71.6x token reduction. The Scene-Aware Ranker (SAR) applies 19-class entity recognition and explicit scenario annotations; negative knowledge alone contributes 25 percentage points of Hit@10 gain. On two 100-question benchmarks, Hit@10 rises from 19.1% to 96.6% (+77.5pp) and knowledge coverage from 56% to 77%, at 4.84--5.33s end-to-end latency.
