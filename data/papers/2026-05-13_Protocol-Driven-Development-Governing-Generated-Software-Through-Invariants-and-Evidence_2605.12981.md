# Protocol-Driven Development: Governing Generated Software Through Invariants and Evidence

- arXiv ID: `2605.12981v1`
- Authors: Jun He, Deying Yu
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.12981v1) | [pdf](https://arxiv.org/pdf/2605.12981v1)

## Abstract

Automated program synthesis has reduced the cost of producing candidate implementations, but it introduces a harder governance problem: determining which generated artifacts are admissible in a software system. Natural-language specifications remain semantically ambiguous, and example-based tests sample only part of the behavioral space. Used alone, neither provides a sufficient control boundary for automated software construction. We introduce Protocol-Driven Development (PDD), a development model in which the primary software artifact is a machine-enforceable protocol rather than implementation code. We define a protocol as the triplet P = (S, B, O), where S specifies structural invariants, B specifies behavioral invariants, and O specifies operational invariants. Their conjunction defines the admissible implementation space of a software component. Under PDD, implementations are treated as replaceable realizations discovered through constrained search. An implementation is admitted if and only if it satisfies the governing protocol and produces a verifiable Evidence Chain of compliance. Admission is therefore grounded not in trust in the generator, but in protocol satisfaction and recorded evidence. By combining ideas from formal methods, property-based testing, policy-as-code, and software provenance, PDD defines a governance layer for automated software engineering. Its organizing principle is simple: code is transient; protocol is sovereign.
