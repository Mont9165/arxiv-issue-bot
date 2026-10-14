# Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents

- arXiv ID: `2607.13157v1`
- Authors: Richmond Alake, Cesare Bernardis, Paul Cayet, Luca Engel, Damien Hilloulin, Sungpack Hong, Allen Hosler, Nickolas Kavantzas, Ingo Kossyk, Son Le, Rhicheek Patra, Kartik Talamadupula, Valentin Venzin
- Published: 2026-07-14
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.13157v1) | [pdf](https://arxiv.org/pdf/2607.13157v1)

## Abstract

Agent memory is a systems problem for long-horizon agents. Practical deployments require retention of task state across extended conversations, recovery of user-specific facts and preferences across sessions, and accumulation of procedural knowledge from prior outcomes. These requirements extend beyond document retrieval: a memory layer must determine which interactions become durable state, how that state is scoped, how it is retrieved under latency constraints, and how it is revised or removed over time. This report studies Oracle Agent Memory as a database-native memory substrate built on Oracle Database. Three themes organize the discussion: memory as a lifecycle spanning ingestion, extraction, consolidation, retrieval, summarization, and revision or removal; a layered architecture that separates an active memory core from a passive memory-store interface with explicit scope control across users, agents, and threads; and evaluation methodology in which downstream task accuracy is complemented by memory-centric measures such as evidence retrieval, recall, latency, and estimated token use. The report summarizes LongMemEval results, reaching 93.8% accuracy, compares Oracle Agent Memory against flat-history baselines, using about 10.7x fewer tokens, and published or reported external baselines where available, and closes with implementation-oriented appendix material covering setup, thread lifecycle, and search semantics.
