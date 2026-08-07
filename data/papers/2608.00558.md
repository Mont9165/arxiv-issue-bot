# AiFlow: Token-Native Reactive Orchestration with Bounded Backpressure for Streaming LLM Applications

- arXiv ID: `2608.00558v1`
- Authors: Qunhui Zhang
- Published: 2026-08-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.00558v1) | [pdf](https://arxiv.org/pdf/2608.00558v1)

## Abstract

Large language model (LLM) applications increasingly operate as streaming workflows combining retrieval, tool calls, safety filters, and multi-agent coordination. Although contemporary frameworks expose provider deltas, workflow nodes often treat generation as coarse request-response steps, leaving queue management, worker allocation, ordering, and backpressure to ad hoc callback code. This paper presents AiFlow, a token-native reactive orchestration model that normalizes provider deltas into typed Context<T> events propagated through a directed streaming graph. Each node is managed by a Node Guardian that declares and enforces local queue bounds, worker concurrency, ordering, overflow policy, cancellation propagation, and retry discipline. We formalize the bounded-memory property, present the compilation from a compact DSL and JSON graph form, and provide static validation for type safety, state concurrency, and injection compatibility. Controlled microbenchmarks, captured DeepSeek trace replay (30 runs), descriptive online runs, LangGraph baselines, a streaming RAG workload, and an Ollama local-backend check show that AiFlow does not alter provider-side Model TTFT but reduces Application TTFPT by 70.9-94.7\% versus aggregation and keeps runtime-owned queue depth within declared bounds (93.7-96.5\% MaxQ reduction versus unbounded policies). The supplementary artifact contains scripts, raw traces, machine-readable tables, checksums, and an API-free smoke test; the public implementation is available through the FIT Framework repository.
