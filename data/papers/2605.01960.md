# LAPRAS : Learning-Augmented PRivate Answering for linear query Streams

- arXiv ID: `2605.01960v1`
- Authors: Pranay Mundra, Adam Sealfon, Ziteng Sun, Quanquan C. Liu
- Published: 2026-05-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.01960v1) | [pdf](https://arxiv.org/pdf/2605.01960v1)

## Abstract

Modern database workloads are highly predictable: query streams are dominated by recurring jobs and templates, even when their arrival order is not known in advance. This motivates a learning-augmented view of online differentially private (DP) analytics: can algorithms utilize predictions about which queries will occur to improve utility under a single global privacy budget, while remaining robust when predictions are wrong? We study online DP query answering, where a curator must answer a stream $Q$ of $S$ linear queries arriving in uniformly random order under privacy budget $(ε,δ)$. We present LAPRAS, which assumes access to an oracle that outputs a prediction set of queries likely to appear in the stream and uses it to guide privacy spending. LAPRAS answers predicted queries using the offline-optimal Matrix Mechanism and answers the remaining queries online from a residual budget. To pace spending across an unknown number of unpredicted queries, we introduce Smooth Allocation, which forms an unbiased stopping-time estimate $\widehat{B}$ from the first $T=Θ(\log^2 S)$ unpredicted queries and continuously recalibrates per-query expenditure. Empirically, over two real datasets, we validate the intended consistency--robustness trade-off: LAPRAS achieves near-offline utility under high overlap and degrades gracefully to baseline-level performance when overlap is low.
