# AGDecode: Semantic Attribute Grammar Derivatives for Safety-Constrained Decoding of Large Language Models

- arXiv ID: `2610.36105v1`
- Authors: Rajan Maghera, Asher Tempest Arya, Aren A. Babikian, Marsha Chechik, Maryam Mehri Dehnavi
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.36105v1) | [pdf](https://arxiv.org/pdf/2610.36105v1)

## Abstract

Large language models (LLMs) are increasingly used for code generation, motivating techniques that guarantee the structural and semantic correctness of generated programs. Constrained decoding enforces correctness during generation by restricting token choices to those that admit at least one valid completion. While existing approaches can enforce syntactic constraints and selected semantic properties such as type safety, they either target specific properties or rely on operational pruning mechanisms that are difficult to generalize to data-dependent, inductive program properties. We present AGDecode, a programmable framework for semantic constrained decoding based on least-fixed-point semantics. AGDecode extends attribute grammars to partially constructed syntax trees, and reduces semantic constrained decoding to a realizability problem over such trees. The framework compiles semantic specifications into systems of relational constraints that are discharged by external verification oracles, such as SMT and CHC solvers, cleanly separating language semantics from constraint-solving machinery. We prove that our approach is sound and complete relative to an ideal verification oracle. In practice, solvers inevitably encounter uncertain queries; conservatively, our system can reject tokens for soundness or speculatively continue to generate until later queries resolve the entire generation. We mechanize the core metatheory in Rocq and evaluate the framework on semantic-constrained generation of C programs, enforcing path-sensitive safety properties including null-pointer safety, division-by-zero freedom, and initialized-variable usage. Our results demonstrate that solver-backed semantic constrained decoding can enforce rich semantic guarantees while incurring modest computational overhead at regular program boundaries.
