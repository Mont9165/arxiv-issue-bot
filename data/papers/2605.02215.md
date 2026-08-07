# HEJ-Robust: A Robustness Benchmark for LLM-Based Automated Program Repair

- arXiv ID: `2605.02215v1`
- Authors: Fazle Rabbi, Jinqiu Yang
- Published: 2026-05-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02215v1) | [pdf](https://arxiv.org/pdf/2605.02215v1)

## Abstract

Recent Large Language Models (LLMs) have shown strong performance on automated program repair across standard benchmarks. However, these benchmarks evaluate models on a single canonical form of buggy code and do not reflect the syntactic variations commonly observed in real-world software, leaving robustness largely unexamined. In this work, we construct HEJ-Robust, a robustness benchmark built from HumanEval-Java-Bug using eight semantics-preserving code transformations, resulting in 1,450 transformed instances. We evaluate five fine-tuned LLMs on this benchmark and show that model performance drops by over 50% under several transformations, indicating that current LLM-based repair models lack robustness to minor syntactic variations.
