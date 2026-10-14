# Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models

- arXiv ID: `2606.16999v1`
- Authors: Mehmet Iscan
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.16999v1) | [pdf](https://arxiv.org/pdf/2606.16999v1)

## Abstract

Frozen small code models (<=1.5B parameters, run locally without fine-tuning) suit offline and privacy-constrained use, but often emit plausible-but-wrong programs. A natural remedy is a post-hoc operator that selects, verifies, repairs, or re-processes the model's samples without retraining; in principled form it is Popperian: attack each candidate with a severe test, keep what survives. We measure whether such operators help. Under one deterministic execution oracle and a leakage-free, matched-compute protocol, 26 semantic post-hoc operators (selection, verification, repair, elimination, portfolios, sound vetoes, generation conditioning) are evaluated against Best-of-N (BoN); on the cells and benchmarks tested, none improves held-out accuracy over BoN. The negative is mechanistic: a coverage wall (systematic hard-task failures deeper sampling does not rescue), a capability scissors (a competent generator leaves almost no discriminable error among visible-test passers), and a near-empty consensus trap (the visible-pass-but-hidden-wrong majority a leakage-free selector needs rarely co-occurs with a correct alternative). A distribution-free do-no-harm bound cannot certify a harm rate <=alpha at zero observed harm unless n>=45. Two operators help on a different axis, outside the semantic output space. An expression-layer recovery (M1), the only accuracy gain here, recovers correct programs the standard extractor discards (robust extraction and public-test signature alignment); it does no harm (b10=0), is leakage-free, and lifts DeepSeek-Coder-1.3B by +12 tasks on HumanEval+ (p=2.4e-4). An adaptive consensus early-stop (ACE) is a calibrated compute-saving control (~19% saving, zero harm). M1 and the selection negative replicate on HumanEval+ and MBPP+ across three model cells. The lesson: fix the harness and measure coverage before blaming semantic post-hoc reasoning.
