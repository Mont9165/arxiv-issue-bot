# Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents

- arXiv ID: `2607.03968v1`
- Authors: Abhishek Kumar, Carsten Maple
- Published: 2026-07-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.03968v1) | [pdf](https://arxiv.org/pdf/2607.03968v1)

## Abstract

Large language models are increasingly deployed as IDE-integrated coding agents that decompose tasks, generate and edit files, run code, and refine outputs over many turns. Yet their safety is still often evaluated as if they were chatbots: one harmful prompt, one response, judged in isolation. We introduce workflow-level jailbreak construction, a failure mode in which a harmful objective is assembled across ordinary stages of a software-development workflow rather than generated through a single direct prompt. Using GitHub Copilot in Visual Studio Code, we study four closed-weight backends: Claude Sonnet 4.6, Claude Haiku 4.5, Gemini 3.1 Pro, and Gemini 3.5 Flash. Across 204 prompts from Hammurabi's Code, HarmBench, and AdvBench , the models show near-complete refusal under direct chat, CSV-read, and single-step code-fix baselines, with only 8/816 successful responses in each baseline condition. Under the full workflow, however, the same prompts and backends produce 816/816 unsafe teaching-shot completions, all independently confirmed by two expert evaluators under a strict rubric. These results show that conversational refusal benchmarks can substantially overstate the safety of deployed coding agents and motivate defenses that reason about safety across multi-turn IDE workflows and their generated artifacts, not only individual chat turns.
