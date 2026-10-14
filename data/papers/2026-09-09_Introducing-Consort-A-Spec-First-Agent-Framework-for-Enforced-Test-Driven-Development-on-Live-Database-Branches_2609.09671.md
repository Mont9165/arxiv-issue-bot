# Introducing Consort: A Spec-First Agent Framework for Enforced, Test-Driven Development on Live Database Branches

- arXiv ID: `2609.09671v1`
- Authors: Kevin Hartman
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.09671v1) | [pdf](https://arxiv.org/pdf/2609.09671v1)

## Abstract

When an agent writes code, the development framework becomes the control system for a non-deterministic worker. Spec-first, agent-driven frameworks have gained rapid traction since 2025; the installable ones, GitHub Spec Kit, obra/superpowers, BMAD, and GSD, and our own, all capture intent through a specification or durable planning artifacts. Since they agree on capturing intent up front, what separates them is how each enforces the engineering discipline that keeps agent-written code clean, correct, and maintainable. Every framework enforces that discipline somehow; they differ in how. We characterize three modes: enforcement by persuasion (prompt discipline the model may ignore), by front-loaded structure (strong specs, then a trusted build), and through controls the agent cannot edit (a deterministic orchestrator, human-approved gates, immutable tests, and a green result that must pass against a live, branched database). We introduce Consort, a spec-first, test-driven agent framework built on the third, enforcing that discipline through controls the agent runs inside but cannot bypass, in which a deterministic orchestrator drives separate role agents through a spec-first design lane and a test-driven build lane on a live database branch. We argue that enforcing the tests and gates in code keeps agent-written code honest and verifiable, while its specialized roles, like the human roles before them, are what make it maintainable, claims we frame as a pre-registered, testable hypothesis.
