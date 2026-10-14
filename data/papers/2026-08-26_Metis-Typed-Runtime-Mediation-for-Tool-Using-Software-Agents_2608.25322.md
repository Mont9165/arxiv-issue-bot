# Metis: Typed Runtime Mediation for Tool-Using Software Agents

- arXiv ID: `2608.25322v1`
- Authors: Jun Yu
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25322v1) | [pdf](https://arxiv.org/pdf/2608.25322v1)

## Abstract

Software agents connect probabilistic model output to operations that change repositories, processes, networks, and graphical applications. We present Metis, a multi-provider runtime that converts provider streams into typed events before admitted calls reach external effects. Its execution path makes permission decisions, interference classes, terminal results, and lifecycle transitions explicit and inspectable. We evaluate these mechanisms on frozen source artifacts. Across 30 matched real-I/O pairs, four-class mediation reduced median elapsed time from 25.958 ms under forced serialization to 14.146 ms. The mean paired difference was -12.295 ms (95% bootstrap interval [-12.968, -11.694]), with mediation faster in all pairs. A ten-case fault matrix exposed duplicate-identifier and rollback limits. In a child-boundary ablation, the full gate-plus-registry condition blocked the declared unauthorized effect and hid all five escape tools. Removing both protections reversed both observations. A decision-only permission oracle matched all ten declared cases across five invocation routes. Five model conditions also completed a fixed Read-marker protocol in 3/3 trials each. These results support bounded claims about dispatch, permission routing, child authority, and provider-valid trace closure. They do not establish model competence, semantic safety, rollback, or superiority over another runtime.
