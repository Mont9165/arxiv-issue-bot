# Foundational Constraint Solving for Expressive Refinement Typing

- arXiv ID: `2607.12226v1`
- Authors: Jam Kabeer Ali Khan, Petros Markopoulos, Nico Lehmann, Ranjit Jhala
- Published: 2026-07-14
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12226v1) | [pdf](https://arxiv.org/pdf/2607.12226v1)

## Abstract

SMT-based program verifiers are hamstrung by two problems: expressiveness, because predictable verification restricts to the boundaries of SMT decidability, and trust, because the solver is a large, unverified artifact whose soundness bugs may quietly compromise every tool built on it. We present FLEX, a foundational Constrained Horn Clause (CHC) solver implemented in LEAN, that reduces the trusted base to the kernel alone, and allows using LEAN's entire proof ecosystem to verify low-level systems code, via three contributions. First, FLEX encodes CHCs as plain LEAN propositions where the Horn variables are existentially bound predicates, and shows how to implement CHC solvers as tactics (meta-programs) that compute kernel checkable proofs of the CHC propositions. Second, we show how to implement two verified CHC generators in LEAN: a Floyd-Hoare style generator for an imperative language, and a refinement-type-based generator for a functional calculus, which can be composed with the solving tactics to yield the first end-to-end foundational CHC-based verifiers. Finally, we show how FLEX allows us to leapfrog the expressiveness limitations of SMT by unleashing LEAN's entire ecosystem of proof machinery to prove arbitrary functional correctness properties of various low-level Rust libraries using the FLUX refinement type checker, and demonstrate the viability of FLEX as a trustworthy CHC backend, by showing it automatically discharges 95.7% of the CHCs from FLUX's benchmark suite.
