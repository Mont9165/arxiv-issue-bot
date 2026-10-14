# CLIR: Liveness-Driven and Structure-Aware Fuzzing for the Cranelift Compiler

- arXiv ID: `2606.26977v1`
- Authors: Shangtong Cao, Tianlei Song, Qiuping Yi, Tianyu Chen, Guoai Xu, Ningyu He, Haoyu Wang
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.26977v1) | [pdf](https://arxiv.org/pdf/2606.26977v1)

## Abstract

Modern compilers are complex software systems that must correctly translate high-level programming languages into machine code across multiple architectures. Cranelift, a fast and modern compiler backend originally developed for WebAssembly and recently adopted as an experimental backend for Rust, has gained increasing importance due to its superior compilation speed compared to LLVM and comprehensive multi-architecture support, including x86-64, AArch64, s390x, and RISCV64. However, despite decades of development in compiler testing, testing Cranelift still presents unique challenges, including (1) constructing valid IR under the strict enforcement of SSA form, (2) generating sequences with sufficient computational density to stress backend components, and (3) balancing broad backend coverage with efficient root cause analysis across heterogeneous architectures.
  To address these challenges, we propose CLIR, a differential testing framework that integrates a syntax-preserving hierarchical generation strategy to guarantee SSA validity, a liveness-guided instruction refinement mechanism to maximize computational density, and a diagnosis-guided cross-architecture adaptation scheme to facilitate efficient root cause analysis across heterogeneous backends. Our comprehensive evaluation demonstrates that CLIR significantly outperforms existing state-of-the-art baselines, detecting 8x, 24x, and 8x more unique bugs than cranelift-fuzzgen, wasm-smith, and WASMaker, respectively, while RustSmith uncovered no bugs. Consequently, within 72 hours of testing, CLIR discovered 24 bugs spanning all target architectures, with 21 confirmed and 9 fixed.
