# Drive the Thoughts: Runtime Monitoring of VLA Reasoning-Trajectory Consistency

- arXiv ID: `2608.29583v1`
- Authors: Tian Yu, Lu Feng, Sebastian Elbaum
- Published: 2026-08-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29583v1) | [pdf](https://arxiv.org/pdf/2608.29583v1)

## Abstract

Autonomous vehicles (AVs) operate in complex environments where failures are consequential. Sophisticated machine learning models for perception and planning are key to overcoming at least part of that complexity, but their black-box nature complicates validation and verification (V&V). The recent integration of Vision-Language-Action (VLA) models into AVs introduces a unique opportunity: besides generating trajectories, these models produce an explicit Chain-of-Thought (CoT) explaining their underlying rationale. This CoT provides a rich specification to cross-check model outputs and detect inconsistencies that may expose unsafe or unintended behavior. This paper assesses whether CoTs from a recent open driving VLA can support such monitoring. We curate DriveAlignBench, a specialized dataset from NVIDIA's Alpamayo 1.5 VLA for AVs containing 150 CoT-trajectory pairs, which we manually annotate for reliability, trajectory consistency, and safety. Our analysis reveals that 33.3% of CoTs are unreliable. Among reliable CoTs, the generated trajectory is consistent with the CoT in 74% of cases. Leveraging this potential, we propose integrating a CoT-trajectory consistency check into a runtime monitor. The check is nontrivial: CoTs express open-vocabulary, scene-relative driving commitments, while trajectories are low-level ego-motion sequences whose semantics depend on road geometry and motion context. To bridge this gap, we develop a family of automated consistency monitors. Our best monitor, lane-relative F-LLM with GPT-5.5, achieves F1 = 0.75, improving over the strongest raw-waypoint LLM baseline by +0.13 absolute F1 and over a rule-based monitor by +0.38. We release DriveAlignBench, the monitor implementations, and annotation tools at https://github.com/776styjsu/drive-the-thoughts.
