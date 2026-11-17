# HorizANN: Elastically Scaling Vector Search with Ghost Edges

- arXiv ID: `2611.19077v1`
- Authors: Talika Gupta, Yunqi Li, Aditya Kunte, Claire Lin, Supawit Chockchowwat, Daniel Waddington, Hubertus Franke, Yongjoo Park
- Published: 2026-11-14
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.19077v1) | [pdf](https://arxiv.org/pdf/2611.19077v1)

## Abstract

Approximate nearest neighbor search (ANNS) is fundamental to modern data-intensive AI applications such as retrieval-augmented generation, recommendation systems, and semantic search. Among existing indexing methods, graph-based indexes emerge as the state of the art due to their superior recall-throughput tradeoffs. Scaling these indexes to multiple machines requires partitioning the data and building indexes on each. However, when new machines are added or removed, the data must be repartitioned and the indexes reconstructed from scratch, making horizontal scaling costly at billion scale. In this work, we present HorizANN, a distributed graph-based ANNS system that scales horizontally without requiring full index reconstruction. To achieve this, we introduce ghost edges, a mechanism for preserving cross-partition connectivity as partition boundaries change during repartitioning. By reusing the structural information that would otherwise be discarded during repartitioning, HorizANN avoids costly full index reconstruction. As the index grows from 100M vectors on one worker to 1B vectors on ten workers, HorizANN inserts each 100M vectors within 2.5 hours and sustains 3.4--3.5K queries per second at 0.998 Recall@10.
