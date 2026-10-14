# Improving Constraint Models with LLM Agents

- arXiv ID: `2608.08127v1`
- Authors: Florentina Voboril, Stefan Szeider
- Published: 2026-08-08
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.08127v1) | [pdf](https://arxiv.org/pdf/2608.08127v1)

## Abstract

The runtime of Constraint Programming (CP) solvers is highly sensitive to modeling choices, such as symmetry breaking, implied constraints, global constraints, constraint reformulation, and variable representation. Improving these constraint models has traditionally required human expertise, and existing automated reformulation systems are restricted to a predefined library of hand-crafted transformation rules. We introduce an agentic framework that instead reformulates a constraint model from an open-ended space and establishes correctness empirically rather than by construction: a Large Language Model (LLM) agent, given a model and three training instances, proposes alternative formulations, validates each by injecting its solution back into the original model, and diagnoses and repairs failures, returning the best variant it finds in a median of about fifteen minutes. The models are expressed in the CPMpy modeling library, and each proposed model is evaluated on three larger test instances. Across nine combinatorial optimization problems, the generated models outperform the originals on 21 of 27 test instances, and on some problems solve more than two orders of magnitude faster. A comparison against non-agentic baselines that reuse the same validation and selection tools indicates that the gains stem from the agent's iterative diagnosis and repair, not merely from sampling several candidates. These results demonstrate that autonomous agentic methods can support the improvement of constraint models.
