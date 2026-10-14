# Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs

- arXiv ID: `2607.12273v1`
- Authors: Xiaoning Ren, Yinxing Xue, Lei Ma, Yuheng Huang
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.12273v1) | [pdf](https://arxiv.org/pdf/2607.12273v1)

## Abstract

As Code Large Language Models (LLMs) become central to modern software engineering, their inherent stochasticity poses significant real-world risks, where even minor errors can lead to severe functional, security, or safety consequences. Reliable automation, therefore, demands the ability to distinguish between confident, well-supported predictions and stochastic guessing. However, existing uncertainty estimation methods face a critical gap: white and grey-box techniques are often inapplicable to closed-source models, while standard "black-box" text metrics fail to capture the unique fragility of code, where syntactic variation does not always imply semantic divergence. To bridge this syntax-semantics gap, we introduce Code-MUE, a purely black-box framework that measures uncertainty through execution-based Semantic Interaction Graphs. Unlike prior approaches that rely on superficial textual similarity, Code-MUE grounds uncertainty in observable runtime behavior, calculating the Von Neumann entropy of the solution space to quantify global semantic diversity. A large-scale empirical study across eight state-of-the-art LLMs demonstrates that Code-MUE achieves a strong negative correlation with functional correctness (Spearman's correlation up to -0.98), significantly outperforming lexical and embedding-based baselines while enabling robust risk detection and selective prediction in practical workflows.
