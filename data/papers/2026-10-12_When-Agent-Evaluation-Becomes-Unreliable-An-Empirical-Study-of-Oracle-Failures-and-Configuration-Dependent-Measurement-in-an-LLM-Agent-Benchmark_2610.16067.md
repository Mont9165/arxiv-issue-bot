# When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark

- arXiv ID: `2610.16067v1`
- Authors: Junjie Chen
- Published: 2026-10-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.16067v1) | [pdf](https://arxiv.org/pdf/2610.16067v1)

## Abstract

Agent evaluation harnesses are software systems that run test suites, generate inputs, and decide outcomes with test oracles. This paper audits such software for reliability defects that score tables cannot reveal.
  We introduce an oracle-integrity auditing approach with five state-integrity invariants and three known-answer controls. We evaluate it by injecting seven oracle defect classes across two task domains and a synthetic domain. All injected defect classes are detected, and the repaired oracle has no false positives. Applied to an agent benchmark, the audit reveals a reward-function defect that changes the environment state before post-run scoring. Across 4,320 episodes, replay-based correction changes database-pass labels from 4,194 to 2,883 and reduces measured success from 94.3% to 65.5%.
  We also study configuration-dependent measurement effects. A component ablation over 3,240 episodes shows that the agent's policy documents, tool descriptions, and tool error strings influence observed trajectory reliability, with tool descriptions showing the largest exploratory effect (-9.2 pp) and error strings the smallest (-5.3 pp). A second task domain reverses the sign of the language effect, so the result is bounded to the tested configuration.
  Finally, we report a portability boundary: the auditing approach cannot validate a second independently implemented benchmark because the required reference terminal state cannot be reconstructed from its recorded API-call log.
  The paper releases a replication package containing the auditing suite, fault-injection catalogue, frozen records, deviation logs, and offline analysis entry points without network access, API keys, or model calls.
