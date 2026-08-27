# XREPOTEST: Benchmarking Multilingual Repository-Level Unit Test Generation for Large Language Models

- arXiv ID: `2608.25939v1`
- Authors: Dung Le Quang, Dong Cao Van, Nam Le Hai, Linh Ngo Van, Anh M. T. Bui, Phuong T. Nguyen
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25939v1) | [pdf](https://arxiv.org/pdf/2608.25939v1)

## Abstract

Large language models (LLMs) have shown promise for automated unit test generation, but existing evaluations largely rely on standalone settings and a narrow set of programming languages, overestimating real-world readiness. We introduce XREPOTEST, a multilingual repository-level benchmark for unit test generation spanning five underexplored languages: Rust, Go, Julia, PHP, and Ruby. XREPOTEST evaluates tests under realistic repository constraints using a containerized execution framework and multiple context augmentation strategies, including file-level, LSP-based, and retrieval-based context. Beyond standard metrics such as test pass rate and coverage, we propose Invocation Rate (IR) to assess whether generated tests meaningfully exercise the intended functionality. Experiments with 14 state-of-the-art LLMs, including Claude 4.5, GPT-5.2, DeepSeek V4-Pro, and Qwen families, reveal a substantial gap between standalone and repository-level performance, as well as trade-offs between richer context and test reliability. Overall, XREPOTEST provides a challenging and informative benchmark to advance scalable and robust unit test generation in realistic software environments. The dataset and code are publicly available at: https://github.com/solis-team/XRepoTest
