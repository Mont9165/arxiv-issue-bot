# A Multi-Layer Testing Framework for Automated Data Quality Assurance in Cloud-Native ELT Pipelines

- arXiv ID: `2605.20500v1`
- Authors: Ismail Gargouri, Hassan Reza
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.20500v1) | [pdf](https://arxiv.org/pdf/2605.20500v1)

## Abstract

Ensuring data quality in cloud-native Extract-Load-Transform (ELT) pipelines is increasingly challenging due to heterogeneous data sources, evolving schemas, and multi-backend execution environments. This paper presents a unified, multi-layer testing framework that integrates orchestration-level validation, declarative dbt tests, large language model (LLM)-generated semantic tests, and cross-store consistency checking between DuckDB and Snowflake, orchestrated through Apache Airflow. Controlled anomaly-injection experiments demonstrate that a manual-only baseline detected 7 of 16 injected anomalies. In contrast, both a manually expanded comparator and the proposed LLM-augmented configuration detected all 16, representing a 128.57% relative improvement in detection rate over the baseline. Post-migration cross-store validation confirmed exact agreement across all three curated tables. Of 25 LLM-generated test assertions, 9 were classified as useful, 4 as redundant, and 12 as executable but low-value. The complete workflow executed in 106.58 seconds across eight instrumented pipeline stages. These results demonstrate that LLM-driven semantic test synthesis can materially strengthen validation coverage while remaining operationally practical for production ELT environments.
