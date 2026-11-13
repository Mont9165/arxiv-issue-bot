# REWEAVE: Online Learning for Workload-Adaptive HNSW Indexes

- arXiv ID: `2611.16060v1`
- Authors: Minghao Li, Nick Koudas, Raghav Mittal
- Published: 2026-11-11
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.16060v1) | [pdf](https://arxiv.org/pdf/2611.16060v1)

## Abstract

Vector databases rely on Hierarchical Navigable Small World (HNSW) indexes for similarity search, but a graph built from data alone can be poorly matched to a skewed or changing query workload. We present REWEAVE (Reward-Guided Rewiring of Vector Graphs), an online index-maintenance method that learns edge utility from query feedback and periodically rewires the bottom layer within the original per-node degree cap. The method supports sparse exact-neighbor feedback combined with self-labels, and standard HNSW serving without learning overhead once adaptation is disabled.
  Under explicit assumptions we prove value-estimation and graph-stabilization guarantees. Under stationary skew, REWEAVE improves held-out recall by up to 23.3 percentage points over HNSW. In comparisons with query-aware baselines on up to 100M vectors, it achieves up to 3.3x NGFix's query throughput at recall@100 of 0.80. On Amazon-ESCI with query drift, it increases stream recall@100 from 0.745 to 0.979 with 34% fewer search distance computations than frozen HNSW. These results illustrate the potential to improve retrieval quality and reduce search effort within an existing graph-degree budget, while incurring additional work during adaptation.
