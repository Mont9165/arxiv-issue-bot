# Bug2Scenario: Root-Cause-Preserving Test Scenario Amplification for Autonomous Driving Software

- arXiv ID: `2611.06229v1`
- Authors: Yuchen Cao, Zhenyu Mao, Jacky Wai Keung, Yifei Wang, Yihan Liao, Jingyu Zhang
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.06229v1) | [pdf](https://arxiv.org/pdf/2611.06229v1)

## Abstract

Simulation-based fuzzing exposes autonomous driving system (ADS) failures by repeatedly mutating and executing scenarios, but converting one failure into reusable regression scenarios remains difficult. Such variants test whether the mechanism persists after software changes, for example by varying weather or actor placement while retaining a collision's actor-route conflict. We present Bug2Scenario, a root-cause-guided post-fuzzing framework. From scenario data, traces, and oracle evidence, it extracts a root-cause pattern. An LLM proposes semantic variations over actors, missions, routes, and weather. Deterministic rules construct DriveFuzz-compatible scenarios. Execution evidence and manual review assess preservation. Separating these responsibilities prevents fluency, syntax, or recurring labels from masquerading as causal evidence. Under matched seeds, six LLM backbones, candidate budget, and execution pipeline, Bug2Scenario improves strict preservation by 6.7 percentage points (p=0.104; not significant) and boundary-inclusive preservation by 10.6 points (p=0.011). Feedback helps some initially unsuccessful seeds yield a strictly preserved candidate. Seed-level stopping then avoids further API calls and simulator runs. Remaining failures reflect actor-placement constraints, simulator instability, and incomplete or conflicting causal evidence. Bug2Scenario thus produces reliable ADS regression assets. Our implementation is available at https://github.com/YgcCoder/Bug2Sce.
