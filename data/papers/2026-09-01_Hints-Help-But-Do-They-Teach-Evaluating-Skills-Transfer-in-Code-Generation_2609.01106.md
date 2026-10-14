# Hints Help But Do They Teach? Evaluating Skills Transfer in Code Generation

- arXiv ID: `2609.01106v1`
- Authors: Will Badr
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2609.01106v1) | [pdf](https://arxiv.org/pdf/2609.01106v1)

## Abstract

When a hint turns a failing generated program into a passing one, does it provide missing information or merely steer the model toward a solution it could already produce? We test these hypotheses on HumanEval+ and MBPP+ using executable evaluation. For Qwen2.5-3B-Instruct, adaptive relevant hints rescue 36 of 79 selected failures; an unrelated hint rescues 19, while eight unhinted samples solve 46 and recover 31 of the 36 relevant-hint rescues. Phi-3.5-mini shows the same pattern: relevant hints rescue 42 of 101 failures, an unrelated hint rescues 17, and unhinted sampling solves 57, including 36 of the 42 relevant-hint rescues. Because the hint conditions use different attempt budgets, these comparisons do not isolate a purely semantic effect. Mechanistic tests on Qwen identify a stable activation direction shared by relevant and unrelated hints. Persistently adding this direction yields 14 rescues and 18 regressions, with no detectable net accuracy gain; learned low-rank interventions have a positive but imprecise estimated effect. Full textual specifications solve 22 of 24 context-defined problems, versus 5-11 for tested virtual-KV prefixes. Post-generation hidden-state probes transfer across benchmarks, with pooled AUROC 0.806 and 0.780, but their top-one selection advantage over token confidence is statistically unresolved. Overall, relevant hints can rescue failures, but most rescued solutions are already reachable through ordinary sampling, and the internal interventions tested here do not establish task-general capability transfer.
