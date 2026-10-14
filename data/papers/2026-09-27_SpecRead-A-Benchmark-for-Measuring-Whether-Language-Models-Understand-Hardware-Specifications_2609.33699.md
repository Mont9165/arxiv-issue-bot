# SpecRead: A Benchmark for Measuring Whether Language Models Understand Hardware Specifications

- arXiv ID: `2609.33699v1`
- Authors: Feilian Huang
- Published: 2026-09-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.33699v1) | [pdf](https://arxiv.org/pdf/2609.33699v1)

## Abstract

Existing benchmarks for large language models (LLMs) in hardware design evaluate downstream artifacts such as generated RTL, assertions, or testbenches. When a model fails such a benchmark, the failure is ambiguous: it may have misread the specification, or it may have understood the specification and failed to write the code. We present SpecRead, a benchmark that isolates specification comprehension from generation ability. SpecRead v2.1 contains 385 questions over 10 open-source OpenTitan IP blocks: exact retrieval, cross-section reasoning, contradiction detection in mutated specifications, and spec-RTL consistency checking, plus 82 controls (41 distractor, 41 consistent-RTL). Type-4 items are built from real RTL mutations; we retain only mutations that Icarus Verilog simulation shows to change observable behavior. A with-spec vs. without-spec ablation suggests the questions require the excerpt, not training recall alone (without-spec accuracy 3/20 on the t1/t2 subset), though memorization of the source text may still help spot mutations. As an initial characterization with a small model, Ministral-3B scores 33.2% overall (128/385; macro average 39.0%): 55.2% on retrieval, 51.7% on cross-section reasoning. On the two contradiction-focused types, the verdict-plus-location measure gives 48.0% (t3) and 63.3% (t4), with a 51.2% false-positive rate on distractors and 100% on consistent-RTL controls. Layered scoring shows the model locates contradictions well (78.9-81.6% location accuracy) but scores lower on their category (43.9-49.7%). A structured "rule-table" prompting intervention lowers accuracy on every question type except t2 (tied). SpecRead is automatically scorable by deterministic checks, with gray-zone cases counted wrong under the conservative main scoring. The benchmark is regenerable for type-3 items via mutation injection, and built exclusively from public sources.
