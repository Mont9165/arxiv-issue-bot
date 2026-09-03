# Towards Behavior Tree-Guided Vulnerability Detection with Lightweight LLMs

- arXiv ID: `2609.01758v1`
- Authors: Enna Basic, Alberto Giaretta
- Published: 2026-09-01
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.01758v1) | [pdf](https://arxiv.org/pdf/2609.01758v1)

## Abstract

Large Language Models (LLMs) are increasingly used for software vulnerability detection, but their performance depends on how source code is represented in the input. Most prompting approaches use source code in its original form, while some works propose the use of structured representations. Abstract Syntax Trees (ASTs) are one of the most popular approaches, but AST verbosity increases input size relative to source code, making them hard to fit within some LLMs context windows. This paper investigates Behavior Trees (BTs) as an alternative intermediate representation for LLM-based vulnerability detection. BTs encode control flow, conditions, and executable actions more compactly than ASTs, making them a natural candidate when token count is a constraint. First, we propose a preprocessing stage that parses Java source code into ASTs and then converts them into BT representations. We then compare vulnerability detection performance across 460 Java samples from the Juliet Java test suite, using three input representations: raw source code, AST, and BT. All experiments use a single quantized local LLM, Mistral Small 3.2 24B (Q4_K_M). Our results show that using BT representations improves recall on short code samples, while raw source code achieves higher precision. On longer samples, BTs improve overall performance over the original representation and fit within the context window, whereas many ASTs exceed the context limit. These findings suggest that BTs can provide a compact and useful structured representation for vulnerability detection with quantized, locally deployable LLMs.
