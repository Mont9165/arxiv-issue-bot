# RLPF: Reinforcement Learning from Performance Feedback for Code Generation

- arXiv ID: `2607.27271v1`
- Authors: Huihao Jing, Haozhe Cui, Wenbin Hu, Shaojin Chen, Haochen Shi, Changxuan Fan, Yuxuan Liu, Hanyu Yang, Sirui Zhang, Ziyi Chen, Haoran Li, Yangqiu Song
- Published: 2026-07-29
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27271v1) | [pdf](https://arxiv.org/pdf/2607.27271v1)

## Abstract

Code models are increasingly trained with execution feedback, but most training signals still stop at correctness. This leaves an important gap for systems code: two programs can pass the same tests while differing greatly in runtime. We study how to train code agents to prefer faster correct implementations, rather than treating efficiency only as an evaluation metric. The key difficulty is that runtime is a fragile reward. It is meaningful only after a program is correct, varies across tasks, and gives little guidance when most sampled programs fail to compile or run. We propose \textbf{RLPF}, reinforcement learning from performance feedback, which turns execution outcomes into a staged reward. Failed programs are ordered by execution progress, while correct programs are ranked by their relative improvement from the baseline toward the expert reference. This gives useful feedback before correctness and performance-sensitive feedback after correctness. Fine-tuning Qwen3-32B with RLPF on PerfCodeBench raises correct-and-runnable solutions from $11.1\%$ to $54.6\%$ and improves relative efficiency from $8.1\%$ to $38.6\%$. The trained model becomes competitive with stronger open-weight systems, and its optimization behavior transfers modestly to EffiBench-X. Additional studies show that model-generated references provide useful but weaker supervision, and that the full composite reward is more reliable than correctness-only or runtime-only baselines. These results suggest that code agents can be trained not only to pass tests, but also to optimize the programs they write.
