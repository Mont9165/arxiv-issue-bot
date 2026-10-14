# Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs

- arXiv ID: `2605.17558v1`
- Authors: Yuxuan Lu, Ziyi Wang, Yingzhou Lu, Yisi Sang, Jiri Gesi, Xianfeng Tang, Yimeng Zhang, Zhenwei Dai, Hui Liu, Hanqing Lu, Chen Luo, Qi He, Benoit Dumoulin, Jing Huang, Dakuo Wang
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.17558v1) | [pdf](https://arxiv.org/pdf/2605.17558v1)

## Abstract

Training tool-calling agents requires large-scale trajectory data with verifiable labels, yet existing approaches either synthesize environments that diverge from real API behavior or generate tasks without ground-truth outcomes for verification. We present FireFly, a pipeline for generating verified tool-call data from real-world MCP servers. Our key insight is to invert the standard synthesis pipeline: rather than generating tasks and hoping they are solvable, we first let a strong LLM explore real APIs along graph-guided DAG structures, then synthesize tasks backward from observed outcomes, guaranteeing label correctness by construction. To handle the scale of real-world tool spaces (${\sim}$1,000 tools), we build a pairwise tool graph and sample sub-DAGs to focus exploration on semantically coherent workflows. To address environment drift in live APIs, we construct a retrieval-augmented simulator that caches all exploration results and replays them during training and evaluation, enabling fully offline and reproducible RL. Applying this pipeline yields 5,144 verified tasks spanning 240 servers and 993 tools. A 4B-parameter model trained with GRPO on FireFly matches Claude Sonnet 4.6 on our held-out test set and shows improvements on multiple tool-calling benchmarks including Tau2-Bench, MCPMark, and MCP-Atlas.
