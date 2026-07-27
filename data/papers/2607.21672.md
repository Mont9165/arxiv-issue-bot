# Pixels for Programs? A Cross-Provider Case Study of Input-Token Accounting for Source Code as Text and Images

- arXiv ID: `2607.21672v1`
- Authors: Ronak Bhalgami
- Published: 2026-07-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2607.21672v1) | [pdf](https://arxiv.org/pdf/2607.21672v1)

## Abstract

Long source-code contexts consume many text tokens, motivating the proposal to render code as images for vision-language models. Recent work asks whether models can still solve code tasks after this transformation. We examine a different systems question: how commercial APIs count the resulting requests. We present a reproducible measurement case study of provider-reported input tokens for raw source text and a compact rendered-image representation. The benchmark pairs requests across five programming languages, nine source lengths from 20 to 2,000 lines, and 15 available model aliases exposed by Anthropic, OpenAI, and Google Vertex AI. These aliases collapse to approximately five distinct accounting signatures and are not independent model replications. Across 675 complete text/image pairs, aggregate image-to-text ratios are 0.135, 0.194, and 0.242, corresponding to reported input-token reductions of 86.5\%, 80.6\%, and 75.8\%, respectively. These totals conceal materially different break-even behavior: Anthropic and OpenAI images receive lower counts at every tested size, while Gemini images require 6.95 times as many tokens at 20 lines and cross below text only at 200 lines in the aggregate. A targeted audit also reproduces non-monotonic Gemini image accounting across a page boundary. This study measures black-box request accounting for one compact rendering pipeline. It does not measure semantic fidelity, task accuracy, latency, monetary cost, or coding-agent efficiency. We release the scripts, revision-pinned corpus specification, raw usage records, validators, and deterministic analysis needed to reproduce and extend the study.
