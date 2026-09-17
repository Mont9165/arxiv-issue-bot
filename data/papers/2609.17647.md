# CARE: A Responsibility-Oriented Architecture for Domain-Scoped Resolution in Modular and Upgradeable Smart Contracts

- arXiv ID: `2609.17647v1`
- Authors: Ali Rajabi Nekoo, Laleh Rasoul, Azadeh Zamanifar
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.17647v1) | [pdf](https://arxiv.org/pdf/2609.17647v1)

## Abstract

Modular and upgradeable smart-contract systems enable replaceable execution logic, but modular dispatch alone does not define which components own architectural responsibilities such as coordination, resolution, shared state, reusable services, and observation. This paper presents CARE, a responsibility-oriented architecture that makes these ownership boundaries explicit and introduces domain-scoped capability resolution, separating execution coordination from the authority that selects an execution target. CARE is defined through a formal architectural model from which five structural properties are derived. Its behavioral semantics are further encoded in TLA+ and evaluated with TLC against seven architectural invariants. Intermediate TLC results were used to refine the architectural model before the final validation run. A controlled empirical evaluation against EIP-2535 and a routing only baseline shows that CARE introduces an approximately fixed 7.7k-gas runtime routing premium in the evaluated workloads, while localized capability replacement remains close to the routing-only control and substantially less expensive than the evaluated EIP-2535 reconfiguration path. Adversarial tests further characterize authorization controls and residual risks associated with delegated execution and reentrancy. These results position CARE as an architectural model for explicit responsibility ownership and localized evolution rather than as a universal replacement for existing smart-contract upgradeability mechanisms
