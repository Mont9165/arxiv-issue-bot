# The Role of Semirings in Incremental View Maintenance

- arXiv ID: `2606.07795v1`
- Authors: Eden Chmielewski, Andrei Draghici, Dan Olteanu, Haozhe Zhang
- Published: 2026-06-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.07795v1) | [pdf](https://arxiv.org/pdf/2606.07795v1)

## Abstract

We study the problem of incremental view maintenance (IVM) under inserts to $K$-databases, where $K$ is a commutative semiring without additive inverse. The key observation put forward in this paper is that the complexity of the IVM problem depends fundamentally on the underlying semiring. We introduce a class of conjunctive queries called $p$-hierarchical and show that for any $p$-hierarchical query with fractional hypertree width $\fhtw$ and any insert-only update sequence of length $N$ to an initially empty $K$-database over an arbitrary semiring $K$ without additive inverse, we can construct a data structure that can be updated in amortized $\bigO(N^{\fhtw-1})$ time and can support constant delay enumeration of the query result. In particular, the amortized update time for any $α$-acyclic $p$-hierarchical query is constant. We also give conditional lower bounds showing that any conjunctive query without self-joins that is not $p$-hierarchical cannot be maintained with amortized constant update time and constant enumeration delay under inserts to $K$-databases. Here, $K$ can be the natural semiring and its generalizations to the provenance and covariance semirings or any idempotent and strictly ordered semiring such as the tropical semiring. When put together, our upper and lower bounds imply a dichotomy for the insert-only maintenance of conjunctive queries without self-joins and the aforementioned semirings: A query can be maintained with amortized constant update time and constant enumeration delay if and only if it is $α$-acyclic $p$-hierarchical.
