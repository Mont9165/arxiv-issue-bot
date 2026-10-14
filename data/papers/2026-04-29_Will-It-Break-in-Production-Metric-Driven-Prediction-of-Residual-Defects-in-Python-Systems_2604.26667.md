# Will It Break in Production? Metric-Driven Prediction of Residual Defects in Python Systems

- arXiv ID: `2604.26667v1`
- Authors: Giuseppe De Rosa, Pietro Liguori
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26667v1) | [pdf](https://arxiv.org/pdf/2604.26667v1)

## Abstract

Python's dynamic nature complicates testing and increases the possibility that some defects evade detection, so an effective fault prediction becomes essential. We examine whether post-release faults can be predicted using modern ML and DL. Using a balanced dataset of over 4,000 labeled faults with 83 product, process, statistical, and Python-specific metrics plus normalized code representations, we conduct cross-project experiments. LLMs and unsupervised models fail to distinguish residual from non-residual faults, while supervised metric-based models (RandomForest, XGBoost, CatBoost) perform far better, yielding a 0.85-0.9 recall and cutting false negatives by an order of magnitude. Process metrics, especially age, churn, and developer-activity, alongside class and file size, consistently prove most predictive. Notably, the Principal Component Analysis shows that metrics and code embeddings occupy distinct regions of the representation space, suggesting that they capture complementary rather than redundant information.
