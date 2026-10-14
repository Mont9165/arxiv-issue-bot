# Machine-Checked Dual-Write Recovery from a Committed Log

- arXiv ID: `2608.00501v1`
- Authors: Andreas Andreakis
- Published: 2026-08-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2608.00501v1) | [pdf](https://arxiv.org/pdf/2608.00501v1)

## Abstract

After a crash, a delivery process faces a question its own database cannot answer: did the other side already receive the effect? Transactional outboxes and change data capture remove the application's dual write, but the relay they introduce delivers and records its own progress as two separate durable acts, so the same decision reappears one stage later.
  Practitioners have handled this boundary for a decade with retries, checkpoints, idempotency keys, and fencing, and the operational advice is largely sound. What has been missing is a precise account of when it works: the exact event the guarantees refer to, the evidence they require, and how long that evidence lasts. This paper supplies the missing account as a machine-checked theory, developed in Isabelle/HOL.
  At its heart is an information bound. Two reachable post-crash states can agree on everything the crashed side durably knows and still differ in what the sink accepted, so any recovery decision computed from that side must duplicate a delivery or leave one owed. This is not a story about sloppy bookkeeping: a single deterministic deliver-then-checkpoint protocol, its own durable cursor included in what recovery reads, is defeated by crash timing alone. Reading the sink's accepted record escapes the bound exactly, under stated premises. The answer can then go stale -- an old request still in flight, a second recoverer racing the first -- and each hazard has its own proved fence at the sink's acceptance boundary, the cost of fencing itself a theorem. Finally, the guarantee has a lifetime: bounded deduplication memory and truncated source history each void it in a proved way. The resulting test for any exactly-once recovery claim is short: what did the sink accept, what can still change that answer, and how long will the evidence survive?
