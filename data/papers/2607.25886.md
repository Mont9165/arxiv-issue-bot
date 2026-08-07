# RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement

- arXiv ID: `2607.25886v1`
- Authors: Fanqing Meng, Lingxiao Du, Qiguang Chen, Ziqi Zhao, Haocheng Lu, Mengkang Hu, Michael Qizhe Shieh
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.25886v1) | [pdf](https://arxiv.org/pdf/2607.25886v1)

## Abstract

Recursive self-improvement requires turning evidence of model failures into better models. Data-centric post-training research entails diagnosing capability gaps, designing and validating training-data strategies, and learning from checkpoint feedback. Can LLM agents automate this loop? Existing benchmarks entangle research decisions with optimization, serving, evaluation, and systems implementation, obscuring agents' research capability. We introduce RSIBench-Data, a controlled benchmark of LLM agents as data-centric researchers with a fixed post-training stack. Agents iteratively revise training-data strategies for a fixed target model; training and serving use Tinker-backed services, official evaluation runs through Harbor and E2B sandboxes, and budgets are fixed across agents. We evaluate four frontier agents on six benchmarks across software engineering, terminal use, scientific question answering, and mathematics. Agents demonstrate core data-centric research capabilities: in 58.33\% of settings, they improve upon the first valid attempt by refining strategies from feedback. However, improvement is inconsistent. Among searches continuing after the best observed score, 78.26\% end with a lower-scoring final attempt, while the rest only recover the same peak. A strong candidate may therefore appear early or midway through a run even as later revisions fail. Trajectory analysis identifies four patterns in stronger runs: accurate hypotheses, validation-grounded supervision, behavior-aligned data, and preservation of strong checkpoints. These findings suggest that current agents can make useful data-centric discoveries but cannot yet translate feedback into consistent improvements. RSIBench-Data provides a measurable, auditable testbed for the research capabilities required for recursive self-improvement. We open-source our code at https://github.com/evolvent-ai/RSIBench-Data.
