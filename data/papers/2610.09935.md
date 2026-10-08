# AgentTracer: Tracing Indirect Prompt Injection Attack through Fine-Grained Intention-Execution Alignment

- arXiv ID: `2610.09935v1`
- Authors: Zitong Yao, Jiangrong Wu, Yixi Lin, Anrui Huang, Luoyun Zhang, Yuhong Nan
- Published: 2026-10-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.09935v1) | [pdf](https://arxiv.org/pdf/2610.09935v1)

## Abstract

Large language model (LLM) agents interact with external resources to complete complex user tasks, exposing them to indirect prompt injection (IPI), where malicious instructions redirect agents toward attacker-intended tasks. Since IPI is difficult to defend against in real-world environments, post-incident tracing is essential for locating the injection source and reconstructing the attack chain. However, existing tracing methods primarily capture explicit control-flow and data-flow dependencies, overlooking the implicit relationships among tool calls driven by the malicious instruction. These tool calls may lack explicit dependencies and be interleaved with legitimate operations, making complete attack-chain reconstruction difficult. In this paper, we present AgentTracer, an intent-aware tracing framework that treats IPI as task intent drift. AgentTracer recovers implicit decision dependencies among tool calls to construct an Intent-Driven Execution Graph that connects dispersed tool calls by task intent. It combines the user request with an operation knowledge base to construct a user intent authorization space and identify intent-drift tool calls. Starting from an anomalous tool call under audit, AgentTracer performs target-based pruning and backward tracing to reconstruct the attack chain and locate the injection source and injection point. To evaluate AgentTracer in the presence of noise from normal tasks, we combine execution logs constructed from successful IPI attacks in AgentDyn and InjecAgent with normal execution logs containing 1,800 user requests and 9,000 background tool calls without IPI. In end-to-end experiments, AgentTracer achieves 94.17 percent injection-point accuracy and 93.56 percent path precision. Comparative experiments show that AgentTracer improves injection-point accuracy over existing methods by 18 to 54 percent.
