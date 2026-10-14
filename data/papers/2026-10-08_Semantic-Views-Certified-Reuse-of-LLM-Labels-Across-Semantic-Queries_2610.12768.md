# Semantic Views: Certified Reuse of LLM Labels Across Semantic Queries

- arXiv ID: `2610.12768v1`
- Authors: Oktie Hassanzadeh, Dharmashankar Subramanian
- Published: 2026-10-08
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.12768v1) | [pdf](https://arxiv.org/pdf/2610.12768v1)

## Abstract

Semantic query engines evaluate natural-language filters with a large language model, and every evaluation is a costly oracle call. Optimizers that reduce these calls face a dilemma: cascades that trust a cheap proxy miss their precision and recall targets on many queries, methods with finite-sample guarantees save little, and all of them discard the oracle's labels when the query ends. We present SemViews, a certified semantic filter that orders tuples by signals that cost no oracle calls (the labels that earlier queries left behind as semantic views, a local embedding, and a helper model's score), refines that order with labels it must pay for anyway, and certifies its answer with fresh stratified oracle samples. The answer meets user precision and recall targets with probability at least $1-δ$ for every workload and every catalog, so a stale or misleading view can cost oracle calls but never accuracy. On four workloads replayed against 725,000 recorded oracle labels, SemViews meets both targets on 99.63% of queries and saves 28%-45% of the oracle calls, whereas the only prior method in our study with the same guarantee needs 1.32x-1.71x as many calls. When a question returns in different words, views cut its calls by a further 27%-36%, with both targets met on at least 99.8% of such queries; similarity caches and entailment-based reuse meet them on only 17%-47%.
