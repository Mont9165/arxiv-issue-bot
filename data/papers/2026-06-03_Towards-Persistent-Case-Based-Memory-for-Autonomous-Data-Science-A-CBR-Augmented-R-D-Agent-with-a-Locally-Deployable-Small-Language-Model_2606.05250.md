# Towards Persistent Case-Based Memory for Autonomous Data Science: A CBR-Augmented R&D-Agent with a Locally Deployable Small Language Model

- arXiv ID: `2606.05250v1`
- Authors: Felix Stocker
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.05250v1) | [pdf](https://arxiv.org/pdf/2606.05250v1)

## Abstract

Most top-performing autonomous data-science agents rely on frontier cloud models and lack persistent, cross-session memory. This paper addresses two open gaps: (1) the underexplored use of formally structured, quality-controlled Case-Based Reasoning (CBR) case bases coupling symbolic case records with executable code artefacts; and (2) the untested viability of Small Language Models (SLMs) as locally deployable agent backbones. We present CBR-augmented R&D-Agent, integrating a persistent CBR layer into Microsoft's R&D-Agent framework with a custom backend for Gemma 4 31B Dense -- the first published end-to-end evaluation of Gemma 4 as an autonomous data-science agent backbone. The CBR layer overrides three R&D loop phases via a surgical subclass toggled by a single environment variable. Cases are stored as structured records with executable code snapshots and quality metadata; a five-gate quality filter and a heuristic reuse-detection mechanism assess knowledge transfer by combining embedding similarity, code-fingerprint overlap, and injection provenance. Evaluated on two Kaggle competitions (NOMAD 2018, Spaceship Titanic) with four seeds over eight improvement loops each, CBR achieves directionally higher accuracy than the CBR-disabled baseline on Spaceship Titanic (0.8147 vs. 0.8098, d = -1.41) with substantially lower variance. Heuristic reuse detection across 108 retrieval events shows high semantic relevance (mean embedding similarity 0.882) alongside variable structural proximity (mean code-fingerprint similarity 0.305), consistent with conceptual guidance rather than verbatim code copying.
