# SessionBound: Turning Enterprise Task Approval into Budgeted Database Sessions

- arXiv ID: `2607.00751v1`
- Authors: Minmin Wu
- Published: 2026-07-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.00751v1) | [pdf](https://arxiv.org/pdf/2607.00751v1)

## Abstract

Enterprise AI agents are useful for internal analysis, audit, compliance review, and operational investigation, but they create a difficult authorization problem. A manager or data owner may approve a business task, while the agent later generates open-ended SQL below the application layer. Existing systems help identify agents, delegate authority, govern data products, or enforce database policy, but they do not directly turn an approved enterprise task into a bounded database execution context. SessionBound fills this gap. It turns approved enterprise tasks into short-lived, budgeted, and auditable database sessions for AI agents. A control plane defines task templates, accepts task applications, records approvals, assigns budgets, and issues signed task tokens. A database runtime, SessionBoundDB, binds a token to a session and enforces safe views, row scope, denied fields, operation limits, query budgets, disclosure budgets, and receipts. The database does not rely on an LLM to decide whether a query is safe. The agent may generate SQL freely, but each attempt must stay inside the approved boundary. A PostgreSQL prototype passed a 24-scenario validation suite. Microbenchmarks show p50 SessionBound execution around 1.4--1.5 ms versus raw PostgreSQL p50 around 0.052--0.074 ms on small synthetic queries: high relative overhead, but low absolute latency.
