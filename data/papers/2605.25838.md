# Same Data, Different Schemas: Robustness of LLM-based Text-to-SQL

- arXiv ID: `2605.25838v1`
- Authors: Nitin Kanchinadam, Aditya Menachery, Amol Deshpande
- Published: 2026-05-25
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.25838v1) | [pdf](https://arxiv.org/pdf/2605.25838v1)

## Abstract

Large language models (LLMs) consistently achieve strong results on text-to-SQL benchmarks, but their robustness to schema variations remains poorly understood. Recent work suggests that the schema structure matters, but does not provide a clear and systematic way to evaluate model behavior when different schemas represent the same underlying data. We address this problem by presenting a framework to evaluate and benchmark text-to-SQL techniques over equivalent relational schemas generated from a common E/R model. By varying the ``shredding'' choices used to translate the conceptual design into relations, we create multiple schema variants that differ structurally while preserving the same underlying semantics. This gives us a controlled setting in which the natural language questions and data remain fixed, and only the schema changes. We use this framework to evaluate four leading LLMs on the same questions across multiple schema variants (for two separate domains), and summarize consistency patterns using pairwise comparison heatmaps. Our results show that schema structure significantly affects LLM behavior: across conceptually equivalent schemas, models often produce SQL queries with very different answers. We also find that providing additional context (specifically, the original E/R specification) improves the performance, but does not fully ameliorate the inconsistencies. In addition to demonstrating that the current text-to-SQL evaluations miss an important notion of robustness, our framework provides a way to generate a large number of synthetic datasets that can be used to train new models, and suggests a mechanism to make text-to-SQL more robust by generating additional candidate plans for a given natural language query through systematic schema variations.
