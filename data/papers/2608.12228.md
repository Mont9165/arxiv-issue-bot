# Towards Automated Domain Model Extraction from Source Code using Heuristics and Open-Source LLMs

- arXiv ID: `2608.12228v1`
- Authors: Alessandra Mancas, Mounir Ammam, Hyacinth Ali, Kevin Delcourt, Houari Sahraoui
- Published: 2026-08-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.12228v1) | [pdf](https://arxiv.org/pdf/2608.12228v1)

## Abstract

Large language models (LLMs) have recently shown strong capabilities for code understanding, making them promising for reverse engineering domain models from source code. However, state-ofthe- art proprietary LLMs cannot be used in many industrial contexts due to privacy and confidentiality constraints, while compact open-source LLMs that can run locally are limited by their context window and cannot process large code bases directly. In this paper, we propose an automated approach to extract domain models from source code using lightweight, locally deployable LLMs. Our method combines structural and semantic heuristics with iterative LLM-based reasoning to overcome context limitations. By progressively analyzing ranked subsets of code elements, the approach identifies domain concepts and refines domain boundaries without requiring full-system context. Our approach achieves high F1-scores on a dataset of ten projects, each comprising a curated domain model and its corresponding implementation, while remaining fully executable on locally deployable LLMs. This makes it particularly suitable for reverse engineering tasks in privacy-sensitive industrial environments.
