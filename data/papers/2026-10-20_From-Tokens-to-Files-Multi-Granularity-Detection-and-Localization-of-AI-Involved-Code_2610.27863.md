# From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code

- arXiv ID: `2610.27863v1`
- Authors: Yue Xu, Xiyang Wang, Hui Liu, Bolei He
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.27863v1) | [pdf](https://arxiv.org/pdf/2610.27863v1)

## Abstract

The increasing use of large language models for code generation calls for methods that distinguish purely human-written code from AI-involved code: files in which any part, however small, was generated or substantially modified by a model. Beyond flagging such files, we aim to localize the lines or blocks attributable to AI. Existing approaches compress a file into a single score, from surface stylistic features or a global code representation, which averages away the evidence when only a few blocks are AI-involved. We propose a framework that models AI authorship at the token level and predicts at the line, block, and file levels. A frozen code language model is equipped with two low-rank adapters, trained separately on machine-written and human-written files; their per-token log-likelihood ratio provides local evidence of AI authorship. Lightweight heads aggregate this evidence within lines and blocks, using the surrounding code context, and their local predictions are aggregated into a file-level decision. We train on mixed-authorship files built from human originals and their AI-generated or AI-modified counterparts, including continuation and fill-in-the-middle scenarios. On an internal test set of 11,773 AI-involved files across six generation regimes against 2,541 human files, our method reaches 72.4 macro F1 at a 1% FPR operating point. With no adaptation, it reaches 62.5 line-level F1 on HybridCodeAuthorship, an external human-AI co-writing benchmark with no training split, above the 56 its own paper reports as the best line-level result. On 19,445 human-written files from repositories created before 2022, the false-positive rate stays between 0.55% and 0.81% under the transported 1% threshold, so the operating point holds on real human code.
