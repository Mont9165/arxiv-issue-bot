# Repo0: Design-Driven Zero-to-All Code Generation

- arXiv ID: `2608.19854v1`
- Authors: Silin Chen, Haoyi Teng, Xiaodong Gu, Yuling Shi, Jiale Huang, Yongpan Wang, Hongyu Zhang, Haibing Guan
- Published: 2026-08-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.19854v1) | [pdf](https://arxiv.org/pdf/2608.19854v1)

## Abstract

Large language model agents have made substantial progress in code generation, yet most existing systems assume a predefined repository architecture. This assumption does not hold in zero-to-all code generation, where an agent must construct an entire software project directly from natural-language requirements while maintaining a modular repository architecture throughout development. We present Repo0, a continuous structural evolution framework for zero-to-all code generation. Repo0 maintains an explicit architectural state instantiated as a Dual-Directed-Acyclic-Graph (Dual-DAG), consisting of a requirement-level DAG, a component-level DAG, and their alignment relation. Starting from natural-language requirements, it iteratively evolves component boundaries through structural actions guided by modularity metrics until structural convergence, after which the converged architecture guides test-driven development code generation. We evaluate Repo0 on six real-world repositories from RepoCraft using GPT-5 mini and DeepSeek V3.2. Repo0 achieves the highest Functionality Coverage and Pass Rate across all settings. Compared with RPG, the strongest repository-planning baseline, Repo0 improves Functionality Coverage by up to 20.08 percentage points and Pass Rate by up to 29.74 percentage points. Ablation and structural-evolution analyses further demonstrate the importance of the Dual-DAG architectural state, modularity-guided structural evolution, and explicit structural convergence.
