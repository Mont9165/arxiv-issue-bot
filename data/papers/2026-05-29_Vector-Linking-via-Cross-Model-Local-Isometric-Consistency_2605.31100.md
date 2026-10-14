# Vector Linking via Cross-Model Local Isometric Consistency

- arXiv ID: `2605.31100v1`
- Authors: Ziying Chen, Yang Cao, He Sun, Beining Yang, Tianjian Yang
- Published: 2026-05-29
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2605.31100v1) | [pdf](https://arxiv.org/pdf/2605.31100v1)

## Abstract

We study Vector Linking: given two embedding clouds produced by different black-box encoders over partially overlapping datasets, recover cross-model object correspondences using only vectors. Empirically and theoretically, we show that independently trained contrastive encoders exhibit local geometric consistency: short-range distances are approximately preserved up to a scale factor, while long-range distances are not due to model-specific distortion. Building on this, we propose an iterative, reference-based geometric embedding hashing that recovers vector links from a tiny seed set of paired anchors. It represents each vector by distances to sampled paired anchors, proposes candidate links via hash-space matching, and aggregates evidence across views in a Beta-Bernoulli posterior to bootstrap high-confidence links as new anchors. Experiments across multiple benchmarks and embedding model pairs demonstrate accurate and robust linking under varying overlap, seed budgets, and out-of-domain anchors, with applications to vector database integration and cross-model clustering. Code is available at https://github.com/DBgroup-Edinburgh/VecLinking.
