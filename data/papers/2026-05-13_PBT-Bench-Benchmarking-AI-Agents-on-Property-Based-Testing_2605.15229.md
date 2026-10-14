# PBT-Bench: Benchmarking AI Agents on Property-Based Testing

- arXiv ID: `2605.15229v1`
- Authors: Lucas Jing, Xinqi Wang, Liao Zhang, Simon S. Du
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.15229v1) | [pdf](https://arxiv.org/pdf/2605.15229v1)

## Abstract

Existing code benchmarks measure whether an agent can produce any test that reproduces a known bug, or whether it can produce a
  patch that fixes a described issue. Neither isolates the distinct skill of property-based testing: deriving a semantic invariant
  from documentation, and then constructing an input-generation strategy precise enough to make a random search reveal the violation.
  We introduce PBT-Bench, a benchmark of 100 curated property-based testing problems across 40 real Python libraries. Each problem
  injects one or more semantic bugs (365 in total, mean 3.65 per problem) designed so that default-strategy random inputs almost
  never trigger them; the agent must read the library's documentation, identify the relevant invariant, and specify a Hypothesis
  @given strategy that concentrates mass in the trigger region. Bugs are stratified across three difficulty levels (L1-L3) spanning
  single-constraint boundary bugs to stateful, cross-function protocol violations. We evaluate eight contemporary LLMs under two
  prompting regimes (open-ended baseline vs. explicit Hypothesis scaffolding) for three independent runs per configuration. Bug
  recall under the PBT-guided prompt ranges from 42.1% to 83.4% across models; under the open-ended baseline, from 31.4% to 76.7%.
  Hypothesis scaffolding lifts mid-capability models by over 20 percentage points, but yields smaller gains for the strongest models,
  with two exceptions showing degradation, suggesting the structured prompt can interfere with certain model behaviours rather than
  complementing them. The hardest bugs prove model-specific: different architectures fail on different problems, leaving persistent
  gaps that no single model closes. We release the benchmark, harness, and full evaluation corpus to support downstream work on
  documentation-grounded semantic reasoning.
