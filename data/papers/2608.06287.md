# Automatic Translation of Unstructured Requirements into Linear Temporal Logic through Large Language Models

- arXiv ID: `2608.06287v1`
- Authors: Alexandra Newcomb, Omar Ochoa
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.06287v1) | [pdf](https://arxiv.org/pdf/2608.06287v1)

## Abstract

Automatically translating unstructured natural language requirements into formal specifications remains a challenge in requirements engineering and formal methods, particularly for safety- and mission-critical systems whose verification depends on mathematically precise specifications. This paper evaluates whether contemporary off-the-shelf Large Language Models (LLMs) can help bridge this gap by generating Linear Temporal Logic (LTL) formulas directly from unstructured requirements. The study examines six modern LLMs using a few-shot prompting strategy on a heterogeneous benchmark of 15 structurally varied requirements. Five independent generations were collected for each requirement-model pair, yielding 450 candidate LTL formulas in total. Performance was assessed through manual semantic evaluation, pass@k for k in {1, 3, 5}, and a self-consistency measure capturing syntactic reproducibility across stochastic trials. The results indicate that current general-purpose LLMs can achieve practically significant performance on the unstructured NL-to-LTL task without task-specific fine-tuning. The study also considers understandability for non-experts by pairing generated formulas with model-produced natural language explanations and discussing the complementary use of timeline-based LTL visualization. The findings suggest that modern LLMs are becoming viable front-end assistants for semi-automated formalization workflows.
