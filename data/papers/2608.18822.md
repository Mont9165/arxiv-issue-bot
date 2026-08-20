# Contract-Aware Rescue of a Drifted Isabelle Development: The Double-Tank Case Study

- arXiv ID: `2608.18822v1`
- Authors: Jim Woodcock, Gabriel Leite, Augusto Sampaio, Ran Wei
- Published: 2026-08-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.18822v1) | [pdf](https://arxiv.org/pdf/2608.18822v1)

## Abstract

Large language models can propose proofs for interactive theorem provers, but a successful build does not show the surrounding verification task was preserved. We study this problem in an Isabelle development of a sampled-data double-tank controller. The work began with nine theories and ten unfinished obligations, grew to a 16-theory build without sorry, oops, added axiomatisation, or oracle use, and accumulated 23 stable and 36 broken proof states. A retrospective audit found material changes in 16 of the 100 original declarations, including a weakened end-to-end assurance theorem that assumed three of the four requirements in its conclusion. We used CAPRI, a contract-aware proof-repair tool, to govern a reconstruction by combining Isabelle acceptance with an independent check of repository changes against machine-readable edit contracts. The reconstruction discharged all ten scoped obligations within the original nine-theory structure. A secondary replay by a co-author reproduced the R10 build, contract checks, control tests, and principal audit findings; independent replication remains future work. Operational end-to-end verification remains incomplete: we still need to connect operational executions to the reconstructed quantitative trace contract, a task requiring an extended contract.
