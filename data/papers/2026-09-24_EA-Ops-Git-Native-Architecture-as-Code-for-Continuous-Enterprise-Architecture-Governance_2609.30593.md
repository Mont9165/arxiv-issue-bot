# EA-Ops: Git-Native Architecture as Code for Continuous Enterprise Architecture Governance

- arXiv ID: `2609.30593v1`
- Authors: Vahid Tavakkoli, Kabeh Mohsenzadegan, Kyandoghere Kyamakya
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.30593v1) | [pdf](https://arxiv.org/pdf/2609.30593v1)

## Abstract

Enterprise architecture (EA) repositories frequently separate architecture models from the engineering workflow used to change software and infrastructure. This article presents EA-Ops, an open-source Git-native Enterprise Architecture-as-Code framework that represents architecture facts as YAML, validates typed relationships against an ArchiMate 3.2 profile, enforces organization-specific governance rules, performs graph-based change-impact analysis, and publishes human-facing reports and a static interactive portal from the same reviewed source. We evaluate EA-Ops with a reproducible GitHub Actions harness. Eight independently injected structural, semantic, and governance fault classes were executed across 30 trials each; all 240 trials matched ground truth exactly, with precision, recall, and $F_1$ of 1.000. Scalability experiments with 30 measured repetitions reached 50,000 objects and 100,000 relationships: median validation time was 52.582~s, median impact traversal was 627.000~ms, and peak resident-set size was 919.2~MB. A ten-scenario Metroville digital-permit reference architecture produced exact validation outcomes and exact impact-set agreement with an independent breadth-first-search oracle in every scenario. The configured 100,000-object end-to-end benchmark generated its model successfully but exceeded the 180-minute CI budget during the performance stage; no timing result is extrapolated. At 50,000 objects, Markdown report generation rather than semantic validation is the dominant scaling bottleneck. The results support Git-native continuous governance as a practical EA operating model at tens-of-thousands-of-object scale while defining clear limits and optimization targets for larger repositories.
