# ProCerDCL: Query-Efficient Black-Box Probabilistic Verification of Deep Learning Compiler Optimization

- arXiv ID: `2610.36499v1`
- Authors: Zexin Li, Weibo Zhang, Linyi Li, Arvind Easwaran, Simin Chen
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.36499v1) | [pdf](https://arxiv.org/pdf/2610.36499v1)

## Abstract

We present \tool, a query-efficient framework for black-box probabilistic verification. Given a fixed, sampleable input distribution and a binary property oracle, \tool assesses the property's violation probability $p$ against a threshold $θ$. Under independent sampling and stateless oracle behavior, acceptance asserts $p\leθ$, rejection asserts $p>θ+η$ for a user-specified separation margin, and an inconclusive verdict indicates insufficient evidence for either conclusion. The probability of each type of erroneous verdict is bounded by its specified error budget. To support this three-valued contract efficiently, \tool uses a single sequential test, eliminating the interval family required by the baseline. The test accounts for repeated sampling checks through either corrected exact binomial confidence intervals or an anytime-valid confidence sequence. We apply \tool to probabilistic local model semantic consistency, where the property oracle detects decision-level inconsistencies between reference and compiled executions under a specified perturbation distribution. Our evaluation covers 24 tasks across TorchInductor and TensorRT and examines sampling efficiency, conclusiveness, and diagnostic behavior. For sampling efficiency, we use paired one-model clean-label radius searches: the baseline requires 3.6-4.2 times as many unique samples under matched numerical parameters while providing a weaker decision contract. For model semantic consistency, checks at $θ=10^{-3}$ yield 817 acceptances, 19 inconclusive verdicts, and 4 rejections across 840 input--backend instances from 21 tasks. Case studies of two documented compiler faults further demonstrate what these local verdicts can diagnose.
