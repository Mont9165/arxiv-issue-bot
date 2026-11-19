# Validating Concurrent Correctness Witnesses with Ghosts by Thread-Modular Abstract Interpretation

- arXiv ID: `2611.23792v1`
- Authors: Michael Schwarz, Zhendong Ang, Umang Mathur
- Published: 2026-11-18
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.23792v1) | [pdf](https://arxiv.org/pdf/2611.23792v1)

## Abstract

Concurrent programs are notoriously difficult to write and to reason about, and even tools based on sound theoretical foundations can produce incorrect results due to implementation bugs. Correctness witnesses have been proposed as a way to increase the confidence in the verdicts of software verifiers by enabling independent validation. Recently, correctness witnesses have been extended to the concurrent setting, by introducing ghost variables to allow encoding more expressive invariants. While different approaches to producing witnesses with ghosts exist, validation techniques are still lacking; instead of leveraging the information encoded in the ghosts to guide the validation process, validators merely treat ghost instrumentation and invariants over ghost variables as additional proof obligations. We propose a novel framework for the validation of concurrent correctness witnesses that exploits the semantic information encoded in ghost variables. It combines a checking phase, which establishes the semantic content of the ghost instrumentation, with an exploitation phase making use of this information. Both phases are formulated as thread-modular abstract interpretation. In particular, we consider two different classes of ghost variables and techniques for exploiting them, one based on resource invariants and one based on phases. Phase ghosts guide the degree to which the abstract interpretation considers interleavings instead of always abstracting them coarsely. In this way, the abstract interpreter can validate witnesses containing invariants beyond the reach of unguided thread-modular analysis, while still retaining its scalability benefits. We have implemented our framework in a static analyzer and evaluate it on witnesses encoding resource invariants obtained from a state-of-the-art software verifier, as well as on hand-crafted witnesses encoding phase information.
