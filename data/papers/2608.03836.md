# Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics in Workflow Persistence Layers

- arXiv ID: `2608.03836v1`
- Authors: Sajjad Khan
- Published: 2026-08-04
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DC`, `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03836v1) | [pdf](https://arxiv.org/pdf/2608.03836v1)

## Abstract

A framework that persists execution state so a run can be interrupted, survive a crash, and continue must decide what a resume means for effects that already fired. Five widely deployed agent workflow frameworks answer differently, none exposes a machine-checkable contract, and behavior violates even the fragments they state. The RESUME CONTRACT states six properties over the persistence API (prefix continuation, effect exactly-once, fork determinism, checkpoint validity, consume-once, recovery determinism), plus fork-intent and liveness obligations. A TLA+ model checks a reference semantics exhaustively, unchanged at scaled bounds (7.4 million states); a 39-cell fault matrix yields the separating models independence requires, and consume-once splits, its consumption clause independent of all six others. A deterministic, LLM-free harness measures them at pinned releases. LangGraph 1.2.9 durably records a second resume value and never consults it, persists schema-invalid state silently, and re-executes durably recorded work after a real SIGKILL: exactly-once across interrupts, at-least-once across crashes, on one API. CrewAI 1.15.2 re-executes completed effect-bearing methods against its written claim; pydantic-graph 1.x cannot resume after a mid-node crash; no two probed frameworks share a conformance profile. Consume-once holds sequentially and fails under concurrent delivery: k processes resuming one parked interrupt fire the gated effect k times, saturation 1.0 in 36 of 40 cells, and the failure crosses hosts. REMIT, a reference sequencer whose Verus-verified recovery core is line-identical to the shipped executable, repairs the fork and validity cells. The cross-process cell is repaired at the read path, and that repair ships: an opt-in gate claims consumption in the shared store, serving one racer and refusing the rest before any node executes.
