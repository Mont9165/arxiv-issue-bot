# Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents

- arXiv ID: `2605.08717v1`
- Authors: Chenyu Zhao, Shenglin Zhang, Yihang Lin, Wenwei Gu, Zhimin Chen, Yongqian Sun, Dan Pei, Chetan Bansal, Saravan Rajmohan, Minghua Ma
- Published: 2026-05-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.08717v1) | [pdf](https://arxiv.org/pdf/2605.08717v1)

## Abstract

Software engineering agents are increasingly deployed in evaluable engineering environments, yet post-failure recovery remains costly, manual, and ad hoc. Existing systems expose traces or generate follow-up feedback, but they do not convert heterogeneous runtime evidence into grounded, bounded recovery guidance for a subsequent attempt. We present PROBE, a failure-anchored framework for structured recovery in software engineering agents. PROBE organizes failed-run telemetry into structured evidence, structured diagnosis, and bounded recovery guidance through a Telemetry Layer, a Diagnosis Layer, and a Guidance Gate. The Telemetry Layer preserves fine-grained runtime signals, the Diagnosis Layer fuses cross-signal evidence into grounded diagnoses, and the Guidance Gate produces diagnosis-derived guidance only when it is evidence-grounded, actionable, and within the scope of agent-side behavior.
  We evaluate PROBE across three settings: repository-level software repair, enterprise workflow recovery, and AIOps service mitigation. On 257 initially unresolved cases, PROBE achieves 65.37% Top-1 diagnosis accuracy and a 21.79% recovery rate, outperforming the strongest non-PROBE baseline by 43.58 and 12.45 percentage points. The results reveal a diagnosis-recovery gap: accurate diagnosis is necessary but insufficient unless translated into bounded guidance that a subsequent attempt can execute and verify. Beyond controlled evaluation, a Microsoft IcM prototype shows that PROBE can attach as a non-intrusive side channel to existing service-diagnosis workflows without changing the agent policy, toolset, or execution budget. These results suggest that telemetry-grounded, failure-anchored recovery can improve post-failure recoverability under realistic engineering constraints.
