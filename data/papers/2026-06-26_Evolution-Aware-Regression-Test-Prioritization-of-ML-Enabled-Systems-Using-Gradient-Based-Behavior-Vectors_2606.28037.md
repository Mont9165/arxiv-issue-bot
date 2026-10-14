# Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors

- arXiv ID: `2606.28037v1`
- Authors: Eunho Cho, Donghwan Shin, In-Young Ko
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.28037v1) | [pdf](https://arxiv.org/pdf/2606.28037v1)

## Abstract

The machine learning(ML) component of an ML-enabled system evolves through retraining, fine-tuning, and optimization, so previously valid test results may no longer hold. A single evolution step can worsen performance on some test cases while improving others, making regression test prioritization inherently directional. We present Gradient-based Behavior Vector-Parameter Delta(GBV-PD), the first approach to operationalize the behavior vector space for evolution-aware regression test prioritization. GBV-PD represents each test case as a gradient-based vector(GBV), a low-dimensional projection of its loss gradient under the original model. It then projects the observed parameter update of the evolved model onto the same PCA basis and uses the resulting alignment to estimate whether each test case's loss is likely to increase or decrease, without running the evolved model on test cases during prioritization. In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching. These results show that behavior-space ideas can be operationalized into a practical and efficient mechanism for repeated-update regression testing of evolving ML-enabled systems.
