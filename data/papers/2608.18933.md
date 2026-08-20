# SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution

- arXiv ID: `2608.18933v1`
- Authors: Silin Chen, Han Li, Xiaodong Gu, Yuling Shi, Haibing Guan
- Published: 2026-08-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.18933v1) | [pdf](https://arxiv.org/pdf/2608.18933v1)

## Abstract

Large language model (LLM) based agents have demonstrated remarkable proficiency in automated software issue resolution, yet they often struggle to resolve issues in a specific repository because they lack project-specific knowledge. Existing self-evolving approaches acquire such knowledge from repository history or online repair trajectories, but they either depend on available historical issue-resolution signals or incur substantial per-issue test-time exploration cost. In this paper, we propose SkillForge, a self-distillation framework that proactively acquires project-specific knowledge from the repository itself. Instead of waiting for real issues to expose project-specific knowledge gaps, SkillForge synthesizes project-specific issues by re-implementing test-covered core functionalities of the repository. By resolving these synthetic issues, SkillForge distills reusable project-specific knowledge into entity-grounded skills and associates them with relevant repository entities for future issue resolution. Extensive experiments using both open-source and closed-source models show that SkillForge consistently improves issue resolution performance over strong baselines. These results demonstrate that proactively acquiring project-specific knowledge before solving real issues substantially improves downstream software issue resolution.
