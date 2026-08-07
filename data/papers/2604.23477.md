# SEMA-SQL: Beyond Traditional Relational Querying with Large Language Models

- arXiv ID: `2604.23477v1`
- Authors: Yin Lin, Tianjing Zeng, Zhongjun Ding, Rong Zhu, Bolin Ding, H. V. Jagadish, Jingren Zhou
- Published: 2026-04-26
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.23477v1) | [pdf](https://arxiv.org/pdf/2604.23477v1)

## Abstract

Relational databases excel at structured data analysis, but real-world queries increasingly require capabilities beyond standard SQL, such as semantically matching entities across inconsistent names, extracting information not explicitly stored in schemas, and analyzing unstructured text. While text-to-SQL systems enable natural language querying, they remain limited to relational operations and cannot leverage the semantic reasoning capabilities of modern large language models (LLMs). Conversely, recent semantic operator systems extend relational algebra with LLM-powered operations (e.g., semantic joins, mappings, aggregations), but require users to manually construct complex query pipelines.
  To address this gap, we present SEMA-SQL, a system that automatically answers natural language questions by generating efficient queries that combine relational operations with LLM semantic reasoning. We formalize Hybrid Relational Algebra (HRA), a declarative abstraction unifying traditional relational operators with LLM user-defined functions (UDFs). The system automates three critical aspects: (1) query generation via in-context learning that produces HRA queries with precise natural language specifications for LLM UDFs, (2) query optimization via cost-based transformations and UDF rewriting, and (3) efficient execution algorithms that reduce LLM invocations by an average of 93% in semantic joins through intelligent batching. Extensive experiments with known benchmarks, and extensions thereof, demonstrate the significant query capability improvements possible with our design.
