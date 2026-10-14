# VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation

- arXiv ID: `2606.07992v1`
- Authors: Harshil Patel, Kunal Pai
- Published: 2026-06-06
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.07992v1) | [pdf](https://arxiv.org/pdf/2606.07992v1)

## Abstract

As the Model Context Protocol (MCP) standardizes tool-calling for autonomous agents, it introduces a critical, unexamined attack surface: the error-handling loop. We hypothesize that tool error messages possess implicit authority, triggering corrective reasoning modes that bypass standard safety heuristics. We introduce VATS (Vulnerability Analysis of Tool Streams), a mutation-driven framework that systematically evolves adversarial payloads across seven structural and linguistic dimensions. Our evaluation across four frontier models, Gemini 3.1 Pro, GPT-5.5, GLM-5.1, and Qwen3-Coder, demonstrates that error-path injection triples the success rate of standard indirect prompt injection (IPI), achieving up to 100% compliance in controlled evaluations. We isolate structural positioning (sandwiching instructions within error context) as the most effective exploit vector across all tested models. While we find that production framework guardrails can mitigate these vulnerabilities, the inherent susceptibility of the model layer poses a systemic risk to bespoke agentic workflows.
