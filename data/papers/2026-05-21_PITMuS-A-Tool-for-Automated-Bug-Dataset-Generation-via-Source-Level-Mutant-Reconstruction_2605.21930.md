# PITMuS: A Tool for Automated Bug Dataset Generation via Source-Level Mutant Reconstruction

- arXiv ID: `2605.21930v1`
- Authors: Tasfia Tasnim, Soneya Binta Hossain
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21930v1) | [pdf](https://arxiv.org/pdf/2605.21930v1)

## Abstract

LLM-based software engineering increasingly depends on executable, context-rich bug artifacts: paired correct and buggy code, methods under test (MUTs), documentation, and metadata. These artifacts support the training and evaluation of automated bug localization and repair techniques, testing and test oracle generation methods, and documentation-driven automation. Although curated benchmarks (e.g., Defects4J) remain valuable, they are static and increasingly vulnerable to contamination as code models are trained on large public corpora. A complementary strategy is to generate fresh, cutoff-aware datasets by selecting real system versions and injecting controlled bugs at the source level.
  Mutation testing is a natural basis for this strategy: it applies predefined mutation operators to programs and records whether the existing test suite detects each injected change. PIT is a state-of-the-practice mutation testing tool for Java that performs mutation at the bytecode level. This design makes mutation testing fast and practical, but PITMuS reports mutants primarily through XML, making them difficult to inspect, replay, or reuse as structured source-level dataset records. To address this gap, we present PITMuS, which combines PITMuS XML metadata with debug information from compiled Java class files to localize and reconstruct the source edit corresponding to each mutant. PITMuS then automatically produces structured datasets containing source-level buggy and fixed code pairs, documentation context, and metadata for downstream training and evaluation. Although we evaluate PITMuS on eight open-source Java systems, it can be applied to any Java system where PITMuS can be integrated.
