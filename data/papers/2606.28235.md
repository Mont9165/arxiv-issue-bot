# Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software

- arXiv ID: `2606.28235v1`
- Authors: Daniel Russo
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.28235v1) | [pdf](https://arxiv.org/pdf/2606.28235v1)

## Abstract

Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Yet agents that each pass their own tests still leave repositories that accumulate problems no single contribution accounts for. We ask whether this problem belongs to the individual agent or to the repository where it accumulates. We study integration friction, the cost of integrating a contribution into a codebase that other contributors are concurrently changing. Across more than 930,000 agent-authored pull requests, we measure how much of the variation in friction stays with the repository after the contribution, its author, its size, and its agent are accounted for. About half does, and it survives full controls. In the same repositories, agent-authored contributions concentrate this repository-level friction roughly twice as much as human ones (intraclass correlation 0.30 versus 0.16), a gap that holds after controlling for codebase size, age, task shape, process maturity, and merge path. The risk is a property of the ecosystem, not the agent. AI-native software is therefore better measured and governed at the ecosystem level than one agent at a time.
