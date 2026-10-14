# Transformations for Evolving Property Graph Schemas

- arXiv ID: `2609.34789v1`
- Authors: Gauvain Devillez, Stefania Dumbrava, Angela Bonifati
- Published: 2026-09-28
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.34789v1) | [pdf](https://arxiv.org/pdf/2609.34789v1)

## Abstract

Property graph databases are widely used to represent complex and evolving data; yet, systematic support for property graph schema evolution remains limited. In practice, schema transformations are typically defined manually, coupled to specific application contexts, and are difficult to reuse across schemas or evolution scenarios. We present GRAFT, a logic-based framework that models prop- erty graph schema evolution as reusable, order-constrained meta- transformations derived from atomic edits. Schema evolution is formulated as exploration of a finite meta-graph with schemas as nodes and grounded meta-transformations as edges. To ensure tractability, GRAFT combines similarity-guided search and pruning, guaranteeing duplication-freeness, termination and correctness. An experimental evaluation on four benchmark and real-world property graph schema evolution scenarios shows that GRAFT effi- ciently computes high-quality schema transformation sequences. Using greedy exploration, GRAFT reaches the exact target schema on most datasets, producing stable transformation sequences while keeping runtimes low. A qualitative study on both real-world and a synthetic large-scale dataset further shows the quality and robust- ness of the obtained reusable meta-transformations.
