# All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code

- arXiv ID: `2606.18168v1`
- Authors: Dipayan Banik, Kowshik Chowdhury, Shazibul Islam Shamim
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.18168v1) | [pdf](https://arxiv.org/pdf/2606.18168v1)

## Abstract

Software practitioners increasingly use AI coding agents that generate test code alongside production code in open source pull requests (PRs). Recent studies report more than 932,000 agent-authored PRs across more than 116,000 repositories, yet whether their test files contain meaningful verification logic remains underexplored. Test files lacking explicit assertions execute code without verifying behavior, so quality gates based on test-file presence overestimate verification strength. The goal of this paper is to help practitioners assess the verification strength of agent-authored patches by characterizing oracle signals and their link to merge outcomes and review effort. We conduct an empirical study of 86,156 test-file patches from 33,596 agent-authored PRs across 2,807 GitHub repositories produced by five coding agents: OpenAI Codex, GitHub Copilot, Devin, Cursor, and Claude Code. A qualitative analysis of 384 stratified patches informs a syntactic taxonomy of eight oracle signal categories. Applied at scale, 80.2% of test patches contain weak or no explicit oracle signals. While raw merge rates are lower for strong-oracle PRs, a regression analysis adjusting for agent, PR size, repository popularity, task type, and language shows strong oracles significantly improve merge likelihood (OR = 1.28, p < 0.001). Our findings suggest that test file counts substantially overestimate verification strength and that practitioners can adopt oracle-aware quality checks to more accurately evaluate agent-authored contributions.
