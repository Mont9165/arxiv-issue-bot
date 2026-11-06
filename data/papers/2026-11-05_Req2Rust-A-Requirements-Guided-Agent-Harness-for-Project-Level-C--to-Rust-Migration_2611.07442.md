# Req2Rust: A Requirements-Guided Agent Harness for Project-Level C++-to-Rust Migration

- arXiv ID: `2611.07442v1`
- Authors: Shengbo Wang, Mingwei Liu, Yuwen Chen, Yanlin Wang
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07442v1) | [pdf](https://arxiv.org/pdf/2611.07442v1)

## Abstract

Memory-safety concerns make Rust an attractive target for modernizing legacy C/C++ systems, yet project-level C++ migration must balance semantic fidelity with Rust-oriented reconstruction. Source-structure-preserving migration can track low-level behavior, but it can also carry source-language organization, unsafe idioms, and project assumptions into Rust. Direct agent-based translation gives the model more freedom to construct a Rust project, but semantic coverage depends on the model identifying the source behaviors that must be preserved. This problem is especially acute for C++, where source behaviors are often hidden in object models, destructor-driven lifetime protocols, and other hard-to-localize C++ semantics. This paper presents Req2Rust, the first project-level LLM-based C++-to-Rust migration harness. Req2Rust first derives an evidence-grounded Migration Requirements Specification (MRS) that records the behaviors and constraints that must be preserved. It then synthesizes a Rust Design Specification (RDS) and realizes it as an initial Rust project. Because real projects contain implementation details and idioms that only become visible during build and validation, Req2Rust treats the initial Rust project as an executable refinement state. Compiler, semantic, and unsafe-reduction validators produce validation reports for improving buildability, behavioral alignment, and unsafe usage. We evaluate Req2Rust on general C++ projects and modules from the large-scale Openharmony codebase against a ClaudeCode baseline. Req2Rust produces buildable Rust crates in both settings and improves test pass rate from 69.5% to 91.9% on general projects and from 45.4% to 87.9% on Openharmony modules.
