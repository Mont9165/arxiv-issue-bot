# Lie to Me: Finding Bugs in ZK DSL Toolchains with Adversarial Witness Injection

- arXiv ID: `2608.30648v1`
- Authors: Sebastian Watzinger, Christoph Hochrainer, Valentin Wüstholz, Maria Christakis
- Published: 2026-08-31
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30648v1) | [pdf](https://arxiv.org/pdf/2608.30648v1)

## Abstract

Zero-knowledge domain-specific language (ZK DSL) toolchains compile programs into constraint systems and generate witnesses for cryptographic proofs. Bugs in these toolchains can leave the enforced constraints weaker than the source-program semantics, admitting proofs for invalid executions. Such soundness bugs may remain invisible to valid-execution testing because all valid executions still behave correctly.
  We present Liezz, a testing framework that generates ZK DSL programs and exposes these bugs through adversarial witness injection. For each generated deterministic program, Liezz executes two public input assignments with different outputs and splices their witnesses, combining the input of one execution with the output of the other. The resulting witness is invalid by construction. A correct toolchain must reject it; acceptance exposes a soundness bug. Controlled divergence and multiple witness-splicing strategies preserve enough consistency to expose missing constraints. Liezz also generates parameterized standard-library calls to reach complex functionality.
  Liezz supports Circom, Corset, Gnark, and Noir. It finds 13 bugs, including seven with soundness impact. Several are reachable only through generated standard-library calls. Under the same testing budget, a valid-execution baseline does not expose any of the soundness failures revealed by accepted injected witnesses, showing that adversarial witness injection reaches failures missed by valid-execution testing.
