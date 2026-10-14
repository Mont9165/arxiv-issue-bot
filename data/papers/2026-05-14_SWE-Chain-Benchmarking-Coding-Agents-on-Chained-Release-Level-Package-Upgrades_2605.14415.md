# SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades

- arXiv ID: `2605.14415v1`
- Authors: Man Ho Lam, Chaozheng Wang, Hange Liu, Jingyu Xiao, Haau-sing Li, Jen-tse Huang, Terry Yue Zhuo, Michael R. Lyu
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.14415v1) | [pdf](https://arxiv.org/pdf/2605.14415v1)

## Abstract

Coding agents powered by large language models are increasingly expected to perform realistic software maintenance tasks beyond isolated issue resolution. Existing benchmarks have shifted toward realistic software evolution, but they rarely capture continuous maintenance at the granularity of package releases, where changes are bundled, shipped, and inherited by subsequent versions. We present SWE-Chain, a benchmark for evaluating agents on chained release-level package upgrades, where each transition builds on the agent's prior codebase. To produce upgrade specifications, we design a divide-and-conquer synthesis pipeline that aligns release notes with code diffs for each version transition, ensuring the requirements are grounded in actual code changes, informative to agents, and feasible to implement. SWE-Chain contains 12 upgrade chains across 9 real Python packages, with 155 version transitions and 1,660 grounded upgrade requirements. Across nine frontier agent-model configurations, agents achieve an average of 44.8% resolving, 65.4% precision, and 50.2% F1 under the Build+Fix regime, with Claude-Opus-4.7 (Claude Code) leading at 60.8% resolving, 80.6% precision, and 68.5% F1. These results show that SWE-Chain is both feasible and discriminative, and reveal that current agents still struggle to make correct upgrades across chained package releases without breaking existing functionality.
