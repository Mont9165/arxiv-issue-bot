# Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work

- arXiv ID: `2606.17099v1`
- Authors: Vincent Schmalbach
- Published: 2026-06-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.17099v1) | [pdf](https://arxiv.org/pdf/2606.17099v1)

## Abstract

AI coding agents increasingly accept assigned software tasks, modify repositories under bounded authority, and return work packages for review. Prior work proposed the software delegation contract, covering the task, authority, returned work package, and acceptance context, as the unit of analysis for delegated coding work, but did not measure its effects. This paper reports a controlled pilot study of explicit delegation contracts for coding agents. We built a dependency-free TypeScript API task environment with seeded defects and documentation gaps, authored ten tasks across five families, and ran 64 agent executions across two model tiers under three conditions: a realistic issue-style prompt, an explicit delegation contract, and a contract with a required evidence bundle. Each run was scored with hidden acceptance tests, mutation checks, and scope analysis, then reviewed by three independent condition-blinded model-based reviewers using a fixed rubric, for 192 reviews. Explicit contracts did not improve objective task outcomes: all 64 runs passed hidden acceptance checks, with zero scope violations. They did improve reviewability. Evidence sufficiency improved in 22 of 30 paired comparisons and worsened in none (+0.83 on a 5-point scale, p < 0.0001, Cliff's delta = 0.66); reviewer ambiguity decreased (p = 0.035); changed-file lists, known-limitations sections, residual-risk sections, and reviewer checklists appeared mostly or only when demanded by the contract. Contracts cost +13% agent tokens and +38% wall-clock time, with larger effects for the weaker model tier. On these small tasks, delegation contracts bought reviewability rather than correctness.
