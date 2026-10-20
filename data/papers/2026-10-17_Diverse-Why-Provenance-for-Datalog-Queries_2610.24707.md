# Diverse Why-Provenance for Datalog Queries

- arXiv ID: `2610.24707v1`
- Authors: Marco Calautti, Mostafa Milani, Andreas Pieris
- Published: 2026-10-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.24707v1) | [pdf](https://arxiv.org/pdf/2610.24707v1)

## Abstract

Datalog is a powerful rule-based language that allows us to express complex recursive queries and has found numerous applications over the years. Explaining why a result to a Datalog query is obtained is an essential task towards explainable and transparent data-intensive applications that rely on Datalog. A standard way of explaining a query result is the so-called why-provenance, which provides information about the witnesses to a query result in the form of subsets of the input database that as a whole can be used to derive that result. The state-of-the-art approach for efficiently computing the why-provenance explanations of a certain query result aims at enumerating, without repetitions, the relevant explanations by relying on off-the-shelf SAT solvers. However, whenever the set of explanations is very large, outputting the entire set might be prohibitively expensive. Moreover, it is questionable the practical usefulness of flooding the user with a very large number of explanations, many of them possibly differing only marginally. In this case, one can argue that it would be practically more useful to compute a small, sufficiently diverse subset of the set of why-provenance explanations. The present work initiates the study of the latter problem. In particular, we formalize the problem of interest as an optimization problem, and, after showing that it is highly intractable (it is NP-hard even in data complexity), we investigate whether ILP optimization solvers can be employed towards practical solutions. Our main finding is that this is achievable as long as we keep the requested set of explanations small, or we employ approximation algorithms (with error guarantees).
