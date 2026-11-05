# Whiel: A Neurosymbolic Platform for Certified Relational Program Verification

- arXiv ID: `2611.05612v1`
- Authors: Jesse Comer, Fangzhu Shen, Shuo Zhang, Mayur Naik, Sudeepa Roy, Val Tannen
- Published: 2026-11-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2611.05612v1) | [pdf](https://arxiv.org/pdf/2611.05612v1)

## Abstract

We present the Whiel (a contraction of Whi(le-R)el) system for Lean-certified reasoning about imperative relational programs. The system can encode containment and equivalence problems for Datalog, its extensions with negation, and the core fragment of graph query languages. It can also represent optimized or incremental evaluation algorithms that are not expressible in the original query language, as well as first-order specifications of integrity constraints, schema mappings, and views arising in data integration, exchange, and sharing. Whiel's program states are database instances, and its imperative structure enables compositional Hoare-style reasoning with first-order relational specifications, using prophecy variables and leveled invariants to support inductive arguments. Whiel supports neurosymbolic discovery of loop invariants whose verification conditions can be checked using the Vampire first-order theorem prover. Counterexamples are fed back into the neurosymbolic pipeline, while proposed solutions are translated into Lean proof certificates. To validate the Whiel system, we evaluate its performance on a curated benchmark suite. In summary, we envision the Whiel system as a tool for tackling mathematically demanding, typically undecidable problems involving complex query and constraint languages, with a high degree of trust in its output.
