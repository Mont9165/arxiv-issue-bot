# JTA: Joint Testability Architecture for Scenario-Based Validation of Safety-Critical Software

- arXiv ID: `2608.05594v1`
- Authors: Wenyao Xue, Jiandi Wang, Yichen Wang
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.RO`
- Links: [abs](http://arxiv.org/abs/2608.05594v1) | [pdf](https://arxiv.org/pdf/2608.05594v1)

## Abstract

Validation adequacy in safety-critical software depends on more than the system under test. Critical scenarios must be constructed under controlled conditions, execution evidence must be aligned into verdict-ready form, and abnormal outcomes must be attributable to actionable causes. Existing testability research remains largely artifact-centric and offers little architectural support for reasoning about the combined capability of the scenario, the test system, and the system under test. Joint Testability Architecture (JTA) addresses this gap by treating those three elements as a single object of analysis and design. It characterizes validation capability along three dimensions--controllability, observability, and isolability--and organizes them through three domains, three bridges, and an analysis-design-evaluation-refinement loop. JTA also introduces scenario contracts, joint capability assessment, validation blind-spot identification, and bridge-oriented design actions that map capability gaps to concrete improvements in control points, evidence organization, and attribution boundaries. An illustrative analysis of ArduPilot failsafe validation shows that link-loss scenarios are comparatively mature, whereas state-estimation anomaly scenarios remain harder to validate because evidence alignment and attribution semantics are weaker. JTA is not a replacement for existing testing or safety-analysis techniques; it provides an architectural basis for modeling, designing, and assessing scenario-based validation in safety-critical software.
