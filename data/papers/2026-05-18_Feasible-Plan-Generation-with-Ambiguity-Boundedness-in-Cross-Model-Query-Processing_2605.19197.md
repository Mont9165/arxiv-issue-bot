# Feasible Plan Generation with Ambiguity-Boundedness in Cross-Model Query Processing

- arXiv ID: `2605.19197v1`
- Authors: Subhasis Dasgupta, Amarnath Gupta
- Published: 2026-05-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.19197v1) | [pdf](https://arxiv.org/pdf/2605.19197v1)

## Abstract

Natural language (NL) interfaces to databases broaden access to heterogeneous data but often yield many ambiguous intermediate logical plans (ILPs) due to uncertain operator scope and predicate semantics. Many candidates are infeasible because of type mismatches, missing bindings, or engine-specific constraints. We address this challenge with \emph{feasibility constraints} for detecting local inconsistencies and introduce the Packed Plan Forest (PPF) a polynomially bounded structure that compactly encodes all feasible ILPs while pruning infeasible ones early. Extending packed parse forest ideas to multi-model settings, PPF supports efficient feasibility analysis through annotated operators. Formal results show polynomial size under bounded arity and annotation vocabularies, and experiments confirm that PPFs capture exponentially many ILPs with minimal overhead, establishing a scalable foundation for NL-to-DB query planning across heterogeneous systems
