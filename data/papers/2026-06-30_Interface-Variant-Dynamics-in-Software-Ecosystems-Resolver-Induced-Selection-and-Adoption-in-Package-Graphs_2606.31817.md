# Interface-Variant Dynamics in Software Ecosystems: Resolver-Induced Selection and Adoption in Package Graphs

- arXiv ID: `2606.31817v1`
- Authors: Faruk Alpay, Baris Basaran
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2606.31817v1) | [pdf](https://arxiv.org/pdf/2606.31817v1)

## Abstract

Compatibility research usually treats an interface change as a local writer-reader decision. Distributed software stacks make that decision population structured: an RPC, telemetry, middleware, or service-contract variant is introduced by one provider release and then spreads, stalls, or is mediated across consumers, transitive dependencies, and resolver rules. This paper asks when that observation is a load-bearing software-engineering estimator rather than evolutionary relabeling. We mine interface histories, audit npm, Maven Central, PyPI, and crates.io package graphs, execute 2100 package-manager resolver probes, estimate an ecosystem-specific selection coefficient $s$ from clean conflict probabilities, and use that measured $s$ to forward evaluate a pairwise-comparison absorbing process on the observed package graph. We separate three evidential roles. Fixation is a forward evaluation, not independent evidence: once $s$ is measured, deviation from $1/N$ follows mechanically from the non-neutral process. Checker-derived direction carries adoption signal: a direction-permutation null gives checker-direction gap MAE 0.07 versus null median 0.43 ($p=0.002$). But because that direction is derived from the same boundary state whose admitting frequency is predicted, it is a diagnostic rather than an orthogonal selection test. The stricter checker-free temporal test asks whether early resolver-channel features predict later blocked-to-admitted flips; in this snapshot they do not beat age-only (Brier 0.28 versus 0.24, AUC 0.51 versus 0.54). The result is a reproducible estimator audit for interface-variant dynamics in distributed package graphs, showing where resolver evidence becomes population input and where the current registry data still fail to close the resolver-to-adoption loop.
