# Neurosymbolic Auditing of Natural-Language Software Requirements

- arXiv ID: `2605.13817v1`
- Authors: Bethel Hall, William Eiers
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.13817v1) | [pdf](https://arxiv.org/pdf/2605.13817v1)

## Abstract

Natural-language software requirements are often ambiguous, inconsistent, and underspecified; in safety-critical domains, these defects propagate into formal models that verify the wrong specification and into implementations that ship unsafe behavior. We show that large language models, equipped with an SMT solver, can audit such requirements: translating them into formal logic, detecting ambiguity through stochastic variation in the generated formalization, and exposing inconsistency, vacuousness, and safety violations through solver queries on the resulting specification. We present VERIMED, a neurosymbolic pipeline that operationalizes this idea for medical-device software requirements, and report two findings. First, stochastic variation across independent formalizations is a signal of ambiguity: requirements that admit multiple plausible interpretations produce SMT-inequivalent formalizations, and bidirectional SMT equivalence checking turns this disagreement into a solver-checkable test. Second, the usefulness of symbolic feedback depends on its granularity: in counterexample-guided repair on a hemodialysis question-answering benchmark, concrete SMT counterexamples raise verified accuracy from 55.4% to 98.5%. Over an extensive experimental evaluation on open-source hemodialysis safety requirements, we show that the LLM-based approach in VERIMED successfully reduces ambiguity-sensitive requirements and enables rigorous auditing of software requirements through SMT-based queries.
