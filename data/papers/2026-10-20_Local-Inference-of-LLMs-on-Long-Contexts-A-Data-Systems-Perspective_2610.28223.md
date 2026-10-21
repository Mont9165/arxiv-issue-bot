# Local Inference of LLMs on Long Contexts: A Data Systems Perspective

- arXiv ID: `2610.28223v1`
- Authors: Mattias Dürrmeier, Alberto Lerner
- Published: 2026-10-20
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.28223v1) | [pdf](https://arxiv.org/pdf/2610.28223v1)

## Abstract

Large language models can solve complex problems across a variety of subjects, such as mathematics and coding. For such complex analytical tasks, models with a long context perform better. Serving models with long context is currently mostly done on powerful systems with multiple GPUs, which are too expensive for most users. An alternative is local inference, or serving a model on a user's own machine, which removes per-token costs and rate limits, besides keeping sensitive data private and giving users full control over the models they run. The common understanding, however, is that local LLMs need compression (e.g., quantization) to run on a single GPU. In this paper, we set out to study the limitations that prevent serving long-context models for single users, besides the capacity issue. Rather than characterizing a single model on one GPU, we analyze how different models behave across several GPU generations. This lets us uncover not just individual bottlenecks but broader trends in where inefficiencies arise. Our analysis confirms that, as expected, self-attention dominates the runtime for long-context inference. More unexpectedly, our evaluation reveals that the current structure of self-attention leaves key GPU resources significantly underutilized, and the newest GPU is often the least well served. Many of these findings are fundamentally data management problems, from paging the KV cache to improving cache utilization and synchronization in the GPU, which is why we bring this study to the Data Systems community. To engage this community, we present our findings as a series of experimental observations and formulate recommendations for future work.
