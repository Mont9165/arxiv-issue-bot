# HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?

- arXiv ID: `2610.07639v1`
- Authors: Zhengyang Zhu, Liming Huang, Runmin Ji, Mingxi Ye, Zihan Zhou, Hanyang Guo, Jingwen Wu, Yuhan Ye, Yuming Feng, Hong-Ning Dai, Zibin Zheng
- Published: 2026-10-06
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.07639v1) | [pdf](https://arxiv.org/pdf/2610.07639v1)

## Abstract

Coding agent harnesses mediate tool use and authorize actions, yet their security mechanisms and runtime effects remain incompletely characterized. We present HarnessSecurity, the first systematic empirical study and benchmark of open- and closed-source coding agent harnesses. First, we derive a ten-mechanism taxonomy and then assess 400 harness-mechanism cells using independent ratings by researchers and large language model (LLM) judges. We find that about half of confirmed mechanism implementations are opt-in, while closed-source harnesses exhibit substantial evidence gaps. Second, we introduce HarnessSecurity-Bench, a benchmark of 23 tasks across five attack surfaces without sacrificing legitimate task requirements. Using separate deterministic oracles to measure task utility and attack effects with security setting comparisons, we evaluate nine mechanisms across six leading harnesses: Claude Code, Codex CLI, Gemini CLI, gptme, Qwen Code, and GitHub Copilot. Under a controlled LLM baseline GLM-5.2, we conduct 2,500 trials, recording 81,155 tool calls and over 2.2 billion tokens. Enabling auto-approve increases utility and raises attack success from 29.2% to 95.6%. Network isolation and read-only mode reduce attack effects with substantial utility losses, while command allowlisting and command denylisting reduce attack effects with a small utility loss and a utility gain, respectively. Task-level cases show that restrictions on a shared capability can obstruct both legitimate and malicious operations, and that allowed tools or commands can leave unauthorized operations reachable through alternative execution paths. Harness providers should make security settings verifiable, test alternative execution paths to protected operations, and assess attack effects alongside task utility and execution costs.
