# Measuring What a Specification Determines: A Formal Semantic-Block Model and an Execution-Judged Benchmark

- arXiv ID: `2608.19475v1`
- Authors: Oleg Grynets, Dmytro Kostetskyi, Vasyl Lyashkevych
- Published: 2026-08-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2608.19475v1) | [pdf](https://arxiv.org/pdf/2608.19475v1)

## Abstract

This work introduces a formal semantic-block model for specifications and an execution-judged benchmark for evaluating specification quality independently of model capability. A specification is represented as a structure comprising semantic blocks, dependency relations, block-owned rules, decision points, and explicitly open questions, subject to four machine-checkable well-formedness conditions: acyclicity, single ownership, constraint domination, and totality or ambiguity-stop. Determinacy is defined model-theoretically as agreement among all conforming implementations and is estimated empirically through convergence across independent implementers. The model is instantiated on an Oracle-to-PostgreSQL migration specification containing 18 blocks and 19 dependency edges. Computational validation shows that the five-layer decomposition reduces mean per-task context by approximately 71% through dependency closures, covers 85.5% of the study-defined Oracle construct taxonomy with all identified gaps triaged, is not Pareto-dominated by the tested alternative partitions, and is recovered at the 99.9th percentile from citation-derived edges not used to define the original structure. The benchmark keeps the implementer panel fixed, includes a mandatory no-specification control arm, and uses PostgreSQL 16 and a live Oracle instance as deterministic execution judges. Six designed studies, including three pre-registered manipulations and three diagnostic analyses, further examine specification effects. Repeated runs on a 25-unit subsample reveal an empirical variability floor with a median arm-delta spread of 14.4 percentage points. The results support determinacy as a formal concept but not as a standalone empirical quality metric for the evaluated contemporary LLM implementers.
