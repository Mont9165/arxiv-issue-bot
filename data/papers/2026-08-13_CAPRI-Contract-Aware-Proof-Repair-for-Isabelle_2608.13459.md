# CAPRI: Contract-Aware Proof Repair for Isabelle

- arXiv ID: `2608.13459v1`
- Authors: Jim Woodcock, Gabriel Leite, Augusto Sampaio, Ran Wei
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2608.13459v1) | [pdf](https://arxiv.org/pdf/2608.13459v1)

## Abstract

We address the use of large language models (LLMs) to help discover Isabelle proofs. An Isabelle build establishes that the submitted theory is accepted, but not that an LLM changed only what the developer authorised. We present CAPRI, a contract-aware repair workflow in which Isabelle checks the proof and an independent checker enforces a machine-readable edit contract. Prompts, proposals, candidate repositories, diagnostics, verdicts, and hashes are retained for audit. We evaluate five workflows on twelve failed proofs from four developments, with three replicates per task and condition, giving 180 runs and 138 valid repairs. Of 144 terminal candidates accepted by Isabelle, six had modified protected text; all arose in iterative workflows that could edit a complete theory. A proof-body-only interface produced 29/36 valid repairs and no contract violations, compared with 31/36 for the corresponding full-theory workflow. One-shot repair produced 22/36, while a later prospectively frozen iterative workflow produced 32/36; these figures compare complete workflows rather than individual mechanisms. A separate post hoc OpenRouter campaign found no improvement in the designated Luna comparisons. A Sol configuration with matched demonstrations produced 33/36 repairs, compared with 29/36 in the frozen OpenAI Responses condition, but the difference was not statistically significant in a one-sided exact McNemar test ($p=0.0625$).
