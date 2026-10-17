# Amora: Communication-Efficient Private Approximate Nearest Neighbors Search

- arXiv ID: `2610.21174v1`
- Authors: Qiuhao Wang, Zuowei Chen, Xu Yang, Saiyu Qi, Yong Qi
- Published: 2026-10-15
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.21174v1) | [pdf](https://arxiv.org/pdf/2610.21174v1)

## Abstract

Approximate nearest neighbors search (ANNS) over cloud-hosted vector databases raises a critical privacy concern: the query vector, which often encodes sensitive user intent, is exposed to the server. Private ANNS (PANNS) allows a client to retrieve nearest neighbors without revealing its query. The state-of-the-art single-server scheme, Pacmann (ICLR'25), achieves high accuracy via graph-based search with private information retrieval (PIR), but incurs substantial communication overhead because each PIR query retrieves only a single vertex. We present Amora, a communication-efficient PANNS system that applies SimplePIR to a partitioned graph index so that one PIR query is amortized over many vertices. To retrieve as much of the distance and neighbor information the search needs under a limited communication budget, Amora adopts a dual-PIR split layout with two heterogeneous PIR matrices that stay balanced in dimension: VecPIR retrieves inner products for an entire partition of vertices as their distance at once, while NbrPIR retrieves necessary neighbor lists at subgroup granularity for graph traversal. This layout shifts the cost model of PIR query from per-vertex to per-partition, which significantly reduces the communication overhead. To further improve efficiency by reducing the number of scans and query rounds in the PIR database, Amora introduces batch PIR to pack multiple queries into one matrix multiplication, centroid-based pruning to filter unpromising partitions, and TopCand exploration that seeds jump-style graph navigation with the closest vertices from each retrieved partition. We evaluate Amora on five datasets spanning 96 to 1024 dimensions and up to 10 million vectors. Compared to Pacmann, Amora reduces online communication by 93--99% while achieving higher search accuracy.
