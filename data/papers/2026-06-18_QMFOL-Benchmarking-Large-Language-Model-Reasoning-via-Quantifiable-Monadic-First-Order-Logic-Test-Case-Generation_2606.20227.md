# QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation

- arXiv ID: `2606.20227v1`
- Authors: Xinyi Zheng, Ling Shi, Tianlong Yu, Yongxin Zhao, Lorenz Goette, Kailong Wang
- Published: 2026-06-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.20227v1) | [pdf](https://arxiv.org/pdf/2606.20227v1)

## Abstract

Large Language Models (LLMs) have made significant progress in reasoning, particularly in deductive reasoning, which is crucial for high-stakes decision-making. As models improve, evaluation benchmarks should evolve to keep pace. However, existing benchmarks lack fine-grained control over logical complexity and struggle to balance semantic diversity with logical consistency.
  To address these issues, we propose QMFOL, an automated framework for generating monadic first-order logic reasoning tasks with quantifiable and controllable complexity. It constructs formal logical structures using conjunction and disjunction patterns, enabling precise control over reasoning depth, width, label types, and distractors. These structures are then translated into natural language via LLMs, with logical consistency ensured through round-trip verification using an external prover. Based on our framework, we build QMFOLBench, a benchmark comprising 2880 instances with 960 configurations across diverse logical and semantic dimensions. Evaluations on six large reasoning models (LRMs) and two LLMs show that performance degrades and computational overhead increases with rising logical complexity. Models perform better on True-labeled tasks than on False or Unknown ones, and exhibit sensitivity to semantic variation. Overall, QMFOL offers a scalable and reliable approach for constructing deductive reasoning benchmarks with controllable complexity, enabling more precise evaluation of reasoning capabilities in modern language models.
