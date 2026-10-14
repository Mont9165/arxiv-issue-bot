# Text2Dashboard: A Governed Agent Architecture for Natural-Language Dashboard Generation over Enterprise DataBrain

- arXiv ID: `2610.06914v1`
- Authors: Yiou Wu, Zezhi Tang, Ningwei Bai, Liuhaichen Yang
- Published: 2026-10-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.06914v1) | [pdf](https://arxiv.org/pdf/2610.06914v1)

## Abstract

Text2Dashboard is a DataBrain-specific prototype that turns natural-language analytic requests into inspectable dashboards. An installable Codex plugin and standalone Agent Runtime combine schema-constrained model decisions with typed tools, persistent state, and deterministic Hooks for approval, audit, checkpointing, recovery, and failure handling. The pipeline resolves entities, discovers metadata, enforces read-only SQL, composes dashboards, and applies static checks, dynamic preflight, and browser inspection. The model proposes actions while deterministic software controls execution and records state transitions.
  We evaluate the workflow on frozen real-DataBrain tasks and controlled Hook faults. Strict success was 6/8 on metadata and SQL tasks: metadata selection passed 4/4, all four SQL tasks met semantic criteria, and 2/4 met the exact output-column contract. The final release passed 4/4 single-panel dashboard tasks, one two-panel task, and one existing-dashboard refinement; a parameterised task exceeded its step limit. All ten fault scenarios met their specified outcomes without unapproved external side effects. Model inference accounted for over 97\% of observed runtime in every reported group. These small, DataBrain-specific results do not establish production readiness, general text-to-SQL accuracy, or an efficiency advantage over manual dashboard construction.
