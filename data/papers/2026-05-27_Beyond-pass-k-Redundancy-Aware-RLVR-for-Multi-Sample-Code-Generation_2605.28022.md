# Beyond pass@k: Redundancy-Aware RLVR for Multi-Sample Code Generation

- arXiv ID: `2605.28022v1`
- Authors: Le Bronnec Florian, Alexandre Verine, Rio Yokota, Benjamin Negrevergne
- Published: 2026-05-27
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.28022v1) | [pdf](https://arxiv.org/pdf/2605.28022v1)

## Abstract

LLMs for code generation are commonly evaluated in repeated-sampling settings using Pass@k, where multiple candidate programs are executed against unit tests under a finite sampling budget. While recent verifier-based reinforcement learning (RLVR) methods improve executable correctness, how these objectives affect redundancy among sampled programs remains poorly understood. In this work, we study implementation-level redundancy in code generation using JPlag, a plagiarism-detection system for code. Across models and benchmarks, we show that correctness-only RLVR often concentrates generations around repeated implementations, whereas Pass@k-aware objectives maintain lower redundancy and improve larger-budget performance. Motivated by these observations, we augment RLVR with direct anti-redundancy rewards based on JPlag similarity. Across 3 models and 3 benchmarks, discouraging near-duplicate generations reliably improves finite-budget executable performance, often matching or outperforming specialized Pass@k-aware objectives.
