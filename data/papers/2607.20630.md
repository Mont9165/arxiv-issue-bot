# Demonstrating GenDB: Instance-Optimized and Customized Query Processing Code Generation via LLM Agents

- arXiv ID: `2607.20630v1`
- Authors: Jiale Lao, Immanuel Trummer
- Published: 2026-07-22
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.20630v1) | [pdf](https://arxiv.org/pdf/2607.20630v1)

## Abstract

Traditional query processing engines require continuous development and extensions to support new techniques and user requirements, and in some cases, entirely new systems must be built from scratch. However, these engines are difficult to extend due to their internal complexity, and building new systems demands significant engineering effort and cost. To address this, we demonstrate GenDB, a generative query engine that shifts query processing from manually engineered systems to query processing code generation driven by Large Language Models (LLMs). An early prototype of GenDB uses LLM agents to generate instance-optimized query execution code tailored to specific data, workloads, and hardware resources. This prototype suits offline code generation for repetitive, templated queries, since the upfront generation cost amortizes over many executions and correctness can be ensured through extensive fuzz testing and manual inspection. For ad-hoc queries, GenDB can work with a traditional DBMS in a hybrid architecture: the DBMS handles one-off queries, while GenDB speeds up frequent SQL templates. Our demonstration allows users to (1) visually and interactively explore how GenDB analyzes workloads, profiles hardware resources and underlying data, produces query plans, generates code based on them, and finally uses an optimizer to iteratively achieve a correct and efficient implementation; (2) use visual inspection and analysis to gain qualitative insights into why GenDB produces code that achieves significantly better performance than state-of-the-art query engines on two benchmarks: TPC-H and a newly constructed benchmark designed to reduce potential data leakage from LLM training data; and (3) upload their own data and queries to explore GenDB with different LLMs and query patterns.
