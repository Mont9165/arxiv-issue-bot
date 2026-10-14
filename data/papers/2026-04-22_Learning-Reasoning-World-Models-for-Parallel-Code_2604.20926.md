# Learning Reasoning World Models for Parallel Code

- arXiv ID: `2604.20926v1`
- Authors: Gautam Singh, Arjun Guha, Bhavya Kailkhura, Harshitha Menon
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20926v1) | [pdf](https://arxiv.org/pdf/2604.20926v1)

## Abstract

Large language models have shown remarkable ability in serial code generation, but they still struggle with parallel code for which training data is comparatively scarce. A common remedy is to use coding agents that interact with external tools, but tool calls can be costly and sometimes impractical, e.g., for partially written code. We propose Parallel-Code World Models (PCWMs), reasoning LLMs that aim to predict tool outcomes directly from parallel source code. To train PCWMs, we design a novel exploration and data generation pipeline that samples diverse parallel-coding problems and candidate implementations across multiple domains, then executes them via tools to record data races and performance profiles. From these, we synthesize hindsight reasoning traces that causally connect source code to observed tool outcomes. Fine-tuning on the resulting data yields noticeable gains, with a 7B-parameter world model improving from 64.3% to 72.8% accuracy in race-outcome prediction, while an 8B-parameter model improves in a performance profiling task from 49.3% to 58.6% accuracy. Furthermore, when open-weight models were tasked with fixing data races, world-model feedback improved their race-fixing rates relative to self-feedback by 2.7%-9.1% using our 7B-parameter world model and by 6.1%-11.1% using our 14B-parameter world model. Our results suggest that reasoning models have the potential to serve as practical substitutes for external tool calls in parallel-coding agents.
