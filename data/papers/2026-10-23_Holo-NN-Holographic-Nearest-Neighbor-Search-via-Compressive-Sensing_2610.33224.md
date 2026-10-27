# Holo-NN: Holographic Nearest Neighbor Search via Compressive Sensing

- arXiv ID: `2610.33224v1`
- Authors: Bryant Gipson
- Published: 2026-10-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.33224v1) | [pdf](https://arxiv.org/pdf/2610.33224v1)

## Abstract

In the age of AI, privacy-preserving approximate nearest neighbor (ANN) search over high-dimensional embeddings has emerged as a critical yet frustratingly challenging domain, dominated by tradeoffs between speed, privacy, and accuracy. Traditional tree and graph-based indexing structures (e.g., HNSW, ScaNN) rely fundamentally on non-linear operations that are computationally intractable under Fully Homomorphic Encryption (FHE) or blind server-side constraints.
  In this paper, we introduce Holo-NN (Holographic Nearest Neighbor Search), an algebraic framework that replaces data-dependent branching with a single linear projection. Our key observation is that while distances across a database are dense, neighborhood membership is inherently sparse: only a handful of points ever lie close to a query. By pairing locality-preserving feature transforms with Compressive Sensing, Holo-NN folds the entire database offline into a compact holographic sensing matrix. At query time, encrypted search reduces to a single, non-interactive matrix-vector multiplication---requiring no FHE bootstrapping, no multi-round interaction, and no client-side index state. This turns private retrieval into an embarrassingly parallel, accuracy-tunable computation that runs out of the box on both CPUs and GPUs, scaling efficiently to production databases. We offer a comparison against other state-of-the-art Private ANN algorithms to help situate the method in the broader context of production-grade private retrieval.
