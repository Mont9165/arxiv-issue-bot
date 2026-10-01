# Approval Laundering: Systematizing Approval--Execution Binding Failures in AI Coding-Agent Harnesses

- arXiv ID: `2609.38983v1`
- Authors: Yang Wang
- Published: 2026-09-30
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.38983v1) | [pdf](https://arxiv.org/pdf/2609.38983v1)

## Abstract

Modern AI coding-agent harnesses (Claude Code, Codex CLI, Cursor) rest their security boundary on a largely unexamined assumption: that the action A a human approves is the same action A' the harness executes, where A is fixed by a stated policy for what a scope grant or session-scoped approval authorizes. We show this assumption fails systematically and reproducibly. We introduce Approval Laundering, a taxonomy of six failure modes by which a harness's enforcement mechanism silently substitutes A' for A after approval: Scope, Argument, Temporal, Tool, Delegation, and Semantic laundering. Unlike prior work that evaluates risk classifiers against static corpora or infers implicit authorization boundaries, we study credential-binding integrity: given an already-approved action, does the harness dispatch exactly that action? Instrumenting Claude Code's pre-execution mediation point (PreToolUse), we conduct a controlled, headless, repeated-measures study of all six classes (N=19-20 runs each), reporting a Bound-Gap Rate (BGR) with Wilson confidence intervals and inter-rater agreement (kappa=1.0). We prototype Approval Token, a keyed capability Hk(principal, agent_id, session_id, tool, arguments, scope, expiry) issued by a mediator that never returns the key to the agent, evaluated via paired before/after replay of 118 runs (McNemar's exact test). The token fully eliminates Delegation laundering and, for our seeded session-identity-mismatch construction, Temporal laundering (p<10^-5), but by design leaves Scope laundering unaffected and shows no significant reduction in Argument laundering (p=1): an honest negative result, since these two classes leave every recorded dispatch field unchanged, diverging one process level below what a field-only verifier can observe. We discuss implications for defenses that bind only at the tool-invocation boundary.
