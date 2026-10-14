# TeleResilienceBench: Quantifying Resilience for LLM Reasoning in Telecommunications

- arXiv ID: `2605.09929v1`
- Authors: Pranshav Gajjar, Emmanuel Ojo, Vijay K Shah
- Published: 2026-05-11
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09929v1) | [pdf](https://arxiv.org/pdf/2605.09929v1)

## Abstract

Deploying large language models in telecommunications requires more than task accuracy. In realistic workflows, a model may inherit partially completed reasoning from a prior step, an upstream agent, or its own earlier generation, and must continue that reasoning even when it is already going wrong. We introduce TeleResilienceBench, a benchmark that quantifies this capability, which we term reasoning resilience, across seven telecom sub-domains drawn from the GSMA Open-Telco LLM suite. Instances are constructed by collecting failures from a weak generator model, truncating the flawed reasoning trace at its midpoint, and asking a target model to continue and correct it. We propose the Correct Flip Rate (CFR) as a direct measure of successful recovery and evaluate eight models spanning the Qwen3.5, Gemma4, and Nemotron-3 families. Our results show that even the strongest model achieves a macro-average CFR of only 29.1%, and scale does not reliably improve resilience within families. Nemotron-3-nano 4b outperforms all Qwen3.5 variants including the 27b model and leads the auxiliary TeleMath numerical evaluation at 23.4% CR%, offering the best resilience-to-cost ratio in the set. A difficulty-stratified analysis further reveals that existing telecom benchmark difficulty labels reflect factual specificity rather than reasoning depth, suggesting that current evaluations measure knowledge coverage more than reasoning ability.
