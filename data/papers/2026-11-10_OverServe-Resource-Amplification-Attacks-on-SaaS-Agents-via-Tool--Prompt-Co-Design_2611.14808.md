# OverServe: Resource Amplification Attacks on SaaS Agents via Tool--Prompt Co-Design

- arXiv ID: `2611.14808v1`
- Authors: Ruiheng Yu, Oteo Mamo, Siyu Gan, Weikuan Yu, Mulong Luo
- Published: 2026-11-10
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.14808v1) | [pdf](https://arxiv.org/pdf/2611.14808v1)

## Abstract

Advances in large language models (LLMs) are enabling software-as-a-service (SaaS) providers to automate longer business workflows with agents. In subscription-based SaaS deployments, model and tool calls consume provider resources without additional customer payments. Because the agent autonomously decides when to stop, a malicious tenant can send a prompt to the agent, exploiting its completion decisions to extend execution and waste provider resources. In this paper, we present OverServe, a multi-agent framework for constructing such attacks against SaaS agents. OverServe co-designs Model Context Protocol (MCP) status tools and completion-confirmation prompts for the attacker. Each tool call returns accurate status and terminates normally, yet the agent may repeatedly check an unfinished condition to satisfy the prompt. This consumes the SaaS provider's resources even after the original business task is completed. OverServe constructs service-specific tool--prompt pairs and uses separate tool and prompt reviews to guide candidate pair selection. Tested tool specifications trigger no alerts in the evaluated MCP scanners. We evaluate Qwen, Nemotron, DeepSeek, and Sonnet on selected tasks from nine benchmarks. All OverServe runs pass the original task checks. OverServe can reach a maximal amplification of API requests by $93.88\times$ while preserving the original task goal and collateral checks.
