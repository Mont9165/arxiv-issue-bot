# SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review

- arXiv ID: `2607.06065v1`
- Authors: Ruoyu Wang, Jierun Chen, Shaowei Wang, Chaofan Tao, Sidi Yang, Yuxin Jiang, Kim-Hui Yap, Lifeng Shang, Xiaohui Li, Haoli Bai
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06065v1) | [pdf](https://arxiv.org/pdf/2607.06065v1)

## Abstract

Coding agents increasingly generate pull requests (PRs) for real-world software issues, yet one-shot PR generation remains open-loop: the PR is proposed without systematic review, diagnosis, or revision. We introduce \textbf{SWE-Review}, a framework for closing this loop with agentic code review. Given an issue and an AI-generated PR, a reviewer agent explores the repository, decides whether the PR should be accepted, and provides structured feedback for revision. We evaluate this setting with our proposed \textbf{SWE-Review-Bench} to measure both review correctness and downstream revision usefulness. We further curate \textbf{SWE-Review-Traj} dataset to study broader applications of agentic review and fill the data-scarcity gap for open reviewer training. Experiments show that agentic review continuously improves PRs through a generate-review-revise loop, outperforms single-turn fixed-context review in both decision accuracy and resolve rate after revision, transfers beyond review to improve issue-resolution models, and enables effective and efficient test-time scaling. These results position agentic code review as a practical mechanism for moving AI coding agents from one-shot PR generation toward closed-loop issue resolution.
