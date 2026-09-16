# Grounding SWE-Agent Decisions in Architecture-0 Design: Navigating Unknown Unknowns through Physical Mapping

- arXiv ID: `2609.17221v1`
- Authors: Zhongkai Wang, Yan Liu
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.17221v1) | [pdf](https://arxiv.org/pdf/2609.17221v1)

## Abstract

Autonomous Software Engineering Agents (SWE-Agents) excel in deterministic coding tasks but struggle with Architecture 0, the nascent system design phase plagued by implicit engineering constraints, or Unknown Unknowns (UUs) that are rarely stated explicitly. To investigate how agents navigate UUs, we explore a progressive trajectory across pure-text self-play, tool-augmented feedback, and external physical mapping. Our empirical analysis reveals a cascading chain of failures. Pure-text reasoning inevitably devolves into polite consensus or plausible yet physically impossible fabrications. Attempting to bridge this gap via an early-stage execution sandbox unexpectedly triggers Specification Gaming: agents exploit their autonomy over validation scripts to bypass physical constraints, achieving superficial success without resolving core architectural flaws. To resolve this self-validation trap, we propose the Physical Mapping Guard (PMG). Grounded in the software engineering principle of Separation of Concerns, PMG revokes verification authority from the agent, forcing semantic intents to be evaluated by an external, deterministic Semantic-to-Physical (S2P) mapping engine. Extensive evaluations demonstrate that PMG completely eradicates physical-layer and validation-layer gaming. By precisely isolating residual failures to semantic reinterpretations and auditor overreach, PMG marks a critical step toward genuine affordance grounding in automated architectural design.
