# PROGRESS: Property-Guided Regression Search for Semantic Falsification

- arXiv ID: `2607.27359v1`
- Authors: Davis Tocheuk Mo, Noshin Ulfat, Matthew B. Dwyer, Soneya Binta Hossain
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27359v1) | [pdf](https://arxiv.org/pdf/2607.27359v1)

## Abstract

Search-based regression-test generation effectively explores complex program structures, yielding high structural coverage, but its oracles are derived from the system under test: faults already present are recorded as expected behavior rather than exposed. Property-based testing offers independent semantic oracles, but depends on high-quality properties and gives little guidance for reaching deep states or satisfying selective preconditions.
  We present PROGRESS (PROperty-Guided REgression Search for Semantic Falsification), integrating intent-driven properties into coverage-guided, search-based evolutionary test generation to reach deep program states and detect violations of intended behavior. PROGRESS (1) extracts intent-bearing code context and uses a language-model pipeline to generate executable jqwik properties while limiting implementation leakage; (2) extends EvoSuite's DynaMOSA with a search objective and property-aware fitness function per property, rewarding progress through preconditions and prioritizing falsifying executions; and (3) binds property parameters and uses jqwik-provided generators to connect quantified inputs to evolving test sequences, steering generation toward coverage and bug-detection goals.
  We evaluate PROGRESS on 25 large-scale Java systems against regression-test generation, standalone property-based testing, and context ablations. PROGRESS detects 328/562 current-version bugs (58%) versus none for regression-test generation, and satisfies all preconditions for 70/150 hard-to-reach properties versus 18 for standalone jqwik. Ablations show documentation and caller/callee context are key to generating valid executable properties. PROGRESS preserves structural exploration while exposing faults missed by regression-derived assertions; we release a comprehensive artifact package.
