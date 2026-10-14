# Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Execution Tasks?

- arXiv ID: `2605.03195v1`
- Authors: Spandan Garg, Vikram Nitin, Yufan Huang
- Published: 2026-05-04
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03195v1) | [pdf](https://arxiv.org/pdf/2605.03195v1)

## Abstract

Modern coding agents increasingly delegate specialized subtasks to subagents, which are smaller, focused agentic loops that handle narrow responsibilities like search, debugging or terminal execution. This architectural pattern keeps the main agent's context window clean by isolating verbose outputs (e.g. build logs, test results, etc.) within the subagent context. Typically when agents employ subagents for such tasks, they use frontier models as these subagents. In this paper, we investigate whether a finetuned small language model (SLM) can achieve comparable performance to frontier models in the task of agentic terminal execution. We present Terminus-4B, which is a post-trained Qwen3-4B model via Supervised Finetuning (SFT) and Reinforcement Learning (RL) using rubric-based LLM-as-judge reward, specifically for this task. In our extensive evaluation spanning various frontier models, training ablations and main agent configurations, we find that Terminus-4B is able to reduce the token usage of the main agent by up to ~30% compared to the No Subagent baseline with no impact to agent performance on benchmarks like SWE-Bench Pro and our internal SWE-Bench C# benchmark, which tends to be heavy in verbose execution tasks. Furthermore, Terminus-4B improves key metrics showing the main agent relying on the outputs of the subagent and doing fewer terminal execution tasks by itself. We see that our model not only closes the gap between the Vanilla Qwen model and frontier models like Claude Sonnet / Opus / GPT-5.3-Codex, but often even exceeds their performance.
