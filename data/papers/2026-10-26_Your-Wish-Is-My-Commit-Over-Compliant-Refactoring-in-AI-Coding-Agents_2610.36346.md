# Your Wish Is My Commit: Over-Compliant Refactoring in AI Coding Agents

- arXiv ID: `2610.36346v1`
- Authors: Haocong Jiang, Sadra Sabouri, Sepand Haghighi, Souti Chattopadhyay
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2610.36346v1) | [pdf](https://arxiv.org/pdf/2610.36346v1)

## Abstract

Large language models are known to be sycophantic, over-complying with users even when doing so is unproductive. When these models act as coding agents, this can be costly: an agent that keeps editing after no edit improves the code writes churn, technical debt, and review burden into the codebase. Yet the consequences of sycophancy in software engineering remain largely understudied. To understand them, we run a controlled study of iterative refactoring, an open-ended task with no stopping criterion, where any edit an agent makes once the code is already clean reflects compliance rather than improvement. Across algorithmic (n=50) and object-oriented (n=10) suites, we repeatedly ask two widely used agents, Codex and Claude Code, to refactor further across five models. Over 3,000 turns, we define six behavioral signals of over-compliance. We hypothesized that a capable agent would stop once it recognized an optimized codebase; none did. Every model kept editing, rewriting up to 31x the original codebase before first stopping and resuming edits even after declaring the task complete. Over-compliance is a costly, multi-turn behavior that compounds with every turn, and our six signals give developers and tool builders a way to detect and curb it.
