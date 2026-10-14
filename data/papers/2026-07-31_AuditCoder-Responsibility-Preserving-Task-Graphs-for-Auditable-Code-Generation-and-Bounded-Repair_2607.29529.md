# AuditCoder: Responsibility-Preserving Task Graphs for Auditable Code Generation and Bounded Repair

- arXiv ID: `2607.29529v1`
- Authors: Kangjie Huang, Chen Lyu
- Published: 2026-07-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.29529v1) | [pdf](https://arxiv.org/pdf/2607.29529v1)

## Abstract

Code generators return programs, but typically do not preserve the construction record needed to connect a failure to the decision that produced the affected code or to delimit a justified repair. We present AuditCoder, which treats the program and an auditable construction trace as joint outputs. Before code generation, a contract-annotated task graph assigns stable responsibility identities that remain attached to each commitment, its owned implementation, provenance, validation evidence, and intervention history. When validation fails, a conservative locator maps heterogeneous evidence to a node or dependency branch---or abstains---and bounded repair regenerates only that region while reusing the frozen complement. On APPS, \method{} reaches $82.5$--$83.0\%$ \texttt{pass@1}, recovering much of the loss caused by unrepaired graph decomposition but trailing AgentCoder by $7.5$--$8.5$ points. On ClassEval, it reaches $75.0$--$82.0\%$, outperforming CoT + retry while remaining below AgentCoder. A separate audit of 200 APPS records yields $0.9725$ task-macro decision--code trace coverage; the locator identifies an evidence-supported node or branch for 26 of 60 failures, and 17 of those localized repairs pass. For tasks with stable, locally testable boundaries, the graph functions not only as a decomposition structure but also as a persistent index for validation and repair.
