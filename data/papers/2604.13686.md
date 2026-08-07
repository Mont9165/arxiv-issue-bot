# IndicDB -- Benchmarking Multilingual Text-to-SQL Capabilities in Indian Languages

- arXiv ID: `2604.13686v1`
- Authors: Aviral Dawar, Roshan Karanth, Vikram Goyal, Dhruv Kumar
- Published: 2026-04-15
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.13686v1) | [pdf](https://arxiv.org/pdf/2604.13686v1)

## Abstract

While Large Language Models (LLMs) have significantly advanced Text-to-SQL performance, existing benchmarks predominantly focus on Western contexts and simplified schemas, leaving a gap in real-world, non-Western applications. We present IndicDB, a multilingual Text-to-SQL benchmark for evaluating cross-lingual semantic parsing across diverse Indic languages. The relational schemas are sourced from open-data platforms, including the National Data and Analytics Platform (NDAP) and the India Data Portal (IDP), ensuring realistic administrative data complexity. IndicDB comprises 20 databases across 237 tables. To convert denormalized government data into rich relational structures, we employ an iterative three-agent framework (Architect, Auditor, Refiner) to ensure structural rigor and high relational density (11.85 tables per database; join depths up to six). Our pipeline is value-aware, difficulty-calibrated, and join-enforced, generating 15,617 tasks across English, Hindi, and five Indic languages. We evaluate cross-lingual semantic parsing performance of state-of-the-art models (DeepSeek v3.2, MiniMax 2.7, LLaMA 3.3, Qwen3) across seven linguistic variants. Results show a 9.00% performance drop from English to Indic languages, revealing an "Indic Gap" driven by harder schema linking, increased structural ambiguity, and limited external knowledge. IndicDB serves as a rigorous benchmark for multilingual Text-to-SQL. Code and data: https://anonymous.4open.science/r/multilingualText2Sql-Indic--DDCC/
