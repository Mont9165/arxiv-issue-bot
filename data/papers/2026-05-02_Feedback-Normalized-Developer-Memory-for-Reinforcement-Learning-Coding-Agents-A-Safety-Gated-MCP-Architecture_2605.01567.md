# Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents: A Safety-Gated MCP Architecture

- arXiv ID: `2605.01567v1`
- Authors: Mehmet Iscan
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.01567v1) | [pdf](https://arxiv.org/pdf/2605.01567v1)

## Abstract

Large language model (LLM) coding agents increasingly operate over repositories, terminals, tests, and execution traces across long software-engineering episodes. Persistent memory is useful, but static vector stores or generic retrieval-augmented generation (RAG) are insufficient for reinforcement-learning (RL) code development, where small details can alter Bellman targets, terminal masks, gradient flow, or validation claims. This paper presents RL Developer Memory, a local-first, Model Context Protocol (MCP)-native developer-memory architecture for RL coding agents. It treats memory selection as a logged contextual decision process: issue_match ranks candidates and records telemetry, issue_feedback maps raw labels to bounded rewards, and issue_record_resolution links verified resolutions to earlier retrieval events. A deterministic ranker remains deployed, while a contextual-bandit residual policy runs in shadow mode and can affect canary behavior only through conservative off-policy-evaluation (OPE) gates. RL/control memories require theory-to-code metadata and review-gated governance. The system is evaluated on a deterministic 200-case benchmark with RL algorithm bugs, hard negatives, review-gated RL/control cases, and low-risk failures. In the same-commit comparison, deterministic control and full shadow/OPE both achieve 80.0% expected-decision accuracy and 100.0% hard-negative suppression; the full configuration adds learning telemetry rather than accuracy gain. Static validation passed 11/11 checks; dynamic integration passed 10/10 cases. The evidence reports limits: active learned-policy deployment and official-client MCP interoperability are unsupported, live full-configuration latency regresses, and 40 residual non-RL failures remain. The contribution is an auditable memory-control architecture with explicit claim boundaries, not a universal coding-agent improvement claim.
