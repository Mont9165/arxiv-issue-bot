# SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents

- arXiv ID: `2606.18733v1`
- Authors: Qiao Zhao, JianYing Qu, Jun Zhang, Yehua Yang, Hanwen Du, Zhongkai Sun
- Published: 2026-06-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.18733v1) | [pdf](https://arxiv.org/pdf/2606.18733v1)

## Abstract

Realistic coding-agent benchmarks often replay public GitHub issues and pull requests, making them vulnerable to overlap with model pretraining, fine-tuning, synthetic-data generation, or benchmark-driven model selection. Fully synthetic tasks avoid direct historical replay, but can drift away from real repository needs. We propose SWE-Future, a forecast-conditioned data synthesis method for future-oriented coding tasks. Given a forecast snapshot at time $T_0$, the method uses only pre-$T_0$ repository evidence to forecast future feature implementation/enhancement, bugfix, and refactor task families. We first validate this forecasting step retrospectively: after forecasts are fixed, later pull requests are used only to measure whether the predicted task families match future repository work. In an 80-repository study, the forecaster achieves 58.1\% future-work relevance under the main semantic matching metric. We then use validated forecast families as conditioning signals to synthesize a 200-task coding-agent dataset across 61 repositories from a task-generation snapshot, rather than replaying the later pull requests used for validation. SWE-Future shows that repository-evolution forecasts can guide realistic, future-oriented coding-task synthesis while reducing direct dependence on historical pull-request replay.
