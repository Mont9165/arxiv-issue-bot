# TICoder: A Repository-Level Code Generation Framework with Test-Driven Planning and Implementation-Aware Reuse

- arXiv ID: `2606.08135v1`
- Authors: Siyu Nan, Yaling Luo, Jian Wang, Neng Zhang, Bing Li
- Published: 2026-06-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.08135v1) | [pdf](https://arxiv.org/pdf/2606.08135v1)

## Abstract

Repository-level code generation with Large Language Models (LLMs) remains challenging, primarily due to complex dependencies and limited context windows. Recent approaches adopt retrieval-augmented generation (RAG) and the planning mechanism to reuse potential callee functions in the repository. However, these approaches often suffer from two limitations: lack of test-driven behavioral guidance during planning and overlooking the implementation logic embedded in repository code during reuse. As a result, generated plans may not align with expected behaviors, and retrieved functions may not be effectively reused. In this paper, we propose TICoder, a novel repository-level code generation framework that improves both planning and reuse. TICoder introduces a test-driven iterative planning mechanism that leverages test cases as behavioral specifications to refine implementation steps. Furthermore, TICoder employs an implementation-aware code reuse strategy, which retrieves potential callee functions using a dual-view similarity that captures both functional and implementation aspects. We then identify relevant usage patterns through a dual-stage selection strategy, combining structure-based clustering and perplexity-based filtering. We conduct extensive experiments on widely used repository-level code generation benchmarks with various LLMs. Experimental results demonstrate that TICoder outperforms state-of-the-art (SOTA) methods, achieving an average improvement of 11.52%.
