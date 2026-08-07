# GUITestScape: Towards Open-set Evaluation on Exploratory GUI Testing

- arXiv ID: `2605.29532v1`
- Authors: Xiaoyi Chen, Yifei Gao, Yang Xu, Xingxing Song, Yi Zhang, Jitao Sang
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.29532v1) | [pdf](https://arxiv.org/pdf/2605.29532v1)

## Abstract

Exploratory GUI testing is a particularly demanding setting for MLLM agents: without predefined test scripts, an agent must autonomously navigate an application and discover defects through its own interaction. However, current evaluation falls short on two fronts. First, existing benchmarks focus almost exclusively on interaction defects, leaving display defects outside the evaluation frame. Second, evaluation protocols are bound to predefined defect annotations, collapsing the testing process into a single end-state judgment that conflates qualitatively distinct failure modes. To address these challenges, we present GUITestScape, an interactive benchmark covering 61 real-world Android applications and 508 preset defects spanning interaction and display types, and introduce GUIJudge, an open-set evaluator that decomposes an agent's testing trajectory into independently diagnosable capabilities. Experimental results demonstrate that GUIJudge achieves reliable process-aware evaluation beyond predefined annotations, substantially outperforming all baselines. Benchmarking on GUITestScape further reveals that detection remains the critical bottleneck for existing models across both defect types, and that integrating GUIJudge's verifiers into existing agents significantly boosts their detection performance without retraining.
