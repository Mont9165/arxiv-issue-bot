# Comparing Domain-Model Similarity Metrics Against Human Expert Ratings

- arXiv ID: `2608.15250v1`
- Authors: Vasiliy Seibert
- Published: 2026-08-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.15250v1) | [pdf](https://arxiv.org/pdf/2608.15250v1)

## Abstract

Domain models are a primary artefact in model-driven software engineering, where they capture the shared understanding between stakeholders and serve as the contractual basis for downstream software development. Automatic comparison of these semantic models has diverse application areas such as requirements engineering, education, automatic generation of domain models and model reuse and repository mining. The literature offers a variety of presented metrics, but for practitioners there is no defensible way to choose between them. The contribution of this paper is the implementation of five such metrics, their execution on a fixed set of 39 domain-model comparisons and the comparison of each metric's output against the human expert ratings produced for the same comparisons. Two research questions are addressed. RQ1 asks how close, on average, each metric is to the human expert rating across the 39 comparisons. RQ2 asks how consistent each metric's per-comparison distance from the human expert rating is. The findings reveal that no single metric achieves dominance across all criteria; rather, different metrics each yield competitive results on individual criteria - some closest on average, others best preserving the per-pair ordering - which suggests that an ensemble approach combining multiple metrics may serve as a viable substitute for human expert grading. The metric implementations are an artefact of this work and are published in accordance with the FAIR4RS recommendations (DOI: 10.5281/zenodo.20942596).
