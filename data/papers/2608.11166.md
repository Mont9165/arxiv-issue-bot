# Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems

- arXiv ID: `2608.11166v1`
- Authors: Audrey Quessada-Vial
- Published: 2026-08-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.11166v1) | [pdf](https://arxiv.org/pdf/2608.11166v1)

## Abstract

Agentic systems are increasingly composed of heterogeneous agents, prompts, tools, models, skills, composite subsystems, policies, and execution workflows whose configurations evolve across frameworks and runtime environments. Existing LLMOps and AgentOps platforms support orchestration and observability but do not provide a common configuration-governance model for representing and governing these systems as coherent, versioned configurations.
  This paper introduces Agentic Configuration Management (ACM), a framework-independent governance and configuration reference model for heterogeneous agentic systems. ACM combines typed and independently versioned Agentic Configuration Items, immutable revisions and baselines, explicit configuration-runtime separation, lifecycle and assurance semantics, dependency-aware impact propagation, and runtime provenance. Heterogeneous native configurations are normalized through semantic projection into a canonical Configuration Graph on which common governance semantics operate.
  We provide a Python reference implementation with adapters for LangGraph, CrewAI, and the OpenAI Agents SDK. The evaluation combines 27 governance scenarios with nine quantitative impact-propagation cases. For the evaluated configurations, the three frameworks yield governance-equivalent ACM representations and reproducible governance outcomes after projection. The impact semantics are formalized as monotone propagation over a finite lattice, establishing convergence, termination, and uniqueness of the least fixed point above the initial impact valuation. These results provide evidence that common governance semantics can support reproducibility, auditability, dependency analysis, and interoperability across heterogeneous agentic execution abstractions within the evaluated scope.
