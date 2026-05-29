# A Query Engine for the Agents

- arXiv ID: `2605.27785v1`
- Authors: Kenny Daniel
- Published: 2026-05-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.27785v1) | [pdf](https://arxiv.org/pdf/2605.27785v1)

## Abstract

The fastest-growing data in production today is unstructured text: agent traces, chat logs, reasoning chains, model outputs. People want to analyze it, and the questions worth asking ("show me where the agent got confused") cannot be answered by SQL alone, since text is not queryable without a model in the query path. The natural place this analysis is happening is the new class of AI applications (Claude Code, Cursor, Claude Desktop, in-browser agents) that run client-side and host both a human user and an LLM agent in the same process. These applications increasingly want to work with data, but the lakehouse read path has been hard to use from a JS runtime: Spark, Trino, and managed warehouses do not fit there. To build this new kind of AI data application, three properties of the engine become first-order: a JS-native distribution that drops into the runtime the application already runs in, a bundle small enough to ship inside a cold tab or per-turn agent sandbox, and a way to interleave analytic operators with model-based interpretation of text. We present Hyperparam, three open-source JavaScript libraries (Hyparquet, Squirreling, Icebird) totaling under 70 KB, that read Parquet and Apache Iceberg directly from object storage and meet the third property with per-cell, async-native SQL execution, so expensive cells fire only when downstream operators demand them. Squirreling runs LLM-shaped async UDFs over 300x faster than DuckDB-WASM on filter-bounded queries (and 192x on sort-bounded queries) and completes a ten-task agent analyst suite at two-thirds lower cost. We argue that data engineering as a discipline needs to update for the AI-native client applications now in production and the agents that work alongside their users.
