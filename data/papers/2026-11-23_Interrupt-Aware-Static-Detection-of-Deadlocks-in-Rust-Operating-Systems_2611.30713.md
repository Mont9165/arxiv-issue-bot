# Interrupt-Aware Static Detection of Deadlocks in Rust Operating Systems

- arXiv ID: `2611.30713v1`
- Authors: Yuzhi Li, Hongliang Tian, Chengjun Chen, Jianfeng Jiang, Hui Xu
- Published: 2026-11-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.30713v1) | [pdf](https://arxiv.org/pdf/2611.30713v1)

## Abstract

Rust is increasingly adopted in operating systems, but Rust's safety guarantees do not eliminate deadlocks, especially those induced by interrupts. The core challenge is to recover interrupt-sensitive lock dependencies from Rust's guard-based synchronization across function boundaries. Applying this analysis across Rust OS projects also requires specifying project-specific synchronization semantics. We present an approach combining interrupt-aware static analysis with diagnostic-guided agent auditing for detecting deadlocks in Rust operating systems. Our approach uses lightweight source-level annotations to recover project-specific lock and interrupt semantics, performs a flow-sensitive MIR-based analysis to track lock-holding and interrupt states, and reports potential deadlocks with supporting evidence. An agent then searches for relevant source code in the repository and returns a confidence assessment with reasons for each supplied report. We evaluate our tool on four real Rust operating systems, identifying 26 true cases corresponding to nine maintainer-confirmed defects. Diagnostic-guided auditing achieves 86.2\% precision and 96.2\% recall based on static analysis results, and offers advantages over the baselines in both cost and effectiveness.
