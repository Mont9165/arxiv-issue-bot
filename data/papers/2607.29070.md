# Query Density-Driven Partitioning for Spatiotemporal Load Balancing on Processing-in-Memory Systems

- arXiv ID: `2607.29070v1`
- Authors: Takato Hideshima, Shigeyuki Sato, Tomoharu Ugawa
- Published: 2026-07-31
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.29070v1) | [pdf](https://arxiv.org/pdf/2607.29070v1)

## Abstract

Processing-in-Memory (PIM) systems, which consist of many processors with small local memory, have recently emerged as commercial products and attracted much attention as a means of overcoming the memory wall, particularly in the context of in-memory database technology. The state-of-the-art PIM-oriented index PIM-tree has been demonstrated to achieve asymptotically good spatiotemporal load balancing---query loads and data sizes are balanced among processors---for skewed queries, by trading spatial locality. Unfortunately, such a sacrifice of spatial locality hinders the PIM-oriented processing of range-aggregate queries. To achieve both spatiotemporal load balancing and efficiently executing range-aggregate queries on PIM systems, we develop a query density-driven key-range partitioning scheme. It balances query density among PIM processors, allowing us to strike a balance between query load and data size via a parameter. We then develop B${}^\text{+}$-Forest, a PIM-oriented B${}^\text{+}$-tree variant based on our partitioning scheme. Experimental results demonstrated that it exhibits higher skew resistance than a B${}^\text{+}$-tree based on space-constrained, query-load-balanced, density-unaware partitioning, and performance comparable to PIM-tree in point-get queries, as well as efficient support for range-aggregate queries.
