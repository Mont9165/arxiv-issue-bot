# Answering Conjunctive Queries with Aggregations under Updates

- arXiv ID: `2607.23881v1`
- Authors: Qichen Wang, Xiao Hu
- Published: 2026-07-26
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.23881v1) | [pdf](https://arxiv.org/pdf/2607.23881v1)

## Abstract

Dynamic query processing keeps query answers up to date during insertions and deletions. For conjunctive queries (CQs) under set semantics, the maintainable classes are known exactly: the $q$-hierarchical CQs under arbitrary updates, widening to the free-connex CQs under insertion-only updates. But modern analytics aggregates, including bag counting, SUM/COUNT, provenance, access control, and shortest paths---all captured by evaluating a CQ over a positive commutative semiring. We ask whether aggregation changes what can be maintained efficiently, and if so, when.
  Under arbitrary updates, it does not: maintenance is at least as hard as over the Boolean semiring. Under insertion-only updates, it does: the boundary retreats from free-connex to a new class we call strong-connex, with $q$-hierarchical $\subsetneq$ strong-connex $\subsetneq$ free-connex $\subsetneq$ acyclic. For every ordered semiring carrying a suitable monotone sequence (e.g., sum-product and tropical), no free-connex but non-strong-connex CQ is maintainable in $O(|D|^{1/2-ε})$ time under the OuMv and OMv conjectures. We further strengthen this lower bound into a family parameterized by the height and dimension of the query, under the combinatorial $k$-clique and generalized OuMv conjectures; these quantify how far the annotated hardness grows as the queries scale.
  On the algorithmic side, a single framework matches these boundaries by adapting CROWN to annotated relations. It maintains every strong-connex CQ in $O(1)$ amortized time under insertion-only updates, regardless of the underlying semiring. Moreover, under arbitrary updates, it maintains every $q$-hierarchical CQ in $O(1)$ amortized time if the semiring has $O(1)$-deletable aggregations. Together, the upper and lower bounds give query- and semiring-parameterized dichotomies that recover the Boolean picture and pinpoint the hardness aggregation adds.
