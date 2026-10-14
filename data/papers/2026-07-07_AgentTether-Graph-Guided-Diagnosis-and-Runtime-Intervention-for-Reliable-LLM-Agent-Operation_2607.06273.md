# AgentTether: Graph-Guided Diagnosis and Runtime Intervention for Reliable LLM Agent Operation

- arXiv ID: `2607.06273v1`
- Authors: Chenyu Zhao, Shenglin Zhang, Wenwei Gu, Yongqian Sun, Dan Pei, Chetan Bansal, Saravan Rajmohan, Minghua Ma
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06273v1) | [pdf](https://arxiv.org/pdf/2607.06273v1)

## Abstract

Large language model (LLM) agents are increasingly used for multi-step, stateful tool-use tasks, yet production reliability remains limited. Unlike static software repair, agent repair must recover dynamic trajectories whose early decisions can propagate into later errors and external state changes. Existing automatic remedies address only part of this problem: blind retry adds no diagnosis, outcome feedback says whether a run failed but not where or why, and self-reflection often lacks grounded evidence to prevent the same failure from recurring. We present AgentTether, a run-time repair framework that automates post-run diagnosis and guided recovery without modifying the underlying agent or environment. AgentTether abstracts each run into Transition Units, links them through a dependency-aware Critical Transition Graph, and localizes failure-critical subtrajectories by combining an offline normal-behavior model with a run-local graph detector. It then converts the localized cause into behavior-scoped guidance backed by cross-iteration Repair Memory, and can optionally apply guarded run-time intervention to keep the correction active during re-execution. The same design can be deployed as an offline diagnostic-and-guidance tool or as an online repair layer.
  We evaluate AgentTether on 261 tau-bench tasks across three domains with Qwen3.7-max, and test cross-model transfer on Banking with GPT-5.4. On the hardest Banking domain, AgentTether repairs 59.04% (49/83) of initially failed Qwen3.7-max tasks and 65.12% (56/86) of initially failed GPT-5.4 tasks. Overall, AgentTether improves repair effectiveness while reducing agent turns and end-to-end approach tokens, suggesting a practical reliability layer that can wrap existing agent deployments, reduce wasted re-execution, and improve recovery without retraining the agent.
