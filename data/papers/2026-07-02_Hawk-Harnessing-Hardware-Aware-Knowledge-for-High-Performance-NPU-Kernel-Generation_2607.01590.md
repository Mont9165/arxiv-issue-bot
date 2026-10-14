# Hawk: Harnessing Hardware-Aware Knowledge for High-Performance NPU Kernel Generation

- arXiv ID: `2607.01590v1`
- Authors: Junyi Wen, Ruiyan Zhuang, Yongjia Xu, Pengtu Li, Rui Zou, Hongyi Chen, Chingman Wan, Puxu Yang, Wuhui Chen, Yanlin Wang
- Published: 2026-07-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01590v1) | [pdf](https://arxiv.org/pdf/2607.01590v1)

## Abstract

Developing high-performance kernels for Neural Processing Units (NPUs) is a critical industry bottleneck, requiring developers to manually navigate implicit hardware constraints and strict memory hierarchies. While large language models offer immense automation potential, they fail catastrophically on NPUs due to a fundamental lack of hardware-specific priors. Naively transplanting code snippets from similar NPU kernels may pass the compiler, but it consistently triggers runtime crashes and performance degradation by blindly violating underlying hardware constraints. To overcome this, we introduce Hawk, a training-free framework that harnesses hardware-aware knowledge through three core modules: (1) Run-Time Knowledge Synthesis Module, which employs a Triple-Part Executable Knowledge Representation to inherently couple the error context with executable semantics; (2) Bottleneck-Aware Knowledge Retrieval Module, which implements a 2D-Retrieval paradigm to project queries into orthogonal syntactic and hardware-aligned semantic spaces; and (3) Effect-Driven Knowledge Distillation Module, which leverages LLM-driven semantic arbitration to continuously distill the knowledge by pruning errors and consolidating redundancies based on the empirical execution feedback. Extensive evaluations on real-world NPU workloads demonstrate that Hawk elevates generation accuracy from 49.4% to 80.0%, while achieving up to a 2.2x execution speedup over state-of-the-art baselines.
