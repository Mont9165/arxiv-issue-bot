# MACAA: Belief-Revision Multi-Agent Reasoning for Open-World Code Authorship Verification

- arXiv ID: `2605.09421v1`
- Authors: Jingwei Ye, Zhi Wang, Xin Li, Cong Gao, Chenbin Su, Jieshuai Yang, Jianfei Tang, Ge Chu
- Published: 2026-05-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09421v1) | [pdf](https://arxiv.org/pdf/2605.09421v1)

## Abstract

Code authorship attribution (CAA) supports software forensics, plagiarism detection, and intellectual property protection. However, existing supervised CAA approaches suffer from scarce training data and closed-world assumptions: they require sufficient labeled code from fixed candidate-author sets, making training difficult in low-data cases and predictions unreliable for open-world test pairs with unseen samples, or heterogeneous code pairs. Large language models remove task-specific training, but direct prompting depends on costly expert-designed prompts, can hallucinate over complex heterogeneous code pairs, and rarely yields auditable evidence traces. We propose MACAA, a belief-revision-based multi-agent framework for training-free code authorship verification. MACAA comprises a Coordinator and four Expert Agents analyzing layout, lexical, syntactic, and programming-pattern evidence. The Coordinator gathers expert signals for expansion, discounts unreliable evidence through contraction, and resolves conflicts through revision to preserve belief consistency, replacing direct LLM judgment with auditable hypothesis refinement. MACAA achieves 89.15\% F1 on same-language benchmarks and 80.00\% on mixed cross-language pairs, surpassing all baselines.
