# InteractBench: Benchmarking LLMs on Competitive Programming under Unrevealed Information

- arXiv ID: `2608.29632v1`
- Authors: Jiaze Li, Aocheng Shen, Bing Liu, Boyu Zhang, Xiaoxuan Fan, Qiankun Zhang, Xianjun Deng
- Published: 2026-08-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29632v1) | [pdf](https://arxiv.org/pdf/2608.29632v1)

## Abstract

Competitive programming is increasingly being used to evaluate the algorithmic reasoning capabilities of large language models (LLMs). However, existing benchmarks primarily focus on full-information tasks where all problem inputs are provided upfront. This overlooks a critical dimension of algorithmic reasoning: the ability of generated programs to operate when key information is not revealed upfront. Interactive problems, a distinctive component of competitive programming, embody this challenge. These problems require programs to engage in multi-round interaction with an interactor (a judge program) under strict protocol constraints and limited query budgets, with new information revealed only in response to queries. To address this gap, we introduce InteractBench, a benchmark comprising 322 high-quality interactive problems curated from Codeforces, AtCoder, IOI, and ICPC. Each problem is packaged with executable local interactors, enabling fully offline evaluation. Unlike existing benchmarks, InteractBench assesses whether model-generated code can acquire information and track state dynamically. Our evaluation reveals a significant interaction gap: even the most advanced reasoning models achieve limited success on interactive problems. Beyond success rates, we propose a fine-grained failure taxonomy to diagnose the root causes of these deficiencies. Although algorithmic logic errors remain dominant, protocol violations and query-budget overruns are frequent. Code is available at https://github.com/kmsgk0/InteractBench.
