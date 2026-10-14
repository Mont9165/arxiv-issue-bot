# ContextPipe: Database-Inspired Context Assembly for Long-Horizon Agents

- arXiv ID: `2609.00749v1`
- Authors: Peng Xu, Zuyu Zhang, Yuze Sun, Feng Tian, Long Wang, Chen Zhang
- Published: 2026-09-01
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.00749v1) | [pdf](https://arxiv.org/pdf/2609.00749v1)

## Abstract

Long-horizon large language model (LLM) agents require context assembly: the runtime must decide what to include in each prompt, in what order, and when to compact history under a hard context-window budget and a byte-sensitive prompt cache. In production agentic systems, this logic is scattered across prompt builders, ad hoc compaction routines, cache-break workarounds, and per-provider shims. We argue that context assembly is structurally isomorphic to query execution in a relational database: both execute under a hard budget, exploit a tiered cache, and leverage statistics. We adopt this discipline in ContextPipe: a five-phase pipeline (Plan Bind Optimize Execute Feedback) backed by a structured data-source catalog, a deterministic cache-aware optimizer, and an EXPLAIN ANALYZE trace. We show that context in ContextPipe is auditable, replayable, and failure-isolated. A preliminary evaluation using the SWE-bench Pro Qutebrowser subset shows that, compared with the append-only context construction policy, ContextPipe reduces total token volume by 31%, LLM calls by 23%, and response time by 9%, at the cost of a lower KV cache-hit ratio.
