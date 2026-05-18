# Bayesian Sequential Verification for Budget-Aware Quantum Program Testing

- arXiv ID: `2605.15601v1`
- Authors: Lei Zhang
- Published: 2026-05-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2605.15601v1) | [pdf](https://arxiv.org/pdf/2605.15601v1)

## Abstract

Quantum programs often produce probability distributions rather than deterministic outputs, making verification inherently statistical and increasingly costly on real hardware. In practice, developers still frequently rely on testing with fixed shot budgets on simulators, which are simple but time-consuming and poorly suited to noisy backends. What is missing is a verification approach that is both statistically explicit and budget-aware.
  This paper formulates Bayesian sequential verification as a reference-based Bayesian hypothesis testing workflow in which priors are derived from explicit reference sources, such as finite-shot reference runs or ideal/statevector-based computation, and verification decisions are updated batch by batch as measurement evidence accumulates.
  This approach is evaluated in Qiskit on two complementary workloads: Bell-state and QAOA-MaxCut. Across both case studies, the results show that Bayesian sequential verification can substantially reduce measurement costs compared to fixed-budget baselines when the success probability of the program exceeds the target threshold.
  The findings position Bayesian sequential verification as a practical verification workflow for quantum programs. The approach provides a foundation for future quantum continuous-integration pipelines that require reliable, budget-aware pass/fail decisions and motivates validation on real quantum hardware.
