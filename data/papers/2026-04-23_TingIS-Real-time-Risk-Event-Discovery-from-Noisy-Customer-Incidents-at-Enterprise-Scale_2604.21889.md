# TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale

- arXiv ID: `2604.21889v1`
- Authors: Jun Wang, Ziyin Zhang, Rui Wang, Hang Yu, Peng Di, Rui Wang
- Published: 2026-04-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.21889v1) | [pdf](https://arxiv.org/pdf/2604.21889v1)

## Abstract

Real-time detection and mitigation of technical anomalies are critical for large-scale cloud-native services, where even minutes of downtime can result in massive financial losses and diminished user trust. While customer incidents serve as a vital signal for discovering risks missed by monitoring, extracting actionable intelligence from this data remains challenging due to extreme noise, high throughput, and semantic complexity of diverse business lines. In this paper, we present TingIS, an end-to-end system designed for enterprise-grade incident discovery. At the core of TingIS is a multi-stage event linking engine that synergizes efficient indexing techniques with Large Language Models (LLMs) to make informed decisions on event merging, enabling the stable extraction of actionable incidents from just a handful of diverse user descriptions. This engine is complemented by a cascaded routing mechanism for precise business attribution and a multi-dimensional noise reduction pipeline that integrates domain knowledge, statistical patterns, and behavioral filtering. Deployed in a production environment handling a peak throughput of over 2,000 messages per minute and 300,000 messages per day, TingIS achieves a P90 alert latency of 3.5 minutes and a 95\% discovery rate for high-priority incidents. Benchmarks constructed from real-world data demonstrate that TingIS significantly outperforms baseline methods in routing accuracy, clustering quality, and Signal-to-Noise Ratio.
