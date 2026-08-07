# Heimdallr: Characterizing and Detecting LLM-Induced Security Risks in GitHub CI Workflows

- arXiv ID: `2605.05969v1`
- Authors: Bonan Ruan, Yeqi Fu, Chuqi Zhang, Jiahao Liu, Jun Zeng, Zhenkai Liang
- Published: 2026-05-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.05969v1) | [pdf](https://arxiv.org/pdf/2605.05969v1)

## Abstract

GitHub Continuous Integration (CI) workflows increasingly integrate Large Language Models (LLMs) to automate review, triage, content generation, and repository maintenance. This creates a new attack surface: externally controllable workflow inputs can shape LLM prompts and outputs, which may in turn affect security decisions, repository state, or privileged execution. Although LLM security and CI security have each been studied extensively, their intersection remains underexplored. In this paper, we present the first study of LLM-induced security risks in GitHub CI workflows. We characterize the problem along the full execution chain and develop a taxonomy of high-level risk classes and concrete threat vectors. To detect such risks in practice, we design Heimdallr, a hybrid analysis framework that normalizes workflows into an LLM-Workflow Property Graph (L-WPG) and combines triggerability analysis, LLM-assisted dataflow summarization, and deterministic propagation to synthesize concrete threat-vector findings. Evaluated on 300 manually annotated unique workflows, Heimdallr achieves high accuracy on LLM-node identification (F1~=~0.994), triggerability classification (99.8%), and threat-vector detection (micro-average F1~=~0.917). As part of an ongoing detection and disclosure effort, we have so far responsibly disclosed 802 vulnerable workflow instances across 759 repositories and received 71 acknowledgments.
