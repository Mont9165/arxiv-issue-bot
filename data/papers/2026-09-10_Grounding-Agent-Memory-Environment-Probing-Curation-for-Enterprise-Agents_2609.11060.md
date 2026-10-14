# Grounding Agent Memory: Environment-Probing Curation for Enterprise Agents

- arXiv ID: `2609.11060v1`
- Authors: Susheel Suresh, Hazel Mak, Sahil Bhatnagar, Chhaya Methani, Alejandro Gutierrez Munoz
- Published: 2026-09-10
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.11060v1) | [pdf](https://arxiv.org/pdf/2609.11060v1)

## Abstract

Persistent memory is entering production-oriented agent platforms to help long-horizon agents accumulate experience across sessions. Yet a post-task curator agent restricted to completed trajectories can preserve errors, overgeneralize partial evidence, or retain stale knowledge. We introduce environment-probing curation, a deployment-compatible extension that gives an existing asynchronous curator agent least-privilege, read-only world tools to check, scope, and refresh candidate memories. It requires no model retraining and leaves the task agent, retriever, memory representation, and production write authority unchanged. In a production-like GitHub Copilot (GHCP) harness built on its SDK, we compare stateless execution, full in-context learning, GHCP + Mem, and GHCP + Mem (w/ Env Probing) on CLBench database exploration and 90 adapted APEX management-consulting tasks. On CLBench, probing raises pass rate from 39% to 73% and pass-discounted reward from 8.60 to 22.60 while reducing queries from 8.8 to 4.7 per question and task-agent cost from \$3.38 to \$1.68. Across six APEX worlds, all 18 memory-versus-baseline mean reward comparisons are positive and task-agent tool calls fall by 16--75%; probing gives the best task-agent reward gain per dollar in five worlds. Probing also attains higher mean reward than GHCP + Mem on both Sonnet 4.6 and Opus 4.7 without schema drift. Environment probing therefore turns existing agent-memory curation into an environment-informed, auditable process while preserving a compact task-time interface.
