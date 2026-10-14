# Delta Debugging for Cyber-Physical Systems with Flaky Test Executions

- arXiv ID: `2607.25695v1`
- Authors: Pablo Valle, Shaukat Ali, Aitor Arrieta
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25695v1) | [pdf](https://arxiv.org/pdf/2607.25695v1)

## Abstract

Simulation-based testing is widely used to validate Cyber-Physical Systems (CPSs), yet modern CPS simulators frequently exhibit non-deterministic (flaky) behavior, making failures difficult to reproduce and debug. Although delta debugging has proven effective for deterministic systems, its underlying assumptions do not hold in stochastic environments. This paper presents three delta debugging algorithms that combine statistical failure analysis, repeated executions, and environment-aware reduction to isolate minimal failure-inducing test inputs for stochastic CPSs. We evaluate the proposed techniques on two complementary case study systems: an industrial elevator dispatching system employing stochastic optimization and an autonomous mobile robot exhibiting simulator-induced non-determinism. The results show that the proposed approaches substantially reduce debugging time while preserving the original failure behavior. More importantly, we observe that minimizing failure-inducing test inputs frequently increases failure reproducibility compared with the original executions. By eliminating execution segments that introduce incidental stochastic effects, the reduced test inputs isolate the causal conditions of the failure and consistently reproduce it with higher probability. These findings suggest that delta debugging not only simplifies failure analysis but also mitigates execution flakiness, providing a practical foundation for debugging CPSs.
