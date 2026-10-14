# Model-Driven Requirements Configuration with Three-Valued Uncertainty Scoring

- arXiv ID: `2607.26220v1`
- Authors: Ahmed Ibrahim
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.26220v1) | [pdf](https://arxiv.org/pdf/2607.26220v1)

## Abstract

Context: Large Language Models (LLMs) offer natural-language flexibility for automated requirements elicitation but frequently generate structurally invalid requirements and logical inconsistencies, lacking formal correctness guarantees.
  Objectives: This study aims to eliminate logical inconsistencies and enforce structural conformance in LLM-generated requirements while quantifying the LLM's pre-validation decision uncertainty within a formal domain model.
  Methods: We present a neuro-symbolic multi-agent architecture that operationalizes the Object-Oriented Method for Requirements Authoring and Management (OOMRAM) lattice. The LLM acts as a non-deterministic heuristic for lattice traversal, while a deterministic symbolic validator enforces all structural constraints. We introduce a three-valued (T, I, F) -- Truth, Indeterminacy, Falsity -- framework to classify and score the LLM's requirement decisions before and after validation.
  Results: Evaluated across 37 natural-language project visions in eleven application families, the system completely eliminated structural inconsistencies in 35 out of 37 cases (94.6%), with the remaining two containing only 6 unresolved structural errors (0.39% of decisions) due to iteration limits. Three-valued analysis revealed that 24.7% of all decisions are indeterminate -- structurally valid but discretionary choices not explicitly mandated by the stakeholder.
  Conclusion: Offloading structural integrity to a deterministic symbolic layer successfully guarantees structural conformance, while the three-valued classification provides a formal way to measure neural uncertainty, facilitating safe LLM deployment in formal requirements engineering.
