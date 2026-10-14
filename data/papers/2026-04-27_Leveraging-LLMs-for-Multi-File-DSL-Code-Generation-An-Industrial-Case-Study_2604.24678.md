# Leveraging LLMs for Multi-File DSL Code Generation: An Industrial Case Study

- arXiv ID: `2604.24678v1`
- Authors: Sivajeet Chand, Kevin Nguyen, Peter Kuntz, Alexander Pretschner
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.24678v1) | [pdf](https://arxiv.org/pdf/2604.24678v1)

## Abstract

Large language models (LLMs) perform strongly on general-purpose code generation, yet their applicability to enterprise domain-specific languages (DSLs) remains underexplored, especially for repository-scale change generation spanning multiple files and folder structures from a single natural-language (NL) instruction. We report an industrial case study at BMW that adapts code-oriented LLMs to generate and modify project-root DSL artifacts for an Xtext-based DSL that drives downstream Java/TypeScript code generation. We develop an end-to-end pipeline for dataset construction, multi-file task representation, model adaptation, and evaluation. We encode DSL folder hierarchies as structured, path-preserving JSON, allowing single-response generation at repository scale and learning cross-file dependencies. We evaluate two instruction-tuned code LLMs (Qwen2.5-Coder and DeepSeek-Coder, 7B) under three configurations: baseline prompting, one-shot in-context learning, and parameter-efficient fine-tuning (QLoRA). Beyond standard similarity metrics, we introduce task-specific measures that assess edit correctness and repository structural fidelity. Fine-tuning yields the most significant gains across models and metrics, achieving high exact-match accuracy, substantial edit similarity, and structural fidelity of 1.00 on our held-out set for multi-file outputs. At the same time, one-shot in-context learning provides smaller but consistent improvements over baseline prompting. We further validate practical utility via an expert developer survey and an execution-based check using the existing code generator.
