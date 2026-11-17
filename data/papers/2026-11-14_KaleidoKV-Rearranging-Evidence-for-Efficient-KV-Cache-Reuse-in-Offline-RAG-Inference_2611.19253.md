# KaleidoKV: Rearranging Evidence for Efficient KV Cache Reuse in Offline RAG Inference

- arXiv ID: `2611.19253v1`
- Authors: Peiting Xie, Xingyu Tan, Xiangjun Zai, Chen Chen, Xiaoyang Wang, Wenjie Zhang
- Published: 2026-11-14
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.19253v1) | [pdf](https://arxiv.org/pdf/2611.19253v1)

## Abstract

Retrieval-augmented generation (RAG) augments large language models (LLMs) on question-answering (QA) tasks with retrieved evidence at inference time. Related questions in an offline batch often retrieve overlapping evidence, but prefix caching reuses key-value (KV) states only for identical token prefixes, making reuse dependent on evidence order. Although all questions and evidence are known before execution, existing reordering methods commit to early grouping decisions and can miss sharing opportunities that require several requests to move together. Evaluating alternative layouts can incur planning costs that offset inference savings, while concurrent requests may still recompute shared prefixes before their KV states become available. To address these challenges, we propose KaleidoKV, a framework that plans evidence orders across the batch and controls when requests enter the engine while preserving each request's evidence set and content. Joint layout planning revises formed groups through coordinated request moves and keeps a move only if it lowers planned prefill, the computation required when each shared prefix is computed once. A global prefix index selects evidence orders by locating reusable prefixes and evaluates each move incrementally from only the affected request paths. Prefix-ready admission tracks nested prefix dependencies, delaying requests whose shared prefixes are still being computed while allowing independent requests to proceed. Experiments on four QA workloads and four LLMs show that KaleidoKV achieves the highest throughput and lowest mean time to first token in all 16 settings, with approximately 1.24-1.75x the throughput of the strongest baseline, including planning time. With Llama-3.1-8B under the default configuration, actual prefill stays within 0.5% of planned prefill across all four workloads.
