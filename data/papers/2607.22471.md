# MineValiCoder: Reliable Code Generation with Test Case Quality Mining and Bipartite Graph-Based Mutual Validation

- arXiv ID: `2607.22471v1`
- Authors: Zhen Zhao, Qihang Yang, Feifei Dai, Xiangfang Li, Bo Li
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.22471v1) | [pdf](https://arxiv.org/pdf/2607.22471v1)

## Abstract

Large Language Model (LLM)-based Test-Driven Development (TDD) has advanced automated code generation. However, existing approaches depend heavily on human-crafted test cases and cannot operate effectively when only natural-language requirements are available. Although recent work enables automatic test generation, it often overlooks the inherent stochasticity of LLMs, leading to two key defects: faulty tests generate misleading feedback that distorts code optimization, while mixed-quality test cases produce conflicting evaluation signals that hinder reliable code selection.
  To address these challenges, we propose MineValiCoder, a collaborative closed-loop TDD framework based on the mutual reinforcement of test-case quality and code quality. MineValiCoder comprises three modules. The Test Case Quality Mining (TCQM) module filters faulty test cases through self-validation, providing reliable optimization supervision. The Parallel TDD Refinement module iteratively optimizes code and generates diverse high-quality code candidates using validated test-case feedback. The Bipartite Graph-Based Code-Test Mutual Validation (BiCoTeV) module dynamically models code-test interactions and performs mutual validation scoring for stable and reliable optimal-code selection.
  Extensive evaluations across four LLMs and mainstream benchmarks show that MineValiCoder significantly outperforms state-of-the-art methods. Specifically, it achieves Pass@1 scores of 96.34% on HumanEval, 87.40% on MBPP, 64.00% on APPS, and 51.33% on LiveCodeBench. These results demonstrate the effectiveness of MineValiCoder in mitigating LLM stochasticity and improving the reliability of automated code generation.
