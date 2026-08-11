# Carnot: Interpretable, Interactive, and Optimized Execution of Deep Research Queries

- arXiv ID: `2608.09532v1`
- Authors: Matthew Russo, Yash Agarwal, Tianyu Li, Zhuohan Gu, Michael Cafarella, Omar Khattab, Tim Kraska, Samuel Madden
- Published: 2026-08-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.09532v1) | [pdf](https://arxiv.org/pdf/2608.09532v1)

## Abstract

Enterprises increasingly seek to query data lakes using natural language via AI-driven tools like semantic operators or deep research agents. However, the latter operates as an opaque black box, hiding its intermediate reasoning and data retrieval steps, and failing to expose controls for managing API costs and execution latency. Meanwhile, the former can be prohibitively expensive for enterprise-scale data lakes. Consequently, analysts using these systems lack the agency to intercept hallucinated premises, verify intermediate results, or correct the system's trajectory. We present Carnot, an interactive execution engine for AI-driven analytics. Carnot compiles natural language requests into physical execution graphs and surfaces them through an interactive notebook interface. Rather than waiting blindly for a final output, users can critique the plan, incrementally execute operators, inspect intermediate data, or directly edit the underlying code or semantic operator instructions. Carnot's query optimizer will optimize the query with respect to cost or latency constraints provided by the user. Our demo will showcase how Carnot helps users achieve efficient and verifiable insights on workloads motivated by real enterprise use cases.
