# Instruction Adherence in Coding Agent Configuration Files: A Factorial Study of Four File-Structure Variables

- arXiv ID: `2605.10039v1`
- Authors: Damon McMillan
- Published: 2026-05-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.10039v1) | [pdf](https://arxiv.org/pdf/2605.10039v1)

## Abstract

Frontier coding agents read configuration files (CLAUDE.md, AGENTS.md, Cursor Rules) at session start and are expected to follow the conventions inside them. Practitioners assume that structural choices (file size, instruction position, file architecture, contradictions in adjacent files) measurably affect adherence. We report a systematic factorial study of these choices using four manipulated variables, measuring compliance with a trivial target annotation across 1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases, three frontier models (primarily Sonnet 4.6, with Opus 4.6 as a CLI-matched cross-model check and Opus 4.7 reported descriptively under a CLI-version confound), and five coding tasks. We use mixed-effects models with a Bayesian companion.
  None of the four structural variables or three two-way interactions produces a detectable contrast after multiple-testing correction. Size and conflict nulls are supported by affirmative-null Bayes factors (BF10 between 0.05 and 0.10); position and architecture nulls are failures to reject without Bayes-factor support.
  The largest effect we measured is within-session: each additional function the agent generates is associated with approximately 5.6% lower odds of compliance per step (OR = 0.944) within the session-length range we tested, though the relationship is non-monotonic rather than a constant per-step effect. This reproduces on a second TypeScript codebase and on Opus 4.6 at matched configuration; it was identified during analysis rather than pre-specified. Within the conditions tested, file-structure variables did not produce detectable contrasts; compliance varies systematically between coding tasks and across each session's sequence of generated functions.
