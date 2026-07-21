# Auto Research for Materials: Auditable AI-Scientist Workflows with Held-Out Transfer

- arXiv ID: `2607.17100v1`
- Authors: Jingjie Ning, Xiaochuan Li, Shanshan Zhong, Ji Zeng, Guolin Ke
- Published: 2026-07-19
- Primary category: `cs.MA`
- Categories: `cs.MA`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17100v1) | [pdf](https://arxiv.org/pdf/2607.17100v1)

## Abstract

An AI research agent can improve the score it sees without finding a modelling change that works on new materials. We ask a stricter question. After repeated experiments, does the selected change survive on data that never entered the loop, and can its code be reused? We separate the search into changes to features, models, representations, and training data. Seven searches produce 701 evaluated changes across ten Matbench endpoints. Agents receive only the mean over five inner folds, reducing reliance on any single development split. We then freeze the selected code and evaluate it once on an untouched holdout. Nine of ten choices remain the best tested single intervention. The surviving changes reveal two materials modelling regimes. With composition alone, feature, model, and representation changes provide comparable routes to improvement. They include held-out MAE reductions of 17.4\% for band gap and 18.6\% for steel strength, as well as gains on both classification endpoints, while screened external data adds little. For structure tasks, richer geometry descriptors and model or calibration changes lower mean held-out MAE by 14.6\% and 7.1\% and lead on different property families, whereas composition embeddings do not transfer. Combining separately found feature and model changes yields a 26.3\% mean held-out improvement. These results show in materials prediction that closed-loop agents can produce decisions that survive unseen evidence and code changes that can be reused across tasks and combined. More broadly, they provide an evaluation design for testing executable discoveries beyond the feedback loop.
