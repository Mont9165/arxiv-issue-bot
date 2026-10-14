# Persistent Semantic Entities in Tool-Augmented LLM Systems

- arXiv ID: `2608.07952v1`
- Authors: Zhaohui Wang
- Published: 2026-08-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.07952v1) | [pdf](https://arxiv.org/pdf/2608.07952v1)

## Abstract

Tool-augmented LLM agents can harbor implicit state that persists across sessions, activates through events, and propagates across agent boundaries---largely invisible to standard debugging. We formalize this as Persistent Semantic Entities (PSEs): constructs defined by name binding, event triggering, and cross-boundary propagation, and evaluate them across 24 models from 11 families (1.5B--1T parameters). First, every tested model is susceptible (20--100% on the 20-model susceptibility panel), with name binding as the necessary and dominant mechanism: without it, contamination is 0%. Second, persistence depends on contamination type rather than scale or deployment: preference contamination persists undecayed on every model probed (100% at t=10) and instruction contamination persists wherever adopted, persona-style injection decays partially (90%$\to$10%), while factual injection is model-dependent---self-corrected on Llama-3.1-8B and GPT-4o-mini but held at ceiling on both Qwen2.5-coder variants, so we do not claim it self-corrects in general. The preference and instruction results hold across providers in our controlled setting. Third, context-isolated self-verification achieves 20--79% reduction (median 36.5%) without oracle references while keyword-based detection produces systematic false positives, and contamination compounds 1.9$\times$ along a four-stage agent pipeline (40%$\to$75%). Preference and instruction contamination---persistent, lacking self-correction, and poorly captured by standard monitoring---represent a particularly concerning attack surface for deployed agent systems.
