# Validating Multi-Model AI-Generated Acceptance Criteria in Requirements Engineering

- arXiv ID: `2611.32374v1`
- Authors: Mateen Ahmed Abbasi, Petri Ihantola, Tommi Mikkonen, Niko Mäkitalo
- Published: 2026-11-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.32374v1) | [pdf](https://arxiv.org/pdf/2611.32374v1)

## Abstract

Large language models (LLMs) are increasingly used in software engineering to generate artifacts such as requirements, user stories, acceptance criteria, documentation, and code. Their use in requirements engineering raises important questions about correctness, traceability, and hallucination, especially because flawed specifications can affect later design, implementation, and verification activities. While much recent work on AI-assisted software engineering has focused on code generation and code-level validation, the validation of AI-generated specifications has received less attention. This paper addresses this gap by presenting a validation-oriented approach for AI-generated acceptance criteria. The approach combines retrieval-augmented generation (RAG), multi-model generation, and an explicitly structured human-in-the-loop workflow. We describe a working prototype that allows users to prepare or enter user stories, generate acceptance criteria using several LLMs, optionally augment generation with retrieved requirements-related examples, compare outputs side by side, inspect retrieved context, and select, edit, or regenerate candidate criteria before explicitly submitting a reviewer-finalized version. The system also records model outputs, user interventions, retrieval settings, and final criteria as part of a logged decision process. Rather than claiming that generation accuracy is already improved, the contribution of this work is to operationalize validation as an explicit, inspectable, and accountable process for AI-generated requirements artifacts.
