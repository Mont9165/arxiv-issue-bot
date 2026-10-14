# EGREFINE: An Execution-Grounded Optimization Framework for Text-to-SQL Schema Refinement

- arXiv ID: `2605.00628v1`
- Authors: Jiaqian Wang, Yutao Qi, Wenjin Hou, Yu Pang, Rui Yang
- Published: 2026-05-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.00628v1) | [pdf](https://arxiv.org/pdf/2605.00628v1)

## Abstract

Text-to-SQL enables non-expert users to query databases in natural language, yet real-world schemas often suffer from ambiguous, abbreviated, or inconsistent naming conventions that degrade model accuracy. Existing approaches treat schemas as fixed and address errors downstream. In this paper, we frame schema refinement as a constrained optimization problem: find a renaming function that maximizes downstream Text-to-SQL execution accuracy while preserving query equivalence through database views. We analyze the computational hardness of this problem, which motivates a column-wise greedy decomposition, and instantiate it as EGRefine: a four-phase pipeline that screens ambiguous columns, generates context-aware candidate names, verifies them through execution-grounded feedback, and materializes the result as non-destructive SQL views. The pipeline carries two structural properties: column-local non-degradation, ensured by the conservative selection rule in the verification phase, and database-level query equivalence, ensured by the view-based materialization phase. Together they make the resulting refinement safe by construction at the column level, with cross-column and prompt-level interactions handled empirically rather than analytically. Across controlled schema-degradation, real-world, and enterprise benchmarks, EGRefine recovers accuracy lost to schema naming noise where applicable and correctly abstains where the underlying task exceeds current Text-to-SQL capabilities, with refined schemas transferring across model families to enable refine-once, serve-many-models deployment. Code and data are publicly available at https://github.com/ai-jiaqian/EGRefine.
