# Metamodel-Guided LLM Decoding for Consistent DSL Generation

- arXiv ID: `2610.29749v1`
- Authors: Boqi Chen, Aren A. Babikian, José Antonio Hernández López
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.29749v1) | [pdf](https://arxiv.org/pdf/2610.29749v1)

## Abstract

Large language models (LLMs) are increasingly used to generate software engineering artifacts written in domain-specific languages (DSLs). Correct DSL instances usually must comply with not only the concrete syntax but also the abstract syntax defined by a metamodel augmented with semantic well-formedness constraints. Existing constrained decoding approaches typically guarantee compliance only with concrete syntax or with a limited set of semantic constraints expressed over the generated text, making metamodel-level constraint consistency difficult to enforce during generation. We present MeMoDecode: a decoding framework that enforces a DSL's concrete syntax, abstract syntax, and well-formedness constraints jointly. Specifically, whenever the LLM generates a complete metamodel concept, MeMoDecode incrementally maps the current output to a partial model and verifies whether it can still be completed into a consistent instance. We combine MeMoDecode with a simple retry mechanism that resumes decoding from the most recent completable snapshot whenever an inconsistency is detected. Under a sound backend verifier, MeMoDecode never performs worse than grammar-constrained decoding on alignment metrics satisfying natural assumptions. Across four DSLs and six open-weight LLMs ranging from 0.6B to 70B parameters, MeMoDecode achieves the highest consistency, improving consistency by 23% on average over unconstrained decoding and by 8% on average over grammar-constrained decoding. It also improves benchmark performance while incurring only modest runtime overhead. These results show that metamodel-guided decoding is an effective approach for enforcing DSL consistency during decoding across diverse DSLs and LLM scales.
