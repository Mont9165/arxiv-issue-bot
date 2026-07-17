# Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control

- arXiv ID: `2607.14890v1`
- Authors: Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, Ian H. White
- Published: 2026-07-16
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.14890v1) | [pdf](https://arxiv.org/pdf/2607.14890v1)

## Abstract

Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence. We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate. The method treats agent outputs as claims rather than lifecycle state, and uses proof operationally to mean gate-admissible evidence under a stated trust model, not semantic program correctness.
  We evaluate an open-source implementation through mechanism tests, a powered control-policy ablation, and operated self-application evidence. The unattended-loop engine passed 10 of 10 scenarios with zero false-DONE, and local-key receipt bundles rejected 18 tamper classes with zero false accepts. In a 9,240-cell ablation, the pre-registered A4 versus A2-prime comparison reduced visible-pass/hidden-fail amplification from 31 of 1,800 injected cells under a compute-budgeted naive loop to 2 of 1,800 under the gated loop, a 1.6 percentage-point improvement in not-amplified rate with a 95 percent confidence interval of [0.8, 2.5]. A near-compute A3 versus A4 comparison, 14 of 1,800 versus 2 of 1,800, indicates that the gain is associated with enforcing review as a lifecycle gate rather than merely adding a reviewer. The self-application corpus contains 565 stories and 1,007 review findings, with 94.8 percent resolved, plus a 68-row high/critical cross-vendor exhibit. These results support Proof-or-Stop as a model-agnostic, host-neutral control layer for deciding which autonomous-agent claims a lifecycle may act on. The evaluation is limited to one model family, 24 ablation tasks, and a self-hosted corpus.
