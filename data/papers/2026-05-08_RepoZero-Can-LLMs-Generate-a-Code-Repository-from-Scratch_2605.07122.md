# RepoZero: Can LLMs Generate a Code Repository from Scratch?

- arXiv ID: `2605.07122v1`
- Authors: Zhaoxi Zhang, Yiming Xu, Weikang Li, Jiahui Liang, Yunfang Wu
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07122v1) | [pdf](https://arxiv.org/pdf/2605.07122v1)

## Abstract

Large Language Models (LLMs) have recently shown remarkable progress in code generation, yet their ability to construct complete software repositories from scratch remains poorly understood. A fundamental bottleneck is the lack of verifiable and scalable evaluation: existing benchmarks either focus on patch-based editing or rely on human or LLM-based judgments, which introduce bias and limit reproducibility. In this work, we present RepoZero, the first benchmark that enables fully automated, execution-based verification of repository-level generation from scratch. Our key idea is to reformulate generation as repository reproduction: given only API specifications, an agent must re-implement an entire repository such that its behavior matches the original implementation. This design allows for strict black-box validation via output equivalence, while naturally supporting large-scale construction by reusing existing open-source repositories. To further mitigate data leakage and shortcut solutions, we introduce cross-language constraints and a sandboxed evaluation protocol. Building on this benchmark, we propose an Agentic Code-Test Evolution (ACE) framework that performs iterative test generation and error-driven refinement, enabling effective test-time scaling for repository-level synthesis. Extensive experiments across multiple state-of-the-art LLMs and agent frameworks reveal that even the strongest LLM agents achieve only limited pass rates (30\% - 55\%), exposing a substantial gap between current capabilities and real-world software development requirements. Our results establish RepoZero as a challenging, scalable, and reliable testbed for end-to-end code generation, and highlight self-verification via test generation as a critical direction for advancing LLM-based coding agents.
