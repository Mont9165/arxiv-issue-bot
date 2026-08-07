# Projectional Decoding: Towards Semantic-Aware LLM Generation

- arXiv ID: `2605.30054v1`
- Authors: Boqi Chen, José Antonio Hernández López, Aren A. Babikian
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.30054v1) | [pdf](https://arxiv.org/pdf/2605.30054v1)

## Abstract

Large language models (LLMs) are increasingly used to generate software artifacts across many software engineering (SE) tasks, yet ensuring the semantic validity of these artifacts remains a fundamental challenge. Existing constrained decoding techniques can enforce syntactic correctness and, in some cases, specific semantic rules, but lack a general representation that bridges LLM-generated text with the reasoning required for semantic validation in SE. In this paper, we propose projectional decoding, a novel conceptual framework that integrates domain semantics directly into the generation process by maintaining, alongside text, a partial graph model as the primary artifact representation throughout generation. This abstract representation enables incremental semantic validation by explicitly capturing uncertainty and natively supporting error detection, while guiding generation toward semantically valid outputs with provable guarantees. We present preliminary results on a program generation task which demonstrate the potential of this approach to improve the semantic validity of LLM-generated artifacts. We also discuss how projectional decoding can enable verifiable automation with LLMs across various SE activities.
