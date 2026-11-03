# TSSDA: An Autonomous Agent for Constructing a Time-Series Text-to-SQL Benchmark

- arXiv ID: `2611.02132v1`
- Authors: Zhihan Zheng, Shaoxu Song, Haitao Yuan, Minxiao Chen
- Published: 2026-11-01
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.02132v1) | [pdf](https://arxiv.org/pdf/2611.02132v1)

## Abstract

As agents increasingly undertake data querying, Text-to-SQL serves as a foundational capability for database access. However, for text-to-SQL in time-series databases, high-quality benchmarks and large-scale training corpora remain scarce, limiting the systematic evaluation and domain adaptation of existing models and agents. Existing automated SQL generation approaches lack sufficient autonomy, leaving key challenges unresolved. First, numerous combinations of temporal syntax and functions complicate comprehensive coverage of valid queries. Second, as the corpus grows, generating valuable and diverse new data becomes increasingly challenging. Third, schema and data heterogeneity hinder reuse of temporal query structures, limiting generation efficiency. To address these challenges, we propose TSSDA, a Time-Series SQL (TSSQL) Generation Data Agent framework, and construct TERN, a comprehensive Time-sERies text-to-SQL beNchmark. First, to achieve broad coverage of valid queries, we systematically model TSSQL syntax and semantics to construct a data generation space. Next, to explore the space and improve diversity, we develop a Data Agent that autonomously orchestrates data generation. The agent comprises a planning and decision-making module and a query generation module, with online adaptation for continuous self-improvement. Finally, we introduce a temporal-aware memory that enables adaptive reuse of experience across heterogeneous data instances, improving generation efficiency. Comprehensive evaluations on TERN reveal the limitations of existing methods in performing Text-to-TSSQL tasks. Furthermore, extensive experiments demonstrate that TSSDA substantially improves coverage, diversity, and complexity.
