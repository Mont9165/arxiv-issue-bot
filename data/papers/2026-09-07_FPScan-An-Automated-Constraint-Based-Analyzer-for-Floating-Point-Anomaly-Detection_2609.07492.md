# FPScan: An Automated Constraint-Based Analyzer for Floating-Point Anomaly Detection

- arXiv ID: `2609.07492v1`
- Authors: Julien Bortolussi, Dorra Ben Khalifa, Pierre-Loïc Garoche
- Published: 2026-09-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `math.NA`
- Links: [abs](http://arxiv.org/abs/2609.07492v1) | [pdf](https://arxiv.org/pdf/2609.07492v1)

## Abstract

Writing error-free floating-point programs is a challenging task, especially for programmers who lack a strong background in numerical analysis and rounding-error propagation. State-of-the-art techniques typically aim to bound such errors using static or dynamic analysis. However, only a few tools explicitly address critical floating-point pitfalls such as absorption and catastrophic cancellation. These anomalies represent situations in which rounding errors are significantly amplified, causing the semantics of the finite-precision computation to deviate substantially from the real-number semantics. In this article, we present FPScan, a novel tool to formally define and detect both catastrophic cancellation and absorption in floating-point programs. Our approach starts with a custom static analyzer based on abstract interpretation to infer the order of magnitude of all program variables. This magnitude information is then used to build a set of first-order constraints that model error propagation and numerical precision within the program. Finally, we employ an off-the-shelf SMT solver to determine whether the program exhibits any of these critical numerical pitfalls. Experiments were conducted on FPBench, a well-known benchmark suite of floating-point programs, to evaluate the effectiveness of our tool. We also present a comparison with state-of-the-art tools regarding soundness and analysis time.
