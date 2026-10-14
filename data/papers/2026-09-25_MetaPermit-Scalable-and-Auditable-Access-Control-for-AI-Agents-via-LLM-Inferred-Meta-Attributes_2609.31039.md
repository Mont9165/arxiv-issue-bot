# MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes

- arXiv ID: `2609.31039v1`
- Authors: Hanzhang Ma, Ali Hariri, Tianxiang Shen, Bohua Zou, Qianjun Zheng, Ji Wang, Li Yi, Ning Jia, Yutao Liu, Haibo Chen, Lin Wang, Debayan Roy
- Published: 2026-09-25
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.31039v1) | [pdf](https://arxiv.org/pdf/2609.31039v1)

## Abstract

The rise of autonomous AI agents equipped with tools has introduced significant security risks, ranging from unintended tool misuse to adversarial manipulation through Indirect Prompt Injection (IPI) attacks. In practice, deployed agent systems such as OpenAI Codex and Claude Code protect tool invocations through a combination of coarse-grained permission rules and LLM-based judgments about individual proposed actions. Both components, however, have important limitations: static policies must anticipate possible user intents and therefore do not scale to open-ended tasks, while LLM-driven authorization supports dynamic decisions but produces inconsistent outcomes and remains vulnerable to targeted IPI attacks. To provide scalable and more consistent authorization, we propose MetaPermit, a policy-based tool access-control framework that decouples semantic inference from security enforcement. By analyzing agent-user interactions, we derive a compact, task-independent set of meta-attributes that capture the relationships among the user's intent, the execution context, and the proposed tool call. These meta-attributes allow MetaPermit to authorize tool use without enumerating user intents. At runtime, an LLM infers the meta-attribute values for each proposed tool call, while a fixed policy evaluates these values to allow or deny the call, making each decision auditable through the inferred values and the applied policy rule. We evaluate MetaPermit on the AgentDojo and AgentDyn benchmarks, across seven task suites and five attack methods, using two widely deployed open-weight LLMs. The results show that MetaPermit produces 31% more consistent authorization decisions than LLM-driven authorization and outperforms the state-of-the-art defenses CaMeL and IPIGuard in both task completion, with improvements of up to 109%, and robustness to IPI attacks, with no malicious tool calls executed.
