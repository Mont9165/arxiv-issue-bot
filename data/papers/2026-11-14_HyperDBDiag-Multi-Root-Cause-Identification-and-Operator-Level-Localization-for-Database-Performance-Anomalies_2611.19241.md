# HyperDBDiag: Multi-Root-Cause Identification and Operator-Level Localization for Database Performance Anomalies

- arXiv ID: `2611.19241v1`
- Authors: Hu Wang, Zhengjin Yan, Hong Zhu, Qiong Zuo
- Published: 2026-11-14
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.19241v1) | [pdf](https://arxiv.org/pdf/2611.19241v1)

## Abstract

Database performance anomalies in modern production environments are not always triggered by a single cause. Instead, they often arise from the concurrent interaction of multiple causes within the same time window, posing substantial challenges to accurate operator-level root-cause analysis. When multiple root causes interact through shared resources, metric anomalies may be amplified, attenuated, or masked. Consequently, salient local anomalies may no longer correspond directly to the actual root causes, making conventional single-path diagnosis and shallow correlation-based methods prone to misdiagnosis. To address this challenge, we propose HyperDBDiag, a method for multi-root-cause identification and operator-level localization of database performance anomalies. HyperDBDiag connects root causes, performance metrics, SQL templates, and execution operators in a knowledge graph, captures joint anomaly patterns across metrics with a metric hypergraph, and uses a constrained LLM to determine the final root-cause set and provide remediation suggestions. When finer-grained localization is possible, HyperDBDiag also identifies the associated anomalous SQL statements and execution operators. We evaluate HyperDBDiag on a database performance anomaly dataset constructed using DB-MAGS. Experimental results show that HyperDBDiag effectively reduces graph complexity while improving root-cause localization accuracy.
