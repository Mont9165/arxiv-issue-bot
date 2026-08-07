# Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers

- arXiv ID: `2604.21700v1`
- Authors: Jiali Wei, Ming Fan, Guoheng Sun, Xicheng Zhang, Haijun Wang, Ting Liu
- Published: 2026-04-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.21700v1) | [pdf](https://arxiv.org/pdf/2604.21700v1)

## Abstract

The growing application of large language models (LLMs) in safety-critical domains has raised urgent concerns about their security. Many recent studies have demonstrated the feasibility of backdoor attacks against LLMs. However, existing methods suffer from three key shortcomings: explicit trigger patterns that compromise naturalness, unreliable injection of attacker-specified payloads in long-form generation, and incompletely specified threat models that obscure how backdoors are delivered and activated in practice. To address these gaps, we present BadStyle, a complete backdoor attack framework and pipeline. BadStyle leverages an LLM as a poisoned sample generator to construct natural and stealthy poisoned samples that carry imperceptible style-level triggers while preserving semantics and fluency. To stabilize payload injection during fine-tuning, we design an auxiliary target loss that reinforces the attacker-specified target content in responses to poisoned inputs and penalizes its emergence in benign responses. We further ground the attack in a realistic threat model and systematically evaluate BadStyle under both prompt-induced and PEFT-based injection strategies. Extensive experiments across seven victim LLMs, including LLaMA, Phi, DeepSeek, and GPT series, demonstrate that BadStyle achieves high attack success rates (ASRs) while maintaining strong stealthiness. The proposed auxiliary target loss substantially improves the stability of backdoor activation, yielding an average ASR improvement of around 30% across style-level triggers. Even in downstream deployment scenarios unknown during injection, the implanted backdoor remains effective. Moreover, BadStyle consistently evades representative input-level defenses and bypasses output-level defenses through simple camouflage.
