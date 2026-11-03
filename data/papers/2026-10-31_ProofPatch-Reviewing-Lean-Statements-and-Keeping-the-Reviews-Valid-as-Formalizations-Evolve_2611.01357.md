# ProofPatch: Reviewing Lean Statements and Keeping the Reviews Valid as Formalizations Evolve

- arXiv ID: `2611.01357v1`
- Authors: Xujun Che, Depeng Xu, Jian Xiang, Taufiqua Khan
- Published: 2026-10-31
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.01357v1) | [pdf](https://arxiv.org/pdf/2611.01357v1)

## Abstract

The kernel of the Lean proof assistant checks that a proof establishes its statement. Whether the statement says what was intended is left to human reviewers. This is the old problem of validating a specification, and it grows more pressing as language models write formal statements in bulk and agents edit formal developments continuously. We present ProofPatch, a tool that helps reviewers judge Lean statements and keeps their judgments valid while the development changes. A reviewer can ask the kernel targeted questions about a statement, such as whether a hypothesis is needed or whether a counterexample exists. Each decision is stored with fingerprints of the statement as Lean elaborated it and of the definitions it depends on, and any declaration can be pinned so that a patch changing it is blocked, whether a person or an agent built on a large language model (LLM) wrote the patch. Working on elaborated terms rather than source text is the central design choice: notation and formatting changes leave a decision intact, and a changed definition reaches every theorem that uses it. On 229 pairs of consecutive revisions of Mathlib, Lean's mathematics library, ProofPatch sends 118 of 12,898 synthetic decisions back for review. Every text-based alternative misses at least 38 of these or sends back at least 13 times as many. On 1,527 labeled statements, kernel evidence flags unfaithful ones with precision 0.88 to 0.96, and in 344 runs of an LLM agent no change to a pinned statement got through.
