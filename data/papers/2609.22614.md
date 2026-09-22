# Concurrency-Aware Process Model Forecasting with Causal Nets

- arXiv ID: `2609.22614v1`
- Authors: Yongbo Yu, Jari Peeperkorn, Johannes De Smedt, Jochen De Weerdt
- Published: 2026-09-18
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.22614v1) | [pdf](https://arxiv.org/pdf/2609.22614v1)

## Abstract

Process model forecasting (PMF) aims to predict the process model that will characterize a future period, thereby providing a process-level view of how behavior is expected to evolve. Existing PMF methods, however, forecast directly-follows graphs, which cannot explicitly represent concurrency. We extend PMF to causal nets by forecasting time series of relation and binding counts and using these forecasts to reconstruct future process models with AND/XOR semantics. To evaluate the resulting models, we introduce a protocol that accounts for partial traces and constructs the workflow nets required for conformance checking. Experiments on four event logs show that the forecasted models achieve conformance levels close to those of models re-mined from observations in the corresponding future windows. They also outperform static discovery baselines, which retain high precision on the structurally stable log but exhibit substantial precision losses on the other three logs. Filtering infrequent bindings improves most conformance metrics, although it also removes much of the concurrent behavior captured by the models.
