# ICALL-BENCH: Benchmarking LLM Interprocedural Reasoning in Binary Programs

- arXiv ID: `2610.37871v1`
- Authors: Shenglong Yao, Zirui Liu, Xiangchi Yuan, Wenke Lee
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.37871v1) | [pdf](https://arxiv.org/pdf/2610.37871v1)

## Abstract

Recent benchmarks show that LLMs achieve strong performance in both function-level binary understanding and end-to-end binary reverse engineering tasks, but whether LLMs can reason over interprocedural semantics in compiled binaries remains unclear. Function-level benchmarks offer limited visibility into cross-function relationships, while whole-program benchmarks typically evaluate final outcomes of tasks that may be solvable from local clues alone, making it difficult to disentangle interprocedural reasoning from exploration, tool use, execution, and retrieval. To address this limitation, we introduce ICALL-BENCH, a benchmark that directly evaluates whether LLMs and agents can understand and reason over interprocedural semantics in binary programs, using indirect-call target recovery as a measurable probe. ICALL-BENCH covers 50 complete real-world C/C++ programs spanning different complexity levels and multiple optimization configurations, with an average of 74,746 lines of code and 941 functions per program. We further introduce three analysis regimes spanning model-only reasoning, static tool-augmented agents, and Internet-enabled open-world agents to examine how intrinsic reasoning, active information acquisition, and external knowledge each contribute to interprocedural binary analysis. We evaluate five recent LLMs and their corresponding agents. Our results reveal a wide separation across current models and agents, with program-level verifiable success rates ranging from 23% to 81%. They also show that greater information access does not consistently lead to better results, with particularly limited gains on the hardest cases, where deeper interprocedural reasoning remains the primary bottleneck. Uneven performance across models and frequent verifiable failures even under an optimistic evaluation indicate that robust binary interprocedural reasoning remains an open challenge.
