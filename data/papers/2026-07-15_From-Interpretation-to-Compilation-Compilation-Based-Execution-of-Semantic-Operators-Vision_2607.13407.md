# From Interpretation to Compilation: Compilation-Based Execution of Semantic Operators [Vision]

- arXiv ID: `2607.13407v1`
- Authors: Wenkai Dong, Yifan Wang
- Published: 2026-07-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.13407v1) | [pdf](https://arxiv.org/pdf/2607.13407v1)

## Abstract

Semantic operator systems extend data processing with natural-language interfaces, supporting operations such as semantic filtering, mapping, and joining. Existing systems commonly execute these operators through interpretation-based execution: for each row, record, or candidate pair, an LLM is invoked to interpret the semantic intent and produce an output. Although expressive, this places expensive LLM calls inside the data-processing loop, causing high latency, monetary cost, and limited scalability.
  We propose compilation-based execution of semantic operators. Instead of using an LLM as a runtime interpreter for every data item, we invoke it once during compilation to translate a semantic operator specification into deterministic executable code. The generated code serves as a compiled physical operator that approximates the behavior of the original LLM-based operator and runs locally over the dataset without per-row or per-pair LLM calls.
  We instantiate this approach for semantic filter, semantic map, and semantic join operators, compare it with LLM-based interpreted execution, and integrate it into an existing semantic operator system. Preliminary results show that compilation-based execution substantially reduces execution time and LLM calls while preserving much of the output quality. More broadly, we argue that semantic operator systems should treat LLMs not only as runtime executors, but also as semantic compilers that generate efficient executable plans, opening new research opportunities at the intersection of database query processing, program synthesis, and LLM-powered data systems.
