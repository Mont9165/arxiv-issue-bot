# Agents Propose, Code Verifies, Humans Decide: Verified Agentic Ingestion of Heterogeneous Scientific Tables into Relational Databases

- arXiv ID: `2611.11045v1`
- Authors: Bharatha Rankothge, Suzanne Hodgkins, Virginia Rich, Michael Kirby
- Published: 2026-11-08
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `q-bio.QM`
- Links: [abs](http://arxiv.org/abs/2611.11045v1) | [pdf](https://arxiv.org/pdf/2611.11045v1)

## Abstract

Public scientific datasets rarely arrive analysis-ready. They arrive as messy folders of wide matrices, long tables, spreadsheets, and per-cohort files whose keys and encodings differ, and every reanalysis must reconnect them first. A coding agent can automate this, but its mistakes can look plausible, and without an audit trail, a mistake that corrupts data can go uncaught. We present an AI-assisted ingestion pipeline built on one rule: LLM agents propose, deterministic code verifies, and humans decide. Narrow agents see compact, citable evidence about the files, never the data, and return typed proposals. A verifier with 39 check types tests each proposal against that evidence in two loops, one for the schema's structure and one for its meaning, and a human reviewer approves the schema and the load. Code compiles PostgreSQL DDL, reshapes the data, quarantines rows it cannot place, records provenance, and reconciles every staged row against the database. On four public biomedical datasets, one held out from development, 9 of 20 first proposals failed a check and every failure was caught: the loops repaired eight, and a one-line reviewer edit fixed the ninth. All 45.1 million values loaded with zero reconciliation gap. Discovering a dataset's structure took 4-7 LLM calls and preparing its data at most one more, costing under $0.50 per dataset. In a separate test, each of nine planted data errors was quarantined with a reason or recorded in an audit log.
