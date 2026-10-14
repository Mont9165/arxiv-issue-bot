# Predicting Acceptance and Review Effort in Human and Agent Pull Requests

- arXiv ID: `2607.12057v1`
- Authors: Kartik Ghanshyambhai Pansuriya, Ehsan Ghorbani, Deepak Singh, Eman Abdullah AlOmar
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12057v1) | [pdf](https://arxiv.org/pdf/2607.12057v1)

## Abstract

Pull requests (PRs) are a central mechanism for reviewing and integrating code changes in modern software repositories. As AI coding agents begin to submit more code changes alongside human developers, maintainers face a new challenge: deciding which PRs are likely to be accepted and which ones may require substantial review effort. This paper studies whether such outcomes can be estimated at the time a PR is opened, before reviewer discussion, CI feedback, or merge decisions are available. Using the AIDev dataset, we construct a leakage-aware prediction pipeline for human- and agent-authored PRs. The feature set is limited to submission-time information, including PR text characteristics, metadata, repository context, temporal signals, and lightweight diff statistics. We evaluate classical machine-learning models, including Logistic Regression, Random Forests, Gradient Boosting, Extra Trees, and MLPs, across pooled, human-only, agent-only, and balanced contributor views. Our results show that acceptance prediction is feasible from early signals: tree-based models achieve F1 scores above 0.95, with textual clarity and metadata among the most influential predictors. Review-effort prediction is more difficult. Comment counts and time-to-merge are only modestly explained by submission-time features, suggesting that reviewer availability, project workflow, and team-specific review practices play a major role. These findings indicate that early PR models can support triage and reviewer prioritization, but should be used as advisory tools rather than automated decision-makers.
