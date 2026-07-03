# Kani: A Model Checker for Rust

- arXiv ID: `2607.01504v1`
- Authors: Rémi Delmas, Zyad Hassan, Qinheping Hu, Rahul Kumar, Felipe R. Monteiro, Thanh Nguyen, Adrián Palacios, Celina Val, Michael Tautschnig, Justus Adam, Daniel Schwartz-Narbonne, Carolyn Zech
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LO`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.01504v1) | [pdf](https://arxiv.org/pdf/2607.01504v1)

## Abstract

Rust's ownership type system prevents memory errors in safe code, but certain desirable properties remain orthogonal to compilation: the soundness of unsafe operations (e.g., raw pointer dereferences), functional correctness, and absence of runtime panics. We present Kani, an open-source model checker for Rust that pushes bounded model checking beyond bug-finding to provide correctness guarantees for these properties. Kani compiles proof harnesses from Rust's Mid-level Intermediate Representation (MIR) into CBMC's bit-precise verification engine, automatically checking a comprehensive set of safety properties with no user annotation. To extend verification from bounded to unbounded, Kani provides a specification language comprising function contracts, loop contracts, quantifiers, and function stubbing. We demonstrate feasibility through case studies on industrial Rust projects, where contracts upgraded verification from panic-freedom to functional correctness, uncovering six previously unknown bugs. Kani operates at scale in production CI, with over 16,000 harnesses verified per code change in the Rust standard library verification campaign.
