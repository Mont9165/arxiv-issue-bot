# Constraint-Guided Multi-Agent Decompilation for Executable Binary Recovery

- arXiv ID: `2604.23940v1`
- Authors: Yifan Zhang, Xiaohan Wang, Yueke Zhang, Kevin Leach
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.23940v1) | [pdf](https://arxiv.org/pdf/2604.23940v1)

## Abstract

Decompilation -- recovering source code from compiled binaries -- is essential for security analysis, malware reverse engineering, and legacy software maintenance. However, existing decompilers produce code that often fails to compile or execute correctly, limiting their practical utility. We present a multi-agent framework that transforms decompiled code into re-executable source through Multi-level Constraint-Guided Decompilation (MCGD). Our approach employs a hierarchical validation pipeline with three constraint levels: (1) syntactic correctness via parsing, (2) compilability via GCC, and (3) behavioral equivalence via LLM-generated test cases. When validation fails, specialized LLM agents iteratively refine the code using structured error feedback. We evaluate our framework on 1,641 real-world binaries from ExeBench across three decompilers (RetDec, Ghidra, and Angr). Our framework achieves 84-97% re-executability, improving baseline decompiler output by 28-89 percentage points. In comparison with state-of-the-art LLM-based decompilation methods using the same GPT-4o backbone, our approach (84.1%) outperforms LLM4Decompile (80.3%), SK2Decompile (73.9%), and SALT4Decompile (61.8%). Our ablation study reveals that execution-based validation is critical: compile-only approaches achieve 0% behavioral correctness despite 91-99% compilation rates. The system converges efficiently, with 90%+ binaries reaching correctness within 2 iterations at an average cost of $0.03-0.05 per binary. Our results demonstrate that constraint-guided agentic refinement can bridge the gap between raw decompiler output and practically useful source code.
