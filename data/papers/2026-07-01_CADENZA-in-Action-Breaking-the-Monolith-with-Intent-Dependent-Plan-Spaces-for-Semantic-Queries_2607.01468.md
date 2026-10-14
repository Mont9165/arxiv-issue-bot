# CADENZA in Action: Breaking the Monolith with Intent-Dependent Plan Spaces for Semantic Queries

- arXiv ID: `2607.01468v1`
- Authors: Jaehyun Ha, Yongjoo Park, Wook-Shin Han
- Published: 2026-07-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.01468v1) | [pdf](https://arxiv.org/pdf/2607.01468v1)

## Abstract

Semantic query processing engines execute semantic operators, whose behavior is specified by natural-language intents, via model inference over multimodal data. Most existing optimizers optimize the operators at the granularity of monolithic implementations -- such as LLMs and embedding models -- forcing a trade-off between expensive model calls and cheaper alternatives that fail to capture intent-dependent semantics. We present CADENZA, a semantic operator optimizer that compiles an intent into decomposed steps, selects concrete physical implementations for each step, and tunes their parameters under user-specified quality-latency-cost preferences. In this demonstration, users interact with CADENZA through a web interface over multimodal databases, exploring how an intent is decomposed into alternative plans, how each plan is optimized, and how different preferences yield different winning plans.
