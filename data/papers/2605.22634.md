# Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents

- arXiv ID: `2605.22634v1`
- Authors: Ting Liu
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.22634v1) | [pdf](https://arxiv.org/pdf/2605.22634v1)

## Abstract

Skills are increasingly used to package agent instructions, workflows, scripts, and reference materials. In enterprise settings, however, skills often need to express more than task guidance: they must make goals, input boundaries, permissions, evidence requirements, output contracts, quality criteria, verification steps, human approval points, and handoff rules inspectable. This paper proposes contractual skills, a GovernSpec-inspired design framework for organizing SKILL.md files as readable task contracts while preserving lightweight skill discovery and progressive loading. The framework clarifies the boundary between contractual skills, GovernSpec YAML contracts, Model Context Protocol surfaces, tool adapters, runtime guardrails, tracing, and evaluation systems.
  We evaluate the framework with two offline experiments. A text-generation study covers three enterprise skills, fifteen synthetic tasks, four instruction conditions, and eight generation models, yielding 960 outputs and 1680 cross-judge score records. Contractual skills outperform no-skill and minimal-skill baselines on all tested models. Relative to information-rich plain expanded skills, the gains are small and mixed, suggesting that contractual fields mainly improve checkability and maintainability rather than raw generation quality. A tool-calling challenge covers eight models and 192 simulated tool-call records. Skills usually reduce high-risk tool attempts, but model differences remain and runtime tool guardrails are still required. The results suggest that contractual skills are best understood as a governance layer that makes task intent, boundaries, and acceptance criteria explicit, not as a standalone safety mechanism.
