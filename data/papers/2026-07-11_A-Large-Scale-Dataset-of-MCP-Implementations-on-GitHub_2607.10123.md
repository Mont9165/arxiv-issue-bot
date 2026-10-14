# A Large-Scale Dataset of MCP Implementations on GitHub

- arXiv ID: `2607.10123v1`
- Authors: Benny Toeppe, Amine Barrak, Emna Ksontini
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.10123v1) | [pdf](https://arxiv.org/pdf/2607.10123v1)

## Abstract

The rapid emergence of the Model Context Protocol (MCP) has introduced a new standard for connecting large language models to external tools and services. Despite its rapid adoption in open-source development, systematic understanding of how MCP is implemented, structured, and maintained remains limited. This study presents the first large-scale, evidence-based dataset of real-world MCP implementation collected directly from GitHub. Using a hybrid pipeline that integrates the GitHub REST and GraphQL APIs with custom Python verification scripts, 3,238 candidate repositories were discovered, filtered, and validated through multi-stage evidence checks. Each verified project was classified by operational role (e.g., client, server, gateway) and exported in a reproducible JSONL schema. A manual review of a representative subset confirmed an overall precision of 83% at a 95% confidence level, and additionally revealed a set of repositories functioning primarily as educational samples, tutorials, or demonstration templates. A targeted exclusion rule was then applied to remove these non-operational repositories, resulting in a final dataset of 2,297 validated MCP projects. The analysis shows that Python and TypeScript dominate MCP development, with hybrid architectures emerging as the most common design pattern. By emphasizing transparent verification strategies, structured evidence tagging, and reproducible data organization, this work establishes a foundational benchmark for studying real-world MCP ecosystems and supports future research on integration, connectivity, and compatibility across the broader developer community.
