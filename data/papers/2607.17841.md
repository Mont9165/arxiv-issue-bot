# From Blind Search to Memory-Aware Evolution: Efficient DBMS Tuning via Collaborative Diagnosis and Utility-Aware Retrieval

- arXiv ID: `2607.17841v1`
- Authors: Zhaoyan Hong, Yishen Sun, Xinyi Zhang, Zhentao Han, Jinhao Dong, Wei Lu, Kai Xu, Liu Tang, Qi Liu, Xiaoyong Du
- Published: 2026-07-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.17841v1) | [pdf](https://arxiv.org/pdf/2607.17841v1)

## Abstract

Modern DBMSs expose multiple configurable components (e.g., knobs, query hints, and indexes) that jointly determine query performance. Multi-component tuning is challenging due to the large combinatorial search space and the difficulty of learning effective tuning policies under limited feedback. Existing approaches still rely on blind search over the configuration space and interaction-heavy policy learning, leading to high tuning overhead and limited performance gains. Recent advances in large language models (LLMs) enable knowledge-driven tuning, but existing LLM-based methods fail to effectively exploit online feedback and historical observations, often converging prematurely to suboptimal configurations.
  In this paper, we present EvoTune, a memory-aware evolution framework for multi-component DBMS tuning. EvoTune first localizes a query-specific high-impact subspace via collaborative diagnosis, which combines lightweight pattern learning with LLM-based reasoning. It further introduces a utility-aware retrieval policy that selects informative observations based on their resulting long-term performance improvement, instead of similarity-based retrieval. To support continual improvement, EvoTune organizes tuning feedback into a hierarchical memory and incrementally refines both subspace localization and tuning policies without requiring LLM fine-tuning. Extensive experiments show that EvoTune consistently outperforms state-of-the-art baselines, achieving up to 44.5% performance improvement under the same tuning budget and reaching the best competing baseline's final performance up to 3.9X faster.
