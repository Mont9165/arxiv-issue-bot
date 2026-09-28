# Beyond Approved Actions: Runtime Validation of Persistent Outcomes in Agent Workflows

- arXiv ID: `2609.31301v1`
- Authors: Haoran Zhang, Hengtong Zhang, Zhiyu Liang, Yu Yan, Decheng Zuo, Hongzhi Wang
- Published: 2026-09-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.31301v1) | [pdf](https://arxiv.org/pdf/2609.31301v1)

## Abstract

Large language model agents increasingly act on software systems, no longer merely generating text but also changing databases and online services. However, an approved database update may succeed yet leave an unapproved notification because execution can produce persistent effects beyond the requested change. Current safeguards can approve an action or record its aftermath, but without checking the persistent result before continuation, an unapproved outcome can be accepted as success and propagated to later steps. We present EffectMatch, a runtime that collects persistent changes within a controlled execution boundary and compares them with what the application approved for the current state and execution. The comparison governs commit and dependent execution. In comparative evaluation on 206 public business tasks, EffectMatch preserved all clean executions and prevented all tested incorrect commits. Six 20-run ablations exposed the failure caused by each removed mechanism, while 80 task-topology cases preserved truthful handoffs and blocked invalid continuation. Together, these results show that EffectMatch blocks the silent acceptance and downstream propagation of persistent outcomes inconsistent with application approval.
