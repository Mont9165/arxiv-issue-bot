# Order-Dependent Complexity of Enumeration and Direct Access for Conjunctive Queries on Dynamic Data

- arXiv ID: `2611.04519v1`
- Authors: Antoine Amarilli, Nofar Carmeli, Clémence Dumoulin
- Published: 2026-11-03
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.04519v1) | [pdf](https://arxiv.org/pdf/2611.04519v1)

## Abstract

This note studies the fine-grained complexity of ranked enumeration and ranked direct access of conjunctive query answers over a dynamic database. We focus on lexicographically sorted answers, defined by an ordering on the query's free variables.
  From the literature, when no particular order is required, we know that when the query is self-join-free and q-hierarchical, we can build a data structure for enumeration (resp. direct access) with linear (resp. linearithmic) preprocessing and constant (resp. logarithmic) update time in the size of the database. For enumeration (resp. direct access), this data structure yields an algorithm that enumerates all query answers (resp. that returns the $k$-th query answer) with constant delay (resp. logarithmic access time). Our goal is to extend these results to ranked enumeration and ranked direct access, with the ranking function defined by a lexicographic order.
  We define a property on the order over the variables of $Q$, which we call being hierarchy-consistent. Given a user-specified query and hierarchy-consistent order, we first propose, for ranked enumeration under updates, an algorithm with linear preprocessing and logarithmic update time that enumerates all the query answers according to the user-specified order with constant delay. Moreover, for ranked direct access under updates, we propose an algorithm with linear preprocessing and logarithmic update time that returns the $k$-th tuple according to the user-specified order with logarithmic access time.
  In contrast, given a user-specified query and non-hierarchy-consistent order, we show a lower bound for ranked direct access under updates.
