# RubricRefine: Improving Tool-Use Agent Reliability with Training-Free Pre-Execution Refinement

- arXiv ID: `2605.09730v1`
- Authors: Will LeVine, Brendan Evers, Sam Saltwick, Abhay Venkatesh
- Published: 2026-05-10
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09730v1) | [pdf](https://arxiv.org/pdf/2605.09730v1)

## Abstract

Iterative self-refinement is a popular inference-time reliability technique, but its effectiveness in code-mode tool use depends heavily on the structure of the feedback signal: unstructured critique helps inconsistently across models, and even revision with real execution feedback improves only modestly ($0.75$ vs. $0.65$ baseline). The dominant failures are inter-tool contract violations - wrong output shape, incorrect tool routing, broken argument provenance - that run to completion without raising errors, making runtime feedback insufficient. We introduce RubricRefine, a training-free pre-execution reliability layer that generates task- and registry-specific rubrics, scores candidate code against explicit contract checks, and iteratively repairs failures before any execution occurs. With zero execution attempts, RubricRefine reaches $0.86$ on M3ToolEval averaged across seven models-improving over prior inference-time baselines on every model tested on this benchmark, at $2.6X$ lower latency than the strongest non-iterative alternative - and remains flat on the predominantly single-step API-Bank, consistent with the method's reliance on inter-tool contract structure. A rubric-category ablation and calibration analysis further characterize when and why the method works.
