# From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes

- arXiv ID: `2606.23797v1`
- Authors: Mariano Garralda-Barrio
- Published: 2026-06-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2606.23797v1) | [pdf](https://arxiv.org/pdf/2606.23797v1)

## Abstract

Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. This conceptual systems paper focuses on the high-complexity end of that design space, where goals can be suspended, resumed, revised, and invalidated by actions in other goals. We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). GODR is not proposed as a replacement for workflow graphs in simple guided processes; it is intended for complex, multi-domain, interruptible conversations where objective continuity cannot be recovered reliably from agent identity, chat history, or execution-graph position alone. The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim.
