# Architecting Fairness-Aware LLM Interactions

- arXiv ID: `2611.00723v1`
- Authors: Alessandra Parziale, Valeria Pontillo, Fabio Palomba, Patrizio Pelliccione
- Published: 2026-10-31
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CY`
- Links: [abs](http://arxiv.org/abs/2611.00723v1) | [pdf](https://arxiv.org/pdf/2611.00723v1)

## Abstract

Large Language Models (LLMs) are increasingly used as decision-support tools but may generate stereotypical, discriminatory, or unfair responses. As LLMs become embedded in decision-critical software systems, fairness can no longer be treated as a downstream evaluation step, but must become an architectural concern of the interaction itself. Yet current fairness approaches operate as standalone evaluation techniques, lacking a reusable mechanism to verify and mitigate violations at runtime. We propose a fairness-assurance architecture grounded in three reusable design patterns, instantiated as a multi-agent framework that evaluates and iteratively refines LLM responses before delivery. A preliminary evaluation across eight configurations involving different LLM families shows that the architecture identifies fairness violations and iteratively produces compliant responses in all configurations, with behavior differing depending on the model-family composition. These results provide initial evidence for the joint instantiation of the proposed patterns and a first step toward architecting non-functional properties into LLM-based systems.
