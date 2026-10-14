# From Assistance to Agency: Rethinking Autonomy and Control in CI/CD Pipelines

- arXiv ID: `2605.07062v1`
- Authors: Marcus Emmanuel Barnes, Taher A. Ghaleb, Safwat Hassan
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.07062v1) | [pdf](https://arxiv.org/pdf/2605.07062v1)

## Abstract

AI agents are assuming active roles in Continuous Integration and Continuous Deployment (CI/CD) workflows, yet the research community lacks a shared vocabulary for describing what it means for CI/CD to be agentic, how much decision authority is delegated, and where control should reside. This paper presents a vision of agentic CI/CD in which the central challenge is not improving task performance but designing authority transfer, defined as the delegation of operational decisions from human-controlled pipelines to agent systems under specified constraints and recourse mechanisms.
  To structure this argument, we introduce a distinction between data-plane authority (localized interventions such as patch generation and test reruns) and control-plane authority (modifications to pipeline configuration, deployment policies, and approval gates). Drawing on research prototypes and industrial platforms, we show that current systems operate mainly at the data plane under bounded autonomy, with safety achieved through surrounding governance infrastructure rather than intrinsic agent guarantees. We identify three recurring patterns: constrained autonomy as the dominant design, external governance as the primary safety mechanism, and a widening gap between deployment momentum and evaluation methodology. We propose a research agenda in which control-plane safety and governance mechanisms represent the most urgent open problem, followed by formalization of autonomy boundaries, evaluation frameworks, and human--agent coordination.
