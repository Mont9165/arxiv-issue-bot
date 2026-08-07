# Latent Programming Horizons in Coding Agents

- arXiv ID: `2607.05188v1`
- Authors: André Silva, Han Tu, Martin Monperrus
- Published: 2026-07-06
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05188v1) | [pdf](https://arxiv.org/pdf/2607.05188v1)

## Abstract

A coding agent solving a software-engineering task spends dozens of steps reasoning, editing code, and running tests, yet little is known about what the underlying language model internally represents about the program it is working on. We show that the residual streams of language models under coding agents linearly encode properties of the evolving program: a logistic-regression probe on hidden states is able to decode whether the current code parses, passes its test suite, reduces the number of failing tests, and introduces regressions, reaching AUC up to 0.83 for correctness across two models and two benchmarks. Our second finding is more surprising: these representations run ahead of the agent's own edits. Probes trained to predict the outcome of future edits (before they are materialized and written on disk) achieve performance above chance up to roughly 25 steps in advance. We call this the agent's latent programming horizon. As a proof of external validity, we show that the probes transfer across benchmarks without retraining. Our positive results open calls for more research in mechanistic interpretability of coding agents.
