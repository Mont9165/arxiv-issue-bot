# Towards Agentic Test-Driven Quality Assurance for 6G Networks

- arXiv ID: `2604.23285v1`
- Authors: Christos Tranoris, Besiana Agko, Kostis Trantzas, Irene Denazi
- Published: 2026-04-25
- Primary category: `cs.NI`
- Categories: `cs.NI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23285v1) | [pdf](https://arxiv.org/pdf/2604.23285v1)

## Abstract

This work proposes an agentic, intent-driven end-to-end (E2E) orchestration framework that integrates intent co-creation with a Test-Driven Quality Assurance paradigm. In this framework, autonomous agents iteratively refine a user's initial intent into a confirmed, auditable specification. Furthermore, the system automatically derives validation tests from these intents before provisioning, directly mirroring the Test-Driven Development workflow in software engineering to ensure proactive Service Level Agreement (SLA) compliance. The architecture is grounded in a standards-aligned knowledge representation using TM Forum (TMF) information models and catalogs. This enables deterministic graph traversal from high-level Product Offerings down to granular Service/Resource and Test specifications. We prototyped this architecture by extending OpenSlice with a message-driven, multi-agent pattern and integrating MCP-enabled (Model Context Protocol) tool access for real-time knowledge retrieval. Currently, our evaluation of the agents targets the intent co-creation phase as a baseline toward full-scale orchestration. Building on experiments with multiple open-source Large Language Model (LLM) backends integrated with the TMF-based knowledge base, we observe substantial variability in tool-use reliability and hallucination patterns, underscoring the critical importance of robust knowledge integration in agentic 6G systems.
