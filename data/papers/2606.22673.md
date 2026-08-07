# AgentLens: Interpretable Safety Steering via Mechanistic Subspaces for Multi-Turn Coding Agent

- arXiv ID: `2606.22673v1`
- Authors: Weidi Luo, Qiming Zhang, Yihao Quan, Mingyu Jin, Jie Cai, Chaowei Xiao, Jingcheng Niu, Zhen Xiang
- Published: 2026-06-21
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22673v1) | [pdf](https://arxiv.org/pdf/2606.22673v1)

## Abstract

Coding agents based on large language models (LLMs) demonstrate remarkable autonomous capabilities, but they also introduce significant safety and misuse risks during multi-turn interactions with external environments. Existing safety mechanisms mainly rely on external guardrails, which have a limited ability to perform fine-grained behavioral control during execution. Meanwhile, recent mechanistic interpretability methods for LLM safety are mostly confined to single-turn or jailbreak-style QA settings, limiting their ability to capture the evolving risk dynamics of multi-turn agent execution. In this paper, we investigate the safety of multi-turn coding agents from an internal perspective. We propose AgentLens (Mechanistic Subspace Intervention and Steering), a white-box defense framework that performs runtime safety detection and representation-level mitigation for coding agents. Unlike conventional agent guardrails, AgentLens detect harmful execution states from step-level hidden representations and mitigate unsafe behavior by intervening in a 10-dimensional subspace within a single layer. To support this research, we introduce the Mechanistic Agent Safety (MAS) benchmark, comprising comprehensively annotated multi-turn execution trajectories across 194 tasks using LLaMA-3.1-8B, Qwen-2.5-7B, and Gemma-2-9B. Extensive experiments show that AgentLens achieves strong safety detection performance, provides preliminary evidence for lookahead risk anticipation, and substantially reduces harmful actions of the coding agent, establishing a foundation for applying mechanistic interpretability to dynamic LLM agent safety. The code is available at: https://github.com/EddyLuo1232/AgentLens
