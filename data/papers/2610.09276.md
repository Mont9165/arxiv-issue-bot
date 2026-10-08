# CATune: Structural Constraint-Aware Bayesian Optimization for DBMS Configuration Tuning

- arXiv ID: `2610.09276v1`
- Authors: Fangping Lan, Qi Zhang, Eduard Dragut
- Published: 2026-10-07
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.09276v1) | [pdf](https://arxiv.org/pdf/2610.09276v1)

## Abstract

Modern DBMSs expose hundreds of configuration knobs, resulting in a high-dimensional and heterogeneous search space that makes automated tuning costly. Existing ML-based tuning systems typically treat the configuration domain as box-constrained and rely on workload feedback to implicitly capture inter-knob relationships. However, DBMS documentation specifies deterministic knob dependency constraints, particularly ordering constraints, that characterize structurally valid regions of the configuration space. We present CATune, a constraint-aware Bayesian optimization (BO) framework that models deterministic inter-knob ordering constraints as structural components of the search domain. Instead of learning feasibility boundaries through sampled violations, CATune performs optimization within a constraint-consistent subspace. We develop a topology-aware sampling strategy that respects dependency structure during exploration and avoids the inefficiencies of post-hoc constraint handling. To enable automated constraint discovery, we further design a precision-first extraction pipeline that combines LLM-based parsing with reliability safeguards to mitigate hallucinated dependencies. Experiments on PostgreSQL and MySQL using TPC-C and TPC-H workloads show that CATune substantially improves both sample efficiency and final tuning quality across surrogate models and BO frameworks. Under default ranges, CATune reaches the baseline optimum up to 12.5x faster and improves throughput by up to 63.37%. The improvements persist under knowledge-guided reduced ranges and alternative optimization implementations. These results demonstrate that explicitly modeling system-defined deterministic ordering constraints enhances optimization robustness and system stability.
