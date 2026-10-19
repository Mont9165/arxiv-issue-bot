# Robust Function Calling for LLM Agents Under Interface Drift

- arXiv ID: `2610.23342v1`
- Authors: Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy
- Published: 2026-10-16
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.23342v1) | [pdf](https://arxiv.org/pdf/2610.23342v1)

## Abstract

Tool-augmented language-model agents rely on interface text: tool descriptions, argument schemas, and the candidate tool list shown at inference time. These interfaces often change after deployment even when the underlying tool semantics remain fixed, creating a practical reliability problem for function-calling systems. We study this failure mode as interface drift and evaluate whether a lightweight, training-free repair layer can recover robustness without retraining the base model. Our method, SchemaShield-Lite, combines schema validation, candidate-set retry for missing tool names, and one-shot constrained repair. On Qwen3.5-9B, it raises DICE-300 accuracy from 0.717 to 0.813 and BFCL-200 accuracy from 0.580 to 0.805, recovering 19/22 and 33/45 drift-induced failures with no observed repair harms. Naive retry does not explain the gains. Ablations show that candidate-set drift, especially distractor tools, accounts for most observed damage, while description and schema edits alone are less harmful. The results position validation-and-repair as a practical robustness layer for deployed LLM-agent tool use.
