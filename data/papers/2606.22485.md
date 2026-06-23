# VADAOrchestra: Neurosymbolic Orchestration of Adaptive Reasoning Workflows

- arXiv ID: `2606.22485v1`
- Authors: Teodoro Baldazzi, Luigi Bellomarini, Andrea Coletta, Michela Iezzi, Carsten Maple, Alessandro Pesare, Emanuel Sallinger
- Published: 2026-06-21
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2606.22485v1) | [pdf](https://arxiv.org/pdf/2606.22485v1)

## Abstract

Decision-making in real-world settings rarely follows a fixed script. Instead, it unfolds as a dynamic reasoning process in which the appropriate course of action evolves as new context and data become available. Traditional Business Process Management systems provide rigor, determinism, and auditability, yet they generally struggle to adapt their execution at runtime. Conversely, agentic systems based on Large Language Models (LLMs) bring flexibility to decision-making, but they are inherently opaque, often unreliable, and suffer from significant scalability constraints when operating over large datasets. To combine these complementary paradigms, we introduce VADAOrchestra, a neurosymbolic framework that models complex workflows as evolving reasoning processes. The framework adopts a hybrid approach: given a user query and a collection of data sources, an LLM-based orchestrator incrementally plans and adapts the workflow. This is encoded as a logic program in a fragment of Datalog+/- where predicates correspond to tool invocations and rules represent both predefined domain dependencies and logic constructs synthesized on demand to manipulate intermediate results. All logical inference tasks are then executed by a state-of-the-art Datalog+/- symbolic engine. This approach provides a verifiable reasoning trace, supporting the auditability and reproducibility of the entire process. Furthermore, by decoupling high-level orchestration from symbolic inference, it addresses scalability concerns, enabling complex reasoning over large datasets through targeted data querying. We evaluate VADAOrchestra on real-world financial use cases, demonstrating faithfulness, scalability, and explainability compared to standard agentic architectures.
