# Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities

- arXiv ID: `2607.12723v1`
- Authors: Qiyuan Fan, Zhi Li, Junjie Li, XiaoFeng Wang, Bin Yuan, Deqing Zou
- Published: 2026-07-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12723v1) | [pdf](https://arxiv.org/pdf/2607.12723v1)

## Abstract

Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore not been accepted into the Linux mainline. Detection methods rely on static rule matching or manual code auditing. Static rules can flag path-related functions but fail to capture the semantics needed to determine whether a host-container interaction exists, causing many false positives. Manual review requires domain expertise, making it costly, inefficient, and difficult to scale.
  To address this threat, we present Bulkhead, an automated framework that integrates large language models (LLMs) with formal methods for semantic vulnerability discovery and remediation. Bulkhead uses a multi-agent system to identify and repair PaTra vulnerabilities through multi-dimensional knowledge patterns generalized from known cases. It first applies high-risk functional patterns to locate entry points for cross-boundary interactions in containerized code, then uses call-chain patterns to recover the corresponding execution paths at suitable depth. The Detection pipeline analyzes these call chains against the application scenarios and threat model, identifying vulnerabilities such as missing security checks and TOCTOU flaws in cross-boundary interactions, and generating proof-of-concept (PoC) exploits for validation. These PoCs then guide patch generation. To ensure remediation correctness, the Patch pipeline performs assertion-driven verification using predefined model-checking templates.
