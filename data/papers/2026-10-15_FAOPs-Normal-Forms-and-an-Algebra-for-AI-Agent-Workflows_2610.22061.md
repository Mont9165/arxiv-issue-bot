# FAOPs: Normal Forms and an Algebra for AI Agent Workflows

- arXiv ID: `2610.22061v1`
- Authors: Ali Mohammadi Shanghooshabad
- Published: 2026-10-15
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.22061v1) | [pdf](https://arxiv.org/pdf/2610.22061v1)

## Abstract

Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory. Yet AOPs are typically kept as coarse-grained files, in which steps bundle actions, copied procedures drift apart, any step may reach any tool, and refactoring goes unchecked. We present Functional Agent Operating Procedures (FAOP), a formal theory that brings database-grade discipline to AI agent workflows. FAOP recasts each workflow as a typed function over scoped state and subjects an entire library to four progressive normal forms: Decomposed (FNF-1) splits a workflow into atomic steps, Typed (FNF-2) makes its data flow explicit and type-checked, Factored (FNF-3) gives each shared procedure a single canonical definition so a change propagates instead of drifting, and Scoped (FNF-4) confines every step to least-privilege tool access. Once normalized, every atomic step is a separate entity with a declared contract and can be type-checked, scope-confined, bounded, tested, traced, and audited on its own. A FAOP algebra of provably sound equalities turns refactoring and parallelization into compiler rewrites; orthogonal extensions add verified termination (+V), optimization (+O), and time and cost bounds (+B); and an architectural-level classifier (0-3) determines whether a workflow needs AI at all. Together, these make integrity, isolation, typing, termination, cost, and optimization compile-time concerns across the whole library, not runtime hopes. We implement the theory in SkillBase, an AOP management system (what PostgreSQL is to data, SkillBase is to AOPs), together with a separate executor that enforces these guarantees at run time. A worked financial workflow illustrates the approach end to end.
