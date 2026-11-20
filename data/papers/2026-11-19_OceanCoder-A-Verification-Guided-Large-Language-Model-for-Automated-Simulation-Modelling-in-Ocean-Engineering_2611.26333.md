# OceanCoder: A Verification-Guided Large Language Model for Automated Simulation Modelling in Ocean Engineering

- arXiv ID: `2611.26333v1`
- Authors: Can Xue, Changhong He, Ziyi Sun, Anliang Ge, Shimin Yu, Bingchen Liang
- Published: 2026-11-19
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.26333v1) | [pdf](https://arxiv.org/pdf/2611.26333v1)

## Abstract

Numerical simulation is important in ocean engineering, but model construction requires expert knowledge. Large language models support automated modelling, but code syntax and successful execution alone do not establish whether generated models and results meet engineering requirements. We present OceanCoder, a Qwen3-8B-based large language model for automated simulation modelling in ocean engineering. To address specialised programming requirements and scarce training data, we develop an extensible data construction pipeline producing 12,000 verified supervised fine-tuning (SFT) examples across 12 engineering task categories. A three-layer verification framework checks model inputs against engineering parameters and task constraints, verifies completion of required simulation analyses, and assesses the engineering plausibility of computed outputs. Its outcomes provide graded rewards for group relative policy optimisation (GRPO), guiding the model towards engineering task completion. We also construct the first benchmark for automated modelling in ocean engineering, covering out-of-distribution tasks and real-world engineering cases. Experiments and ablation studies demonstrate the effectiveness of the data pipeline, verification framework and reward design. OceanCoder outperforms both base models and the closed-source comparison, with Pass@1 increasing from 0% for the base model to 46.77% after SFT and 51.43% after GRPO. These results support engineering verification as a training signal for automated simulation modelling.
