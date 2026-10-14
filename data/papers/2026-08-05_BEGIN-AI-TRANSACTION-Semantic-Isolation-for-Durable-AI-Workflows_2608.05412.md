# BEGIN AI TRANSACTION: Semantic Isolation for Durable AI Workflows

- arXiv ID: `2608.05412v1`
- Authors: Barzan Mozafari
- Published: 2026-08-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.05412v1) | [pdf](https://arxiv.org/pdf/2608.05412v1)

## Abstract

An AI execution can now outlive the environment in which it began. What once fit inside one model call increasingly unfolds across pauses, retries, branches, subagents, and model-selected tools. Meanwhile, prompts, model aliases, indexes, policies, and tools are deployed independently: stable names can acquire new behavior, and workflows can discover resources only after they start. The workflow can therefore combine saved state with changed assumptions, producing an internally inconsistent result even when every call succeeds. This is an isolation problem: database transactions constrain concurrent data updates, but workflow checkpointing provides no corresponding contract for concurrent changes to an AI workflow's semantic environment.
  We define four automatically detectable anomalies: semantic read skew, compatibility skew, context escape, and merge skew. To control which anomalies are allowed, we derive a partial order of isolation levels, from Semantic Read Committed to Semantic Snapshot Isolation, by combining three independent guarantees: resource stability, cross-resource compatibility, and continuation inheritance. In a conservative source audit of the 100 most-starred public repositories with executable LangGraph code, we find that 7.4 percent of codebases with durable workflows resolve live or dynamically selected semantic resources within the same workflow, without an evident immutable binding. We show that these guarantees can be checked and enforced efficiently in middleware. Our prototype, SemIso, propagates semantic context and blocks incompatible resources and branch merges with microsecond-scale checks.
