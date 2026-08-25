# From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents

- arXiv ID: `2608.23282v1`
- Authors: Radouane Bouchekir, Damir Safin, Tomas Bueno Momcilovic
- Published: 2026-08-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.23282v1) | [pdf](https://arxiv.org/pdf/2608.23282v1)

## Abstract

Large Language Models (LLMs) agents deployed in vehicles must satisfy a written operating policy on every turn: a single hallucinated identifier, omitted mandatory side-effect, or premature completion claim fails the task. We present AgentGuardUtil, our entry to CAR-bench Track~1, which treats the AI planer (LLM) as a fallible proposer inside a grounded verify-and-revise loop. Its core novelty is a runtime policy compiler: the natural-language policy shipped with each conversation is compiled, once per policy, into typed machine-checkable rules, a subset of which receive an executable form. A deterministic obligation engine interprets these rules against live tool results and the simulated post-write state of the draft itself, emitting the exact remedial calls with computed arguments rather than natural-language reminders. Around this engine, 25 deterministic gates (identifier provenance, schema and enum validity, gather-before-act, confirmation and future-time protocols) and an LLM critic produce tiered findings that drive a bounded revision loop tuned for the pass k metric.
