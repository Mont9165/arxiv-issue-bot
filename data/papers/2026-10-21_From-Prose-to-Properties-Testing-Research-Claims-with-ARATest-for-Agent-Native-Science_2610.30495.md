# From Prose to Properties: Testing Research Claims with ARATest for Agent-Native Science

- arXiv ID: `2610.30495v1`
- Authors: Yifeng He, Jiachen Liu, Hao Chen
- Published: 2026-10-21
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.30495v1) | [pdf](https://arxiv.org/pdf/2610.30495v1)

## Abstract

AI agents now run experiments and report findings, so research produces claims faster than researchers can check them. Each empirical claim implies a property that must hold over its cases, but it states that property only in prose. Without an explicit property, no test can decide which evidence would falsify a claim, so validation cannot keep pace with the claims agents produce. To make claims testable, we approximate a claim's semantics by abstracting its property skeleton, a parameterized relation that recurs across claims. We present ARATest, a property-based testing library that checks these skeletons as executable tests. A typed declaration binds a claim to a skeleton and fixes the claim's compared quantities, cases, scope, and numerical policy. A shared case type makes every generator supply cases in the claim's statistical unit. A three-valued semantics assigns each property one of three verdicts: holds, violated, or inconclusive. Every violation carries a replayable witness. A default generator reads the evidence that agent-native research artifacts (ARA) link to each claim, and auto-research generators dispatch an agent to run released code for fresh cases. Our DissClaimer plugin supplies that agent and runs these generators as continuous testing.
  Of 243 claims in 33 ARA artifacts, 54 received faithful declarations bound to evidence: 32 held, eight were violated, and 14 remained inconclusive. Two violations exposed errors in published papers that their authors confirmed. ARATest detected all 553 seeded faults without a false alarm on 19 valid controls, outperforming two LLM judges. Fresh runs exposed behaviors that reported evidence could not show. These results suggest that one fixed test can check explicit claim properties against both reported and fresh evidence.
