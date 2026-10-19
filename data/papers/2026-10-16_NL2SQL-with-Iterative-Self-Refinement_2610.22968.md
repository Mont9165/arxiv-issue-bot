# NL2SQL with Iterative Self-Refinement

- arXiv ID: `2610.22968v1`
- Authors: Anjali Vemula, Akshat Dasula
- Published: 2026-10-16
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.22968v1) | [pdf](https://arxiv.org/pdf/2610.22968v1)

## Abstract

Bridging the gap between human intent and machine logic remains a critical challenge in data access for non-technical users, yet Large Language Models (LLMs) remain unreliable: they hallucinate schema elements, generate syntactically invalid queries, or fail to capture user intent. These limitations are especially critical in domains such as insurance, where KPIs, regulatory constraints, and legacy relational systems demand high precision. We introduce a multi-agent, persona-driven NL2SQL framework that combines (1) domain relevance detection, (2) schema-grounded knowledge construction, (3) KPI-aware SQL synthesis, (4) syntax-level self-repair using sqlite execution feedback, and (5) semantic consistency checking via SQL-to-NL reverse engineering. Our system significantly reduces query hallucination and improves semantic fidelity compared to direct LLM prompting. Evaluated on 60 queries (50 from a HuggingFace text-to-SQL dataset and 10 custom domain queries), the system achieves 90% correctness using Mistral across seven coordinated LLM calls showing that this approach can substantially increase the reliability of NL2SQL pipelines in high-stakes environments.
