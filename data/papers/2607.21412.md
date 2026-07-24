# Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog

- arXiv ID: `2607.21412v1`
- Authors: Bartolomeo Bogliolo
- Published: 2026-07-23
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.21412v1) | [pdf](https://arxiv.org/pdf/2607.21412v1)

## Abstract

Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symbolic engines, yet most integrations are bespoke and lack a standardized interface for tool-augmented agents. This paper presents Euclid-MCP, an open-source MCP server that provides deterministic logical reasoning via SWI-Prolog. Euclid-MCP introduces Euclid-IR, an engine-agnostic intermediate representation for Horn-clause logic that is human-readable, easy for LLMs to generate, and straightforward to compile into Prolog or alternative backends. The server exposes a compact tool interface that supports a translate-run-inspect-repair loop, enabling LLM clients to delegate inference while retaining full access to proof traces and derivation logs. We evaluate Euclid-MCP on a realistic IT security and compliance use case. Results show that while LLMs alone are sufficient on small knowledge bases, they hallucinate systematically on larger problems, whereas Euclid-MCP delivers exact answers with lower latency and more compact outputs. We argue that semantic RAG is fundamentally unsuited for rule enforcement, and that Euclid-MCP can serve as a stable, shared reasoning substrate for both RAG-based assistants and agentic systems.
