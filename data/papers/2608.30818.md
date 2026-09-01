# ProofPulse: Interactive Proof Coverage Analysis for Dafny

- arXiv ID: `2608.30818v1`
- Authors: Álvaro F. Silva, Ruben Martins, Alexandra Mendes
- Published: 2026-08-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30818v1) | [pdf](https://arxiv.org/pdf/2608.30818v1)

## Abstract

Deductive verification ensures that an implementation satisfies its specification, but successful verification does not guarantee the quality of the specification. As such, weak specifications and redundant invariants may create overconfidence in ``verified'' code.
  We present \proofpulse, a tool for Dafny that diagnoses specification quality using a three-valued proof coverage model. By analyzing proof dependencies, ProofPulse distinguishes between elements that contribute to specification intent, those used only for auxiliary checks, and those irrelevant to any proof obligation.
  Evaluated against an oracle of 252 programs from the dafny-synthesis benchmark, ProofPulse provides a high-precision signal for specification weaknesses, particularly unnecessary preconditions and vacuous proofs. With unsat-core minimization, ProofPulse achieves perfect precision for precondition classification and reduces false positives across all evaluated categories. These results show that proof coverage is a practical complement to verification. Although it cannot fully capture semantic intent, it can reveal weak proof coupling in programs that otherwise appear fully verified.
  Just as a pulse check distinguishes vitality from the mere absence of symptoms, ProofPulse exposes weaknesses in proofs that technically verify successfully but still suffer from inadequate or redundant code and specifications.
