# HybridCodeAuthorship: A Benchmark Dataset for Line-Level Code Authorship Detection

- arXiv ID: `2606.12620v1`
- Authors: Luke Patterson, Li Wang, Adam Faulkner
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.12620v1) | [pdf](https://arxiv.org/pdf/2606.12620v1)

## Abstract

Thanks to the rapid adoption of AI code assistants powered by large language models (LLMs), industry codebases are, increasingly, a hybrid of AI- and human-authored code. For risk management and productivity analysis purposes, it is crucial to enable fine-grained location detection of AI-generated code. To develop algorithms for this task, quality benchmarks are needed to assess performance. However, existing benchmarks tend to comprise academic, LeetCode-style problems and presume a code snippet is either completely human-authored or completely AI-authored, which is not reflective of the diverse intents and styles of industry codebases utilizing AI code assistants. To fill these gaps, we introduce HybridCodeAuthorship, a novel benchmark of Python code files with interleaved human- and AI-authored lines of code to simulate authentic utilization of AI code assistants. In this paper, we first present our dataset construction pipeline, which leverages CodeSearchNet, a massive collection of links to open sourced repositories on GitHub. We then benchmark the performance of two state-of-the-art AI-generated code detection algorithms at both the line- and chunk-level. Experimental results demonstrate that HybridCodeAuthorship is a challenging benchmark with a top-scoring algorithm, AIGCode Detector, obtaining a highest F1 score of 0.48 and 0.56 on chunk-level and line-level code detection tasks, respectively.
