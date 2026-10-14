# Agentic Separation Logic Specification Synthesis

- arXiv ID: `2605.27531v1`
- Authors: Tarun Suresh, David Korczynski, Julien Vanegue
- Published: 2026-05-26
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.27531v1) | [pdf](https://arxiv.org/pdf/2605.27531v1)

## Abstract

Specification synthesis, the task of automatically inferring formal specifications from program implementations and natural language, is important for refactoring, transpilation, optimization, and verification, yet remains an open challenge for large C++ repositories. Existing LLM-based approaches fail to simultaneously scale to such repositories, produce specifications expressive enough to capture systems-code features such as dynamic memory and heap-allocated data structures, and systematically validate those specifications to rule out incorrect candidates. We present Spec-Agent, an agentic system for synthesizing expressive, well-validated specifications across large C++ codebases. Spec-Agent targets a ladder of specification languages: propositional logic, first-order logic, propositional separation logic, and first-order separation logic. For each function, Spec-Agent uses static analysis and runtime heap tracing to select the appropriate target specification language, generalizes existing functional tests into fuzz harnesses, and iteratively refines LLM-generated candidates via counterexample-guided feedback. We evaluate Spec-Agent on open source C++ codebases comprising millions of lines of code. Spec-Agent synthesizes valid specifications for 85% of target functions, with no false positives observed under fuzzing and expert validation, outperforming Claude Code Opus 4.6 at 10x lower token cost.
