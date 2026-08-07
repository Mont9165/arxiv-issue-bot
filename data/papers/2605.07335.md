# CellScientist: Dual-Space Hierarchical Orchestration for Closed-Loop Refinement of Virtual Cell Models

- arXiv ID: `2605.07335v1`
- Authors: Mengran Li, Bo Li, Jiaying Wang, Wenbin Xing, Yixuan Dong, Chengyang Zhang, Hongliang Zhang, Yuzhong Peng, Jinlin Wu, Bob Zhang, Bingo Wing-Kuen Ling, Fuji Yang, Zhen Lei, Jiebo Luo, Zelin Zang
- Published: 2026-05-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07335v1) | [pdf](https://arxiv.org/pdf/2605.07335v1)

## Abstract

Virtual Cell Modeling (VCM) requires models that not only predict perturbation responses, but also support targeted revision when predictions fail. Current LLM-assisted modeling workflows face a refinement-routing problem: prediction discrepancies are observed through executable implementations, but the relevant revision may involve the modeling assumption, representation design, implementation, or task constraint. Without structured feedback propagation across these levels, iterative refinement may repair code while failing to revise the assumption responsible for the discrepancy. We propose CellScientist, a dual-space hierarchical framework that couples a high-level hypothesis space with a low-level executable implementation space. CellScientist represents modeling decisions as structured states, realizes them as admissible programs under task and interface constraints, and routes execution discrepancies back to targeted hypothesis or implementation updates. This enables a closed Hypothesis -> Implementation -> Hypothesis loop where failures become structured signals for model refinement rather than debugging events. Across morphology and transcriptomic benchmarks, with additional single-cell perturbation evaluations, the final executable models selected by CellScientist improve over reference baselines under fixed split and evaluation protocols, while the workflow produces auditable refinement traces.
