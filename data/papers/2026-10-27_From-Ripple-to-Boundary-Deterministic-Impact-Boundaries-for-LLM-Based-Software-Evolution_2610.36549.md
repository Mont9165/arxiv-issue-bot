# From Ripple to Boundary: Deterministic Impact Boundaries for LLM-Based Software Evolution

- arXiv ID: `2610.36549v1`
- Authors: Jiameng Bai, Zhitao Wang, Long Wang, Keyue Qian, Sai Wu
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.36549v1) | [pdf](https://arxiv.org/pdf/2610.36549v1)

## Abstract

The landscape of software evolution is undergoing a fundamental paradigm shift in the era of Large Language Models. As industrial software engineering increasingly transitions toward design-driven code generation, the bottleneck of evolution has shifted from writing code to maintaining deterministic consistency between multi-source design assets and the generated code. When a design asset changes, LLM agents currently lack a deterministic impact boundary to identify which code must be evolved, leading to two failure modes: hallucinating missing changes or breaking unrelated code. Probabilistic approaches, such as semantic retrieval or text-based diffing, fail to capture the structural ripple effects across highly interconnected design dependencies. We propose a paradigm shift from probabilistic semantic retrieval to deterministic structural constraints. We formalize the design assets as a Knowledge Graph and organize them into a content-addressed Merkle Directed Acyclic Graph. Our key insight reveals a topological isomorphism between the logical ripple effect of a design change and the content hash propagation within the DAG. By leveraging this, we transform ambiguous impact analysis into verifiable structural operations. Through a two-phase diffing process, we extract a precise causal chain that defines the exact modification boundary. This boundary enables deterministic context injection, providing the LLM agent with strictly scoped code and design updates, thereby fundamentally guaranteeing evolution safety. As a by-product, the KG serves as an agent-queryable knowledge base for natural language design retrieval. Early deployment on a large-scale industrial payment platform demonstrates that our mechanism successfully computes the exact impact boundary and generates incremental code modifications that meet the expected design changes.
