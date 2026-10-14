# Building a Process-Modeling Tool using Agentic AI: An Experience Report on PM4Py-UCM

- arXiv ID: `2607.28825v1`
- Authors: Daniel Amyot
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.28825v1) | [pdf](https://arxiv.org/pdf/2607.28825v1)

## Abstract

Enterprise-modeling (EM) tools are often complex and hard to extend. Yet, users may want to explore new EM features and capabilities that currently do not exist. AI coding agents can help here by enabling the development of new capabilities and entire tools, but whether we can trust a modeling-language tool an LLM largely wrote remains a question. This paper reports on the AI-assisted construction of PM4Py-UCM, an open-source tool that mines Use Case Map (UCM) models from event logs. PM4Py-UCM's capabilities include some expected from process mining tools (e.g., performance heat-maps and dashboards) and distinctive ones (e.g., mined executable scenarios/variants, and model decomposition). We mined the development record itself, composed of 18 agent sessions (374 human turns and 10,328 tool actions over 65 hours), 151 commits, 20 releases, and a test suite grown from 108 to 691 test functions, in order to characterize, in a single in-depth case, how the tool was built with an agent (Claude Code), complemented by an independent static assessment of the resulting code (coverage, complexity, maintainability, security, architecture). We contribute a reproducible, privacy-preserving toolkit and taxonomy that classify human turns and flag cross-cutting consistency work, agent corrections, and retracted requests. Up to version 0.7.4, fixes outnumber features 2.3:1, with ~18% of turns for correcting agent errors. Feature waves dragged a measurable tail of documentation/test/notebook consistency work, and tests grew lockstep with features. We finally present lessons learned, centered on making model transformations mechanically checkable, and the oracle-based validation strategy that closed the "the agent said it works" gap, for responsibly engineering EM tooling with AI.
