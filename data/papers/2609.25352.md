# SSP-Bench: A Hybrid Data Generation Framework for Safety, Security, and Privacy Evaluation

- arXiv ID: `2609.25352v1`
- Authors: Fatih Deniz, Yazan Boshmaf, Issa Khalil
- Published: 2026-09-21
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.25352v1) | [pdf](https://arxiv.org/pdf/2609.25352v1)

## Abstract

Evaluation of large language models (LLMs) for safety, security, and privacy (SSP) relies heavily on static benchmarks, which suffer from score saturation, data contamination, and aggregation artifacts, and fail to capture sensitivity to linguistic variation. As a result, models that perform well on fixed test sets often fail under semantically equivalent rephrasings. We introduce SSP-Bench, a dynamic benchmarking framework that generates evaluation instances on demand while preserving domain consistency. The framework ensures label validity through externally grounded sources, enforces scope via service-specific validation, and calibrates difficulty using a multi-model steering panel. Benchmark construction is formulated as a multi-objective optimization problem over difficulty, separability, novelty, and diversity. Across 24 models and four SSP services, SSP-Bench reveals systematic failures of static evaluation, including near-zero correlation in safety rankings due to construct mixing, strong safety--over-refusal coupling, and hidden within-family regressions. These results show that static benchmarks can misrepresent model behavior, motivating dynamic, deployment-relevant evaluation.
