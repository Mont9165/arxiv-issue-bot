# Benchmarking Code Improvement with Progressive, Adaptive, and Interactive Feedback

- arXiv ID: `2607.01360v1`
- Authors: Cuong Chi Le, Aashish Yadavally, Minh Le-Anh, Tien N. Nguyen
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01360v1) | [pdf](https://arxiv.org/pdf/2607.01360v1)

## Abstract

Large language models (LLMs) are typically evaluated on code generation and program repair using binary functional correctness: a generated program or patch either passes or fails a test suite. This protocol is simple but coarse, as it ignores partial progress, feedback use, regressions, and the refinement trajectory through which models often improve code. We introduce PAIR-Bench, a progressive and adaptive benchmark for evaluating code improvement: transforming an incorrect or incomplete program into a more correct one through feedback-guided refinement. PAIR-Bench uses progressive hinting, a structured feedback protocol with two controls. Failure-region control determines what the feedback targets by grouping hidden failing tests into failure scenarios, while hint-depth control determines how much repair-relevant information is revealed, from coarse symptoms to implementation-level guidance. This design enables PAIR-Bench to measure whether a model repairs targeted failures, generalizes beyond the hint, preserves already-correct behavior, and how much assistance it requires. By evaluating repair trajectories progressive metrics rather than only final pass/fail outcomes, PAIR-Bench provides a finer-grained assessment of LLM code-improvement capability.
