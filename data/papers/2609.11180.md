# SemVerBench: Benchmarking LLM Comprehension of Version-Constraint Resolution Semantics

- arXiv ID: `2609.11180v1`
- Authors: Qibai Chen, Zeming Liu
- Published: 2026-09-10
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.11180v1) | [pdf](https://arxiv.org/pdf/2609.11180v1)

## Abstract

Large language model (LLM) coding agents constantly decide whether a version satisfies a constraint such as ^1.2.3 or >=2.0,<3, yet their grasp of version-constraint semantics has never been measured directly. We introduce SemVerBench, the first benchmark of LLM version-constraint resolution semantics across three ecosystems (npm, PEP 440, Cargo): 240 machine-checkable items with unique answers, built author-neutrally from four balanced sources (each ecosystem's official test suite plus three frontier LLM proposers) and labeled by a non-circular two-implementation oracle. Evaluating six frontier models, we find systematic, predictable per-mechanism blind spots: a partial-comparator carry rule (>1.2 means >=1.3.0) traps every model on Cargo (near 60%), and although standard PEP 440 prefix matching is universal, on zero-pad/post-release corner cases GPT-5.1 collapses (0/26) while Claude stays at 97-100% (verified on a 67-item oracle-validated set). Opus significantly outperforms all other models, and Sonnet outperforms the OpenAI models (McNemar). The failures look more like an activation/application gap than a knowledge gap: injecting the rule or a light correct hint recovers most errors, whereas interval decomposition does not, and models are at ceiling on the basic forms of the same rules. An author-stratified analysis finds no statistically significant self-favoritism. Because the task is verifiable and a free, 100%-correct resolver exists, tool delegation reaches ~100%: coding agents should delegate version resolution to a resolver rather than reason about versions in-head.
