# Fidelity Synopses: Pre-Execution Plan Selection for Approximate Vector Search

- arXiv ID: `2610.41407v1`
- Authors: Adithya Ramanatha, Sanskar S. Singh, Maya Ramanath
- Published: 2026-10-30
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2610.41407v1) | [pdf](https://arxiv.org/pdf/2610.41407v1)

## Abstract

Vector search has become a database operator with many physical implementations: different index families, build-time and search-time parameters, and compressed or disk-resident variants. Each trades cost against fidelity, the fraction of a query's exact top-k nearest neighbors that a configuration returns. Deployments nevertheless choose one configuration offline and use it for every query, so they are sized for their hardest queries and overpay for the rest. On a 5.8M-item LAION benchmark with four embedding models, running each query on the cheapest configuration that suffices for it would roughly halve the cost in a typical setting. Exploiting this requires predicting each configuration's fidelity before running it, which is hard because fidelity is defined by the very exact search that approximate indexes avoid. Relational optimizers solve the analogous problem for cardinality with offline synopses; we propose one for vector search. A fidelity synopsis divides the embedding space into cells around a set of landmarks and records, for every cell and configuration, how often that configuration met a fidelity target on a sample of queries. At query time, one nearest-landmark lookup yields a calibrated estimate for every configuration, and an optimizer chooses configurations so that the workload misses the target no more often than its requirement allows. We test the two premises the synopsis relies on, that fidelity varies smoothly across the embedding space and that its loss is specific to each configuration. Held to the same requirement a static deployment is built to meet, synopsis-guided selection lowers cost in all 16 combinations of model and query direction, to a median of 0.72x the static deployment, with a batched lookup of 21-32 microseconds per query. The saving persists against the best static choice among the same indexes, and within a single index at no extra memory.
