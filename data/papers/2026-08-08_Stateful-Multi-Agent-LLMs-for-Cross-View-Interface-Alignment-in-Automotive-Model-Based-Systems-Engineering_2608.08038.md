# Stateful Multi-Agent LLMs for Cross-View Interface Alignment in Automotive Model-Based Systems Engineering

- arXiv ID: `2608.08038v1`
- Authors: Aleksei Velsh, Nenad Petrovic, Alois Knoll
- Published: 2026-08-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.08038v1) | [pdf](https://arxiv.org/pdf/2608.08038v1)

## Abstract

While Large Language Models (LLMs) can accelerate Model-Based Systems Engineering (MBSE) for software-defined vehicles, their probabilistic nature causes "architectural drift", fabricating interfaces in behavioral views that lack structural foundations. To enforce deterministic interface alignment, we propose a stateful, multi-agent validation pipeline. The framework utilizes a sequential generation matrix (Class->Activity->Sequence) and Vehicle Signal Specification (VSS)-grounded Retrieval-Augmented Generation (RAG). An independent AI Validator Agent dynamically audits outputs against a strict error taxonomy, triggering state-preserving backtracking loops to resolve incompatibilities. Evaluated on an Advanced Driver Assistance System (ADAS) scenario, standard RAG yielded 0% Entity Traceability. Conversely, our multi-agent workflow eradicated cross-phase hallucinations, achieving 97% Entity Traceability, 87% Signal Conservation, and an 85% F1-score. This proves adversarial auditing enables LLMs to reliably synthesize zero-error MBSE architectures.
