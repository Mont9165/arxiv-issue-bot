# Real-time SQL Plan Management in Oracle

- arXiv ID: `2608.27758v1`
- Authors: Sunil Chakkappen, Mohamed Ziauddin, Hong Su, Shreya Kunjibettu, Nigel Bayliss
- Published: 2026-08-27
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.27758v1) | [pdf](https://arxiv.org/pdf/2608.27758v1)

## Abstract

Consistent query performance is essential for mission critical database applications, yet SQL execution plans can change due to factors such as database upgrades, DML changes, new indexes, etc. While plan stability mechanisms such as stored outlines prevent regressions by freezing execution plans, they also inhibit performance improvements by disallowing plan evolution. We introduced SQL Plan Management (SPM) in Oracle 11g to address this trade-off by maintaining a set of accepted execution plans and allowing plan evolution only when new plans demonstrably outperform existing baselines. However, prior implementations of SPM primarily rely on background performance verification processes, delaying regression detection and recovery. This issue is amplified in autonomous cloud database systems, where several automatic actions that could cause plan change driven regressions are performed with limited customer control. Timely detection and remediation is paramount, but the constrained background resources on cloud may not keep pace. To overcome these limitations, we introduce Real-Time SPM in Oracle 26ai, a novel extension of SPM that performs foreground verification of new execution plans during user query execution. Real-Time SPM leverages runtime session context to immediately validate plan changes, enabling rapid adoption of superior plans while promptly detecting and preventing regressions. This paper presents the architecture and design of Real-Time SPM - including technical challenges like reliably comparing performance of previous plans - and contrasts it with traditional background plan evolution.
