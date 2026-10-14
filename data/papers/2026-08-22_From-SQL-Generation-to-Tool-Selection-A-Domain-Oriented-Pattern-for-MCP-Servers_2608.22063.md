# From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers

- arXiv ID: `2608.22063v1`
- Authors: Bartolomeo Bogliolo
- Published: 2026-08-22
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.22063v1) | [pdf](https://arxiv.org/pdf/2608.22063v1)

## Abstract

Agents built on Large Language Models (LLMs) increasingly reach enterprise data through the Model Context Protocol (MCP), and many MCP database servers maximize flexibility by exposing a single generic SQL execution tool. This paper proposes the Domain-Oriented Tooling Pattern: instead of generating SQL at query time, the model selects from a small set of domain-aligned tools whose parameterized queries encapsulate schema navigation, joins and business rules on the server side. We formalize the pattern around three architectural invariants and introduce Model Demotion, the observation that replacing SQL synthesis with intent classification lowers the model tier required to serve routine requests. As a reference implementation we present MCP Blueprint, an open-source framework in which domain tools are defined declaratively as YAML metadata plus external parameterized SQL files. We evaluate the pattern with a public reproducibility benchmark comparing three MCP server designs - raw SQL execution, a thin generic tool pack, and a verticalized domain pack - on four local models (3B-8B) across seventeen customer-facing tasks over the Sakila database (609 completed cells; temperature 0; three repetitions per cell). The verticalized pack reaches a pooled mean score of 0.939 versus 0.666 for raw SQL and 0.605 for the generic pack; the smallest model improves from 0.583 to 0.929, matching or exceeding every larger configuration while cutting cost per correct answer by an order of magnitude. All harness code, prompts, gold answers, frozen packs and per-cell results are publicly available.
