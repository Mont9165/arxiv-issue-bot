# Auditing and Decomposing Feedback-Driven Evolution in LLM Test Generation under the Oracle Problem

- arXiv ID: `2608.19626v1`
- Authors: Yunhao Liang, Chengguang Gan, Ruixuan Ying, Hanjun Wei, Zhe Cui, Shiwen Ni
- Published: 2026-08-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.19626v1) | [pdf](https://arxiv.org/pdf/2608.19626v1)

## Abstract

Execution feedback is often treated as a self-verifying signal for improving LLM-generated tests. However, when generated inputs are executed on a single accepted program and its outputs are used as ground truth, invalid or underspecified inputs can create spurious fault detections and apparent evolutionary gains. We audit this failure mode in feedback-driven test generation using 142 development tasks, 114 locked external tasks, and 138 held-out tasks, with two code models, three seeds, and fault-cross-fitted real submissions. On external inputs for which three accepted implementations agree, generated outputs match the panel on only 27.79% and 50.12% of cases. A single-reference oracle inflates the measured gain from evolution by 9.46-14.85 percentage points; after auditing, equal-budget independent resampling outperforms mutation-based evolution by 6.01-18.83 points. We further compare a genuine three-round feedback loop with a density-matched placebo. External Real-Placebo differences are +0.13 and -0.50 points, while held-out differences are +1.99 and +0.28 points and do not provide robust evidence of fine-grained feedback benefit. A blinded semantic audit by two software engineering doctoral students classifies 94.41% of panel-disconfirmed inputs as invalid but 3.60% as valid, showing that panel disagreement is informative but not semantic proof. We propose an audit-and-placebo protocol that separates verifier artifacts, interaction scaffolding, and grounded feedback credit in evaluations of self-evolving test generators.
