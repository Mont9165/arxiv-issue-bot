# CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates

- arXiv ID: `2607.25884v1`
- Authors: Aidan Dakhama, Ajitha Rajan
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25884v1) | [pdf](https://arxiv.org/pdf/2607.25884v1)

## Abstract

Deploying deep neural networks on resource-constrained hardware relies on mixed-precision quantisation (MPQ). current deployment toolchains severely fragment this process. Quantisation typically occurs as a hardware-agnostic preprocessing step in front-end frameworks, disconnected from the downstream compilers that generate the physical machine code. This separation leads to suboptimal configurations where assigned bit-widths map poorly to the target machine's heterogeneous hardware execution blocks such as tensor cores and variable-width vector units, incurring severe runtime execution penalties. Furthermore, evaluating these configurations via exhaustive hardware-in-the-loop (HIL) testing is intractable due to the exponentially large search space. We present CONQuER, a unified compiler-integrated infrastructure for hardware-aware MPQ. CONQuER shifts quantisation into the compiler pipeline at the TOSA level, enabling intelligent configuration handling based on compiler support. To evaluate this combinatorial search space of different of model layers within practical compilation budgets, CONQuER couples an NSGA-II evolutionary algorithm with a dual-surrogate prescreening engine. This engine evaluates theoretical cache memory bounds and feature space isotropy to discard non-viable configurations. CONQuER then executes only the strongest candidate policies on hardware via IREE, feeding the execution metrics into an online calibrator. This calibrator aligns the surrogate models with the true hardware behaviour during an NSGA-II evolutionary search. Evaluation across mobile and laptop CPUs, and server GPUs demonstrates that optimal quantisation policies are hardware-dependent. By coupling quantisation with compiler lowering and physical execution, CONQuER discovers Pareto-optimal configurations up to 12.19x faster inference with top-1 accuracy within 1.44% of the unquantised baseline.
