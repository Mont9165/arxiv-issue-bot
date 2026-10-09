# Retromorphic Testing of Quantum Compiler Passes

- arXiv ID: `2610.11195v1`
- Authors: Mushahid Khan, Olivia Di Matteo
- Published: 2026-10-08
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.11195v1) | [pdf](https://arxiv.org/pdf/2610.11195v1)

## Abstract

Quantum compilers play a critical role in transforming high-level quantum programs into optimized, hardware-compatible circuits. However, verifying the correctness of compiler passes remains challenging, as determining the expected output of large, deeply entangled quantum circuits is computationally intractable. This challenge is further amplified when compiler passes modify already complex circuit structures, making manual validation of transformed circuits impractical.
  In this work, we perform a systematic analysis of unit tests for quantum compiler passes in four quantum programming frameworks (PennyLane, Qiskit, Cirq, and pytket). Our findings indicate validation is dominated by program-content and program-metric assertions, and test circuits are generally small and shallow. Motivated by these observations, we introduce a testing methodology for automated validation of quantum compiler passes based on retromorphic testing and principles from the Hadamard test. This methodology analyzes a compiler pass, test circuit, and expected pass behavior to verify semantic preservation and intended structural modifications.
  We implement our methods in a framework, RetroQ, and apply it to compiler passes in PennyLane and Qiskit. Experimental evaluation reproduced several existing bugs as well as uncovered previously undetected defects, such as flawed symbolic parameter handling, incorrect commutation logic, failure to recognize self-adjointness of gates, and runtime crashes. These findings highlight the need for compiler-pass-specific testing methodologies to improve the reliability of the evolving quantum software stack.
