# Modern Software Engineering with Verification Agents: A Spec-First Architecture for Autonomous Synthesis, Verification IRs, and Organizational Scale

- arXiv ID: `2611.02285v1`
- Authors: Jason Hickey
- Published: 2026-11-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2611.02285v1) | [pdf](https://arxiv.org/pdf/2611.02285v1)

## Abstract

When autonomous coding agents synthesize implementation code, formal specifications, and mechanical proofs simultaneously, the software engineering hierarchy inverts: the formal specification becomes the primary human-reviewed artifact, while source code and proof scripts become disposable build outputs. This paper presents an end-to-end architecture for agent-authored, formally verified software engineering. First, we establish a logic-agnostic foundation combining a spec-first stack inversion, a zero-code-review workflow gated by automated continuous integration (CI) checks, and a minimal Verification Intermediate Representation (VIR) lowered via a thin, verified translator. Second, we pair an extensional Computational Type Theory (CTT) specification layer with Higher-Order Abstract Syntax (HOAS) and linear resource typing in the VIR--eliminating rewrite friction for synthesis agents while defining an experiment, its protocol frozen before the first reader, to measure whether removing boundary coercions improves human specification readability. Third, we scale collaboration across multi-team organizations using Personal Spec-Copilots and a Shared Synthesis Fleet that detects cross-team Semantic Merge Conflicts and fuses modular contracts into zero-copy binaries. We illustrate this architecture on a zero-copy authenticated message router and distinguish our existing empirical baselines (salt, SaltBench, x86lean, and MetaPRL) from newly proposed components.
