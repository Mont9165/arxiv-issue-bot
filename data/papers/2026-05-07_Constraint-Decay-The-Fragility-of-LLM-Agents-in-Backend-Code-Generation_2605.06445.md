# Constraint Decay: The Fragility of LLM Agents in Backend Code Generation

- arXiv ID: `2605.06445v1`
- Authors: Francesco Dente, Dario Satriani, Paolo Papotti
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.06445v1) | [pdf](https://arxiv.org/pdf/2605.06445v1)

## Abstract

Large Language Model (LLM) agents demonstrate strong performance in autonomous code generation under loose specifications. However, production-grade software requires strict adherence to structural constraints, such as architectural patterns, databases, and object-relational mappings. Existing benchmarks often overlook these non-functional requirements, rewarding functionally correct but structurally arbitrary solutions. We present a systematic study evaluating how well agents handle structural constraints in multi-file backend generation. By fixing a unified API contract across 80 greenfield generation tasks and 20 feature-implementation tasks spanning eight web frameworks, we isolate the effect of structural complexity using a dual evaluation with end-to-end behavioral tests and static verifiers. Our findings reveal a phenomenon of constraint decay: as structural requirements accumulate, agent performance exhibits a substantial decline. Capable configurations lose 30 points on average in assertion pass rates from baseline to fully specified tasks, while some weaker configurations approach zero. Framework sensitivity analysis exposes significant performance disparities: agents succeed in minimal, explicit frameworks (e.g., Flask) but perform substantially worse on average in convention-heavy environments (e.g., FastAPI, Django). Finally, error analysis identifies data-layer defects (e.g., incorrect query composition and ORM runtime violations) as the leading root causes. This work highlights that jointly satisfying functional and structural requirements remains a key open challenge for coding agents.
