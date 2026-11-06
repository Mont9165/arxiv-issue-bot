# Per-Query Recall Guarantees for Approximate Nearest Neighbor Search in Dynamic Vector Databases

- arXiv ID: `2611.07579v1`
- Authors: Woong-Kee Loh, Suan Lee
- Published: 2026-11-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.07579v1) | [pdf](https://arxiv.org/pdf/2611.07579v1)

## Abstract

Vector search runs as an operator in database systems, where a missed neighbor can make a filter, join, or aggregate wrong, yet approximate nearest neighbor (ANN) indexes are tuned only for an average recall target. In our measurements, indexes tuned to an average recall of 0.99 left 5-19% of in-distribution queries and, tuned without a query log, up to 99.6% of real out-of-distribution queries below this target, and the misses grew under updates. We present PQR-Search, a k-ANN search method that guarantees $\Pr[\mathrm{Recall}(q)<τ]\leδ$ for every query. The probability is only over a random orthogonal transformation inside the index, so no distributional assumption is needed, only that queries and updates do not depend on it; the guarantee holds after insertions and deletions without retuning. PQR-Search stores 1-bit codes of rotated residuals with respect to IVF centroids and prunes with exact quantiles of their error distribution. A formula predicting the fraction of vectors that pass the code test, with no data-fitted constants, chooses index parameters and maintenance operations without affecting the guarantee. On 20 datasets of up to 100 million vectors, failure rates stayed at most $δ$ in every audit, including all 33 steps of the official NeurIPS'23 streaming runbook, whereas CTR, a conformal guarantee averaged over queries, left up to 16.4% of queries below the target. Where HNSW tuned to an average recall of 0.99 met that target, PQR-Search had 2.5x its single-query latency and 1.3x lower batch throughput, yet that HNSW still left 3-29% of queries below 0.99. PQR-Search was faster than FAISS exhaustive search in every static setting (26.4x geometric mean in batch; 69-154x at 100M scale), faster than IVF with nprobe chosen afterwards for every test query in all 52 main settings, and 27-76x faster at one thread than PUFFINN, which also gives per-query guarantees.
