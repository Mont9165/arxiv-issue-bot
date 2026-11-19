# A Survey on RLOps for Large Language Models

- arXiv ID: `2611.23357v1`
- Authors: Lingzhe Zhang, Tong Jia, Chiming Duan, Minghua He, Leyi Pan, Kening Zheng, Zhaoyang Liu, Bolin Ding, Philip S. Yu, Ying Li
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2611.23357v1) | [pdf](https://arxiv.org/pdf/2611.23357v1)

## Abstract

Reinforcement learning (RL) has become increasingly important for improving the reasoning, instruction-following, and task-solving capabilities of large language models (LLMs). However, scaling RL training exposes failures in distributed execution, feedback computation, and learning dynamics that can waste computational resources, slow training, and undermine model improvements. These challenges have motivated a growing body of techniques for LLM RLOps, which manages the efficiency and reliability of operations throughout the LLM reinforcement learning training lifecycle. Despite growing interest, these techniques remain scattered across research areas, with limited synthesis of their operational roles and interactions. To bridge this gap, we present a systematic survey of LLM RLOps methods. We organize existing approaches into five stages: Training Setup, Experience Collection, Reward Computation, Policy Optimization, and Model Evaluation. Within each stage, we examine operational concerns, management techniques, and evaluation evidence. Building on this taxonomy, we identify open challenges and future directions in training process observability, cross-stage coordination, generalizable RLOps, multi-run management, and RLOps for recursive self-improvement. These directions extend operational management from individual training runs to diverse training settings, shared infrastructure, and successive improvement cycles. We maintain a GitHub repository indexing relevant papers and open resources at https://github.com/zhanglingzhe0820/Awesome-RLOps.
