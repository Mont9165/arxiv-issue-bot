# MultiFixer: A Coordinator-Proposer Based Multi-Agent Framework For Fixing Multi-Hunk Bugs

- arXiv ID: `2607.26591v1`
- Authors: Haichuan Hu, Chunrong Fang, Ye Shang, Jiawei Liu, Weifeng Sun, Guoqing Xie, Chenxing Zhong, Quanjun Zhang
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26591v1) | [pdf](https://arxiv.org/pdf/2607.26591v1)

## Abstract

Automated Program Repair (APR) has benefited greatly from Large Language Models (LLMs), but existing LLM-based APR methods still struggle with multi-hunk bugs that require coordinated changes across multiple locations. These bugs demand repository-level context understanding, repair-order scheduling, and effective hunk-level patch generation and selection. To address these challenges, we propose MultiFixer, a novel Coordinator-Proposer based multi-agent framework for multi-hunk repair. MultiFixer performs tool-augmented bug analysis, constructs fine-grained repair context, iteratively generates patches through a Coordinator-Proposer architecture, and applies two-stage patch refinement for syntactic and semantic correctness. We evaluate MultiFixer on 835 bugs from Defects4J and three vulnerability benchmarks. On Defects4J, MultiFixer fixes 326 bugs, including 62 multi-method and 27 multi-file bugs, and outperforms prior APR baselines in the reported comparisons with the same base model. Moreover, MultiFixer also fixes 46 multi-hunk bugs among 95 unique fixes. When combined with Claude-3.5-Sonnet, MultiFixer repairs 420 bugs, establishing a new state of the art on Defects4J. On VUL4J, MultiFixer repairs 24 real-world vulnerabilities, including 5 multi-hunk cases. On the multi-hunk subsets of SEC-bench and PatchEval, MultiFixer fixes 11 and 19 vulnerabilities, respectively, outperforming all compared baselines under GPT-3.5. These results demonstrate the effectiveness of MultiFixer for multi-hunk repair.
