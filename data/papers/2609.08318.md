# AttnCompress: Dynamic Attention-Guided Trajectory Compression for Software Engineering Agents

- arXiv ID: `2609.08318v1`
- Authors: Zhengran Zeng, Yixin Li, Rui Xie, Wei Ye, Shikun Zhang
- Published: 2026-09-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.08318v1) | [pdf](https://arxiv.org/pdf/2609.08318v1)

## Abstract

The transition from human-centric assistance to Autonomous Software Engineering (ASE) agents has enabled the resolution of complex real-world SE tasks. However, the trial-and-error nature of these agents generates lengthy interaction trajectories, creating severe bottlenecks in terms of context window limits and cost. While context compression offers a potential remedy, prior approaches suffer from static pruning strategies and granularity mismatches, often failing to preserve the semantic dependencies and syntactic details crucial for SE tasks. To strictly preserve critical task evidence while reducing context length, we introduce AttnCompress, a dynamic attention-guided trajectory compression framework. Unlike existing approaches, AttnCompress bridges the gap between semantic integrity and dynamic adaptability through three key mechanisms: (1) structure-aware segmentation via perplexity (PPL) spikes to preserve the syntactic structure of code and logs; (2) relevance estimation using proxy attention weights to quantify the precise relevance of historical blocks to the agent's current reasoning; and (3) a dynamic rolling window to re-evaluate and recall historical context as the task evolves. Extensive evaluation on SWE-Bench-Verified and Multi-SWE-Bench demonstrates that AttnCompress achieves a pass rate of 53.17%, outperforming prior state-of-the-art baselines while reducing token consumption by 21.6% and total costs by 33.6%. The framework proves to be model-agnostic and generalizes effectively across diverse programming languages.
