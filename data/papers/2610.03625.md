# FALCON: A Model and Dataset Agnostic Framework for Synthetic Data Generation for NL2SQL Pairs

- arXiv ID: `2610.03625v1`
- Authors: Darian Lee, Shannon Rumsey, Jack St. Clair, Xinyi Tang, Aditya Bansal, Yuanming Shi
- Published: 2026-10-02
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.03625v1) | [pdf](https://arxiv.org/pdf/2610.03625v1)

## Abstract

Relational databases are among the most widely deployed forms of structured knowledge, and natural language access to them requires grounding language onto schema entities and relations while handling the ambiguity inherent in how people phrase requests. Existing synthetic NL-to-SQL data generation methods largely ignore this ambiguity and produce oversimplified queries that fail to prepare models for the complexity of real-world structured knowledge access. We present FALCON, a framework that generates realistic, ambiguity-aware NL-to-SQL data matching the complexity of challenging real-world benchmarks, at low cost using compact open models. Our approach combines reserved-word SQL seeding and persona-based prompting to generate structurally complex queries, while alignment-based filtering preserves difficulty by distinguishing genuinely incorrect examples from complex but valid queries. Human evaluation confirms consistent high quality across model sizes, and our generated data exceeds existing benchmarks in both SQL complexity and natural language richness. Difficulty-stratified analysis shows models trained on FALCON data increasingly outperform baseline-trained models as query complexity increases, validating our pipeline's success in generating challenging training data. When combined with a small proportion of existing benchmark data, mixed training recovers performance on simpler queries while preserving these advantages on complex ones. The model- and database-agnostic design enables organizations to generate high-complexity NL-to-SQL training data locally without external APIs.
