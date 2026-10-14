# Efficiency Hallucination: Formalizing and Measuring Behavioral Calibration in LLM-Based Code Optimization

- arXiv ID: `2609.14839v1`
- Authors: Sarah Wilson, Gail Kaiser, Patrick Musau
- Published: 2026-09-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.14839v1) | [pdf](https://arxiv.org/pdf/2609.14839v1)

## Abstract

The integration of Large Language Models (LLMs) into automated code optimization introduces a critical reliability risk we term the Efficiency Hallucination: an LLM's tendency to issue non-functional mutations with unsubstantiated performance claims on already-optimized code. This is driven by the Evaluation Trap, wherein binary benchmarks incentivize unnecessary modifications over safely abstaining. We present a validation framework using classification penalty methods, evaluated across 180 optimization runs on nine models (GPT, Claude, Gemini) using EffiBench. Under standard prompts, models exhibit a 100% over-edit rate on optimal code. Our guardrail raises correct abstention from 0% to to 44.4%, preserving a 100% edit rate on sub-optimal code with zero false abstentions. Calibration is uneven: GPT-5.4 Mini approaches near-perfect abstention, and simple code is recognized more reliably than complex code. Our framework offers a training-free mechanism to mitigate LLM overconfidence before deployment in production.
