# Specification-Driven DevOps for Multi-Service Environments

- arXiv ID: `2607.25141v1`
- Authors: Oleg Grynets, Kyrylo Fursov, Vasyl Lyashkevych, Volodymyr Veres
- Published: 2026-07-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LO`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2607.25141v1) | [pdf](https://arxiv.org/pdf/2607.25141v1)

## Abstract

Large Language Models (LLMs) are increasingly used to generate executable software environments from repository artifacts. However, functional executability does not necessarily imply conformity with architectural, security, workflow, and production intent. This study investigates whether a frontier LLM can generate Dockerfiles and Docker Compose configurations for multi-service applications using repository contents without access to developer-authored deployment artifacts. Three heterogeneous repositories combining Python, Node.js, .NET, React, Rust, Java, Redis, PostgreSQL, and MySQL-compatible infrastructure were evaluated using deterministic end-to-end HTTP oracles and manual structural comparison. All three generated environments became functionally operational, although one required a Rust base-image update from version 1.85 to 1.88. The model correctly reconstructed service topology, application ports, infrastructure dependencies, service hostnames, a background worker, hidden proxy configurations, and a file-based Docker secrets mechanism. However, it consistently omitted network segmentation, multi-stage builds, dependency-layer caching, live-reload volumes, production frontend serving, restrictive backend-port policies, and cross-platform build logic. Based on these observations, the study formalizes the distinction between functional correctness and deployment-intent fidelity and analytically derives a minimal explicit deployment specification for information that cannot be reliably inferred from repository artifacts.
