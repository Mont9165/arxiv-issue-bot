# Beyond Source Code: Evaluating Natural Language Specifications for LLM-Based C-to-Rust Translation

- arXiv ID: `2611.17581v1`
- Authors: Biruk Tadesse, Lawrence Arkoh, Marcelo D'Amorim, Wesley K. G. Assunção
- Published: 2026-11-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.17581v1) | [pdf](https://arxiv.org/pdf/2611.17581v1)

## Abstract

Large language models (LLMs) have shown promising results for C-to-Rust translation, yet existing approaches primarily rely on source code as input, leaving natural-language specifications of program behavior underexplored as an alternative or complementary representation. We hypothesize that direct code translation encourages LLMs to preserve C-specific implementation choices, producing Rust that may be functionally correct but unnecessarily verbose, reliant on unsafe constructs, and less idiomatic. We investigate this hypothesis by comparing three translation settings: code-only, specification-only, and code-and-specification. Using 300 C programs from the IBM CodeNet dataset, we evaluate GPT-5.2 and GPT-4o-mini on functional correctness, maintainability, complexity, idiomaticity, unsafe construct usage, and cost. Code-only translation achieves the highest test pass rate (98.6%) but often mirrors C's implementation patterns. In contrast, specification-only translation produces the most idiomatic and compact Rust, reducing unsafe blocks by approximately 6x and Clippy style warnings by 2.4x. However, using specifications without validation yields test pass rates as low as 86% with our best performing model. Adding an iterative test-based validation and refinement step for specifications raises this to a 95.3% test pass rate. Overall, specification-based translation consistently improves code quality relative to code-only translation, while code-and-specification offers the best balance between correctness (98.3% test pass rate) and maintainability. Our study systematically compares these translation settings, highlighting the trade-offs among specification quality, translation correctness, code quality, and computational cost.
