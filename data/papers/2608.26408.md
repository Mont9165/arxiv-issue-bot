# STILL: Recovering Lowered STL Semantics for LLM-assisted C++ Decompilation

- arXiv ID: `2608.26408v1`
- Authors: Xiaohan Wang, Kevin Leach
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26408v1) | [pdf](https://arxiv.org/pdf/2608.26408v1)

## Abstract

LLM-assisted decompilation improves readability and re-executability, but still underperforms on stripped C++ functions that use the Standard Template Library (STL). Compilation, optimization, and symbol stripping remove or obscure source-level semantics such as container types and library-call structure, while traditional decompiler output often fails to recover them. We present STILL, a structured semantic interface that predicts function-level STL container semantics from stripped control-flow graphs and renders them as compact hints for LLM refinement. On StlBench, STILL predicts common container-level STL semantics, with the strongest cross-dataset results for stable string and vector slices. On stripped HumanEval decompilation, these hints enable DeepSeek-chat refinement to reach 28.4% executability, compared with 17.4% for no-hint refinement and 8.9% for raw Ghidra decompilation; hint utility is downstream-backbone-dependent, with decompilation-specialized models requiring lightweight adaptation to benefit from the same interface.
