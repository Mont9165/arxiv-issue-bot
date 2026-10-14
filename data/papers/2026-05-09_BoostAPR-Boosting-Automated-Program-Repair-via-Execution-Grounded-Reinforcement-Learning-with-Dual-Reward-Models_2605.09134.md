# BoostAPR: Boosting Automated Program Repair via Execution-Grounded Reinforcement Learning with Dual Reward Models

- arXiv ID: `2605.09134v1`
- Authors: Yuanhao Li, Hongbo Wang, Xiaotang Shang, Xunzhu Tang, Yiming Cao, Xuhong Chen
- Published: 2026-05-09
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09134v1) | [pdf](https://arxiv.org/pdf/2605.09134v1)

## Abstract

Reinforcement learning for program repair is hindered by sparse execution feedback and coarse sequence-level rewards that obscure which edits actually fix bugs. We present BoostAPR, a three-stage framework addressing these challenges: (1) supervised fine-tuning on execution-verified demonstrations with reasoning traces, (2) training dual reward models--a sequence-level assessor and a line-level credit allocator--from execution outcomes, and (3) PPO optimization where the line-level model redistributes rewards to critical edit regions. This line-level credit assignment operates at an intermediate granularity naturally suited to code changes. Trained on SWE-Gym and evaluated on four benchmarks, BoostAPR achieves 40.7% on SWE-bench Verified (+22.9pp over base model), 24.8% on Defects4J (Python-to-Java transfer), 84.5% on HumanEval-Java, and 95.0% on QuixBugs, achieving competitive results among open-source models with strong cross-language generalization.
