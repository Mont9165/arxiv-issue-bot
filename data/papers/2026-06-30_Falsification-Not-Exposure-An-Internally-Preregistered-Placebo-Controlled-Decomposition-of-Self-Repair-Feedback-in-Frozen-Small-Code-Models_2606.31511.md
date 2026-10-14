# Falsification, Not Exposure: An Internally Preregistered Placebo-Controlled Decomposition of Self-Repair Feedback in Frozen Small Code Models

- arXiv ID: `2606.31511v1`
- Authors: Mehmet Iscan
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.31511v1) | [pdf](https://arxiv.org/pdf/2606.31511v1)

## Abstract

In deployment settings where retraining is infeasible, small frozen code models are routinely asked to repair a failed program after seeing their own failing output, usually treated as a retry mechanism. From a Popperian view, a generated program is a conjecture and a test-execution violation is an oracle-relative, executable counterexample, so feedback's value should be attributed not to re-exposure to failing code but to whether the conjecture is opened to external, executable criticism. As the third stage of a falsification-centered measurement program, this study builds a placebo-controlled instrument that decomposes the feedback packet against a blind-resampling baseline at matched output-generation budget and against content-free, shape-matched placebos. The contribution is not a new repair algorithm but a reflexive methodology (packet decomposition, placebo mirroring, matched-budget discordant-pair tests, fresh-generation confirmation, executable audits) that makes both the model's program conjecture and the researcher's "feedback content works" claim falsifiable. Across six HumanEval+/MBPP+ cells with three 0.5B-1.5B frozen models, 290 dead task-cell units (no best-of-8 candidate passing the public tier) were evaluated; the main run produced 7,000 fresh generations and a preregistered follow-up 1,400 more. Blind resampling exceeded bare-code retry by +18 net unlocks (25/7, Holm p=0.0021). Code-plus-facts recovered +18 over bare code (21/3, p=0.00042) and +15 over a generic-bullet placebo (p=0.0041). An instruction-only effect was not distinguishable (+3, p=0.36). Code-plus-facts and blind resampling tied at 26 unlocks each (not equivalence). Six external-controller follow-ups tied a content-free shape placebo. In this regime, falsification helped not as vocabulary or self-critique, but as comparison with external, executable counterexamples.
