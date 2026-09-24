# Kubernetes Misconfigurations in the Wild: Taxonomy, Evolution, and Automated Repair with Large Language Models

- arXiv ID: `2609.27030v1`
- Authors: Mostafa Anouar Ghorab, Ahmad Abdel Latif, Mohamed Aymen Saied
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.27030v1) | [pdf](https://arxiv.org/pdf/2609.27030v1)

## Abstract

Kubernetes is widely used to orchestrate cloud-native applications, yet its declarative configuration model often introduces security misconfigurations that threaten system reliability. Despite available detection tools, misconfiguration patterns and scalable remediation remain insufficiently understood.
  This paper presents an empirical study of Kubernetes security misconfigurations based on 2,662 developer-reported Stack Overflow issues. We derive a taxonomy of recurring security weaknesses across configuration objects and categories. We analyze severity variations and investigate how misconfigurations evolve between incubator and stable project stages. Findings show that while some operational issues decrease as projects mature, critical security misconfigurations often persist or reappear.
  We then evaluate Large Language Models (LLMs) for automated remediation under progressively enriched contextual conditions. Contextual grounding improves correction accuracy, with the best standalone model achieving 89.06%. To enhance structural correctness and schema compliance, we introduce Kubecurity, a schema-guided validation framework based on official Kubernetes specifications. Combining contextual LLM reasoning with deterministic schema enforcement achieves 98.50% correction accuracy while substantially reducing newly introduced misconfigurations.
  This work advances the understanding of Kubernetes security misconfigurations and demonstrates a hybrid approach to more reliable automated remediation.
