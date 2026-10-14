# Conflict Extraction in Probabilistic Datalog Analyses

- arXiv ID: `2608.10755v1`
- Authors: Siyu Chen, Chungha Sung, Xuyang Li, Jingbo Wang
- Published: 2026-08-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2608.10755v1) | [pdf](https://arxiv.org/pdf/2608.10755v1)

## Abstract

Probabilistic extensions of Datalog enable static analyses such as pointer analysis, data race detection, and side-channel analysis to rank alarms by likelihood, but this added expressiveness also introduces a new challenge absent from deterministic analyses: the final output may contain alarms that are individually plausible yet mutually inconsistent, because marginal probabilities do not guarantee joint satisfiability. As a result, developers may spend effort investigating combinations of alarms that can never co-occur in any possible world. We address this problem by formalizing such inconsistencies as minimal unsatisfiable subsets (MUSes) and introducing PPProbe, a conflict extractor specialized for probabilistic Datalog analyses. Rather than improving MUS enumeration in general, PPProbe exploits the structure of Datalog derivation graphs to guide the search toward likely conflicts and prune the search space through bottom-up UNSAT inference. We evaluate PPProbe on 70 benchmarks from power side-channel analysis, data race detection, semantic diffing, and Bayesian-network inference. The results show that PPProbe achieves 2.5 to 24 times higher throughput than state-of-the-art MUS enumerators, and that the conflicts it identifies yield a conservative estimate of false-positive reduction, filtering out an average of 47.7% of mutually inconsistent alarms.
