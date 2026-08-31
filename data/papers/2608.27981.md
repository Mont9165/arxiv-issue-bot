# CHISEL-ing Back Source Code with AI-enabled Iterative Recovery

- arXiv ID: `2608.27981v1`
- Authors: Varun Kohli, N Raghava, Biplab Sikdar, Dinil Mon Divakaran
- Published: 2026-08-28
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.27981v1) | [pdf](https://arxiv.org/pdf/2608.27981v1)

## Abstract

Decompilation aims to recover high-level, compilable, and semantically equivalent code from binaries. Traditional decompilers produce pseudo-C that is difficult to read and does not compile, while the recent LLM-assisted approaches generate readable, but semantically incorrect code. LLM-aided iterative recovery is an emerging branch of research, but prior works rely on supplied test suites for semantic recovery. In this work, we present CHISEL, a test suite-free framework to iteratively recover source code from Ghidra-derived pseudo-C. CHISEL uses simple yet effective feedback from a compiler (static analysis) and a coverage-guided fuzzer (differential analysis), augmented by rich observables for grounded divergence detection and feedback, cross-iteration divergence memory, and best candidate retention. We systematically evaluate CHISEL for compilation and semantic recovery, feedback oracle soundness, and iteration overhead on 120 ExeBench functions compiled for the x86-64 architecture, across four optimizations (O0-O3), in both stripped and unstripped variants, using the open-weight Gemma4:31b LLM. CHISEL, with all recommended features, achieves an average of 96.1% re-compilability and 79.8% re-executability rates at an average of 2.1 iterations. Significantly, CHISEL recovers 26% of first-generation execution errors. At the same time, CHISEL feedback oracle falsely accepts only 9.4% candidates. Lastly, CHISEL performs significantly better than two recent prior work on LLM-assisted decompilation.
