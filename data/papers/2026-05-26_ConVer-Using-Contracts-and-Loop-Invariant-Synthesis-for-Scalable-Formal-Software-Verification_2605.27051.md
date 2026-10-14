# ConVer: Using Contracts and Loop Invariant Synthesis for Scalable Formal Software Verification

- arXiv ID: `2605.27051v1`
- Authors: Muhammad A. A. Pirzada, Weiqi Wang, Yiannis Charalambous, Konstantin Korovin, Lucas C. Cordeiro
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.27051v1) | [pdf](https://arxiv.org/pdf/2605.27051v1)

## Abstract

Formal verification of large C programs is impeded by state-space explosion: Bounded Model Checking (BMC) tools must encode the entire state space up to the predetermined bound by unrolling all nested constructs. We present ConVer, a top-down compositional verification tool. Given a C program with a top-level assertion, ConVer decomposes verification top-down: it uses a large language model (LLM) to synthesise function contracts from the system property, then alternates system-level and function-level checks in a CEGAR-CEGIS loop, refining contracts whenever a check fails via SMART ICE learning. We evaluate ConVer on four benchmark suites of increasing difficulty and against other state-of-the-art (SOTA) tools. On the Frama-C benchmark of 45 simple C programs, ConVer achieves 82-96% verification success across three LLM backends, with 93-95% of converged programs requiring only a single CEGAR-CEGIS iteration. On the X.509 parser benchmark (6~programs) and LF2C-Simple suite (17 programs), ConVer achieves 33-50% and 82-88% success respectively. On the VerifyThis suite of 11 recursive and loop-intensive programs, the Pre-Abstraction strategy achieves 55-64% success. In addition, we present ESBMC-LF a preprocessor tool that converts LF models to C while preserving the properties of the LF files, enabling ConVer to verify them. We transpile the LF Verifier Benchmarks using ESBMC-LF to C; we denote those LF-Hard. We show that ConVer successfully verifies 67% of LF-Hard benchmarks overall.
