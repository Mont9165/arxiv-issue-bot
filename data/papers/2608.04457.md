# Eigenius: A Typed Knowledge-Graph DBMS with Epistemic Stratification and Institution-Mediated Reasoning

- arXiv ID: `2608.04457v1`
- Authors: Hans-Martin Will, Allen L. Brown, Matthew Fuchs
- Published: 2026-08-05
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2608.04457v1) | [pdf](https://arxiv.org/pdf/2608.04457v1)

## Abstract

As "AI Scientists" emerge to drive research via the Model Context Protocol (MCP), systems relying on ephemeral scripts will fail. The sheer scale of stateful, interconnected evidence requires a machine-walkable warranty grounded in a purpose-built database architecture. Eigenius is an open-source, typed knowledge-graph DBMS built on a single premise: answering the audit question ("what do you know, and what is your warranty?") requires a unified kernel. By tightly coupling the type system, storage engine, and integration protocol, Eigenius turns data provenance into a structural invariant rather than a property reconstructed across subsystem boundaries. The kernel rests on three pillars: a dependent type theory woven through the core, institutions acting as strongly typed integration boundaries, and a content-addressed immutable storage layer. On this foundation, epistemic status (declared/observed/derived/verified) is enforced as a strict commit-time invariant. Cross-system translations (comorphisms) are checked at commit and materialized directly into the graph as durable, first-class resources. To eliminate O(N^2) polystore bottlenecks, shared on-chain intermediate representations (IRs) collapse multi-system translations to identity. Crucially, this architecture unifies both domains of scientific epistemology: it relies on justification logic for empirical science, while embedding a fast, in-process term checker to safely evaluate formal mathematical proofs (via Lean 4) without IPC overhead. In an end-to-end recomputation of a published Nature study from fragile scripts to a materialized evidence graph, all 52 derived conclusions hold from pinned data, surfacing four machine-checked discrepancies in the original study.
