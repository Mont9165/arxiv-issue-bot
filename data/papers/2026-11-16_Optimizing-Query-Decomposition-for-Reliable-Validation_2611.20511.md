# Optimizing Query Decomposition for Reliable Validation

- arXiv ID: `2611.20511v1`
- Authors: Shuo Zhang, Sudeepa Roy, Jun Yang
- Published: 2026-11-16
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.20511v1) | [pdf](https://arxiv.org/pdf/2611.20511v1)

## Abstract

Large language models (LLMs) have made querying databases more accessible, but cannot guarantee that the SQL they generate is correct. Without a trusted reference query, a validator (human or LLM) must decide whether a generated query answers the intended question. Enterprise questions often require queries with multiple joins, nested subqueries, and multi-level aggregation, and validating such a query in one judgment is error-prone. Decomposition simplifies this task by rewriting a query into smaller queries (blocks) that recompose to the original, each checked against its own sub-question.
  Decompositions differ, however: smaller blocks make each judgment easier but require more judgments, and the best balance depends on the validator's ability. We formulate validation-aware query decomposition as an optimization problem. Just as a query optimizer chooses among equivalent plans by estimated cost, we choose among decompositions by how reliably a given validator is expected to check them. We model how task difficulty and validator ability jointly affect reliability and define an objective that balances reliability against the number of judgments. Over a space of decompositions derived from logical-plan rewrites, our search finds an optimal one. We implement it in DecoVal, a pipeline that presents each block with its sub-question and input interface, combines local verdicts into a query-level decision, and localizes errors to blocks.
  A user study shows that decomposition helps human validators catch and locate errors: with DecoVal, participants caught 91% of the errors, up from 36% without decomposition, and located the error in nearly every rejection. Experiments on BEAVER and Spider 2.0 with LLM validators show that DecoVal also raises error-detection recall over whole-query validation while keeping precision high, and that the best granularity depends on the validator.
