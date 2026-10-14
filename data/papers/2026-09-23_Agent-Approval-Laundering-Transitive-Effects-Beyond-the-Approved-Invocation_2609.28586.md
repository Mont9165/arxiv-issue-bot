# Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation

- arXiv ID: `2609.28586v1`
- Authors: Jinqian Zhang, Haojun Xia, Shujiang Wu, Jingkun Yue, Xia Zhang, Zhangpei Cheng, Bibo Tu
- Published: 2026-09-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.28586v1) | [pdf](https://arxiv.org/pdf/2609.28586v1)

## Abstract

Coding-agent approval interfaces bind a human decision to a command or tool call, while developer tools execute the transitive workflow that invocation activates. Package installation can run lifecycle hooks and write files; an MCP call can exercise network authority. We call the resulting record-coverage failure approval laundering: the durable record names the entry invocation but omits effects exercised by its workflow.
  We present the first systematic security analysis of this record-to-closure relation in agent systems. We formalize closure-bound approval over six effect classes and derive an information limit: identical policy-visible fields can require different effect-specific decisions, so no record-only policy can guarantee both. The Approval-to-Action Security Benchmark binds approval objects and decision-time metadata to post-execution evidence.
  Across 111 fixed approval-object/trace pairs, residual records fall from 40 under explicit fields to 17 with command semantics and 13 with decision-time metadata. Across 11 fixed-SHA executions, the ladder reaches zero metadata residuals; two exact mappings recur across three product frontends. For prospective recovery, effect-bound records commit frozen, source-backed predictions and provenance before authorization. On 17 prespecified holdout workflows, predictions achieve 0.926 macro recall and 0.941 macro precision; binding them cuts residual effects from 10 to 3. A Claude Code PreToolUse integration carries the frozen record through the permission path without automatic approval. These results establish approval laundering as a measurable, recurrent record-coverage failure despite truthful invocation identity. They motivate binding each invocation before authorization to a source-backed prediction of its workflow's transitive effect boundary and preserving that binding with the decision.
