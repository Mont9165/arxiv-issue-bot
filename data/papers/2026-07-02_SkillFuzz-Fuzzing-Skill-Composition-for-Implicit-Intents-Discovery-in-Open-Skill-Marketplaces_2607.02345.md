# SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces

- arXiv ID: `2607.02345v1`
- Authors: Jinwei Hu, Yi Dong, Youcheng Sun, Xiaowei Huang
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.02345v1) | [pdf](https://arxiv.org/pdf/2607.02345v1)

## Abstract

Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting such intents is challenging because the effect emerges only through skill composition, execution environments are often unavailable at admission time, and the space of possible co-activations grows exponentially with marketplace size. In this paper, we formulate implicit-intent discovery as a fuzzing problem over skill compositions, where skill compositions are the unit under test, planning artifacts expose agent intent before execution, and deviations from a skill-free baseline serve as a differential oracle. Based on this formulation, we propose skillfuzz, the first execution-free testing approach that extracts structured skill contracts and uses contract-guided Monte Carlo Tree Search to prioritize potentially conflicting compositions. Across representative skill-marketplace workloads, skillfuzz discovers over 1,000 distinct implicit intents under a fixed query budget, confirms more than 80% of the highest-risk flagged compositions during execution-time validation, and identifies substantially more high-severity implicit intents than alternative search strategies while exploring only a fraction of the pairwise interaction space they require.
