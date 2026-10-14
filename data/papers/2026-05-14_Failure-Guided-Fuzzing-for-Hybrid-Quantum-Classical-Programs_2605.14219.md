# Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs

- arXiv ID: `2605.14219v1`
- Authors: Lei Zhang
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2605.14219v1) | [pdf](https://arxiv.org/pdf/2605.14219v1)

## Abstract

Hybrid quantum-classical (HQC) algorithms, such as the Variational Quantum Eigensolver (VQE) and the Quantum Approximate Optimization Algorithm (QAOA), are central to near-term quantum computing but remain challenging to test. Sampling-based fuzzing can expose faulty or non-convergent configurations, but under realistic execution budgets, it may miss failure-prone regions in the joint space of classical optimizer settings and quantum circuit parameters.
  This paper studies failure-guided fuzzing for HQC programs. It models a hybrid input as a pair of classical optimizer hyperparameters and quantum circuit parameters, and evaluates a two-phase strategy that first searches for non-convergent seeds and then locally fuzzes circuit parameters around those seeds. To understand where the gains come from, five budgeted strategies are compared: random hybrid testing, classical enumeration without fuzzing, random-seed local fuzzing, enumeration-seed local fuzzing, and concolic-seed local fuzzing. The study is implemented on a VQE instance and a QAOA MaxCut instance in Qiskit. The results show that failure-guided local fuzzing is the main driver of improvement over random testing, while concolic seed discovery provides additional benefits on VQE but is less stable on QAOA. These findings suggest that reusing failure information is a promising direction for HQC testing, but that the value of concolic seed discovery is workload-dependent.
