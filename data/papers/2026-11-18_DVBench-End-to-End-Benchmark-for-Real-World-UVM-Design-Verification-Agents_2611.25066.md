# DVBench: End-to-End Benchmark for Real-World UVM Design Verification Agents

- arXiv ID: `2611.25066v1`
- Authors: Jiaru Qian, Jiawei Li, Xiaolong Hu, Zheng Shen, LiMing Zhao, Xin Zhang, Siyuan Jiang, Yongqiang Wei, Dong Liu, Jianyang Li, Yihua Chen, Yangxu Liao, Yuxin Wu, Jing Liang, Bin Wen, Junjie Zhang, Yongsheng Han, Yihong Dong, Ge Li
- Published: 2026-11-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.AR`
- Links: [abs](http://arxiv.org/abs/2611.25066v1) | [pdf](https://arxiv.org/pdf/2611.25066v1)

## Abstract

Design verification (DV) remains a major bottleneck in hardware development, with large-scale verification using the Universal Verification Methodology (UVM) being highly labor-intensive. Recent advances in large language models (LLMs) and agentic systems offer new opportunities for DV automation. However, existing benchmarks primarily construct mutually decoupled subtasks, which deviates from the real-world workflow. In this paper, we present DVBench, the first end-to-end benchmark for Real-World UVM design verification agents. DVBench comprises 95 tasks across 9 functional domains and 5 difficulty levels, covering diverse verification scenarios and design scales. Each task requires agents to independently complete the full verification workflow. DVBench evaluates final testbenches via compilation, coverage, and bug detection, while assessing intermediate artifacts including feature lists, test plans, and reference models. We evaluate frontier LLMs (e.g. Claude Opus 5.5, GPT-6 Astra) and agent frameworks (e.g. Claude Code, Codex, OpenCode). Experimental results show that the best LLM-based agent (Codex \& GPT-6 Astra) can only achieve an overall success rate of 21.05\%, revealing substantial room for improvement in complex verification tasks.
