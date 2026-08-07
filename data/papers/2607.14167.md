# Structured Feedback Improves Repair in an LLM Agent Loop

- arXiv ID: `2607.14167v1`
- Authors: Jaideep Ray, Ankit Goyal
- Published: 2026-07-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.14167v1) | [pdf](https://arxiv.org/pdf/2607.14167v1)

## Abstract

LLM agents often retry after external validation rejects a candidate, but the interface between validation and the next model call remains underspecified. We introduce VeriHarness, a code-controlled agent loop in which models generate candidates while external validators control acceptance, budgets, and traces. We use it to compare raw diagnostics with feedback that identifies the failure location, observed value, and admissible alternatives. Across 50 paired TextWorld games under a four-call cap, feedback containing all three fields raises terminal success from 14/50 to 36/50 for Qwen2.5-Coder-14B (+44 percentage points) and from 8/50 to 29/50 for Llama-3.1-8B (+42 points). Ablations locate most of the gain in the admissible alternatives: feedback containing only the location and observed value remains near the raw diagnostic baseline. Presenting the complete repair information in prose instead of a keyed JSON record yields nearly the same success, providing no evidence that JSON syntax itself improves repair. The ordering persists across the tested call budgets and one sampled-decoding setting.
