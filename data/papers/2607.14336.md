# Copy-on-Write Scoring: Application-Specific Agent Evaluations

- arXiv ID: `2607.14336v1`
- Authors: Joanna Roy, Sven Hoelzel
- Published: 2026-07-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.14336v1) | [pdf](https://arxiv.org/pdf/2607.14336v1)

## Abstract

Trustworthy deployment of LLM-based agents in software systems requires evaluating how they perform on application-specific workflows, with enough granularity to localize where they succeed and fail. Yet existing agent evaluation mechanisms are limited: benchmarks have low construct validity for application-specific workflows and environments, and replica evaluation environments are expensive and prone to drift. We propose Copy-on-Write (CoW) Scoring, a framework that evaluates agent operations directly within application environments using a PostgreSQL-level Copy-on-Write mechanism to isolate agent writes. CoW Scoring produces session- and operation-level scores that highlight where agents' database write operations succeed and fail in a given application environment, enabling inexpensive evaluation and iteration on agent harnesses and tool surfaces. We demonstrate the framework on Plane, an open-source project-management platform, where analysis surfaced specific issues in the tool surface, and corresponding fixes produced measurable improvements on affected models.
  Python library: https://github.com/trail-ml/agent-cow-python
