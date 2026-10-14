# A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving

- arXiv ID: `2607.07103v1`
- Authors: Heye Huang, Jingguang Li, Zhiyuan Zhou, Paul Liang, Mingyu Wu, Kitae Jang, Jianqiang Wang
- Published: 2026-07-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.07103v1) | [pdf](https://arxiv.org/pdf/2607.07103v1)

## Abstract

Safe autonomous driving requires both rapid responses to common high-risk events and deeper reasoning over rare, extreme long-tail scenarios in traffic safety. These scenarios are severely under-represented in naturalistic driving data, and existing trajectory and language-augmented datasets seldom provide high-risk event labels, semantic annotations, and verifiable safety signals. Here we present K-Risk, a knowledge-augmented dataset that combines structured driving trajectories with large language model generated semantic annotations for safety-critical driving scenarios. K-Risk integrates 20 human-driven and autonomous-vehicle trajectory datasets from Europe, China, and the United States, covering highways, urban freeways, intersections, and roundabouts. Using a unified risk-centric extraction pipeline, K-Risk curates 31,398 high-risk events, together with a 1,036-event extreme subset of near-collision cases. Each event is released as a synchronized trajectory, metadata, and language triplet containing structured scenario descriptions, abnormal-behavior notifications, and, for a representative subset, causal risk analyses and action recommendations validated through a closed-loop simulator with iterative reflection. By combining multi-dimensional risk annotations, interpretable language supervision, and verifiable decisions, K-Risk bridges structured traffic trajectories, semantic reasoning, and decision supervision, providing a standardized foundation for developing and evaluating next-generation risk-aware autonomous driving agents.
