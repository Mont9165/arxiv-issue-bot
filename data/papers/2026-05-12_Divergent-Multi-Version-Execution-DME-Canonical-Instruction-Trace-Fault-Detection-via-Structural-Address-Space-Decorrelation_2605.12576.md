# Divergent Multi-Version Execution (DME): Canonical Instruction-Trace Fault Detection via Structural Address-Space Decorrelation

- arXiv ID: `2605.12576v1`
- Authors: Petro Baran Yrievich
- Published: 2026-05-12
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.12576v1) | [pdf](https://arxiv.org/pdf/2605.12576v1)

## Abstract

Traditional redundancy (lockstep, TMR) executes identical binaries with identical memory layouts. A single correlated fault - for example, an arbitrary program counter value or a perturbation delta-PC in all replicas - redirects all replicas along the same incorrect path. The same applies to corruption of data pointers. Both types of faults, regardless of their origin (deliberate tampering, software bug, compilation bug, or physical disturbance), cause silent data corruption and erroneous program execution. This work presents Divergent Multi-Version Execution (DME), a runtime semantic consistency verifier for diversified executions. Each replica is compiled independently, producing different code and data memory layouts while preserving identical semantics. Faults are detected by comparing canonical instruction traces, which include opcodes, register identifiers, loaded/stored values, and results, while discarding layout-dependent addresses.
