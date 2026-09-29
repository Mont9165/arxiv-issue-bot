# RAISE: Reinforcing Access Control Policy Synthesis in LLMs via Symbolic Evaluation

- arXiv ID: `2609.33796v1`
- Authors: Yingming Zhou, Adarsh Vatsa, William Eiers
- Published: 2026-09-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.33796v1) | [pdf](https://arxiv.org/pdf/2609.33796v1)

## Abstract

Translating natural-language access-control requirements into policies requires careful reasoning about permissions, constraints, and exceptions, and even frontier LLMs often produce policies that violate the intended authorization semantics. We construct CedarInstruct, to our knowledge the first dataset that supports both training and semantic evaluation for formally verifiable Cedar policy synthesis. It contains 5,800 scenarios across 44 domains and 1,408 representing a single synthetic organization, each with a verified target policy and an executable verification plan. On this data we introduce RAISE, which trains policy synthesizers from formal verification in two stages, verified supervised fine-tuning (SFT) followed by a reinforcement learning (RL) stage that learns from verifier signal. We find that SFT succeeds largely by letting models express authorization logic they already have, since untrained models rarely write valid Cedar but often reason correctly when they do. After SFT, how the verifier's information is used matters more than how much of it is used. Of six RL instantiations that consume progressively richer verifier signal, only RAISE-OC improves meaningfully on SFT; it turns failed checks and symbolic counterexamples into guided exploration and learns from the result with off-context GRPO. With about 5.4K verified scenarios and LoRA fine-tuning, RAISE-OC trains Qwen3.5-9B to surpass zero-shot GPT-6 Astra and Claude Opus 5 by 13.33 and 16.26 percentage points in semantic success on held-out scenarios, and training transfers to the independently constructed CedarBench.
