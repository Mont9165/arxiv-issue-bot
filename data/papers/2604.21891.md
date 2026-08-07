# A Multi-Stage Warm-Start Deep Learning Framework for Unit Commitment

- arXiv ID: `2604.21891v1`
- Authors: Muhy Eddin Za'ter, Anna Van Boven, Bri-Mathias Hodge, Kyri Baker
- Published: 2026-04-23
- Primary category: `eess.SY`
- Categories: `eess.SY`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21891v1) | [pdf](https://arxiv.org/pdf/2604.21891v1)

## Abstract

Maintaining instantaneous balance between electricity supply and demand is critical for reliability and grid instability. System operators achieve this through solving the task of Unit Commitment (UC),ca high dimensional large-scale Mixed-integer Linear Programming (MILP) problem that is strictly and heavily governed by the grid physical constraints. As grid integrate variable renewable sources, and new technologies such as long duration storage in the grid, UC must be optimally solved for multi-day horizons and potentially with greater frequency. Therefore, traditional MILP solvers increasingly struggle to compute solutions within these tightening operational time limits. To bypass these computational bottlenecks, this paper proposes a novel framework utilizing a transformer-based architecture to predict generator commitment schedules over a 72-hour horizon. Also, because raw predictions in highly dimensional spaces often yield physically infeasible results, the pipeline integrates the self-attention network with deterministic post-processing heuristics that systematically enforce minimum up/down times and minimize excess capacity. Finally, these refined predictions are utilized as a warm start for a downstream MILP solver, while employing a confidence-based variable fixation strategy to drastically reduce the combinatorial search space. Validated on a single-bus test system, the complete multi-stage pipeline achieves 100\% feasibility and significantly accelerates computation times. Notably, in approximately 20\% of test instances, the proposed model reached a feasible operational schedule with a lower overall system cost than relying solely on the solver.
