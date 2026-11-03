# Self-Refining Prompt Induction for Streaming Text-to-SQL

- arXiv ID: `2611.00960v1`
- Authors: Gaetano Rossiello, Alfio Gliozzo, Nandana Mihindukulasooriya, Erick Lee, Nabila Siregar, Lisa Amini
- Published: 2026-10-31
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.00960v1) | [pdf](https://arxiv.org/pdf/2611.00960v1)

## Abstract

Text-to-SQL assistants for streaming engines must handle dialect-specific types, windowing rules, and temporal semantics, including constructs poorly handled by generic prompts. We present Self-Refining Prompt Induction (SRPI), an offline method that converts generation failures into reusable dialect instructions while keeping model weights fixed. A Refiner revises the Generator's prompt using reference-conditioned feedback from three LLM judges; a sampled regression guard checks earlier successes, and a separate Compressor reduces prompt length. Inference uses the frozen prompt without retrieval or query repair. We evaluate cross-domain and cross-model transfer on Confluent Cloud Flink SQL using a controlled synthetic workload seeded by 30 expert-written examples, with 335 induction examples and 257 questions from held-out domains. The same induced prompt improves mean judge scores across seven Generators by 7.1-19.2 percentage points, including an increase from 85.3% to 97.5% for the induction model. A separate compression study reduces prompt length by 52.7% with a 0.19-percentage-point score decrease. An assistant using the induced prompt is in early access, with initial user feedback to inform subsequent refinement.
