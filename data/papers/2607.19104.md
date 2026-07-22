# SciCodePile: A 128GB Corpus and Executable Benchmark for Challenging Scientific Code Generation

- arXiv ID: `2607.19104v1`
- Authors: Weifeng Sun, Ye Fan, Yuchen Chen, Gou Tan, Jieke Shi, Yuan Yidi, Swee Liang Wong, Jonathan Pan, David Lo
- Published: 2026-07-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.19104v1) | [pdf](https://arxiv.org/pdf/2607.19104v1)

## Abstract

Large language models (LLMs) excel at general-purpose code generation, yet how well they handle scientific code remains an open question. Existing datasets and benchmarks are limited in scale, domain coverage, or executable verification, leaving the true gap between current LLMs and reliable scientific code generators inadequately assessed. To address these limitations, we present SciCodePile, the largest scientific code corpus to date, constructed from 37,737 public repositories and collectively comprising 128GB of code that spans multiple computational science disciplines. From this corpus, we further curate an executable benchmark of 200 tasks, each equipped with a sandboxed execution environment and an automated test harness for functional verification. We evaluate 15 LLMs from both open-source and closed-source families on three tasks: prefix-to-suffix completion, fill-in-the-middle infilling, and executable code generation. Results show that scientific code generation remains highly challenging: The best CodeBLEU reaches only 38.13 and 38.37 on the two completion tasks, while the strongest model achieves just 12.30\% Pass@1 on the executable benchmark, underscoring how far current models remain from reliable scientific code generation. To demonstrate the training utility of SciCodePile, we further show that continued pretraining on our corpus improves CodeBLEU by $\times$2.84 on scientific code completion, and instruction tuning on our data improves Pass@1 by $\times$4.79 on the executable benchmark. All code and data are available at https://huggingface.co/SciCodePile.
