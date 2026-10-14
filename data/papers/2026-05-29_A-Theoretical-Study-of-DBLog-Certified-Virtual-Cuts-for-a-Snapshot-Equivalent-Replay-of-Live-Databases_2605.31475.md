# A Theoretical Study of DBLog: Certified Virtual Cuts for a Snapshot-Equivalent Replay of Live Databases

- arXiv ID: `2605.31475v1`
- Authors: Andreas Andreakis
- Published: 2026-05-29
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.31475v1) | [pdf](https://arxiv.org/pdf/2605.31475v1)

## Abstract

This paper is a theoretical follow-up to the 2019 DBLog paper, which introduced a change-data-capture (CDC) mechanism for both backfilling a downstream system from a live source database and streaming its ongoing changes, while the source keeps accepting writes. DBLog reads the table in primary-key range scans (chunks) interleaved with the source change log: watermarks locate each chunk in log order, chunk rows become refresh events, and CDC events repair stale chunk observations. The mechanism requires no table lock, no pause in writes, and no global read transaction, and has since been adopted by Debezium and Apache Flink CDC.
  The 2019 paper described the mechanism operationally but did not formalize its correctness object. This paper formalizes that object: DBLog constructs a snapshot-equivalent replay certificate without a single physical snapshot read.
  The central formal object is a certified virtual cut: a finite evidence bundle whose certified replay reaches the same per-key state as the source at a chosen frontier on a chosen key scope. A virtual cut is extensional: replay equality at a frontier, not a physical snapshot read, and does not assert one source timestamp across chunk rows. The paper proves per-key replay equality for every wellformed DBLog run at its frontier and scope, and that an accepted certificate, evaluated against faithful source observation, witnesses such a run and yields a virtual cut. It also proves a source-side continuation result: on the same scope, an established cut advances to later frontiers by appending the scope-filtered faithful CDC segment committed in between. Each result is Conditional on premises stated where the result appears. Whole-table correctness, exactly-once delivery, sink-state convergence, and transfer to named deployments are not consequences of certificate acceptance alone. All proofs are machine-checked in Isabelle/HOL.
