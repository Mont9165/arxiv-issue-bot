# Passing Tests, Missing Semantics: Evidence of Interpretive Lock-In in Plan-Based DataFrame Code Generation

- arXiv ID: `2610.15797v1`
- Authors:  Jingjing,  Liu, Dishu Yang, Hongbo Qin, Hansong Zhang
- Published: 2026-10-11
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.15797v1) | [pdf](https://arxiv.org/pdf/2610.15797v1)

## Abstract

Planning and revision are intended to bring generated code closer to the task specification. Yet a mistaken interpretation can persist across the plan, implementation, and tests - a pattern we call interpretive lock-in. We investigate this risk on 30 DataFrame tasks derived from TPC Benchmark DS, comparing Frozen One-Pass, Test-Guided Revision, and PlanAudit-Guided Revision. Test-pass counts rose from 22/30 to 29/30 and 30/30, yet no generated solution matched its stored reference output. Evaluator controls returned the expected outcome in 57/57 cases. Same-engine SQL re-execution reproduced 28/30 references; all 77 test-passing runs on these tasks still failed reference agreement. PlanAudit-Guided Revision improved code scores on 3/30 tasks and test coverage on 11/30, but the median paired change was zero for both measures. Failure analysis revealed tests that omitted requirements, adopted candidate-defined schemas, used nondiscriminating fixtures, or repeated the implementation's incorrect logic. Fresh generation on ten targeted tasks produced 0/30 reference matches and 25/25 false passes among test-passing runs. These findings are diagnostic rather than causal: the pipelines differ in feedback, grounding, call budgets, and editing permissions, and the study uses one model and one primary generation per eligible task. Because pre-adjudication human labels were not retained, inter-rater agreement cannot be reconstructed and the mechanism analyses remain exploratory. Overall, increasingly successful self-generated tests did not establish semantic correctness, even after excluding unreproduced references.
