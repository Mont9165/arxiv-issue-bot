# AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair

- arXiv ID: `2607.29422v1`
- Authors: Michael Fu, Qiyue Mei, Patanamon Thongtanunam, Kla Tantithamthavorn
- Published: 2026-07-31
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.29422v1) | [pdf](https://arxiv.org/pdf/2607.29422v1)

## Abstract

Automated vulnerability repair aims to reduce the time and effort required to patch security flaws from a vulnerability triage report. Recent agentic AI approaches have shown promising results in automated program repair. However, vulnerability repair demands richer program context than general bug repair - context that security engineers routinely assemble in practice but that existing agentic approaches do not engineer. We identify three critical gaps: code-structure context capturing cross-file data flows and memory operation patterns, runtime-execution context revealing crash semantics and memory origins, and commit-history context recovering how fragile code patterns were introduced. We present AgenticRepair, an agentic vulnerability repair framework that addresses the gaps through multi-faceted program context engineering. AgenticRepair orchestrates three specialized LLM subagents to engineer the contexts, which are then embedded into the memory of a dedicated repair subagent for context-conditioned patch synthesis. Evaluated on SEC-Bench comprising 300 real-world instances with sanitizer-based patch verification, AgenticRepair achieves a 73% success rate, substantially outperforming the strongest baseline by 29%. Our ablation study confirms that the three context facets are mutually complementary, and that multi-agent scaffolding and base-model capacity each play an essential role. Collectively, these findings establish multi-faceted program context engineering as a promising design direction for agentic vulnerability repair.
