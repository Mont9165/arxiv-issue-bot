# Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets

- arXiv ID: `2605.26165v1`
- Authors: Furkan Sakizli
- Published: 2026-05-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.26165v1) | [pdf](https://arxiv.org/pdf/2605.26165v1)

## Abstract

Agentic RAG systems that equip language models with dozens to hundreds of tool definitions face a critical resource conflict: tool schemas consume the same context window needed for retrieval-augmented generation. We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions. Applying TSCG conservative-profile compression (44-50% schema token savings), we observe a binary enablement effect: at 8K tokens, JSON-schema tool definitions overflow the context window entirely, yielding near-zero EM (2.6% average), while compressed schemas restore RAG functionality with +20.5 pp average exact-match lift across all eight models (+24.7 pp among the six exhibiting full enablement). At 32K -- where both formats fit -- four of five tested models show delta <= 1 pp, confirming the effect is purely budget-driven. External validation on HotpotQA (50 multi-hop questions) shows +48 pp EM under the same overflow scenario. Frontier scaling tests demonstrate that JSON schemas overflow at ~494 tools while compressed schemas remain operational beyond 800 tools. Our results establish tool-schema compression as a necessary infrastructure layer for agentic RAG in constrained-context deployments. All code, data, and checkpoints are publicly available.
