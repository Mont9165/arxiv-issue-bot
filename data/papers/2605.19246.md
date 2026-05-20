# Example-Driven Intent Synthesis for Constrained Data Bundle Retrieval: Focused Text Snippet Extraction and Beyond

- arXiv ID: `2605.19246v1`
- Authors: Whanhee Cho, Kuangfei Long, Mahmood Jasim, Matteo Brucato, Alexandra Meliou, Peter J. Haas, Anna Fariha
- Published: 2026-05-19
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.19246v1) | [pdf](https://arxiv.org/pdf/2605.19246v1)

## Abstract

Selecting a bundle of items that collectively satisfies constraints is a fundamental task across databases, recommender systems, and text summarization. Unlike traditional retrieval that returns individual or top-k items, bundle retrieval is inherently combinatorial and, in general, NP-hard. Although package queries can efficiently retrieve bundles given a well-formed query, two key user-centric challenges remain: (1) expressing and tuning multi-dimensional bundle intent through a user-friendly interface, and (2) ensuring feasibility when the query yields empty results. We introduce Ex2Bundle, an Example-driven Bundle retrieval framework that enables users to specify their intent through example bundles and automatically synthesizes package queries that capture the intent implicit in those example bundles via aggregate constraints. Ex2Bundle also addresses a challenge unique to bundle retrieval: when inferred aggregate constraints are infeasible over the target data, our data-aware constraint relaxation minimally adjusts the constraint bounds while preserving alignment with user intent. We instantiate a specific application of focused text snippet extraction by example to demonstrate the efficacy of the Ex2Bundle framework. Extensive experiments over real-world datasets and a user study demonstrate that Ex2Bundle improves usability and consistently returns intent-aligned bundles even under distributional shifts of the target database.
