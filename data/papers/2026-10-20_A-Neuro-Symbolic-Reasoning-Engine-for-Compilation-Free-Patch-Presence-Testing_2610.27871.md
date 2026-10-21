# A Neuro-Symbolic Reasoning Engine for Compilation-Free Patch Presence Testing

- arXiv ID: `2610.27871v1`
- Authors: Siyuan Li, Jiayi Zhou, Zhiyuan Xia, Weijie Wang, Yaowen Zheng, Weiran Tang, Hong Li, Hongsong Zhu, Shanqing Guo
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.27871v1) | [pdf](https://arxiv.org/pdf/2610.27871v1)

## Abstract

Code reuse in modern software ecosystems facilitates the spread of 1-day vulnerabilities, posing significant security risks. Determining if patches are present is crucial, but traditional methods suffer from limited usability and accuracy, often depending on a fragile compilation process. In our prior work, we introduced Lares, the first compilation-free framework for patch presence testing that combines large language models (LLMs) with SMT solvers. However, Lares treats the LLM and the SMT solver as two separate, parallel decision channels: the symbolic channel (Z3) succeeded in only 20% of code cases, and the remaining cases fell back to the neural channel (the LLM) for the final decision. Letting the LLM act as the final arbiter turns verification into an informal, non-deterministic process that is prone to hallucination errors, while the two channels never reinforce each other. To overcome these limitations, we propose SyLares, which reformulates compilation-free patch presence testing as neuro-symbolic reasoning. Instead of letting the LLM emit a final verdict, SyLares uses the LLM as a neural feature extractor that perceives heterogeneous source code and decompiled pseudocode and produces specification-compliant SMT-LIB inputs, and delegates the final, deterministic judgment to the symbolic Z3 solver. This neural-perceives, symbolic-decides coupling is realized by a Code2SMT reasoning engine that combines deterministic syntactic parsing with LLM-driven code normalization and symbol alignment, so that every case is reduced to a formal equivalence query rather than an opaque LLM guess.
