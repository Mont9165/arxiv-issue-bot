# Joint Optimization of Tool Creation and Use for Large Language Model Agents

- arXiv ID: `2608.24571v1`
- Authors: Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee
- Published: 2026-08-25
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24571v1) | [pdf](https://arxiv.org/pdf/2608.24571v1)

## Abstract

Tool-augmented language models are bounded by the APIs humans bothered to write; existing tool-creation systems patch this by prompting a frozen LLM at inference time, leaving the model that writes a tool decoupled from the one that uses it, with no signal that the schemas it produces are schemas it can invoke. We propose SMITH (Schema-grounded Multi-task Iterative Tool Honing), a reinforcement learning framework that jointly trains tool creation and tool use inside a single policy. Each rollout is either a build task (write a tool from a few examples) or a use task (invoke a pooled tool on a held-out question). Three separate reward axes catch schema, code, and outcome failures independently, so each failure mode contributes its own gradient. A 4B Qwen3 trained with SMITH on 13 procedural reasoning tasks with exact verifiers reaches 79.8 macro-average accuracy on held-out tasks, the best across all evaluated methods and ahead of an untrained 30B-A3B tool-writer. It also reaches 40.4 on TabMWP-Hard and 42.6 on out-of-domain GQA (+7.6 over the best same-backbone inference-time baseline), without any visual or tabular training data. Tools written by our 4B models also lifted the performance of LFM-2.5-350M and Qwen3-30B-A3B under same reasoning tasks.
