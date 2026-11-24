# Admitted Is Not Effective: Lessons from a Notary-Gated Retrospective Loop in an Agentic Pipeline

- arXiv ID: `2611.29727v1`
- Authors: Lo Gullstrand Heander, Emma Söderberg, Christofer Rydenfält
- Published: 2026-11-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.29727v1) | [pdf](https://arxiv.org/pdf/2611.29727v1)

## Abstract

Agentic software development pipelines with frozen prompts can repeat the same mistakes across pull requests (PRs), yet ungoverned additions to instruction files grow without bound and do not generally improve task success. We present a retrospective loop for a four-stage large language model (LLM) pipeline in which a Retrospective agent proposes edits to learned rules every ten PRs and a Notary admits, merges, or rejects them while recording each decision in a provenance ledger. In a pre-registered study of 880 PRs on two Python repositories, the loop ran end to end and the Notary admitted 55 of 89 proposals, rejecting 8 that cited nonexistent evidence.
  However, held-out review comments and hidden-test resolution did not improve after ten retrospectives. Tracing each step of the loop, we found that sparse review signal (0.45 comments/PR) left little to learn from and that rules admitted on their stated evidence did not show measurable held-out effects. We derive six lessons and argue that governed loops should admit and retire every learned rule as a testable hypothesis.
