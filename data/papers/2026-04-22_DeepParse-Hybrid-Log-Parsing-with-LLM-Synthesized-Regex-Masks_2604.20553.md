# DeepParse: Hybrid Log Parsing with LLM-Synthesized Regex Masks

- arXiv ID: `2604.20553v1`
- Authors: Amir Shetaia, Sean Kauffman
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20553v1) | [pdf](https://arxiv.org/pdf/2604.20553v1)

## Abstract

Modern distributed systems produce massive, heterogeneous logs essential for reliability, security, and anomaly detection. Converting these free-form messages into structured templates (log parsing) is challenging due to evolving formats and limited labeled data. Machine-learning-based parsers like Drain are fast but accuracy often degrades on complex variables, while Large Language Models (LLMs) offer better generalization but incur prohibitive inference costs. This paper presents DeepParse, a hybrid framework that automatically mines reusable variable patterns from small log samples using an LLM, then applies them deterministically through the Drain algorithm. By separating the reasoning phase from execution, DeepParse enables accurate, scalable, and cost-efficient log structuring without relying on brittle handcrafted rules or per-line neural inference. Across 16 benchmark datasets, DeepParse achieves higher accuracy in variable extraction (97.6% average Parsing Accuracy) and better consistency than both heuristic and LLM-only baselines. Integrating DeepParse into an anomaly detection pipeline reduced false alarms by over 30% and reduced inference latency by 36% compared to heuristic baselines.
