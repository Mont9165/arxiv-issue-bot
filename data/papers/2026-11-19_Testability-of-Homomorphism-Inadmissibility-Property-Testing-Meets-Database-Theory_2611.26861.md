# Testability of Homomorphism Inadmissibility: Property Testing Meets Database Theory

- arXiv ID: `2611.26861v1`
- Authors: Hubie Chen, Yuichi Yoshida
- Published: 2026-11-19
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CC`, `cs.DS`
- Links: [abs](http://arxiv.org/abs/2611.26861v1) | [pdf](https://arxiv.org/pdf/2611.26861v1)

## Abstract

In this paper, we utilize the perspective of property testing to consider the testability of relational database queries. A primary motivation is the desire to avoid reading an entire database to decide a property thereof. We focus on conjunctive queries, which are the most basic and heavily studied database queries. Each conjunctive query can be represented as a relational structure $\mathbf{A}$ such that deciding if the conjunctive query is satisfied by a relational structure $\mathbf{B}$ is equivalent to deciding if there exists a homomorphism from $\mathbf{A}$ to $\mathbf{B}$. We phrase our results in terms of homomorphisms.
  Precisely, we study, for each relational structure $\mathbf{A}$, the testability of homomorphism inadmissibility from $\mathbf{A}$. We consider algorithms that have oracle access to an input relational structure $\mathbf{B}$ and that distinguish, with high probability, the case where there is no homomorphism from $\mathbf{A}$ to $\mathbf{B}$, from the case where one needs to remove a constant fraction of tuples from $\mathbf{B}$ in order to suppress all such homomorphisms. We provide a complete characterization of the structures $\mathbf{A}$ from which one can test homomorphism inadmissibility with one-sided error by making a constant number of queries to $\mathbf{B}$. Our characterization shows that homomorphism inadmissibility from $\mathbf{A}$ is constant-query testable with one-sided error if and only if the core of $\mathbf{A}$ is $α$-acyclic. We also show that the injective version of the problem is constant-query testable with one-sided error if $\mathbf{A}$ is $α$-acyclic; this result generalizes existing results for testing subgraph-freeness in the general graph model.
