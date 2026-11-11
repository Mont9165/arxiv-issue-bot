# ARoute: Task-Aligned Batch and Streaming Model Routing

- arXiv ID: `2611.13209v1`
- Authors: Daofu Zhang, Qingcheng Zeng, Chunwei Liu, Fuheng Zhao
- Published: 2026-11-09
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.13209v1) | [pdf](https://arxiv.org/pdf/2611.13209v1)

## Abstract

Language models increasingly power data-intensive applications, from semantic data processing to question answering and agentic workflows. Using frontier models for every request is prohibitively expensive, while relying only on smaller models reduces accuracy. We study model routing under a user-specified cost budget, aiming to maximize accuracy under task-specific correctness criteria. Existing routers fall short in two ways: pretrained routers rely on generic preference signals that may not reflect a task's own correctness criteria or a new model pair, and model cascades run the weaker model first on every request, adding sequential latency. We present ARoute, a task-aligned router that learns cost and accuracy signals to select a model for each request before inference. ARoute has two variants: ARoute-Batch operates on a batch of requests known in advance, routing requests with the greatest expected benefit to the stronger model subject to the budget, whereas ARoute-Stream processes requests online, using a threshold calibrated on a small validation set to satisfy the cost quota and dynamically adjusting it as the budget is consumed. For ARoute-Stream, we provide a finite-sample guarantee on expected normalized spending. We evaluate ARoute on MMLU-Pro, LiveCodeBench, SuperGPQA, and two value-filling tasks built from SWAN semantic query benchmark against other state-of-the-art approaches. At matched cost, ARoute-Batch achieves the highest mean accuracy in all 15 task-cost settings, improving over the strongest baseline by 4.1 percentage points on average and by up to 11.9 points. ARoute also completes a batch up to 2.8x faster than cascades.
