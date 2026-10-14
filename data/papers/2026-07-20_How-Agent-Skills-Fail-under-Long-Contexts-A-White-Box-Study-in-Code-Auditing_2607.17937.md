# How Agent Skills Fail under Long Contexts: A White-Box Study in Code Auditing

- arXiv ID: `2607.17937v1`
- Authors: Yue Xue
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17937v1) | [pdf](https://arxiv.org/pdf/2607.17937v1)

## Abstract

Agent Skills package procedural instructions and checks for use by general-purpose agents, but loading a skill does not guarantee that every requirement remains active throughout a long tool-using trajectory. We study this problem in a production-derived, white-box code-audit workflow. Holding the task and 24 artifact checks fixed, we vary the surrounding context and classify where failures first become visible: lost requirements, editing drift, failed checking, or non-agent evaluator/runtime failures. Codex with gpt-5.4-mini passes 8/10 runs in a 10,991-character clean context but only 3/10 in both a 299,140-character relevant context and an equal-length irrelevant context. This 50-percentage-point difference is large but remains trend-level under two-sided Fisher tests (p = 0.0698). Requirement coverage nevertheless stays above 92% in both long conditions, showing that a few omissions can invalidate an otherwise complete artifact. A second task passes all clean and long runs, so the evidence does not support a universal context-length threshold. A detailed external checklist passes 10/10 runs, compared with 5/10 for a generic self-check (p = 0.0325). Coding-agent scaffolds may help by selecting a smaller working set, but they do not eliminate failures. We do not introduce context rot or a new general monitoring method; we provide a bounded failure classification and empirical case study for white-box code auditing.
