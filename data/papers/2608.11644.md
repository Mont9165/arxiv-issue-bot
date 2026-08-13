# Guided Table Retrieval for Structured Data Search

- arXiv ID: `2608.11644v1`
- Authors: Alekh Jindal, Jyoti Pandey, Christina Pavlopoulou, Ronith PR, Sharath Prakash, Shi Qiao, Shivani Tripathi, Wangda Zhang
- Published: 2026-08-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.11644v1) | [pdf](https://arxiv.org/pdf/2608.11644v1)

## Abstract

Answering natural language questions over structured databases requires identifying the relevant tables and determining how to join them---a task that demands both schema knowledge and semantic understanding of the user's intent.We present guided table retrieval, a four-phase pipeline that combines deterministic grounding via hash-based predictors, structural exploration of join-graph reachability, LLM-powered disambiguation of sources and targets, and algorithmic merging into minimal, topologically ordered join trees. By decomposing the problem into phases with distinct responsibilities--- determinism, coverage, semantic reasoning, and coherence--- the pipeline avoids the brittleness of end-to-end LLM approaches while leveraging LLMs where their contextual judgment is most needed. We evaluate on BIRD-DEV and the enterprise-scale BEAVER benchmark, achieving 94% and 70% precision respectively, with 92% and 53% F1---substantially outperforming existing baselines on precision and F1 while producing exact join trees that can be directly consumed by downstream query compilers.
