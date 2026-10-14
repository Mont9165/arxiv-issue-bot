# Structural Adversarial Attacks on Relational Deep Learning under Integrity Constraints

- arXiv ID: `2607.07089v1`
- Authors: Alan Gany, Bogdan Cautis, Silviu Maniu
- Published: 2026-07-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.07089v1) | [pdf](https://arxiv.org/pdf/2607.07089v1)

## Abstract

Relational Deep Learning (RDL) has become a standard methodology for machine learning on relational databases: the database is encoded as a heterogeneous temporal graph in which tuples become nodes and primary-key to foreign-key (PK-FK) dependencies become typed edges, over which a graph neural network is trained for downstream prediction. We study the adversarial robustness of this pipeline. We consider a white-box attacker who knows how the graph is built and the model is trained, reasons about perturbations on the graph, but can only act on the upstream database, by rewiring foreign-key references while preserving the integrity constraints of the schema (foreign-key validity, the degree-one FK constraint, and functional dependencies). This restricts the attacker to a constrained, combinatorial set of admissible edits under a global perturbation budget, which is intractable to explore exhaustively and made non-additive by GNN message passing. We investigate seven attack heuristics - two random sampling baselines and five gradient-guided variants that exploit differentiable edge masks - and evaluate them on the RelBench rel-f1 benchmark. Gradient-based attacks consistently outperform random baselines on regression tasks, whereas gains on classification are smaller, which we attribute to low label-flip rates and greater local stability of classification outputs.
