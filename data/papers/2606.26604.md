# Quantum Mutant Equivalence via Transpilation

- arXiv ID: `2606.26604v1`
- Authors: José Campos, Andriy Miranskyy
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.26604v1) | [pdf](https://arxiv.org/pdf/2606.26604v1)

## Abstract

Mutation testing evaluates test suite quality by introducing artificial faults (mutants) and checking whether tests detect (kill) them. A central challenge is the equivalent mutant problem: some mutants are syntactically different from the original program but semantically identical to it and therefore cannot be killed by any test. If left unidentified, such mutants waste testing effort and distort mutation scores. In quantum software, mutation testing is increasingly used, but the equivalent mutant problem remains unsolved. A recent study generated more than 700,000 quantum circuit mutants and found that roughly half survived the available tests, making it unclear whether these survivors reflect weak tests or semantic equivalence. We propose Transpiler-Based Equivalence (TBE), a lightweight approach that identifies equivalent quantum mutants by transpiling original and mutated circuits under the same configuration and comparing their resulting OpenQASM code. We evaluate TBE on 348,299 surviving mutants, 92,011 of which are equivalent; TBE identifies 29,536 of them (32.1%) as equivalent while achieving 100% precision and 82% accuracy.
