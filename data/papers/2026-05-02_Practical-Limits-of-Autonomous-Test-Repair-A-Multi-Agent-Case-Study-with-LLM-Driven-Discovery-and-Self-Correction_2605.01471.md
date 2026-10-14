# Practical Limits of Autonomous Test Repair: A Multi-Agent Case Study with LLM-Driven Discovery and Self-Correction

- arXiv ID: `2605.01471v1`
- Authors: Hyukjoo Lee
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.01471v1) | [pdf](https://arxiv.org/pdf/2605.01471v1)

## Abstract

Maintaining reliable UI test suites in large-scale enterprise applications is a persistent and costly challenge. We present an industrial case study of a multi-agent autonomous testing system evaluated using anonymized execution data from a production-like enterprise UI testing prototype. The application features several hundred dynamic UI elements per screen. Built on a large language model with LangGraph orchestration, Playwright execution, and a RAG knowledge base, the system evolves from human-directed testing toward High-autonomy feature discovery and test execution: given no explicit test targets, it discovers over 100 testable features across 10 UI screens, dynamically expands coverage by an additional 15--30 features through runtime DOM analysis, and iteratively repairs failing tests without human intervention.
  We analyzed 300 consecutive autonomous execution reports encompassing 636 individual test-case executions across 10 distinct scenario families. The system achieved a 70% repair convergence rate at the scenario-family level, with a mean of 3.4 repair iterations to convergence. However, only 10% of scenario families succeeded on first attempt, 38% of reports failed to produce any executable test artifact, and we documented concrete instances of assertion weakening and test-case deletion used as workaround mechanisms to achieve superficial convergence.
  Our findings show that unrestricted autonomy leads to unstable and often misleading outcomes, while constrained autonomy transforms such systems into operationally viable workflows. Rather than advocating full autonomy, our findings suggest that reliable autonomous testing in enterprise-scale settings requires explicit constraints, validation boundaries, and human oversight to preserve semantic correctness and operational trustworthiness.
