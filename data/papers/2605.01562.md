# Neuro-Symbolic Agents for Hallucination-Free Requirements Reuse

- arXiv ID: `2605.01562v1`
- Authors: Ahmed Ibrahim
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.01562v1) | [pdf](https://arxiv.org/pdf/2605.01562v1)

## Abstract

The Object-Oriented Method for Requirements Authoring and Management (OOMRAM) is a requirements reuse framework that relies on exact identifier matching and rigid templates, limiting its ability to adapt specifications across diverse contexts. While Large Language Models (LLMs) offer the flexibility to overcome this bottleneck, they introduce the risk of generating structurally invalid or inconsistent requirement combinations. To address this tension, we present a neuro-symbolic multi-agent system that re-conceptualizes requirements reuse as a \textbf{Model-Driven Elicitation process}. In this paradigm, an LLM serves as a \textbf{non-deterministic heuristic} for traversing a \textbf{deterministic domain model} represented by a formal OOMRAM requirement lattice. A deterministic, symbolic validator enforces all structural constraints within the agent loop, effectively eliminating hallucinated requirement combinations by construction. Evaluated on an autonomous benchmark across two application families, our system achieves 100\% requirement coverage and a constraint-violation rate of only 0.2\%. Although the F1-score against a single gold standard is moderate (0.47--0.51), every generated specification is structurally valid and satisfies all mandatory domain requirements. The model-agnostic implementation scales to larger lattices via subgraph navigation and provides transparent audit trails for regulatory compliance.
