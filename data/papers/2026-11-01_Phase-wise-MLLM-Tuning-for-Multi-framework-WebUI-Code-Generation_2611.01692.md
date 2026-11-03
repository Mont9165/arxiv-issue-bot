# Phase-wise MLLM Tuning for Multi-framework WebUI Code Generation

- arXiv ID: `2611.01692v1`
- Authors: Haoran Ma, Linxiao Li, Chenyue Wang, Haochen Sui, Jiechao Gao
- Published: 2026-11-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.01692v1) | [pdf](https://arxiv.org/pdf/2611.01692v1)

## Abstract

Multimodal large language models (MLLMs) achieve strong performance in translating WebUI screenshots into HTML/CSS. However, when they faced multiple frameworks (React/Vue/Angular), they often suffer from negative transfer that leads to compilation failures. These failures commonly stem from mixing framework specific syntax and violating framework constraints. This paper studies supervised fine-tuning for multi-framework WebUI code generation and proposes a phase-wise MLLM tuning method driven by compatibility and heterogeneity signals across frameworks. We first apply a normalization mapping that preserves each framework's native syntax while suppressing noise from variable naming and literal content. We then estimate cross framework heterogeneity and compatibility offline, and automatically derive training groups and their ordering by maximizing a phased objective. Finally, we perform phase-wise adapter tuning to reduce cross framework interference. Experiments on multiple benchmarks show that our proposed method improves both generation quality and compilation success rate compared with baselines.
