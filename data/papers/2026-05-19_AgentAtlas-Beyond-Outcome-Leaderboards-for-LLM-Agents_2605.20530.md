# AgentAtlas: Beyond Outcome Leaderboards for LLM Agents

- arXiv ID: `2605.20530v1`
- Authors: Parsa Mazaheri, Kasra Mazaheri
- Published: 2026-05-19
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.20530v1) | [pdf](https://arxiv.org/pdf/2605.20530v1)

## Abstract

Large language model agents now act on codebases, browsers, operating systems, calendars, files, and tool ecosystems, but the benchmarks used to evaluate them are fragmented: each emphasizes a different unit of measurement (final task success, tool-call validity, repeated-pass consistency, trajectory safety, or attack robustness). A line of 2024-2025 work has converged on the diagnosis that a single accuracy column is no longer the right unit of comparison for deployable agents. AgentAtlas extends this line of work with four components: (i) a six-state control-decision taxonomy (Act / Ask / Refuse / Stop / Confirm / Recover); (ii) a nine-category trajectory-failure taxonomy with two orthogonal hierarchical labels (primary_error_source, impact); (iii) a taxonomy-aware vs. taxonomy-blind methodology that measures how much of a model's apparent capability comes from the supervision in the prompt; and (iv) a benchmark-coverage audit mapping fifteen agent benchmarks against six behavioral axes. To demonstrate the methodology we run a small fixed eight-model set (1,342 generated items, four frontier closed and four open-weight) under both prompt modes. Removing the explicit label menu drops every model's trajectory accuracy by 14-40 pp to a tight 0.54-0.62 floor regardless of family, and no single model wins on all three of control accuracy, trajectory diagnosis, and tool-context utility retention. We treat the synthetic run as a measurement-protocol demonstration, not a benchmark release.
