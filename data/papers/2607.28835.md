# From C to Idiomatic Rust: A Ship-of-Theseus Agentic Translation

- arXiv ID: `2607.28835v1`
- Authors: Vasily A. Sartakov
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.OS`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.28835v1) | [pdf](https://arxiv.org/pdf/2607.28835v1)

## Abstract

C underpins operating systems, embedded platforms, and network infrastructure because its abstractions map directly to machine behaviour. Its explicit memory model, predictable data representations, and minimal runtime allow compilers to generate fast, deterministic code. These properties also leave correctness and memory safety entirely to the programmer, making undefined behaviour, pointer misuse, and lifetime errors persistent sources of defects and security vulnerabilities in long-lived C codebases. Rust eliminates most of failure modes through a static ownership and borrowing model that enforces memory safety and aliasing constraints at compile time. However, mature C systems cannot be translated directly: implicit layout assumptions, aliasing patterns, and undefined behaviour must be reconstructed before safe Rust can be produced.
  This paper presents a migration methodology that first generates a semantics-preserving, non-idiomatic Rust baseline and then incrementally rewrites it into idiomatic Rust using agentic AI, validating each step through compilation and behavioural testing. Applied to iodine (12.5k SLOC), the approach demonstrates that reliable C-to-Rust migration is a structured transformation workflow rather than a single translation step.
