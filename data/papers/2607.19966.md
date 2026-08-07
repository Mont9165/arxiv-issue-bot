# Towards Reliable C-to-Rust Translation with Rule-Guided Reasoning and Reinforcement Learning

- arXiv ID: `2607.19966v1`
- Authors: Feng Luo, Jiachen Liu, Cuiyun Gao, Jia Feng, Kui Liu
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.19966v1) | [pdf](https://arxiv.org/pdf/2607.19966v1)

## Abstract

The migration of legacy C programs to Rust has become an important direction for improving software memory safety while alleviating the high cost of manual rewriting. Leveraging large language models (LLMs) for automated C-to-Rust translation has emerged as a promising direction. However, existing LLM-based approaches remain limited. On the one hand, LLMs exhibit limited capability in identifying Rust-specific rules, and inadequate handling of Rust syntax often results in incorrect translations. On the other hand, existing LLMs often struggle to accurately capture the semantics of complex code, resulting in incorrect translations. To address these challenges, we propose a Translation fRAmework Via rule-guided reasoning and rEinforcement Learning, namely TRAVEL, consisting of two modules. The first module employs Monte Carlo Tree Search (MCTS)-based reasoning path construction guided by Rust-specific rules, steering the search toward translation steps that respect the syntactic rules that LLMs frequently violate. The second module introduces reinforcement learning that couples execution feedback with reasoning-quality signals, encouraging the model to construct reasoning paths that accurately capture program semantics, thereby ensuring that the generated Rust code preserves the intended behavior of the original C program. We evaluate TRAVEL on three datasets: xCodeEval (a public benchmark), OS-Bench (functions collected from the Linux kernel), and HW-Bench (an industrial dataset from Huawei). On xCodeEval, TRAVEL outperforms all baselines across three backbone LLMs. In particular, compared to the strongest prompting baseline IRENE, TRAVEL improves computational accuracy (CA) by 26.22% and compilation success rate (CSR) by 18.77%. On HW-Bench and OS-Bench, TRAVEL further improves CSR by 18.28% and 16.51%, respectively, while reducing unsafe rate (UR) by 13.06% and 13.08%, respectively.
