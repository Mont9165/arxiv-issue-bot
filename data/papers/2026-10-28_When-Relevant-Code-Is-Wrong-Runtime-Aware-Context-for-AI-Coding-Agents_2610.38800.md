# When Relevant Code Is Wrong: Runtime-Aware Context for AI Coding Agents

- arXiv ID: `2610.38800v1`
- Authors: Wesley K. G. Assunção, Ramesh Periyathambi
- Published: 2026-10-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.38800v1) | [pdf](https://arxiv.org/pdf/2610.38800v1)

## Abstract

AI coding agents increasingly rely on retrieved code and development history to guide software changes. However, highly relevant artifacts may describe implementations that are inactive or incompatible with the target deployment. Neither semantic similarity nor recency establishes whether retrieved information remains applicable under feature flags, architectural migrations, and deployment-specific configurations. We challenge relevance-oriented retrieval by introducing operational context validity, a task-, deployment-, and time-dependent criterion for determining whether software evidence can legitimately guide implementation decisions. We instantiate this new retrieval principle in CASE, an agent-agnostic framework that connects repository artifacts with runtime configurations and architectural evolution, classifies evidence as valid, invalid, or unknown, and generates context packages distinguishing actionable guidance from historical rationale and unresolved constraints. We investigate its feasibility through a reproducible preliminary evaluation involving six development tasks, 15 artifacts, and three deployments. Conventional retrieval exposes 16 incompatible artifact occurrences as actionable, whereas CASE excludes them while retaining all applicable artifacts under the prototype's reference rules. Recency filtering reduces valid recall to 0.43, while removing feature-flag evidence from CASE reduces it to 0.13. Although these results demonstrate feasibility rather than improvements in coding-agent correctness, they reveal limitations of relevance-based retrieval and motivate a new research direction: enabling coding agents to reason not only about which information is relevant, but also whether it remains operationally valid.
