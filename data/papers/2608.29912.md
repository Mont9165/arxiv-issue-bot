# Verification-Time Dependency on a Disappearing Evaluator

- arXiv ID: `2608.29912v1`
- Authors: Ho Wa Ku, Jameel Ahmed Siddiqui
- Published: 2026-08-30
- Primary category: `cs.CY`
- Categories: `cs.CY`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29912v1) | [pdf](https://arxiv.org/pdf/2608.29912v1)

## Abstract

AI governance and assurance often assume that a consequential model-mediated decision can be reconstructed or tested after the fact. That assumption may fail when the evaluator that produced the decision is no longer accessible in the same version and execution context. This paper develops three verification-time constructs derived from Execution Governance (EG) 3.0: Decision-State Commitment, Independent Verifiability, and Counterfactual Auditability. Independent reprocessing of released Study 2 artifacts reproduces two original within-family behavioural comparisons: 52.0% modal-decision reversal for Llama 3.1 8B versus Llama 3.3 70B (26/50) and 30.0% for GPT-OSS 20B versus GPT-OSS 120B (15/50). The corrected baseline establishes that these are within-family comparisons, not provider-established succession. Post-hoc re-pairing against Groq-designated migration paths yields 64.0% and 38.0% reversal, but these figures remain descriptive because the cross-family invocation parameters were asymmetric. A 22-event retirement census independently recomputes to median 16.45 months, mean 18.72 months, range 3.9-40.3 months, with 17/22 intervals below 24 months, while also showing that evaluator availability can differ by service surface. The joint contribution is an operational verification-time protocol and optional Verification-Time Preservation Package (VTPP) specifying what evidence to bind at authorization time, what a separately trusted verifier can substantiate later, how stability and paired counterfactual tests should be calibrated, and which semantic checks remain beyond JSON Schema validity. The protocol is downstream and non-authorizing: it does not alter the EG Core Formula, add a seventh live condition, or state jurisdiction-specific legal admissibility.
