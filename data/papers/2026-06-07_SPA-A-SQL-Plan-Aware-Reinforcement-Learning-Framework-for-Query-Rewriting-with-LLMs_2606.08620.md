# SPA: A SQL-Plan-Aware Reinforcement Learning Framework for Query Rewriting with LLMs

- arXiv ID: `2606.08620v1`
- Authors: Xinyi Huang, Zhengjie Miao
- Published: 2026-06-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.08620v1) | [pdf](https://arxiv.org/pdf/2606.08620v1)

## Abstract

SQL query rewriting is a well-established technique for improving database performance without schema or index changes, yet finding effective rewrites for modern analytical workloads remains difficult: rule-based methods are limited to predefined transformations, while LLM-based approaches often produce rewrites that are semantically valid but compile to equivalent physical plans or degrade runtime performance. We present SPA, a SQL-Plan-Aware reinforcement learning framework that trains LLMs to rewrite queries using physical execution feedback. SPA formulates rewriting as a policy optimization problem and extends GRPO with rewards spanning semantic equivalence, textual rewrite distance, physical-plan divergence, and runtime speedup. To handle reward sparsity across query difficulty, SPA introduces Probability-Gated Adaptive Reward Shaping, a query-level curriculum that unlocks higher-level rewards only once a rollout group achieves sufficient mastery of lower-level objectives, and further improves sample efficiency through on-policy self-improvement by recycling slowdown rewrites from the current policy as targeted training signals. On both IID and OOD workloads, SPA outperforms rule-based and strong LLM baselines in end-to-end runtime, substantially reduces harmful slowdown rewrites, and yields strong tail-latency gains.
