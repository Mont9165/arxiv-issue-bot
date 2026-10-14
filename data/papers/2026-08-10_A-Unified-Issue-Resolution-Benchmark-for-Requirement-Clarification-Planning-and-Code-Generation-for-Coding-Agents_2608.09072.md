# A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents

- arXiv ID: `2608.09072v1`
- Authors: Xin Zhou, Chun Yong Chong, Kisub Kim, Yun Peng, Rui Shu, Zihan Wu, Xu Han, Guowen Yuan, Zeyang Zhuang, Jounghoon Kim, Jeongjin Ju, Seongmin Ju, Taein Yoon, David Lo
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.09072v1) | [pdf](https://arxiv.org/pdf/2608.09072v1)

## Abstract

Large language model-powered coding agents are increasingly used to modify existing code repositories, for example, by adding features or fixing bugs. Yet existing repository-level benchmarks typically evaluate only whether the final patch passes tests. Satisfying a user request requires a long chain of interdependent reasoning and decisions: an agent must recover explicit and implicit requirements, formulate a repository-grounded implementation plan, and translate it into correct code. A pass/fail outcome cannot characterize how an unsuccessful trajectory diverges from the requirements and implementation process needed for a correct patch. To address this gap, we introduce SWE-RPG, a repository-level benchmark that combines executable patch evaluation with validated ground-truth references (GTs) for (1) Requirement Clarification and (2) Implementation Planning. These intermediate GTs support retrospective, GT-aligned diagnosis of complete coding-agent trajectories across clarification, planning, code generation, and artifact submission. SWE-RPG comprises 163 tasks from 31 Python and Java repositories, including 113 bug fixes and 50 feature additions. We evaluate 3 coding agents, including Claude Code, Codex, and OpenCode, with 6 large language model backends, including Claude-Sonnet-5 and GPT-5.6-Terra. Results show that the evaluated popular coding agents still struggle to implement user requests in existing repositories, achieving an average resolved rate of only 31.5% on SWE-RPG. Intermediate-GT diagnosis further identifies implicit requirement recovery as the main bottleneck, accounting for 24.5%--46.0% of agent runs. This result suggests implicit-requirement recovery as a key candidate direction for improving coding agents. The benchmark data and evaluation code are available at https://github.com/Xin-Zhou-smu/SWE-RPG-Bench.
