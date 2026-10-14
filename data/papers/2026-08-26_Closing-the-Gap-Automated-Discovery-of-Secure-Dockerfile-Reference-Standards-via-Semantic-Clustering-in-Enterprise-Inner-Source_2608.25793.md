# Closing the Gap: Automated Discovery of Secure Dockerfile Reference Standards via Semantic Clustering in Enterprise Inner Source

- arXiv ID: `2608.25793v1`
- Authors: Jessica Hösl, Benedikt Hofmann, Patrick Stöckle
- Published: 2026-08-26
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25793v1) | [pdf](https://arxiv.org/pdf/2608.25793v1)

## Abstract

Containerization dominates enterprise software delivery, yet Dockerfiles that assemble container images frequently harbor security misconfigurations and structural technical debt. This problem is poorly understood in corporate inner-source environments, where proprietary context and isolated governance prevent direct application of open-source findings.
  We present an automated, six-stage pipeline that: (1) crawls an enterprise GitLab instance, (2) enriches each Dockerfile with static security and quality metrics (Hadolint, ShellCheck, Trivy) and lifecycle data, (3) groups functionally identical workloads using LLM-generated semantic descriptions and HDBSCAN, and (4) quantifies the optimization gap against cluster-internal reference implementations.
  Applied to 11,470 Dockerfiles from over 6,200 repositories at a single large industrial company, we find a systemic deficit: 99\% of files contain at least one security misconfiguration, 80.8\% violate Dockerfile best practices, and the median artifact has not been revised for 838~days. Despite this, high-quality reference implementations already exist within 83\% of functional clusters. Adopting these internal standards would increase the average security posture score by 60.4\% without developing any new templates. These findings, grounded in one organization's inner-source ecosystem, provide a data-driven foundation for future automated, context-aware recommender systems targeting enterprise supply-chain security; whether the observed technical-debt distribution and optimization gap generalize to other enterprises remains an open question for future multi-organization study.
