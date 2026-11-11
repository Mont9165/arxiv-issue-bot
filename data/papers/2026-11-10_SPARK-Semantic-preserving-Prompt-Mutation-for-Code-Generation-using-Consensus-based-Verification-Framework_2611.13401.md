# SPARK: Semantic-preserving Prompt Mutation for Code Generation using Consensus-based Verification Framework

- arXiv ID: `2611.13401v1`
- Authors: Alireza Daghigh, Chung-Yu Wang, Luca Filippelli, Hamed Taherkhani, Hadi Hemmati, Hung Viet Pham
- Published: 2026-11-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.13401v1) | [pdf](https://arxiv.org/pdf/2611.13401v1)

## Abstract

Automated code generation with large language models (LLMs) has improved in recent years. With the lack of test cases in real-world usages, generated code is not automatically verifiable and often requires manual validation. Previous studies have leveraged consensus verification, where code solutions and corresponding test cases are generated and evaluated based on functional consistency. Building on this, SPARK incorporates semantic-preserving mutations to problem descriptions such as paraphrasing, grammatical adjustments, function renaming, and other alterations to enhance the robustness and correctness of LLM-generated code. For each mutated description, SPARK generates a set of code solutions and test cases. These candidate solutions are evaluated using consensus-based verification, where the solutions' quality is measured by how consistently they pass generated tests. We assess the effectiveness of SPARK on three benchmarks (LiveCodeBench, BigCodeBench, and DLBench) across three LLMs (o4-mini, DeepSeek-R1-Basic, and Gemini-2.5-Pro). Our evaluation demonstrates that SPARK outperforms state-of-the-art consensus-based verification approaches by up to 4.1%. Our generalization experiment highlights the practical potential of SPARK as an effective strategy for enhancing the reliability and correctness of LLM-based code generation systems in scenarios where traditional validation resources are scarce, while our qualitative analysis shows insight into how SPARK's mutation helps LLMs generate better code solutions.
