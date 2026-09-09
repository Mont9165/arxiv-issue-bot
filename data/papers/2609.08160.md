# Generalized DBLog: A Verified Contract for Interleaving Database Rows with a Change Log

- arXiv ID: `2609.08160v1`
- Authors: Andreas Andreakis
- Published: 2026-09-08
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2609.08160v1) | [pdf](https://arxiv.org/pdf/2609.08160v1)

## Abstract

Change-data capture (CDC) feeds downstream systems like caches, search indexes, and data warehouses from a database's log of committed row changes. When bootstrapping, adding a table, or repairing downstream data, a pipeline must also copy existing rows. Merging this copy with the active log introduces the copy-to-log handoff problem. Changes must not fall through a gap, and older copied state must not overwrite a newer logged update or resurrect a deleted row. DBLog, developed at Netflix, addressed this problem by reading tables in chunks and interleaving those reads with the live log. Watermarks identify the changes that overlap each read, and the log wins when a copied row is stale. Debezium and Flink CDC have since adapted this design. Earlier work proved that applying the original algorithm's copied rows and logged changes in their emitted order reconstructs the source's rows, including the effect of every logged insert, update, and delete processed. Generalized DBLog asks when the same result holds for variants of that design. We state the conditions the source and capture implementation must satisfy. Once copying and reconciliation are complete, we prove that the result holds across all selected tables and key ranges even when their rows were read at different times. A single database snapshot is not required for the copy. Further logged changes advance the reconstructed state one event at a time. We establish these guarantees for classic watermarking, Debezium's signal-table and read-only modes, Flink CDC's parallel chunks, reads and dumps tied to exact log positions, and engine-consistent backups whose log position lies within known bounds. The complete theory is machine-checked in Isabelle/HOL, its core independently verified in Lean 4, and the protocols are also examined by bounded model checking in TLA+.
