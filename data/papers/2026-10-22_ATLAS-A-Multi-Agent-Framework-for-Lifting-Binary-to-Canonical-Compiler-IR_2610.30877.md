# ATLAS: A Multi-Agent Framework for Lifting Binary to Canonical Compiler IR

- arXiv ID: `2610.30877v1`
- Authors: Xiaoao Zhu, Ni Zhang, Jie Ren, Zhiqiang Li, Jie Zheng, Zhanyong Tang, Zheng Wang
- Published: 2026-10-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.30877v1) | [pdf](https://arxiv.org/pdf/2610.30877v1)

## Abstract

Lifting stripped, heavily optimized binaries to a canonical, pre-optimization LLVM intermediate representation (IR) is essential for downstream security analysis and legacy software migration when source code is unavailable. However, aggressive compiler optimizations rewrite control and data flow, remove structural metadata, and introduce type-erased low-level idioms, causing current lifters to produce malformed or semantically divergent IR. We present ATLAS, a multi-agent framework designed to reconstruct formally valid and canonical LLVM IR from optimized disassembly.ATLAS combines (i) Structure-aware, region-level retrieval, which utilizes pseudo-probe attribution to align optimized instructions with canonical IR exemplars, and (ii) a collaborative refinement loop that closes the gap between probabilistic generation and deterministic compiler constraints. Concretely, a Lift agent generates an initial IR draft conditioned on retrieved exemplars, an Advisor agent interprets LLVM verifier/compilation diagnostics and static checks to propose localized repair actions, and a Validation agent applies the edits, re-runs toolchain verification and (when available) runtime checks, and feeds the resulting diagnostics back to the Advisor. The agents iterate until the IR is verifier-clean and behaviorally consistent, or a budget limit is reached. On HumanEval-Decompile and MBPP, ATLAS outperforms seven baselines on lifting LLVM IR, achieving 91.8% re-executability and 89.4% CFG similarity across ARM, x86-64, and RISC-V binaries. Moreover, our evaluation demonstrates that ATLAS also outperforms the Binary to C to IR pipelines in pointer-flow precision and downstream analyzability. By recovering a well-formed, machine-centric representation, ATLAS enables practical cross-ISA recompilation and verifiable binary-only migration workflows.
