# Inference Validation for Regulated AI: Building a Decision Pipeline on NVIDIA AIPerf

- arXiv ID: `2611.12737v1`
- Authors: Dev Akre, Roman Bobalo, Manoj Dobbali
- Published: 2026-11-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2611.12737v1) | [pdf](https://arxiv.org/pdf/2611.12737v1)

## Abstract

Deploying large language models in regulated industries requires more than picking the fastest inference engine: it requires evidence that a configuration meets contractual and legal obligations before it serves a single customer request. We describe Runway, an internal validation harness built at MasterControl that builds a governed decision pipeline around NVIDIA AIPerf. The key insight is separating concerns: AIPerf provides the trusted measurement, while Runway provides the experiment design that comes before it and the compliance, cost, and audit decisions that come after. We describe the architecture and the storage model that makes caching and audit one mechanism. We report three findings from Runway sweeps: TensorRT-LLM and vLLM rankings invert with concurrency; a newer, pricier GPU instance can be the cheaper one per request; and speculative decoding behaves differently across engines under load, so engine configuration can outweigh engine choice.
