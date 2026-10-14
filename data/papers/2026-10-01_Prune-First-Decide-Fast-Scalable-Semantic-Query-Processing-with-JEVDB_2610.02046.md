# Prune First, Decide Fast: Scalable Semantic Query Processing with JEVDB

- arXiv ID: `2610.02046v1`
- Authors: Zhengle Wang, Hanxu Yan, Fuheng Zhao, Chunwei Liu
- Published: 2026-10-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.02046v1) | [pdf](https://arxiv.org/pdf/2610.02046v1)

## Abstract

Semantic database systems extend SQL with foundation-model inference over unstructured data, but current engines rely heavily on autoregressive LLMs for discrete relational decisions, creating high latency and monetary cost. We present JEVDB, a scalable semantic database system that uses fast, typed decision models for semantic filters, joins, classification, and ranking, while selectively escalating uncertain cases to generative LLMs. To reduce semantic-join work, JEVDB combines exact Yannakakis-style semijoin reduction over relational structure with Semantic Bloom Filters (SBFs), which use registered necessary conditions to screen candidates across latent semantic edges.
  We evaluate JEVDB on SemBench and Shelob, a TPC-DS-derived semantic-join workload. On SemBench, JEVDB-Flash achieves the lowest latency on all 21 evaluated queries and the lowest cost on 19, while maintaining competitive answer quality. On Shelob, where joins scale to 540K candidate pairs, JEVDB completes all queries with 95.7%-97.5% mean F1. SBF screening removes 87.4% of candidate pairs before semantic evaluation, and reusable condition-index scoring further reduces reasoning-model escalations by 55.2%. An interactive query simulator, source code, and benchmarks are available at https://jevdb.org.
