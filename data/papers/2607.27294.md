# AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents

- arXiv ID: `2607.27294v1`
- Authors: Jiajun Zhou, Zhaoxuan Ke, Jihang Ye, Xuanze Chen, Shanqing Yu, Qi Xuan
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27294v1) | [pdf](https://arxiv.org/pdf/2607.27294v1)

## Abstract

Large language model (LLM)-based workspace agents execute stateful, multi-step workflows across heterogeneous resources, external tools, and persistent state. Their safety must therefore be assessed from actions, side effects, and state changes throughout execution. Although recent benchmarks have advanced executable safety testing and trajectory-aware verification, they rarely provide a unified account of where risks enter, how they elicit unsafe behavior, which harms they target, and where supporting evidence appears during execution. We introduce AgentS4D, a sandboxed benchmark for lifecycle-wide runtime safety evaluation. Its four-dimensional runtime-safety framework uses six risk-entry sources, six induction strategies, and nine target harms to guide case construction, while seven lifecycle checkpoints organize post-run evidence. AgentS4D contains 328 risk-injected cases. We evaluate all 20 combinations of four harnesses (Hermes, OpenClaw, Claude Code, and Codex) and five LLM backends (GPT-5.5, Gemini 3.1 Pro, DeepSeek-V4-Pro, MiniMax-M3, and Qwen3.7-Plus) on these cases, yielding 6,560 runs. Overall, 4,461 runs (68.0%) trigger prespecified unsafe signals. Across the 20 configurations, the observed safety of an agent system varies with both its harness-LLM pairing and how risk is introduced. Agent systems exhibit markedly different safety behavior when the same induction strategy reaches them through different risk carriers. They also respond differently to the same target harm when it is realized through different carriers and strategies. Moreover, 4,344 runs (66.22% overall) are unsafe yet complete. Thus, task completion cannot establish runtime safety, and testing only one form of a risk can conceal important weaknesses. Evaluations should examine complete agent configurations across diverse risk conditions and retain evidence throughout execution.
