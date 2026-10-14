# Bounded Semantic Planning and Deterministic Compilation for Reliable Enterprise Text-to-SQL

- arXiv ID: `2608.16663v1`
- Authors: Yi Ai
- Published: 2026-08-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.16663v1) | [pdf](https://arxiv.org/pdf/2608.16663v1)

## Abstract

Direct text-to-SQL asks a language model to do two jobs: interpret the business question and construct the complete relational query. In enterprise schemas, SQL can execute successfully while using the wrong relationship role or aggregation grain. We study an alternative placement of the stochastic boundary. A multi-turn planner grounds phrases and selects from question-specific governed options; graph traversal, role predicates, grain lowering, SQL construction, and deterministic checks are implemented in code. We evaluate this semantic path compilation (SPC) system against direct DDL-to-SQL generation on the ACME insurance benchmark. On a 38-question adjudicated comparison set with three runs per question, SPC was adjudicated correct on every run for 37 questions (97.4%), compared with 21 (55.3%) for the baseline. The paired discordance was 16 questions in favor of SPC and none in favor of the baseline (two-sided exact McNemar p=3.05x10^-5). SPC answered all 38 questions correctly at least once and produced one refusal and no adjudicated wrong-but-executed run across 114 run outcomes; the baseline produced 29 adjudicated wrong runs and seven additional judge-flagged data-only coincidences on the same set. A strict-equivalence sensitivity analysis increased the paired difference. Additional SPC runs with GPT-5.4 and Gemini-3.6-Flash showed similar question-level robustness, although their per-run verdict artifacts were not preserved. Six additional benchmark items are retained in an all-item analysis and documented separately by failure class. The study supports an end-to-end systems result, not a causal claim that compilation alone produced the gain, because SPC receives governed semantic artifacts that the DDL baseline does not.
