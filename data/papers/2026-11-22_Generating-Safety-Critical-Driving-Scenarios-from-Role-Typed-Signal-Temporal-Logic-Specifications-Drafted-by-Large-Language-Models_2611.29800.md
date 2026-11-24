# Generating Safety-Critical Driving Scenarios from Role-Typed Signal Temporal Logic Specifications Drafted by Large Language Models

- arXiv ID: `2611.29800v1`
- Authors: Zifan Zeng, Qunli Zhang, Peng Wang, Shiming Liu, Feng Liu, Zheng Hu
- Published: 2026-11-22
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.29800v1) | [pdf](https://arxiv.org/pdf/2611.29800v1)

## Abstract

Safety-critical scenarios are rare in recorded driving and must be generated to test and train motion planners of automated vehicles. In guided diffusion models, each scenario type needs its own weighted objective, separate from the validity check. Optimized together with the attacker, the vehicle under test can cancel the attack or draw it toward itself. We state each scenario as a signal temporal logic specification with clauses typed by role. Every clause names the agent it may change and the agents it may read, and the vehicle under test reads the attacker only from the attack onset. A large language model drafts the specification from a description, and a type checker accepts it. A compiler derives the optimization: it edits a diffusion model's samples by the smallest change that satisfies the specification, each clause moves only its owner, the attacker is solved against the unreacted vehicle under test before its response, and the monitor of the same specification decides acceptance. On nuScenes and CommonRoad, judged independently of the specification, one parameter set produced valid scenarios at a rate 0.14 above a weighted objective tuned per scenario type, and descriptions yielded at least one valid scenario for 11 of the 16 pre-crash types expressible in the public data. Learned planners fail more often on the generated scenarios than on their seeds. Fine-tuning on them lowers a planner's failure rate on critical scenarios, and the time headway one clause of the label requires, not the generator, sets the size of the gain.
