# Silent Instrument Errors Reorder Agent Leaderboards

- arXiv ID: `2611.04399v1`
- Authors: Yangze Liu
- Published: 2026-11-03
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.04399v1) | [pdf](https://arxiv.org/pdf/2611.04399v1)

## Abstract

On a public agent leaderboard, a general-purpose agent trails a scaffold built for an airline customer-service benchmark by 13 points on the tasks that touch its database, and a reader could conclude that generality costs accuracy. The gap comes from the grader. The general agent often ends its conversations in a way that never triggers grading, so only about half of its episodes were scored and the rest were stored as failures. Grading the ungraded half under the benchmark's own rule closes the pooled gap, without rerunning any agent. We audit two carefully maintained public leaderboards, HAL and tau2-bench, from their published artifacts alone and find three more instrument errors. A cost column counts nested model calls twice, unevenly across rows. Archived trajectories record grader-written actions as agent actions. Re-grading saved trajectories under a newer evaluator is itself a new measurement: a correct and announced fix reorders a leaderboard, and a mode check that misreads four files collapses their scores by 59 to 82 points while printing no error. Each produced a plausible number, and the HAL maintainers confirmed their three within five weeks. Together the cases show that the infrastructure of agent evaluation, meaning the code that grades, logs, replays and versions an evaluation, is part of the measurement and fails silently, so scores and orderings can move with no visible sign. These failure modes follow from how agent evaluation pipelines are built, and those pipelines change as fast as the agents they measure, so we expect more of them elsewhere. We propose cheap checks that expose the instrument: report the graded fraction, aggregate cost from root spans, tag the provenance of every recorded action, and pin evaluator versions with a published re-grade diff.
