# BatchBench: Toward a Workload-Aware Benchmark for Autoscaling Policies in Big Data Batch Processing -- A Proposed Framework

- arXiv ID: `2605.12272v1`
- Authors: Venkata Krishna Prasanth Budigi, Siri Chandana Sirigiri
- Published: 2026-05-12
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.12272v1) | [pdf](https://arxiv.org/pdf/2605.12272v1)

## Abstract

Autoscaling has become a baseline expectation for cloud-native big data processing, and the design space has expanded beyond rule-based heuristics to include learned controllers and, most recently, large language model (LLM) agents. Yet despite a growing body of work spanning these paradigms, the community lacks a shared benchmark for comparing them. Existing evaluations rely on synthetic TPC-style queries, vendor blog posts with proprietary baselines, or narrow trace replays. Each new policy reports favorable numbers against a different baseline, on a different workload, with a different cost model, making cross-paper comparison effectively impossible. This is a position paper. We propose BatchBench, an open benchmarking framework designed to place rule-based, learned, and agentic autoscaling policies on equal experimental footing. The contribution is the design of the framework, not empirical results. We contribute: (1) a workload taxonomy of six batch processing classes synthesized from published autoscaling benchmarks and publicly released cluster traces; (2) the design of a parameterized workload generator with a validation methodology based on two-sample Kolmogorov-Smirnov and earth-mover distance; (3) a five-axis evaluation harness specification covering cost, SLA attainment, scaling responsiveness, scaling thrash, and decision interpretability, with first-class accounting for LLM inference cost; and (4) a standardized agent interface that lets LLM-based and reinforcement-learning autoscalers be evaluated alongside rule-based controllers with a single API. We discuss the expected evaluation surface, identify open research questions the framework is designed to answer, and outline a roadmap for the empirical paper that will follow. BatchBench's reference implementation is in active development and will be released as open source.
