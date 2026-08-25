# DAGSmith: Dependency-Aware Rewriting for dbt-Style SQL Pipelines

- arXiv ID: `2608.22551v1`
- Authors: Jie Liu, Lin Ma, Barzan Mozafari
- Published: 2026-08-23
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.22551v1) | [pdf](https://arxiv.org/pdf/2608.22551v1)

## Abstract

Modern analytics is increasingly organized as recurring SQL pipelines rather than isolated SQL statements. Tools such as dbt, which have gained extreme popularity in recent years, allow teams to write each transformation as SQL and make dependencies between transformations explicit, producing directed acyclic graphs (DAGs) with hundreds or thousands of interdependent SQL models. Traditional query optimizers and source-to-source query rewriters operate on one query at a time, while materialized-view selection and multi-query optimization address narrower forms of reuse. They do not exploit the pipeline-level information exposed by explicit dependencies: how intermediate results are consumed, which downstream outputs depend on each computation, where expensive work sits relative to data reduction, which results are worth persisting, and how refresh schedules relate to input change and output demand.
  We introduce DAGSmith, to the best of our knowledge the first holistic dependency-aware source-to-source rewriting system for SQL pipeline DAGs. DAGSmith treats explicit dependencies as optimization signals. It analyzes each transformation with its upstream inputs, downstream consumers, and position in the pipeline DAG, uses an LLM to propose pipeline-level refactorings, separates SQL generation and equivalence checking to reject unsafe rewrites, retunes persistence choices with a learned cost model, and selects a globally compatible, conflict-free set of rewrites. This enables dependency-edge simplification, non-local semantic reuse, downstream-aware pruning, pipeline-aware work placement, rewrite-materialization co-optimization, and frequency-aware optimization. On the open-source Tuva dbt project, DAGSmith reduces elapsed time by 42.6% and warehouse compute cost by 67.7%, 98.1%/348.3% larger than state-of-the-art single-query rewriting.
