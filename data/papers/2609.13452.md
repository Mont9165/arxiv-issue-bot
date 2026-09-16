# COMPASS: Steering Distributed Vector Search with Scientific Knowledge Graphs

- arXiv ID: `2609.13452v1`
- Authors: Song Young Oh, Amal Gueroudji, Seth Ockerman, Rob Latham, Orcun Yildiz, Ian Foster, Kyle Chard, Robert Ross
- Published: 2026-09-11
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2609.13452v1) | [pdf](https://arxiv.org/pdf/2609.13452v1)

## Abstract

Vector databases use hashing to partition data across "shards," logical units for distributed execution. This placement, however, destroys semantic locality, forcing each query into scatter-gather limited by the slowest shard. Vector-space clustering can help, but scientific evidence is often connected by factual relations that do not align with embedding distance. We present COMPASS, a framework that uses a knowledge graph (KG) to determine data placement and query-time shard selection. COMPASS detects communities, splits oversized communities, inserts embeddings by subject entity, and routes queries to a small set of shards. Across four biomedical KGs, our method searches only 13-18% of the corpus while preserving broadcast recall and recovering up to 2.6x more multi-hop evidence than an embedding-based baseline. On 15 HPC nodes, COMPASS sustains 7.9x higher throughput with lower tail latency than hash-based broadcast. These results show that KG structure provides a compact complement to embedding geometry for scalable vector search.
