# Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda

- arXiv ID: `2608.21107v1`
- Authors: Wei Lin, Tao Zhou, Zhaofei Xie, Changgui Hong
- Published: 2026-08-21
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.21107v1) | [pdf](https://arxiv.org/pdf/2608.21107v1)

## Abstract

Large Language Models (LLMs) are moving from code completion toward repository-scale agents that retrieve context, edit files, execute tools, and participate in security-sensitive workflows. The evidence for these systems, however, remains divided between software engineering evaluations centered on functional task completion and software security evaluations centered on vulnerability detection, secure generation, or exploit-oriented validation. This evidence-centered structured survey synthesizes representative work available through May 31, 2026 across software engineering tasks, software security tasks, adaptation mechanisms, artifact granularity, and evaluation design. In addition to a task taxonomy, we introduce an assurance framework that separates functional correctness, security, operational reliability, evidence provenance, and agent authority. The review shows that execution feedback and repository access can substantially improve engineering task completion, but do not by themselves establish security; conversely, static-analysis labels or vulnerability-classification scores rarely establish deployable correctness. We identify recurring validity threats--weak test oracles, duplicated and temporally leaked data, changing agent harnesses, proxy-only security checks, and under-reported budgets and human intervention--and derive a minimum reporting protocol for cross-study comparison. The resulting research agenda prioritizes jointly secure-and-functional benchmarks, repository-scale threat models, calibrated human oversight, longitudinal maintainability evidence, and reproducible agent evaluation. The central conclusion is that model capability should be judged as an assurance case supported by task-appropriate evidence, rather than by a single benchmark score.
