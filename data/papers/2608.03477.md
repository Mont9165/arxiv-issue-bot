# Getting to the Root: A Combined Complexity Perspective on Consistent Query Answering

- arXiv ID: `2608.03477v1`
- Authors: Miika Hannula
- Published: 2026-08-04
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.03477v1) | [pdf](https://arxiv.org/pdf/2608.03477v1)

## Abstract

The data complexity of consistent query answering has been extensively studied over the past two decades. In this paper, we study its combined complexity, which has gained less attention. The input is a triple consisting of a set of integrity constraints, a (potentially inconsistent) database, and a query, and the question is to determine whether all repairs of the database with respect to the constraints satisfy the query. Our aim is to isolate query-specific structural features that make this problem computationally tractable. We focus on Boolean self-join-free conjunctive queries over primary-key constraints, as in this context the corresponding data complexity problem has been completely classified. Moreover, we restrict attention to queries with an acyclic attack graph, which are precisely those queries that admit a first-order rewriting. As an additional simplifying assumption, we focus on unary primary keys. Each conjunctive query with unary primary keys naturally gives rise to a directed graph, which we call the key-nonkey graph, where each atom contributes an edge from its key variable to each of its non-key variables. Our main result is that, under the stated assumptions, the combined complexity of consistent query answering is in polynomial time whenever the number of source strongly connected components (SCCs) in the key-nonkey graph is bounded by a constant. To prove this result, we develop novel concepts, such as variable guarding and attack-propagation graphs, and techniques, such as database and query saturation and query normalization. In addition, without the boundedness restriction, the combined complexity of this problem is shown to be Pi_2^P-complete.
