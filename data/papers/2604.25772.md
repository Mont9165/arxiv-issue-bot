# Scenario-based System Testing for Distributed Robotics Applications

- arXiv ID: `2604.25772v1`
- Authors: Jan Peleska, Felix Brüning, Wen-Ling Huang, Anne E. Haxthausen
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.25772v1) | [pdf](https://arxiv.org/pdf/2604.25772v1)

## Abstract

We present the SCenario Specification Language (SCSL) for automated generation and execution of system-level tests. SCSL targets complex distributed systems (e.g., collaborating autonomous robots) where classical model-based testing becomes impractical because (1) the overall system complexity is too high for a single monolithic model, (2) test behaviour cannot be fully precomputed due to substantial nondeterminism in the distributed system under test (SUT), and (3) the SUT configuration may change dynamically at runtime. Challenge (1) is addressed by scenarios: each scenario specifies test-specific expected SUT behaviour and/or stimuli to be applied during execution. Complex system tests are composed from elementary scenarios using sequential and parallel composition. To address (2), the SCSL tool platform supports online (on-the-fly) testing, selecting and executing test steps during runtime. For (3), SCSL provides a collaboration construct that supports dynamic reconfiguration: removing unavailable components, registering newly joining components, and rewiring interfaces during test execution. We illustrate the syntax and semantics of SCSL using a system-test example in which robots perform a salvage mission, and we use an automatically generated test execution to demonstrate the concepts supported by our prototype tool platform.
