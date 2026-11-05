# Agentic Behavior Engineering: A Design-by-Contract Methodology for Specifying, Verifying, and Governing Enterprise AI Agents

- arXiv ID: `2611.05454v1`
- Authors: Yang Song
- Published: 2026-11-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.05454v1) | [pdf](https://arxiv.org/pdf/2611.05454v1)

## Abstract

Enterprise teams that deploy large language model (LLM) agents inherit a maintenance problem that traditional testing does not address. The model is non-deterministic, but the larger risk is that most of what changes an agent's behavior (a retired model version, a revised policy, an upstream schema change, a prompt edit meant to fix one case) originates outside the owning team and is discovered as a production defect rather than caught as a regression. This paper presents Agentic Behavior Engineering (ABE), a platform-agnostic methodology that treats observable agent behavior, rather than the prompt or the model, as the version-controlled engineering artifact. ABE adapts Design by Contract to non-deterministic systems. A specification-only behavior contract with stable rule identifiers states what the agent must do, must not do, and when it must abstain for lack of evidence; a lightweight scenario library turns each rule into concrete situations; and every engineering artifact (tests, runtime policies, telemetry) references the contract in one direction only, so that specification and implementation can change independently without drifting apart. The method organizes the work into five responsibilities (Specify, Ground, Control, Verify, Observe), treats missing evidence and a verified negative as different things, enforces authority outside the model, gates releases on per-scenario pass^k reliability rather than aggregate accuracy, and classifies every production run against the contract so that each finding routes to the asset that must change. We illustrate the method with an executable capacity-allocation boundary suite and a constructed worked example of a product-review approval workflow.
