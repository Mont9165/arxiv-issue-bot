# Zarc: Exact Nearest Neighbors over a Billion Vectors in Seconds

- arXiv ID: `2611.29252v1`
- Authors: Dongfang Zhao
- Published: 2026-11-22
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.29252v1) | [pdf](https://arxiv.org/pdf/2611.29252v1)

## Abstract

Exact k-nearest-neighbor vector search lies on the critical path of machine learning systems, from sparse attention in the latest large language models (LLMs) to long-context memories and training-data deduplication. Exhaustive GPU search scans the whole dataset for every query, while approximate indexes return inexact neighbors. Recent methods skip almost every vector with a cheap half-precision proof that it lies too far away, but only on one GPU that holds the whole dataset. Our insight is to keep only the short rows of these proofs in GPU memory and to fetch the few remaining full vectors from host memory. Our system, Zarc, answers Euclidean, cosine, inner-product, and filtered queries exactly under updates. On four H100 GPUs, it answers 10,000 exact queries over one billion vectors in 1.1 seconds instead of five minutes. On eleven open LLMs, it retrieves the exact top-10 attention keys 2.2x to 13.1x faster than exhaustive search. In sparse attention over one million tokens, it runs 3.1x faster than bf16 selection with FlashInfer, which misses the exact top-64 for most queries.
