# DBcover: A White-box SQL Test Generation Framework for Coverage Improvement

- arXiv ID: `2608.25573v1`
- Authors: Yankai Rong, Shuang Liu, Jinhao Dong, Qiang Yin, Wei Lu, Jianhua Wang, Xiaoyong Du
- Published: 2026-08-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25573v1) | [pdf](https://arxiv.org/pdf/2608.25573v1)

## Abstract

Relational Database Management Systems (RDBMSs) are the backbone of modern data-intensive applications, making reliability and robustness critical. However, achieving high coverage in RDBMS testing remains challenging because of large codebases and complex execution logic. Traditional fuzzing relies on random SQL generation and cannot capture the correspondence between SQL inputs and internal execution paths, while symbolic execution suffers from prohibitive cost and scalability limitations.
  We propose DBcover, an LLM-driven white-box SQL test generation framework based on contextual reasoning. DBcover uses lightweight dynamic analysis to extract SQL-to-path correspondence and call graphs as global context, and collects source-level information around target functions as local context. These contexts are organized in a unified knowledge graph for efficient retrieval and reuse. DBcover then performs two-phase test generation: it first selects a semantically relevant seed whose execution path is close to the uncovered target, and then guides the LLM with global and local context to generate SQL test cases that trigger previously uncovered code regions. Experiments show that DBcover achieves 80.1% and 82.3% coverage on PostgreSQL and MySQL, and is also effective on the enterprise RDBMS KingbaseES, demonstrating its practical applicability to closed-source systems.
