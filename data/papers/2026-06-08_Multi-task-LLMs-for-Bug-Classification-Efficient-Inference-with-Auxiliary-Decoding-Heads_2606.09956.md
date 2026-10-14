# Multi-task LLMs for Bug Classification: Efficient Inference with Auxiliary Decoding Heads

- arXiv ID: `2606.09956v1`
- Authors: Nikolai Rozanov
- Published: 2026-06-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.09956v1) | [pdf](https://arxiv.org/pdf/2606.09956v1)

## Abstract

The rapid adoption of LLM-powered code generation has dramatically accelerated software development, yet effective verification methods remain severely underdeveloped. Existing bug localization techniques are either prohibitively expensive, requiring minutes of agentic reasoning and thousands of generated tokens per file, and/or operate at coarse function-level granularity unsuitable for precise debugging. While works that focus on line-level granularity and are more light-weight are often limited in their performance or context size. We introduce a novel line-level bug localization approach that addresses these limitations through three key contributions: (1) a token alignment algorithm that overcomes fundamental tokenization challenges in previous work, (2) a lightweight multi-task LLM for bug localization (MLC) enabling efficient line-level bug classification, and (3) an optimized training recipe for multi-line prediction. Our method achieves state-of-the-art performance among similar setups on line-level bug localization with full-file context. At the same time we reach comparable performance to agentic approaches on Defects4J and PypiBugs benchmarks while reducing inference latency by orders of magnitudes, requiring only a single generated token per file. We further demonstrate strong generalization by introducing and evaluating on a small out-of-domain evaluation datasets in Python. We will open source our code, models, and datasets upon acceptance.
