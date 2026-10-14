# Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply Chains

- arXiv ID: `2607.01136v1`
- Authors: Changguo Jia, Tianqi Zhao, Runzhi He, Minghui Zhou
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.01136v1) | [pdf](https://arxiv.org/pdf/2607.01136v1)

## Abstract

Agent skills package reusable operational knowledge for Large Language Model (LLM) agents, yet as they grow in scope, they become dependency-bearing artifacts whose identities, versions, and provenance remain implicit. This opacity already causes duplicated dependencies and inconsistent installations, exposing a gap that dependency management has yet to close. We introduce Agent Skill Supply Chains (ASSCs) to characterize mixed skill-package-service dependency graphs and help close this gap. Borrowing from Software Bill of Materials (SBOMs), we design SkillDepAnalyzer to capture natural-language dependency evidence and model skills as dependency-bearing artifacts. On the SKILL-DEP benchmark, SkillDepAnalyzer recovers skill metadata and dependency graphs accurately and comprehensively, substantially outperforming an LLM-based baseline and package-centric SBOM tools. Applying SkillDepAnalyzer to over 1.43 million skills, we obtain ASSCs and explore their structural diversity and security signals. We find four structural patterns: skill metadata is activation-ready but governance-poor; dependency graphs span skill, package, and service dependencies with concentrated reuse; recursive skill reuse expands dependency graphs and creates hidden package inventory; and skill dependency clusters form around related workflows. We also find that inspecting a skill alone misses security-relevant signals hiding in its dependencies. By analyzing ASSCs, we identify and report known malicious skills persisting in ASSCs to their developers. Based on these findings, we recommend typed dependency manifests, first-class dependency-cluster management, risk-warning audit commands for skill infrastructure maintainers, and lockfile-like records for skill developers.
