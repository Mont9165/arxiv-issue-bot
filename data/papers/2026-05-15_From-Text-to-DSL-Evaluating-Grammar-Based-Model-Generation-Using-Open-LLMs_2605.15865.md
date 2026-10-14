# From Text to DSL: Evaluating Grammar-Based Model Generation Using Open LLMs

- arXiv ID: `2605.15865v1`
- Authors: Junaid Baber, Nicolas Hili, Didier Schwab, Léo Challier, Cécilia Satrin
- Published: 2026-05-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15865v1) | [pdf](https://arxiv.org/pdf/2605.15865v1)

## Abstract

Large Language Models (LLMs) have shown increasing potential in automating model-driven software engineering tasks, particularly in generating models conforming to Domain Specific Languages (DSLs) from natural language. While most existing approaches rely on large proprietary models, their high cost and limited deployability hinder broader adoption.
  In this paper, we evaluate whether open-source LLMs of varying sizes (0.5B to 32B parameters) can generate DSL-conformant models using only few-shot prompting, without any fine-tuning. Our evaluation focuses on key model-driven engineering (MDE) requirements, including syntactic validity, semantic completeness, and inter-model reference consistency.
  We extend our prior work by moving from generating user interface models (referred to as "UI models" in this paper) over fixed, predefined data schemas ("data models") to generating both the UI and data models entirely from scratch. This shift serves two purposes: first, it highlights the LLM's ability to infer domain-specific relationships and maintain consistency across multiple interconnected models; second, it allows us to generalize earlier findings by testing DSL generation across models of different natures and structural roles. Our structured evaluation combines automatic parsing and expert feedback across 39 LLMs, revealing that several compact models (e.g., \texttt{gemma3:12b}, \texttt{mistral:7b-instruct}) approach or match the quality of much larger models.
  These findings demonstrate the feasibility of using smaller, open-source LLMs for grammar-conformant DSL generation in MDE workflows, offering a cost-effective and deployable alternative to closed LLMs.
