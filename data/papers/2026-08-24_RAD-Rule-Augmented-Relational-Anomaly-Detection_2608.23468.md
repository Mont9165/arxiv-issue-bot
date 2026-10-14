# RAD: Rule-Augmented Relational Anomaly Detection

- arXiv ID: `2608.23468v1`
- Authors: Noah Dahle, Anne Tumlin, Ngoc Tran, Xenofon Koutsoukos, Tyler Derr
- Published: 2026-08-24
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.23468v1) | [pdf](https://arxiv.org/pdf/2608.23468v1)

## Abstract

Anomaly detection is often applied to data stored in relational databases, yet most existing methods require flattening multiple tables into a single feature matrix. This flattening can obscure entity identity, schema structure, and multi-hop dependencies, limiting the detection of anomalies that depend on relational context rather than isolated feature values. Beyond preserving relational structure, relational anomaly detection raises an additional challenge: how to incorporate symbolic behavioral evidence into learned relational representations. To address these challenges, we study relational anomaly detection, where the goal is to identify anomalous entities or events in a multi-table database. We propose RAD, a rule-augmented relational anomaly detector that combines heterogeneous graph representation learning with refined symbolic rule signals. RAD derives candidate rules from random-forest paths over flattened summaries of the entities or events being scored, refines them into compact interpretable predicates, injects the resulting rule features into the graph model, and learns anomaly scores using reconstruction-based and pairwise-ranking supervision. To evaluate this setting, we introduce a relational anomaly detection benchmark spanning three settings: LANL cybersecurity event detection and two unexpected user-churn anomaly tasks derived from Amazon and H&M relational databases. Experiments show that RAD improves anomaly ranking over flattened tabular detectors and relational baselines under natural class imbalance, achieving the best average rank on AUROC and AUPRC across the benchmark. Ablations show that direct rule injection and ranking-based supervision are key contributors to performance, while edge reconstruction is not uniformly beneficial. Our code and data are available at: https://github.com/noahd15/RAD_RelationalAnomalyDetection.
