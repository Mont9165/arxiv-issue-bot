# Incremental Evaluation and Training in Relational Deep Learning

- arXiv ID: `2608.13023v1`
- Authors: Jakub Peleška, Gustav Šír
- Published: 2026-08-13
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.13023v1) | [pdf](https://arxiv.org/pdf/2608.13023v1)

## Abstract

Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs to enable end-to-end representation learning. However, prevailing RDL evaluation practices rely on static, single-episode dataset snapshots, overlooking the continuous, time-evolving nature of real-world databases. Consequently, current RDL benchmarks fail to capture how model performance changes as new data accumulates over time. To address this limitation, we introduce an incremental, multi-episode evaluation and training paradigm to assess and improve the temporal robustness and adaptability of state-of-the-art RDL models. Using established large-scale datasets, we examine data evolution and model training dynamics, demonstrating that temporal concept drifts occur in the majority of predictive tasks. We present multiple incremental training regimes for fine-tuning the models and demonstrate that transfer learning is both feasible and highly effective in the RDL setting. Alongside a new temporal evaluation metric that prioritizes near-future accuracy, we show that our incrementally fine-tuned models consistently outperform the standard, expensive, from-scratch trained baselines.
