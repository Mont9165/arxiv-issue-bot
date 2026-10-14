# Credo: Reusable Declarative Primitives for Agentic Workflows

- arXiv ID: `2608.27790v1`
- Authors: Duo Lu, Andrew Crotty, Uğur Çetintemel
- Published: 2026-08-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.27790v1) | [pdf](https://arxiv.org/pdf/2608.27790v1)

## Abstract

An LLM application depends on both a model and a harness: the program that determines what each call sees, how many calls to make, and which answers to trust. Coding agents can now discover strong harnesses by searching over candidate programs, but the resulting artifact is an opaque block of imperative code whose logical steps, runtime signals, physical execution decisions, and prompt strategies remain implicit and task-specific, forcing subsequent tasks to start the harness search process from scratch. The potential for reuse, however, is substantial. A searched harness encodes significant knowledge, such as the logical steps that work, the signals that matter, the physical operator decisions that adapt execution, and the prompt strategies that are effective, yet this knowledge is buried in imperative code with no inspectable or reusable structure, nor does it carry any provenance or metadata. Credo addresses this problem by recovering a structured declarative description of a searched harness, tagging each extracted primitive with relevant metadata, and cataloguing all of it with provenance. A compiler can then bind stored primitives to generate harnesses for new tasks without having to start the search over from scratch. This paper provides preliminary results demonstrating the potential of our approach and lays out a related research agenda that the database community is well-positioned to tackle, including cost-based compilation over declarative catalogs and catalog maintenance under model and workload drift.
