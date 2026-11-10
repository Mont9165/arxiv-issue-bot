# Replay Fidelity in LLM Agent Evaluation: Randomness, Hidden State, and Test Oracles in AppWorld

- arXiv ID: `2611.11216v1`
- Authors: You Liu, Quanchao Lu
- Published: 2026-11-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.11216v1) | [pdf](https://arxiv.org/pdf/2611.11216v1)

## Abstract

Reproducibility in large language model (LLM) agent evaluation depends on replay fidelity: which parts of an execution trace are reconstructed, controlled, and compared. This matters for agent debugging, failure analysis, and counterfactual evaluation of stateful tool use. We audit all 71 unsuccessful executions in a fixed historical AppWorld corpus using 284 isolated fixed-code replay attempts. Reconstructed declared settings admit 42 cases under printed-output, pre-oracle database-delta, and native-verdict/test-count checks; resetting the random-number generator before each interaction admits 68. The 26-case gap contracts to four under database/oracle checks, with one endpoint unknown. Mechanism studies identify four materialized-state discrepancies despite matching outputs and verdicts. In one admitted endpoint pair, an identical API call yields matching responses but different row effects; common future Python RNG removes that deterministic difference in two paired repetitions. A separate JWT credential-equality program and alignment controls expose authentication/write differences, with missing repetitions retained. For all 10 affected post-oracle export cases, native export from retained output trackers restores the reference comparison without changing original cached contents. A purposeful 12-case BFCL pilot shows no discrepancy under its tested public-state, return, and verdict checks. We preserve resource censoring and infrastructure deviations. The contribution is a bounded empirical characterization of replay eligibility, hidden state, and test-oracle integration, without estimating debugger accuracy, repair gains, or method-ranking distortion.
