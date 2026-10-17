# Reflective Compositional Grounding for Natural-Language-to-SPARQL

- arXiv ID: `2610.21796v1`
- Authors: Isabelle Mohr, John Dujany, Andre Freitas
- Published: 2026-10-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.21796v1) | [pdf](https://arxiv.org/pdf/2610.21796v1)

## Abstract

Natural-language query generation over large knowledge graphs embodies the classical vocabulary problem in human-systems communication. Questions express concepts through wording and compositions that can differ substantially from the target schema, while limited model context requires selective access to schema information. We present an NL2SPARQL framework that places conceptual compositionality at the center of query interpretation and connects it to the relational composition required for binding and query construction. A fixed concept encoder represents compound expressions jointly, and schema candidates are ranked using semantic similarity, type compatibility, and hierarchy proximity. Reflective refinement critically examines how the grounded meanings are realized through argument bindings, joins, and operator scope. Diagnosed semantic discrepancies guide revisions to the responsible stage. We formalise a monotone refinement discipline that accumulates scoped interpretation requirements and establish conditions under which changes to the composed process preserve previously validated interpretations. Across five benchmark/knowledge-graph targets, mean schema recall@10 increases from 0.712 to 0.837. With retrieval held fixed, reflective prompt rewriting adds 2.27-3.33 answer-F1 points. These experiments evaluate the grounding and refinement mechanisms, while the formal analysis specifies the stronger requirements for conservative adaptation across queries.
