# Governing Enterprise AI Traffic at Scale: Design and Operation of a Policy-Driven, Multi-Vendor LLM Gateway on Envoy

- arXiv ID: `2610.35509v1`
- Authors: Mithun Sasidharan, Srinivasan Manoharan, Rupesh Thakur, Abhinav TK, Ashwin Hegde, Anand Gautam
- Published: 2026-10-26
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.35509v1) | [pdf](https://arxiv.org/pdf/2610.35509v1)

## Abstract

Large organizations consume large language models (LLMs) from several vendors at once, each with its own API dialect, credential model, streaming protocol and pricing. Integrated directly, this heterogeneity yields credential sprawl, format lock-in, unbounded spend and inconsistent governance. We present the design and production operation of the Cosmos LLM Gateway, the governed entry point for enterprise LLM traffic at PayPal. Built on Envoy, it splits work by latency profile: I/O-bound control decisions (authentication, credential brokering, policy and budget evaluation) run in an out-of-process external-processing service, while wire-format translation, token metering and prompt-cache shaping run in-proxy as a Rust WebAssembly filter, so that, by default, streamed response body chunks never wait on an out-of-process call. Models, providers and prices are largely validated data rather than code. Governance is declarative policy evaluated by Open Policy Agent and managed through a control plane with role-scoped authoring, approvals, pilots, shadow-mode rollout, usage notifications and versioned policy bundles. For use cases that require it, a data-loss-prevention layer can block, redact or pseudonymize detected sensitive content before it reaches a provider. Spend scopes are views over per-model usage counters, so a new budget applies to spend already recorded in its window without migration. As of September 2026, the gateway serves more than 12,000 developers and hundreds of business use cases, handling roughly 200 billion tokens per day across more than 100 models at 99.999% availability to business. In a benchmark of the core request path against a synthetic upstream, it adds a median of 4 ms and a p99 of 11 ms of overhead at more than 2,200 requests per second on two 4-vCPU instances. We report the architecture, policy model, evaluation and lessons learned.
