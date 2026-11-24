# Multi-Agent Coordinated Method-Level Refactoring of Rust Code

- arXiv ID: `2611.29321v1`
- Authors: Yijian Zheng, Yi Zhang, Juyuan Zhang, Di Cui
- Published: 2026-11-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.29321v1) | [pdf](https://arxiv.org/pdf/2611.29321v1)

## Abstract

As Rust codebases evolve, developers refactor code to reduce duplication, simplify complex methods, and keep related functionality together. Developers can make these changes manually or use IDE assists for supported operations, then check the resulting code with compiler diagnostics and tests. Method-level refactoring in Rust must preserve observable behavior while accounting for ownership, borrowing, and lifetimes. We present a large language model (LLM)-based workflow for extracting, inlining, and moving methods in Rust. The workflow combines candidate generation, configurable specialist review,and container-based validation. On six tasks from three open-source Rust projects, three end-to-end configurations passed all task checks on their first attempt, using 6, 13, and 31 model calls. To isolate the effect of review, we then gave four configurations the same six reference patches and six deliberately behavior-changing variants. A designated specialist rejected all six behavior-changing patches before container validation and let all six reference patches proceed, reducing Docker invocations from 24 to 12 relative to direct validation. The fixed specialist panel also caught all six faults early and rejected two reference patches over unmeasured performance concerns. On this workload, specialist review reduced execution work, while its effect on total time depended on review overhead and which patches reached validation.
