# TDD Governance for Multi-Agent Code Generation via Prompt Engineering

- arXiv ID: `2604.26615v1`
- Authors: Tarlan Hasanli, Shahbaz Siddeeq, Bishwash Khanal, Pyry Kotilainen, Tommi Mikkonen, Pekka Abrahamsson
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.26615v1) | [pdf](https://arxiv.org/pdf/2604.26615v1)

## Abstract

Large language models (LLMs) accelerate software development but often exhibit instability, non-determinism, and weak adherence to development discipline in unconstrained workflows. While test-driven development (TDD) provides a structured Red-Green-Refactor process, existing LLM-based approaches typically use tests as auxiliary inputs rather than enforceable process constraints. We present an AI-native TDD framework that operationalizes classical TDD principles as structured prompt-level and workflow-level governance mechanisms. Extracted principles are formalized in a machine-readable manifesto and distributed across planning, generation, repair, and validation stages within a layered architecture that separates model proposal from deterministic engine authority. The system enforces phase ordering, bounded repair loops, validation gates, and atomic mutation control to improve stability and reproducibility. We describe architecture and discuss encoding software engineering discipline directly into prompt orchestration, which we think offers a promising direction for reliable LLM-assisted development.
