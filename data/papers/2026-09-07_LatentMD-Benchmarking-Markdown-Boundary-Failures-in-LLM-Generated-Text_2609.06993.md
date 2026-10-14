# LatentMD: Benchmarking Markdown Boundary Failures in LLM-Generated Text

- arXiv ID: `2609.06993v1`
- Authors: Sungjune Lee, Myungjoo Kang
- Published: 2026-09-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.06993v1) | [pdf](https://arxiv.org/pdf/2609.06993v1)

## Abstract

Large language models (LLMs) increasingly generate Markdown that is consumed by renderers, agents, code extractors, and structured downstream pipelines. Yet existing evaluations often conflate content quality with format adherence, leaving Markdown boundary failures under-measured. We introduce LatentMD, a benchmark and evaluation protocol for diagnosing CommonMark-level fence-boundary failures in LLM-generated Markdown. LatentMD separates content correctness from boundary correctness, enabling detection of outputs that are content-correct but boundary-broken. The benchmark contains 4,179 prompts and a CLI for scoring arbitrary model outputs. Across 9 LLMs and roughly 37,600 generations, we find that Markdown boundary failures are widespread: 38.0% of valid main-grid outputs are content-correct but boundary-broken, with substantial boundary breakage under unspecified prompts and in a small human-authored validation set. Ablations show that failures are driven primarily by same-family symmetric-delimiter collisions rather than nesting alone, are only partially mitigated by prompt hints, and generalize to Python triple-quote docstrings while JSON remains robust as an asymmetric-delimiter control. LatentMD provides a reproducible diagnostic target for parser-sensitive LLM evaluation.
