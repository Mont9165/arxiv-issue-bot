# Skills as Verifiable Artifacts: A Trust Schema and a Biconditional Correctness Criterion for Human-in-the-Loop Agent Runtimes

- arXiv ID: `2605.00424v1`
- Authors: Alfredo Metere
- Published: 2026-05-01
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.00424v1) | [pdf](https://arxiv.org/pdf/2605.00424v1)

## Abstract

Agent skills -- structured packages of instructions, scripts, and references that augment a large language model (LLM) without modifying the model itself -- have moved from convenience to first-class deployment artifact. The runtime that loads them inherits the same problem package managers and operating systems have always faced: a piece of content claims a behavior; the runtime must decide whether to believe it. We argue this paper's central thesis up front: a skill is \emph{untrusted code} until it is verified, and the runtime that loads it must enforce that default rather than infer trust from a signature, a clearance, or a registry of origin. Without skill verification, a human-in-the-loop (HITL) gate must fire on every irreversible call -- which is operationally untenable and degrades into rubber-stamping at any non-trivial scale. With skill verification treated as a separate, gated process, HITL fires only for what is unverified, and the system becomes sustainable. We give a trust schema (§\ref{sec:schema}) that includes an explicit verification level on every skill manifest; a capability gate (§\ref{sec:gate}) whose HITL policy is a function of that verification level; a \emph{biconditional} correctness criterion (§\ref{sec:biconditional}) that any candidate verification procedure must satisfy on an adversarial-ensemble exercise (§\ref{sec:eval}); and a portable runtime profile (§\ref{sec:guidelines}) with ten normative guidelines abstracted from a working open-source reference implementation \cite{metere2026enclawed}. The contribution is harness- and model-agnostic; nothing here requires retraining, fine-tuning, or proprietary infrastructure.
