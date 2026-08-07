# REBENCH: A Procedural, Fair-by-Construction Benchmark for LLMs on Stripped-Binary Types and Names (Extended Version)

- arXiv ID: `2604.27319v1`
- Authors: Jun Yeon Won, Xin Jin, Shiqing Ma, Zhiqiang Lin
- Published: 2026-04-30
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.27319v1) | [pdf](https://arxiv.org/pdf/2604.27319v1)

## Abstract

Large Language Models (LLMs) have achieved remarkable progress in recent years, driving their adoption across a wide range of domains, including computer security. In reverse engineering, LLMs are increasingly applied to critical tasks such as function and variable name recovery and type inference. However, despite the rapid growth of research in this area, progress has been hindered by the absence of a standardized dataset. Existing studies rely on disparate datasets, preprocessing pipelines, and evaluation metrics, making fair comparisons between approaches difficult and obscuring a clear understanding of LLM capabilities in binary analysis. To address these challenges, we present REBench, a comprehensive benchmark dataset for evaluating LLMs on binary reverse engineering tasks. REBench consolidates a superset of existing datasets, comprising hundreds of millions of lines of source code and a diverse collection of binaries spanning multiple architectures and optimization levels. REBench adopts a knowledge-base-driven methodology that stores byte-level stack information to generate ground truth, ensuring that task difficulty is preserved while maintaining universal applicability. This design enables fair evaluation across tasks while avoiding simplifications that could bias results. As a use case, we apply REBench to measure the reverse engineering performance of LLMs and the result demonstrates difficulties in complex tasks.
