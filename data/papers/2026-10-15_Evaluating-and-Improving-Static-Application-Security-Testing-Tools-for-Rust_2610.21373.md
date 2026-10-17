# Evaluating and Improving Static Application Security Testing Tools for Rust

- arXiv ID: `2610.21373v1`
- Authors: Huaien Zhang, Zhengjie Zhao, Yu Pei, Tian Dong, Minxue Pan, Shin Hwei Tan, Hao Chen
- Published: 2026-10-15
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.21373v1) | [pdf](https://arxiv.org/pdf/2610.21373v1)

## Abstract

Rust has become a popular systems programming language in recent years because of its strong guarantees on memory and concurrency safety. Many types of system software have been re-implemented in Rust. However, Rust programs can still suffer from common memory and concurrency vulnerabilities due to unsafe code and misunderstandings of its complex mechanisms. To mitigate such vulnerabilities, developers often rely on static application security testing (SAST) tools. However, the effectiveness of existing Rust SAST tools on real-world vulnerabilities remains underexplored. In this paper, we first conduct an empirical evaluation of mainstream Rust SAST tools using security vulnerabilities identified in real-world Rust applications. We systematically assess their effectiveness, uncover common weaknesses, and analyze the root causes behind them. Motivated by the study, we propose TRUST, a large language model (LLM)-assisted automated testing framework. TRUST automatically analyzes the official Rust reference to derive and implement semantics-preserving transformations. It leverages these transformations to generate mutant programs for evaluating Rust SAST tools and uncovering potential faults within them. Overall, TRUST has revealed 46 faults across six popular SAST tools, 17 of which have been confirmed. In addition, our study yields ten empirical findings and four practical lessons that provide actionable guidance for developing more effective, robust, and maintainable Rust SAST tools.
