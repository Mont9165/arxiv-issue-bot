# PLRTune: Importance Pre-Sampling and LLM-Guided Reinforcement Learning for Automatic Database Tuning

- arXiv ID: `2606.14312v1`
- Authors: Xinyue Yang, Chen Zheng, Yaoyang Hou, Renhao Zhang, Yinyan Zhang, Heng Zhang
- Published: 2026-06-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.14312v1) | [pdf](https://arxiv.org/pdf/2606.14312v1)

## Abstract

Configuration tuning is critical to database performance, yet automatic database tuning remains challenging due to high-dimensional knob spaces, substantial online tuning cost, unreliable textual hints derived from Large Language Models (LLMs) or community documents, and the difficulty of exploiting the remaining optimization room after initialization.
  Hence, we propose PLRTune, a staged database tuning system that leverages workload-specific domain knowledge to identify a reduced search space and further optimize within this promising region. First, we develop an importance pre-sampling and reranking strategy to identify the dominant knob subset in a workload-specific manner and derive a compact state representation. Second, we design an execution-guided hint refinement technique to improve the initialization quality of documentation-guided tuning. Finally, we propose a post-tuning refinement stage that leverages Twin Delayed Deep Deterministic Policy Gradient (TD3) to explore the dominant knob subset and further exploit the remaining optimization room.
  We evaluate PLRTune on MySQL and PostgreSQL across diverse benchmark workloads. Compared with state-of-the-art approaches, PLRTune achieves the best final result on all tested workloads, improving over the corresponding best-performing alternative by 9.50% on average. Moreover, PLRTune reaches the strongest baseline's best performance level 9.03 times faster on average across workloads, demonstrating its practical runtime efficiency without sacrificing final tuning quality.
