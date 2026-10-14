# Bespoke-Card: Why Tune When You Can Generate? Synthesizing Workload-Specific Cardinality Estimators

- arXiv ID: `2606.09361v1`
- Authors: Johannes Wehrstein, Anton Winter, Timo Eckmann, Carsten Binnig
- Published: 2026-06-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.09361v1) | [pdf](https://arxiv.org/pdf/2606.09361v1)

## Abstract

Cardinality estimators are built to support arbitrary schemas and workloads, forcing them to rely on generic statistics even when the schema and workload is known in advance, leaving optimizers prone to large errors and poor plans. We present Bespoke-Card, an agent-driven system that synthesizes workload-specific cardinality estimators as executable code: a planning agent designs the estimators strategies, a coding agent implements them, and a validator scores the estimates against true cardinalities and PostgreSQL estimates, forming a robust and deterministic harness. Going beyond naive prompting, Bespoke-Card uses structured q-error feedback, regression analysis, concrete outlier subplans, a curriculum isolating join-only, filter-only, and full-subplan errors, and archival selection of the best implementation. Injecting its estimates into the optimizer cuts total PostgreSQL runtime on JOB by 33% and reduces median q-error over all JOB subplans by 41%, while synthesizing a strong estimator in under one hour for less than $10. Bespoke-Card is opening a new avenue for cardinality estimation next to classical generic estimators and learned estimator architectures.
