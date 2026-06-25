# Evaluating LLMs on Real-World Software Performance Optimization

- arXiv ID: `2606.25530v1`
- Authors: Ezgi Sarıkayak, Wenchao Gu, Hesham Ghonim, Chunyang Chen
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2606.25530v1) | [pdf](https://arxiv.org/pdf/2606.25530v1)

## Abstract

Software performance optimization is a notoriously complex and manual task. Despite the growing use of Large Language Models (LLMs) for code refinement, we still lack benchmarks that capture how optimization actually happens in real-world codebases. Existing frameworks often oversimplify the problem by focusing on isolated functions or a single performance metric, missing the critical trade-offs between execution time and memory footprint, the inherent noise of the measurement environment, and the variability introduced by different input data and execution conditions. We address this by introducing SWE-Pro, a repository-level benchmark derived from 102 expert-written optimizations from open-source projects. Unlike previous benchmarks, SWE-Pro pairs each task with parameterized tests to evaluate runtime, peak memory, and Time-Weighted Memory Usage (TWMU) across varying input data and execution conditions under noise-aware measurement conditions. Our evaluation shows that current LLMs struggle significantly: runtime gains are negligible, and memory optimizations are nearly non-existent. This stands in sharp contrast to expert implementations, which achieve an aggregate speedup of 15.5x and peak memory reduction of 171.3x over benchmark tasks. Expert-written improvements are observed in 91.2% of tasks for runtime and 65.7% for peak memory. Our findings expose a substantial gap between current LLM capabilities and the demands of expert-level engineering.
