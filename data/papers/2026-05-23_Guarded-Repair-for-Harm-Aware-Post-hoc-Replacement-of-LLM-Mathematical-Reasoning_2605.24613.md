# Guarded Repair for Harm-Aware Post-hoc Replacement of LLM Mathematical Reasoning

- arXiv ID: `2605.24613v1`
- Authors: Haizhou Xia
- Published: 2026-05-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.24613v1) | [pdf](https://arxiv.org/pdf/2605.24613v1)

## Abstract

Post-hoc repair of LLM mathematical reasoning introduces an asymmetric risk: fixing an incorrect reasoning trace is useful, but replacing a trace that was already correct can be harmful. We study this problem under a selective replacement setting, where a system must decide whether a repaired candidate is safer than preserving the original cached trace. We present GuardedRepair, a guarded best-of-N repair framework that diagnoses cached reasoning traces, selectively triggers repair, and accepts answer-changing candidates only when deterministic verification guards support replacement. The framework combines lightweight symbolic checks, surface semantic-risk diagnostics, bounded candidate generation, and conservative acceptance policies. On the full GSM8K test set, where the initial reasoner already achieves 95.60% accuracy, GuardedRepair improves final accuracy to 96.89%, fixing 17 of 58 remaining errors without measured broken-correct cases in the main run. On a weak-reasoner ASDiv setting, accuracy improves from 78.40% to 87.60%. Direct regeneration baselines show that this gain is not explained by stronger-model re-solving alone: re-solving all GSM8K examples lowers accuracy to 93.03% and breaks 47 initially correct answers. Additional analyses show that guarded repair substantially improves the fixed/broken tradeoff, while also revealing that replacement risk is reduced rather than eliminated. These results support viewing post-hoc repair as harm-aware selective replacement rather than unconstrained re-solving.
