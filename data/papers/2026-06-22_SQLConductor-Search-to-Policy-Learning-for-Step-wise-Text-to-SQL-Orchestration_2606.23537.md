# SQLConductor: Search-to-Policy Learning for Step-wise Text-to-SQL Orchestration

- arXiv ID: `2606.23537v1`
- Authors: Yizhang Zhu, Zhangyang Peng, Boyan Li, Yuyu Luo
- Published: 2026-06-22
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.23537v1) | [pdf](https://arxiv.org/pdf/2606.23537v1)

## Abstract

Text-to-SQL enables users to access relational databases via natural language, but real-world settings remain challenging due to coordinated reasoning over complex database environments. Existing systems often use multi-stage pipelines or reasoning models specialized for individual stages. However, fixed pipelines rely on predefined stage orders, limiting their adaptivity to query demands and intermediate evidence. Recent orchestration-based methods provide flexibility by composing specialized modules for each query, but typical plan-then-execute approaches still commit to a complete workflow before execution and cannot adapt to intermediate artifacts and feedback.
  In this paper, we propose SQLConductor, a step-wise orchestration learning framework for Text-to-SQL. SQLConductor formulates Text-to-SQL subtasks as specialized actions for workflow composition and trains a policy model to select the next action based on intermediate artifacts and feedback. To learn this policy, SQLConductor introduces Search-to-Policy Learning, which uses Monte Carlo Tree Search to explore candidate workflows and stability estimation to identify robust supervision. The policy model is trained with Stability-weighted Supervised Fine-tuning to prioritize high-quality orchestration patterns and further enhanced through Curriculum Reinforcement Learning. This transforms offline workflow search into a deployable policy for step-wise orchestration at inference time. Experiments on BIRD-Dev and out-of-distribution datasets show that SQLConductor achieves superior execution accuracy and strong generalization, reaching 73.2% EX on BIRD-Dev with a compact orchestration policy coordinating frozen larger action models, outperforming prior methods that directly train comparable or larger Text-to-SQL backbones. Further analyses show that the learned policy adapts orchestration to diverse query demands.
