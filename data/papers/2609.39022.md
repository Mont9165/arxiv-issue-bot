# From Verification Failures to Reusable Guidance for Coding Agents

- arXiv ID: `2609.39022v1`
- Authors: Yuqing Zhai, Xiaohong Chen, Lingming Zhang, Sriram Vishwanath, Grigore Rosu
- Published: 2026-09-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2609.39022v1) | [pdf](https://arxiv.org/pdf/2609.39022v1)

## Abstract

Coding agents need to establish that a program satisfies a specification and that the specification captures the requested behavior. We study how expert diagnosis of verification failures can become reusable guidance for this work. Our approach combines executable language definitions in the K framework with a kit of procedures for constructing specifications, repairing proofs, and auditing their adequacy. A human-guided development campaign on HumanEval, a benchmark of 164 Python programming tasks, achieves a 164/164 success rate with the semantics and the kit, measured by final AI audit Pass verdicts after two targeted repairs. To examine whether auditing detects problems that successful proofs leave unresolved, we construct 12 author-reviewed pairs of clean and defective packages. Every package passes its K proofs, and completed audits identify all defects and accept all clean packages. We then use KleverBench to test specification and proof construction for 31 programs with changed operator meanings. Comparisons with complete acceptance rules and equally long generic advice yield mixed results across two model and budget settings, motivating further work on selecting useful guidance within resource limits. Human-reviewed Optimism proofs establish expected pause reverts for six operations within declared input bounds under London semantics with unbounded gas. We report progress, difficulties, and lessons toward agents that deliver programs with checkable correctness arguments.
