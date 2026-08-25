# Repo2Skill-Evo: Repository Skills Go Stale in Silence

- arXiv ID: `2608.21964v1`
- Authors: Chenyuan Duan, Ge Shi, Zineng Mao, Ge Zhang, Hao Liang, Yinzhu Piao, Yuchen Wu, Zhixin Yao, Kaiyu Huang, Wenhao Huang, Linzhuang Sun, Shen Yan, Wentao Zhang
- Published: 2026-08-22
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.21964v1) | [pdf](https://arxiv.org/pdf/2608.21964v1)

## Abstract

Large language model (LLM) agents increasingly operate over evolving software repositories, where success depends on repository-specific procedural knowledge: which APIs to call, which scripts to run, and which conventions the current release expects. Agent skills externalize this knowledge into reusable units, and prior work shows that they can improve agent performance. What remains unclear is whether that improvement is durable. The same version specificity that makes a skill useful also makes it fragile: after a release, it may become stale without raising any explicit signal, while continuing to provide obsolete guidance. Externalizing knowledge into a skill can therefore make its decay invisible.
  We study whether agents can keep this externalized knowledge current. Repo2Skill-Evo casts each release transition as a skill-maintenance task: given a V1 skill set and the official V1-to-V2 patch, an agent must update obsolete skill content while preserving guidance that remains valid. Across 57 real-world repositories and 105 selected release transitions, every evaluated transition invalidates part of the V1 skill set. Yet six frontier agents reach only 29.9%-69.7% avg@3 macro F1 under a patch-grounded removal metric that balances stale-content recall against over-editing precision. Across runs, two opposing errors dominate: incomplete coverage of affected files in the skill set leaves stale content untouched, while overbroad editing is associated with higher recall but lower precision. Repository skills go stale in silence, and even frontier agents cannot reliably maintain them.
