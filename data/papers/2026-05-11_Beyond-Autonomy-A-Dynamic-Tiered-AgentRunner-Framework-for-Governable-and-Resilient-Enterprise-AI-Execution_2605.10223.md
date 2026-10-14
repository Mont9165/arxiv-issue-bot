# Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution

- arXiv ID: `2605.10223v1`
- Authors: Kai Pan, Rong Hou
- Published: 2026-05-11
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10223v1) | [pdf](https://arxiv.org/pdf/2605.10223v1)

## Abstract

Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
