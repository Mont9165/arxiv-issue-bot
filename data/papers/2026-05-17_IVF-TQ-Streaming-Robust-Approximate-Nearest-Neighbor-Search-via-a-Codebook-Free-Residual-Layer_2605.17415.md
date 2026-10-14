# IVF-TQ: Streaming-Robust Approximate Nearest Neighbor Search via a Codebook-Free Residual Layer

- arXiv ID: `2605.17415v1`
- Authors: Tarun Sharma
- Published: 2026-05-17
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2605.17415v1) | [pdf](https://arxiv.org/pdf/2605.17415v1)

## Abstract

We propose IVF-TQ, an IVF index with a codebook-free residual layer: a fixed random rotation followed by precomputed Lloyd-Max scalar quantization depending only on (b, d). Only the IVF coarse partition is trained. Building on TurboQuant (Zandieh et al., 2025), the design substantially reduces a key failure mode of trained-codebook ANN indexes (PQ, OPQ, ScaNN): staleness under streaming ingestion.Empirical (3 seeds): Per-batch PQ retraining does not recover the streaming gap at any tested bit budget (paired-t p > 0.28 everywhere). On streaming Deep-10M, IVF-TQ holds at 87.4% -> 86.6% (Delta = -0.80 +/- 0.10pp) while IVF-PQ degrades -3.23pp. A shuffled-i.i.d. control on SIFT-1M shows IVF-PQ losing -3.9pp without distribution shift. At higher PQ bit budgets (~1.5x IVF-TQ memory), absolute recall favors PQ as expected from rate-distortion (+6.1pp Deep-10M; +2.0pp SIFT-10M); the durable IVF-TQ benefit is operational (no codebook to retrain), robust across memory regimes.Prior art: IVF around a codebook-free residual quantizer is architecturally not new -- IVF-RaBitQ ships in Milvus, cuVS, LanceDB, Weaviate; Shi et al. (2026) is concurrent GPU work. TurboQuant itself tests only flat-rotation ANN.Contributions: (i) A multi-seed streaming-operational story for codebook-free IVF: 10M-scale evidence across PQ memory budgets. (ii) A uniform-over-sphere IP-error bound for the TQ residual quantizer with one fixed rotation (proof sketch in v1; rigorous in v2). (iii) Adaptive IVF-TQ: a partition-only refresh recovering 67% -> 97.8% under worst-case rotation shift with re-ranking (90.3% without).Code, data: https://github.com/tarun-ks/turboquant_search
