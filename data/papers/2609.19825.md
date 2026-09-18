# EviRCA: Decoupling Evidence Extraction from Reasoning for Microservice Root-Cause Analysis

- arXiv ID: `2609.19825v1`
- Authors: Yuhao Wang, Zhen Qin, Xingliang Wang, Guochang Li, Weize Li, Shuiguang Deng
- Published: 2026-09-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.19825v1) | [pdf](https://arxiv.org/pdf/2609.19825v1)

## Abstract

Root-cause analysis (RCA) is a critical yet labor-intensive task for maintaining modern microservice systems, making it an attractive target for large language models (LLMs). Recent agentic approaches allow an LLM to iteratively explore raw telemetry by generating and executing code, asking a single model to simultaneously retrieve evidence, localize faults, and infer root causes over large volumes of heterogeneous telemetry, which leads to high computational cost, unstable behavior, and limited diagnostic accuracy. However, raw telemetry consists of numeric metrics, structured traces, and machine-generated logs that are not directly suitable for LLM processing. We present EviRCA, a framework for LLM-based RCA that decouples deterministic evidence extraction from LLM reasoning. A system-agnostic extraction stage converts raw metrics, traces, and logs into a compact set of faithful multimodal evidence cards, while the LLM reasons only over these structured observations through a small set of predefined read-only tools, without accessing raw telemetry or executing code. We evaluate EviRCA on OpenRCA, a benchmark built from real, heterogeneous telemetry across three enterprise systems. EviRCA achieves a correct rate of 40.6%-43.9% across two different LLMs, substantially outperforming prior OpenRCA baselines that achieve up to 15.2%, while reducing token consumption by 15-26x and execution time by 3-20x. Moreover, EviRCA solves hard cases requiring simultaneous reasoning over time, components, and root causes, a setting where previous approaches reported near-zero performance. Our process-level failure analysis further shows that the bottleneck lies in judging the evidence that the extraction stage has already surfaced, rather than searching for it, suggesting that the effectiveness of LLM-based RCA depends heavily on the quality of evidence extraction.
