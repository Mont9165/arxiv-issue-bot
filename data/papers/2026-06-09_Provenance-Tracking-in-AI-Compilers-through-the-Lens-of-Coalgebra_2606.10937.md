# Provenance Tracking in AI Compilers through the Lens of Coalgebra

- arXiv ID: `2606.10937v1`
- Authors: Zilu Tian, Liying Liu
- Published: 2026-06-09
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.10937v1) | [pdf](https://arxiv.org/pdf/2606.10937v1)

## Abstract

AI compilers aggressively rewrite computation graphs through normalization, lowering, and optimization, making it difficult to track the provenance of tensors and operators across compilation. Reliable provenance is essential for attaching platform-specific postprocessing, debugging compiler behavior, and validating transformations, yet existing solutions are either invasive or ad hoc under non-injective graph rewrites.
  We present a lightweight, generative approach to provenance tracking based on observational semantics. Instead of propagating identifiers through compiler passes, we observe graph transformations and reason about provenance in terms of observable computational actions. We formalize this approach using a coalgebraic model and bisimulation, which preserves provenance even when intermediate nodes are eliminated. Furthermore, we implement this approach in a prototype AI compiler COVAN, demonstrating stable provenance across compilation pipelines with minimal engineering overhead.
