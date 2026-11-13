# FlinkEval: A Synthetic Corpus for Evaluating Natural Language Interfaces to Streaming SQL

- arXiv ID: `2611.17093v1`
- Authors: Alfio Massimiliano Gliozzo, Nandana Mihindukulasooriya, Gaetano Rossiello, Erick Lee, Lisa Amini
- Published: 2026-11-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.17093v1) | [pdf](https://arxiv.org/pdf/2611.17093v1)

## Abstract

Existing natural-language-to-SQL benchmarks primarily evaluate queries over bounded relational data, leaving streaming semantics underexplored. We introduce FlinkEval, an execution-grounded synthetic benchmark comprising 3,903 question--SQL pairs across 45 industry domains and 45 semantic labels. We create diverse schemas and domain-plausible, temporally consistent data through iterative generation and validation. SQL patterns collected from the human-written NL2SQL pairs and vendor documentation drive quota-balanced generation, and execution with a repair loop on Confluent Cloud Apache Flink produces reference queries covering windowing, temporal joins, pattern matching, nested types, and data manipulation. The corpus includes paired schema-explicit and business-language requests, with annotations for analysis by query pattern, complexity, and execution mode. A seven-level Question Specification Ladder examines semantics-preserving reformulation and underspecified requests augmented with oracle-derived clues. Baseline evaluations combine execution outcomes with adjudicated LLM judgments, revealing challenges in pattern composition and request specification.
