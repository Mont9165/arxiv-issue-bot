# Spider 2.0-AIFunc: Extending Real-World Text-to-SQL to AI-Native SQL Workflows

- arXiv ID: `2607.06229v1`
- Authors: Tianyang Liu, Canwen Xu, Fangyu Lei, Nikki Lijing Kuang, Jixuan Chen, Tao Yu, Julian McAuley, Zhewei Yao, Yuxiong He
- Published: 2026-07-07
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.06229v1) | [pdf](https://arxiv.org/pdf/2607.06229v1)

## Abstract

Major cloud data platforms now expose large language model capabilities as native SQL functions, enabling analysts to perform classification, filtering, sentiment analysis, extraction, similarity search, and aggregation within ordinary SQL queries. Yet existing text-to-SQL benchmarks evaluate only conventional SQL and provide no signal on whether models can generate such AI-native SQL. We introduce Spider 2.0-AIFunc, a benchmark of 465 verified instances across 125 real-world databases covering six types of AI functions on the Snowflake platform. Starting from an existing enterprise text-to-SQL benchmark, we construct Spider 2.0-AIFunc through an agent-based pipeline that rewrites source tasks into AI-native form, simultaneously transforming target queries and refining natural language instructions to make the intended AI-native solution explicit and reduce ambiguity. All instances pass a multi-round repeated execution protocol across temporally separated windows to confirm result stability before release. Evaluating ten state-of-the-art language models, we find that the strongest proprietary models reach 67-70% execution accuracy while the best open-source model achieves 58.1%, a gap driven primarily by errors in predicate specification, schema grounding, and AI function parameterization. Agent frameworks designed for traditional text-to-SQL challenges, such as schema retrieval and relevant table selection, do not transfer effectively to AI-native SQL: a minimal agent setup consistently matches or outperforms more elaborate alternatives, suggesting that the strategies these frameworks employ are less critical in this setting. Data are available at https://github.com/Leolty/Spider2-AIFunc .
