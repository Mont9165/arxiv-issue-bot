# Automatic Unsupervised Ensemble Outlier Model Selection--Extended Version

- arXiv ID: `2605.16567v1`
- Authors: Hong-Phuc Phan, Tuan-Anh Vu, Tung Kieu, Son Ha Xuan, Bin Yang, Christian S. Jensen
- Published: 2026-05-15
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.16567v1) | [pdf](https://arxiv.org/pdf/2605.16567v1)

## Abstract

Unsupervised outlier detection is attractive because it eliminates the need for labeled data. Moreover, forming multi-model ensembles can improve detection robustness. However, composing an ensemble without labeled data is challenging. Naively composed ensembles can suffer from ensemble saturation, where redundant or unreliable detection models degrade performance and incur unnecessary computation. We propose MetaEns, an automatic unsupervised framework for selecting ensembles of outlier detection models. Using labeled meta-datasets, MetaEns learns a model that predicts marginal ensemble gains, estimating the expected improvement from adding a candidate model to a partially constructed ensemble. At test time, this learned signal is combined with a submodular-inspired proxy objective that enforces diminishing returns through diversity-aware discounting and family-level risk regularization, thereby enabling greedy sequential selection with adaptive early stopping. As a result, MetaEns constructs compact, high-quality ensembles without access to ground-truth labels. Experiments on 39 real-world datasets show that MetaEns consistently outperforms state-of-the-art unsupervised selectors and ensemble baselines, achieving higher average precision while using fewer models.
