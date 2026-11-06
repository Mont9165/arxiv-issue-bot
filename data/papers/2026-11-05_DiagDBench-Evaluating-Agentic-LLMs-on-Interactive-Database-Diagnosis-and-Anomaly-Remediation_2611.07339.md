# DiagDBench: Evaluating Agentic LLMs on Interactive Database Diagnosis and Anomaly Remediation

- arXiv ID: `2611.07339v1`
- Authors: Xinxin Zhao, Rong Kang, Tieying Zhang, Cuiping Li, Hong Chen, Jing Zhang
- Published: 2026-11-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.07339v1) | [pdf](https://arxiv.org/pdf/2611.07339v1)

## Abstract

Database diagnosis and anomaly remediation are essential to reliable database management system (DBMS) operation. Despite advances in large language model (LLM)-based database agents, constructing live DBMS environments that reproduce diverse anomalies at scale remains challenging, limiting the availability of executable samples for database agent training and evaluation. To this end, we introduce DiagDBench, a large-scale benchmark for training and evaluating database agents on interactive diagnosis, anomaly remediation, and optional workload performance optimization across diverse, realistic anomaly scenarios. Each sample pairs a user request, comprising an issue description and an anomaly-verified workload under which the issue was observed, with a self-contained, executable DBMS environment that supports real-time monitoring, interactive diagnosis, remediation, and workload execution. To construct these samples at scale, we propose an LLM-based framework with two complementary pipelines: Manual-Guided Anomaly Synthesis, which sequentially synthesizes user requests, database modifications, and anomaly-injection scripts grounded in DBA manuals and official DBMS documentation; and Incident-Guided Anomaly Reproduction, which reconstructs anomaly samples end to end from real-world enterprise online diagnosis incidents. Built using this framework with sample filtering, expert review, and refinement, DiagDBench comprises 6,940 synthesized training samples and a held-out test set of 454 expert-annotated samples, spanning three hardware configurations, two DBMSs, and three database schemas. Extensive evaluations of database agents powered by multiple LLMs demonstrate that even the best-performing agent, ReAct with GPT-6 Astra, scores only 56.24, whereas most agents score below 45, underscoring the difficulty of DiagDBench.
