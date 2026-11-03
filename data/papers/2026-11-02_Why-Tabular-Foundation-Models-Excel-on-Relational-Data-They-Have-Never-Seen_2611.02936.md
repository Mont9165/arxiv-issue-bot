# Why Tabular Foundation Models Excel on Relational Data They Have Never Seen

- arXiv ID: `2611.02936v1`
- Authors: Linjie Xu, Yiqun Hu, Jixiang He, David Wipf
- Published: 2026-11-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.02936v1) | [pdf](https://arxiv.org/pdf/2611.02936v1)

## Abstract

Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As candidate targets are numerous in enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models (FMs) based on in-context learning (ICL) and RDB-specific pre-training provide a viable solution, but the ideal design still remains largely unresolved. Perhaps unexpectedly, preliminary evidence has recently shown that existing single-table FMs (aka TFMs), when combined with suitable parameter-free relational encoders, can be quite competitive in practice despite zero exposure to RDB pre-training or relational data of any kind. In this work we first empirically confirm this phenomenon with a more diverse array of experiments. We then turn to our main contribution, namely, surfacing multiple complementary explanations for why TFMs behave so effectively. These explanations ultimately hinge on innate synergies whereby parameter-free encoders map relational effects to fixed-length embeddings that loosely mimic distributions for which TFMs were originally designed; in so doing, desirable single-table properties transfer to relational settings (e.g., convergent posterior predictive distributions). Collectively, our analysis forges new pathways for improving RDB FMs, particularly when we prioritize interpretability and inevitable integration within agentic systems.
