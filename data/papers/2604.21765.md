# PrismaDV: Automated Task-Aware Data Unit Test Generation

- arXiv ID: `2604.21765v1`
- Authors: Hao Chen, Arnab Phani, Sebastian Schelter
- Published: 2026-04-23
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21765v1) | [pdf](https://arxiv.org/pdf/2604.21765v1)

## Abstract

Data is a central resource for modern enterprises, and data validation is essential for ensuring the reliability of downstream applications. However, existing automated data unit testing frameworks are largely task-agnostic: they validate datasets without considering the semantics and requirements of the code that consumes the data.
  We present PrismaDV, a compound AI system that analyzes downstream task code together with dataset profiles to identify data access patterns, infer implicit data assumptions, and generate task-aware executable data unit tests. To further adapt the data unit tests over time to specific datasets and downstream tasks, we propose "Selective Informative Feedback for Task Adaptation" (SIFTA), a prompt-optimization framework that leverages the scarce outcomes from the execution of data unit tests and downstream tasks. We evaluate PrismaDV on two new benchmarks spanning 60 tasks across five datasets, where it consistently outperforms both task-agnostic and task-aware baselines in generating unit tests that reflect the end-to-end impact of data errors. Furthermore, we show that with SIFTA, we can automatically learn prompts for PrismaDV's modules that outperform prompts written by hand or generated from a generic prompt optimizer. We publicly release our benchmarks and prototype implementation.
