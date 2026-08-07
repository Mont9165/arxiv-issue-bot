# WebDesignIter: Co-Evolving Design Knowledge for Repository-Level Front-End Code Generation

- arXiv ID: `2607.10621v1`
- Authors: Zheng Pei, Mingwei Liu, Zhenxi Chen, Zihao Wang, Yanlin Wang
- Published: 2026-07-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.10621v1) | [pdf](https://arxiv.org/pdf/2607.10621v1)

## Abstract

Front-end development accumulates change after change at the repository level, weaving complex cross-file dependencies that current LLM coding agents tuned for single-shot tasks cannot reliably track across multiple iterations, leading to functional regressions and code that resists maintenance. We argue the missing piece is design knowledge: architectural principles, module responsibilities, and structural constraints that developers lean on to keep code readable, maintainable, and evolvable as a system scales. To operationalize this, we propose WebDesignIter, a framework built around a persistent knowledge graph (WebAppArchKG) that fuses repository structure with design knowledge and keeps both in sync across development cycles. WebDesignIter works in two stages: design-informed planning pulls historical context and architectural overviews from WebAppArchKG to produce an implementation plan with corresponding test scripts, and design-aware generation executes that plan through targeted diff-based patches, validated by sandbox execution and automatic syntax repair. On Web-Bench, WebDesignIter delivers an average Pass@2 gain of 9.55 percentage points across nine foundation models over existing baselines. More importantly, WebDesignIter outperforms every general-purpose coding agent Claude Code, OpenHands, SWE-Agent, Codex CLI on every model configuration, posting the highest Pass@1 and Pass@2 while consuming 2530 fewer input tokens. Ablation singles out design knowledge as the most impactful component: stripping it drops Pass@1 by 11.40 percentage points, a degradation far larger than removing code-graph retrieval, patch-based generation, or sandbox verification, confirming that design knowledge provides a fundamentally more efficient and reliable path to repository-level code generation.
