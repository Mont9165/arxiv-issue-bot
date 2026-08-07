# Understanding Developer Pain Points in Federated Learning: Insights from Stack Overflow and GitHub

- arXiv ID: `2607.19621v1`
- Authors: Sahand Saed, Khairul Alam, Banani Roy
- Published: 2026-07-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.19621v1) | [pdf](https://arxiv.org/pdf/2607.19621v1)

## Abstract

Federated Learning (FL) enables collaborative model training without centralizing raw data, but building and operating FL systems remains difficult due to distributed execution, rapidly evolving frameworks, and privacy and governance requirements. In this paper, we present an empirical study of FL developer challenges by independently analyzing 495 Stack Overflow posts and 9,116 GitHub issues and pull requests from 92 FL-related projects. Using BERTopic-based topic modeling and difficulty indicators such as unresolved rates and median resolution time, we characterize recurring problem areas and compare how they manifest across the two support platforms, Stack Overflow and GitHub. Our analysis surfaces nine dominant Stack Overflow topics and thirteen GitHub topics, with persistent difficulties concentrated in environment setup and dependency compatibility, API breakages and migration, training instability under non-IID data, evaluation and metric correctness, and the integration of privacy-preserving mechanisms. We also categorize posts by question intent to understand the kinds of help developers seek; this intent analysis shows that "How"-type questions dominate, reflecting strong demand for procedural guidance. Several topics, such as "TFF Installation and Environment Compatibility" and "Federated Feature Engineering and SecureBoost Issues," exhibit high unresolved rates and long resolution times, suggesting shortcomings in tooling, documentation, and debugging support. Based on these findings, we provide actionable implications for FL framework designers, documentation authors, and educators. Although our results are constrained to public discussions and a subset of widely discussed frameworks, the study offers a scalable method for continuously monitoring developer pain points and improving the usability, reliability, and deployability of FL systems.
