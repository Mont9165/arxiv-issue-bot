# ACEM: A Cost Estimation Model for Agentic Software Engineering

- arXiv ID: `2608.02582v1`
- Authors: Mohammad El-Ramly
- Published: 2026-08-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.02582v1) | [pdf](https://arxiv.org/pdf/2608.02582v1)

## Abstract

Traditional software cost estimation models, such as COCOMO II, Function Points, and Story Points, assume that development effort is primarily driven by human labor in design, coding, and testing. Agentic software engineering, where autonomous AI agents perform substantial implementation work and humans focus on planning, specification, and validation, challenges this assumption. New cost dimensions arise: large language model (LLM) token consumption across agent actions, Human-in-the-Loop (HITL) oversight effort, and infrastructure costs for agent orchestration and tooling. These costs are nondeterministic: identical tasks may consume different tokens, follow divergent reasoning paths, and require varying human correction, phenomena absent in traditional development. A new framework is needed to bridge standard sizing metrics with this cost structure.
  This paper proposes ACEM (Agentic Cost Estimation Model), which decomposes total agentic development cost into three additive dimensions: LLM, HITL, and infrastructure cost. ACEM introduces three constructs for agentic dynamics: the Revision Factor (RF), modeling token overhead from output rejection and retries; the Context Factor (CF), capturing rising token consumption as context accumulates; and the HITL Intensity Score (HIS), a four-level oversight classification scheme. It further maps Use Case Points, Story Points, and Function Points to estimated token consumption, enabling organizations to reuse existing project-scoping data for agentic cost forecasting.
  ACEM is presented as a fully specified model structure and calibration methodology, with constants left symbolic pending empirical grounding. As an early-stage proposal, it invites the research community to calibrate, test, and extend the model through real project data.
