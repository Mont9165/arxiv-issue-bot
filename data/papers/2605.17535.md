# AgentModernize: Preserving Business Logic in Legacy Modernization with Multi-Agent LLMs and Behavioral Specification Graphs

- arXiv ID: `2605.17535v1`
- Authors: Sheikh Nazib Ahmed, Marnim Galib
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.17535v1) | [pdf](https://arxiv.org/pdf/2605.17535v1)

## Abstract

Legacy modernization breaks business logic. Most tools and LLM-based approaches treat modernization as syntax translation, losing implicit rules, edge-case handling, and cross-module constraints. We present AgentModernize, a multi-agent framework that treats modernization as a behavioral preservation problem. Four specialized agents handle extraction, specification, code generation, and validation. The key intermediate artifact -- a Behavioral Specification Graph (BSG) -- forces extracted business logic to be explicit and inspectable before any code is generated. We evaluated on LegacyModernize-8, eight scenarios spanning telecom and banking, using three models (GPT-4o-mini, GPT-4o, GPT-5.3-codex) under a fair protocol: same gold-standard tests, 3 trials, temperature 0.0. Full AgentModernize with feedback was the only configuration with non-zero mean BER under every backbone. SP-LLM and CoT-LLM scored 0.0% on every scenario, on every backbone. AgentModernize without feedback scored 0.0% mean BER with GPT-4o-mini and GPT-5.3-codex; under GPT-4o it achieved non-zero BER only on S1 (44.4%; 5.6% mean over scenarios). Mean BER for full AgentModernize was 9.4% (mini), 8.1% (GPT-4o), and 19.4% (codex). The BSG captures 91.2% of gold-standard rules, confirming that the bottleneck is code generation, not extraction.
