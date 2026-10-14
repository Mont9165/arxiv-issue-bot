# Credo: Declarative Control of LLM Pipelines via Beliefs and Policies

- arXiv ID: `2604.14401v1`
- Authors: Duo Lu, Andrew Crotty, Uğur Çetintemel
- Published: 2026-04-15
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.14401v1) | [pdf](https://arxiv.org/pdf/2604.14401v1)

## Abstract

Agentic AI systems are becoming commonplace in domains that require long-lived, stateful decision-making in continuously evolving conditions. As such, correctness depends not only on the output of individual model calls, but also on how to best adapt when incorporating new evidence or revising prior conclusions. However, existing frameworks rely on imperative control loops, ephemeral memory, and prompt-embedded logic, making agent behavior opaque, brittle, and difficult to verify. This paper introduces Credo, which represents semantic state as beliefs and regulates behavior using declarative policies defined over these beliefs. This design supports adaptive, auditable, and composable execution through a database-backed semantic control plane. We showcase these concepts in a decision-control scenario, where beliefs and policies declaratively guide critical execution choices (e.g., model selection, retrieval, corrective re-execution), enabling dynamic behavior without requiring any changes to the underlying pipeline code.
