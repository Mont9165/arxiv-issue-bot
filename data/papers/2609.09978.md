# Few Rows Tell Them Apart: Equivalence of Queries Mixing Set and Bag Semantics

- arXiv ID: `2609.09978v1`
- Authors: Sara Cohen
- Published: 2026-09-09
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.09978v1) | [pdf](https://arxiv.org/pdf/2609.09978v1)

## Abstract

Bounded SQL equivalence checkers search for a counter-example database of bounded size, and a search that comes back empty proves nothing. We supply missing theory: computable bounds $B$ such that agreement on all databases with at most $B$ tuples per relation implies equivalence. We work in the combined-semantics framework, which captures SQL's mix of duplicate-eliminating (DISTINCT) and duplicate-preserving computation over set-valued relations. For conjunctive queries we prove a bound linear in the query size for fixed multiset width: inequivalent queries already disagree on a database with at most $2^w |Q|$ tuples, where the width $w$ counts only the columns the queries actually read, independently of the total number of multiset variables. Declared keys shrink the bound to $2^{kw} |Q|$ for the smaller key-width $kw$, acyclic foreign keys leave it unchanged, and the result extends to several classes of queries with comparisons, for which equivalence had not previously been characterized. For these fragments, bounded search becomes a terminating, complete decision procedure.
