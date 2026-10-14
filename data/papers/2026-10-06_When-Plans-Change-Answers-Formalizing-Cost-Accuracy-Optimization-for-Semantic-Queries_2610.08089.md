# When Plans Change Answers: Formalizing Cost-Accuracy Optimization for Semantic Queries

- arXiv ID: `2610.08089v1`
- Authors: Kyoungmin Kim
- Published: 2026-10-06
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.08089v1) | [pdf](https://arxiv.org/pdf/2610.08089v1)

## Abstract

In semantic query engines, predicates are evaluated by machine-learned models, and the choice of a query plan affects not only the cost of a query but also its result. Existing systems either apply a fixed threshold to each semantic operator or tune accuracy per operator, without accounting for how errors propagate through joins. We give a formal problem definition for cost-accuracy optimization of such queries. Our starting point is the calibrated confidence that decision models such as Jev attach to each decision. It yields an expected error for every decision; weighting these errors by each decision's contribution to the output (in the simplest case, its fan-out) gives the expected output quality of a plan without any labeled data, and the same computation in reverse turns an output-level accuracy target into a price on each base or intermediate tuple. Building on this, we define an oracle semantics for relational algebra with semantic operators, physical plans as pairs of a logical plan and a decision policy, declarative output-level targets, and a hierarchy of plan equivalence. We show that accuracy is plan-invariant under pointwise-deterministic policies, and that selection pushdown is not quality-sound when escalation bands are calibrated on the plan's own candidates. Expected quality can be computed in polynomial time under bag semantics; under set semantics it follows the dichotomy of tuple-independent probabilistic databases when every relation carries a semantic predicate. Choosing which tuples to drop is NP-hard, while the optimization problem decomposes into per-tuple decisions through two Lagrange multipliers. Simulations on a synthetic workload illustrate these effects; an evaluation on real engines is left for future work.
