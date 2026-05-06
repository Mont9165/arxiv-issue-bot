# ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection

- arXiv ID: `2605.03378v1`
- Authors: Shihao Weng, Yang Feng, Jinrui Zhang, Xiaofei Xie, Jiongchi Yu, Jia Liu
- Published: 2026-05-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03378v1) | [pdf](https://arxiv.org/pdf/2605.03378v1)

## Abstract

The rise of Large Language Model (LLM) agents, augmented with tool use, skills, and external knowledge, has introduced new security risks. Among them, prompt injection attacks, where adversaries embed malicious instructions into the agent workflow, have emerged as the primary threat. However, existing benchmarks and defenses are fundamentally limited as they assume context-insensitive settings in which the agent works under a fully specified user instruction, and the attacks are straightforward and context-independent. As a result, they fail to capture real-world deployments where agent behavior usually depends on dynamic context, not just the user prompt, and adversaries can adapt their attacks to different context. Similarly, existing defenses built on this narrow threat model overlook the nature of real-world agent delegation.
  In this paper, we present AgentLure, a benchmark that captures context-dependent tasks and context-aware prompt injection attacks. AgentLure spans four agentic domains and eight attack vectors across diverse attack surfaces. Our evaluation shows that existing defenses often struggle in this setting, yielding poor performance against such attacks in agentic systems. To address this limitation, we propose ARGUS, a defense mechanism that enforces provenance-aware decision auditing for LLM agents. ARGUS constructs an influence provenance graph to track how untrusted context propagates into agent decisions and verify whether a decision is justified by trustworthy evidence before execution. Our evaluation shows ARGUS reduces attack success rate to 3.8% while preserving 87.5% task utility, significantly outperforming existing defenses and remaining robust against adaptive white-box adversaries.
