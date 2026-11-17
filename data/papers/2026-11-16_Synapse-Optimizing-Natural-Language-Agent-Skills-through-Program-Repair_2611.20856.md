# Synapse: Optimizing Natural-Language Agent Skills through Program Repair

- arXiv ID: `2611.20856v1`
- Authors: Lijuan Li, Zhenpeng Chen, Chenxi Zhang, Yihao Huang, Yang Liu, Chong Wang
- Published: 2026-11-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.20856v1) | [pdf](https://arxiv.org/pdf/2611.20856v1)

## Abstract

Large language model (LLM) agents can improve task performance by optimizing reusable natural-language skills without updating model parameters. Execution feedback reveals failures but does not directly identify which instructions to edit, which related instructions matter, or which tasks an edit may break. We propose Synapse, which casts skill optimization as generate-and-validate repair over a partial program view. A deterministic compiler translates recognized skill constructs into SkIR, a source-linked intermediate representation, while retaining other requirements in the text. Synapse combines execution traces with control-flow and dependence relations to localize faults, propose typed mutations, and select related repair tests, including previously passing ones. Each mutation is written back to its mapped source span and recompiled; validation determines acceptance. Every accepted patch yields a well-formed skill and preserves untargeted instruction spans. Under a one-hop-local execution assumption, selected tests include every test an edit can affect. On DocVQA and LiveMath with three execution models, Synapse improves task success rates over SkillOpt by 3.74-4.54 and 2.40-4.00 percentage points, respectively, and outperforms Trace2Skill and SkillBoost in all six settings. Replacing SkIR-based repair and its test screening with constrained text editing screened only on failing tests lowers DocVQA success rates by 2.40 and 2.67 percentage points for two models. In two recorded repair runs, structural relations add tests for 23 of 37 patches; in one repair, a test added through a control-flow relation exposes a regression missed by coverage of the edited instruction.
