# SAGE: Structured Agentic Graph Editing for Software Diagrams

- arXiv ID: `2607.01102v1`
- Authors: Tyler Sivertsen, Neal Singh, James C. Davis
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01102v1) | [pdf](https://arxiv.org/pdf/2607.01102v1)

## Abstract

Software diagrams are difficult to edit through human-friendly interfaces because edits expressed in natural language must still preserve visual layout, editable structure, and semantic relationships. As a step forward, we present SAGE, a browser-based tool for prompt-guided editing of Draw.io and Mermaid-style engineering diagrams. The tool maps diagrams into an editable graph representation, translates natural language requests into structured edit intents, analyzes those intents into graph-oriented operation steps, validates and repairs common Draw.io XML issues, and stores successful results as recoverable versioned artifacts. This design separates structured state management from model-driven interpretation, while acknowledging that some prompt-guided XML edits remain model-assisted. The tool also supports direct canvas editing and a secondary mask-based image-editing workflow. We evaluate the system using unit tests and a Kubernetes architecture case study, measuring structural validity, edit success, preservation of unrelated elements, and failure causes.
