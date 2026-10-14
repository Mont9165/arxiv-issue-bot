# Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails

- arXiv ID: `2609.16461v1`
- Authors: Harish Gaggar
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.16461v1) | [pdf](https://arxiv.org/pdf/2609.16461v1)

## Abstract

Agentic large language model (LLM) systems rely on long interaction histories to preserve instructions, tool states, intermediate decisions, and unresolved dependencies, but unrestricted context growth increases computational cost and can reduce efficiency. This study evaluates protocol-preserving context trimming as a reliability-constrained approach for multi-step agentic workflows. Five trimming strategies - recency-based, relevance-based, summarization, protocol-aware trimming, and adaptive budget guardrails - were compared across retained-context levels and workflow-complexity classes using task success, protocol adherence, valid tool calls, token savings, latency reduction, cascading failures, and critical context thresholds. Conventional strategies achieved about 60% mean token savings but lower task success (66.6-77.3%) and protocol adherence (85.5-88.6%). Protocol-aware trimming improved task success to 92.2%, while adaptive guardrails achieved 96.0% task success, 96.3% protocol adherence, and 1.0% cascading failure with 56.0% mean token savings. Retained-context budgets of 25% or less increased failure odds 10.92-fold relative to budgets of 50% or more (p < 0.001). Protocol-aware trimming produced 5.24-fold greater odds of successful completion than conventional methods under aggressive budgets, while adaptive guardrails further increased success odds 2.11-fold versus fixed protocol-aware trimming (p < 0.001). Critical context thresholds also increased with workflow complexity. These findings indicate that reliable context reduction depends more on preserving protocol-critical state than on maximizing token removal, and that adaptive guardrails can improve efficiency, scalability, and reliability in long-horizon agentic systems.
