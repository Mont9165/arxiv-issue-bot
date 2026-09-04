# KnowFeat: Knowledge-Guided Feature Engineering via LLM Agents

- arXiv ID: `2609.03529v1`
- Authors: Chengsong You, Wangyue Li, Weiqiao Que, Qizhou Chen, Kunyan Wu, Wei Deng, Feng Zhu, Xiaofeng He
- Published: 2026-09-03
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.03529v1) | [pdf](https://arxiv.org/pdf/2609.03529v1)

## Abstract

Automated feature engineering with large language models (LLMs) can produce semantically meaningful features for tabular data, yet existing methods lack structured domain knowledge, rigorous verification, and explainable provenance. We propose KnowFeat, a knowledge-guided feature engineering framework that organizes domain knowledge into five types -- schema metadata, regulatory indicators, detection rules, expert opinions, and court document evidence -- and injects them as structured context into an LLM agent. A three-stage verification pipeline filters candidates through code execution, statistical quality checks, and model effectiveness evaluation. Every accepted feature carries a provenance record tracing its design to specific knowledge assets. Under a strict held-out protocol that eliminates feature-selection leakage, KnowFeat ranks first (avg. rank 2.3) across twelve public benchmarks among seven methods (one-sided Wilcoxon p=0.017), with a peak gain of +11.6 pp AUC on a telecom churn dataset. On a real-world Bitcoin anti-money laundering (AML) dataset (Elliptic) and a synthetic digital currency AML benchmark (SimECNY), KnowFeat maintains competitive detection performance with full provenance traceability.
