# Validation-Gated ML Pipeline Synthesis with Expert-Grounded Self-Evolving Skills

- arXiv ID: `2611.04180v1`
- Authors: Zixiao Zhao, Jing Sun, Zhe Hou, Mengze Li, Qian Liu, Cheng-Hao Cai, Zijian Zhang, Xin Wang, Gillian Dobbie, Jin Song Dong
- Published: 2026-11-03
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.04180v1) | [pdf](https://arxiv.org/pdf/2611.04180v1)

## Abstract

Recent advances in large language models have enabled agentic systems that automate machine learning pipeline construction from minimal user input. However, existing agentic AutoML methods either depend on rigid templates that limit adaptability, target narrow task domains, or rely on free-form code generation that lacks reliability guarantees, leaving intermediate errors to propagate silently and degrade the final model. We present EvoML, an agentic framework for end-to-end ML pipeline synthesis built on expert-grounded skills that evolve across runs, executed through a validation-gated harness. The framework decomposes pipeline construction into four phases coordinated by three agents: an Orchestrator that enforces validation gates, advancing each phase only when its outputs pass structural, execution, and semantic checks, which precludes error propagation and keeps every artifact auditable; an Executor that runs expert-grounded skills, grounded in the nnU-Net workflow and pairing reusable templates with online adaptation; and a Curator that performs post-run evolution, consolidating the scripts and guidance recovered during a run into the skill library so it improves across datasets. We evaluate EvoML on eight datasets spanning six sophisticated, real-world ML task types, against agentic AutoML systems and command-line coding tools. EvoML achieves full automation and the best final model quality on all eight, spanning segmentation (up to 0.94 Dice), classification (0.99 accuracy), reconstruction (0.95 SSIM), and denoising (0.79 normalized PSNR), while transferring to broader ML tasks.
