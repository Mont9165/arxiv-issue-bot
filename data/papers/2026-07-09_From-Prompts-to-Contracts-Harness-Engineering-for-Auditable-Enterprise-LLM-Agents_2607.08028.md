# From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents

- arXiv ID: `2607.08028v1`
- Authors: Joongho Ahn, Moonsoo Kim
- Published: 2026-07-09
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.08028v1) | [pdf](https://arxiv.org/pdf/2607.08028v1)

## Abstract

Enterprise large language model (LLM) applications often begin as prototypes whose behavior is carried by prompts and retrieval context. Productization adds requirements for source boundaries, entity routing, answer contracts, and reproducible traces. We present a harness-engineering approach that reconstructs this pattern into a traceable, auditable LLM-agent architecture: deterministic behavior moves into code, manifests, schemas, and validation artifacts around a replaceable composition boundary, while source-backed claims remain the authority for runtime answers. We instantiate it on a public-data slice of five Korean corporate groups (25 listed companies) and evaluate three research questions. (1) The harness preserves its source-grounding, entity-routing, trace, output-hygiene, and recommendation-language contracts across the fixed validation scenarios; a fault-injection control confirms the validators flag deliberately broken contracts. (2) The checks the harness enforces held under model substitution: across three hosted models, they passed on all 270 composition-boundary runs; failures were confined to the model-composed side and were caught and recorded. (3) The code-owned guarantees are load-bearing, not reproducible by prompting alone: holding the model fixed and varying only the enforcement layer, prompt instructions alone let recommendation-language and internal-trace-leakage violations reach the reader, which the harness blocks entirely. A bolt-on external guardrail prevents such violations too but over-refuses, dropping utility to 88/120 where the harness preserves full utility (120/120); in this ablation, only code-owned enforcement preserves both safety and utility. The result is a reusable engineering pattern for turning exploratory prototypes into auditable applications with versioned source, control, and validation artifacts.
