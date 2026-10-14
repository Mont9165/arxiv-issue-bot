# MCP Server Architecture Patterns for LLM-Integrated Applications

- arXiv ID: `2606.30317v1`
- Authors: Carson Rodrigues, Oysturn Vas
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.30317v1) | [pdf](https://arxiv.org/pdf/2606.30317v1)

## Abstract

The Model Context Protocol (MCP), introduced by Anthropic in November 2024, defines a standardized interface for connecting large language models (LLMs) to external tools, data sources, and services. Within months of release, hundreds of community-built MCP servers appeared on GitHub, but no software-maintenance literature has yet described how the ecosystem is being structured in production. This industry experience paper catalogues five recurring MCP server architectural patterns observed across an enumerated corpus of fifteen independently developed servers (five production servers from the ANSYR voice AI platform plus ten public servers from the official MCP registry): Resource Gateway, Tool Orchestrator, Stateful Session Server, Proxy Aggregator, and Domain-Specific Adapter. Each pattern is described in the structured form of Gamma et al.: context, problem, solution, and consequences. We also document four anti-patterns and a set of cross-cutting concerns around authentication, versioning, and observability. The quantitative evaluation contributes three measurements: inter-rater reliability of the taxonomy across two independent LLM raters on 54 held-out servers (Cohen's kappa = 0.76), which also localizes three pattern-boundary ambiguities; transport overhead measured end-to-end on loopback and modeled for cross-host paths; and a tool-count study showing tool-selection accuracy drops below 90% between 10 and 15 tools per context for Claude Haiku 4.5 and between 20 and 30 tools for Sonnet 4. Code, corpus, and prompts are released as a replication package.
