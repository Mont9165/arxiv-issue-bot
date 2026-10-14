# Specification-Guided Synthesis of Deadlock-Free Communication Protocol Refinements with Large Language Models

- arXiv ID: `2607.27964v1`
- Authors: Yang Li, Ping Hou, Nobuko Yoshida
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.27964v1) | [pdf](https://arxiv.org/pdf/2607.27964v1)

## Abstract

Ensuring behavioural correctness in communication protocols is a central challenge in distributed software systems, as subtle inconsistencies can lead to deadlocks. In such settings, protocol refinement - the safe substitution of a protocol that preserves correctness and compatibility with other components - is essential. Large language models (LLMs) have demonstrated strong capabilities in code generation and program synthesis, yet lack mechanisms to reliably produce outputs with correct behaviour. Formal specification approaches, such as multiparty session types (MPST), offer rigorous guarantees, including deadlock freedom, but provide limited support for automatically constructing protocol refinements. In this paper, we present Syntropy, a framework for synthesising protocol refinements guided by MPST specifications and LLMs. It incorporates refinement constraints directly into the generation process, ensuring the generated variants satisfy these guarantees. Our comprehensive evaluation indicates that Syntropy achieves 95.6%-99.5% validity while maintaining high syntactic correctness, and produces diverse, non-trivial refinements across multiple LLMs.
