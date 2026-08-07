# Loop-Based Slicing and Input-Driven Concretization: An Empirical Study of Termination and Non-Termination Analysis

- arXiv ID: `2607.08988v1`
- Authors: Negar Fathi, Rahul Purandare, Tachio Terauchi, Hiroshi Unno
- Published: 2026-07-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.08988v1) | [pdf](https://arxiv.org/pdf/2607.08988v1)

## Abstract

Termination and non-termination are fundamental correctness properties, but verifying them in real-world C programs remains difficult because loop interactions and nondeterministic inputs challenge existing analyzers. This paper presents an empirical study of lightweight, tool-independent source-level preprocessing for (non-)termination analysis. We implement FocusTNT, a C front end that applies loop-based slicing to isolate loop-level obligations and input-driven concretization to specialize nondeterministic inputs into selected input-scenario variants. We evaluate slicing, concretization, and their combination across six analyzers on 117 C/C++ programs derived from real-world non-termination bugs and their fixes. The study examines effects on analyzer correctness, complementarity with original-program analysis, loop-level diagnostics, feature sensitivity, runtime behavior, semantic scope, and integration potential. Results show that preprocessing is not uniformly beneficial: its impact depends on the analyzer, task, and program features. Slicing provides conservative structural isolation and localization, whereas concretization can improve detectability for selected scenarios but narrows semantic scope and may increase analysis effort. Their combination is not consistently additive. Overall, the results support adaptive use of preprocessing as a complement to original-program analysis and provide practical guidance to application developers interpreting verification outcomes and tool developers improving analyzer robustness.
