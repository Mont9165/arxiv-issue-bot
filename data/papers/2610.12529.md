# Fix What's Wrong, Keep What's Right: Hallucination Repair for LLM-Based Optimization Modeling

- arXiv ID: `2610.12529v1`
- Authors: Jiageng Wu, Chao Shen, Zihan Guo, Junyan Shao, Zongyan Zhang, Jie Song, Zhong Li, Mingyang Sun
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `math.OC`
- Links: [abs](http://arxiv.org/abs/2610.12529v1) | [pdf](https://arxiv.org/pdf/2610.12529v1)

## Abstract

Large language models (LLMs) are increasingly being explored to automate operations research modeling, reduce modeling time and lower the expertise barrier to optimization based decision support. However, this process often introduces inconsistencies between generated artifacts and the original problem, which we refer to as optimization modeling hallucinations. Despite progress in general-purpose hallucination mitigation, optimization modeling poses a distinct repair challenge: restoring fidelity to the original problem through coordinated model-code updates. We introduce OPT-Kraken, a training-free hallucination repair framework. To the best of our knowledge, it is the first post-hoc framework for repairing hallucinations in LLM-based optimization modeling artifacts. It extracts problem requirements and instance data, localizes errors by checking problem-model fidelity, model-code consistency, and data grounding, and selects repair granularity by the affected scope. For local repair, category rules and instance evidence are compiled into contracts specifying permitted edits, expected effects, and protected content. Experiments on established optimization modeling benchmarks show positive gains across automatic modeling frameworks and fine-tuned models. On zero-shot artifacts from multiple base models, OPT-Kraken effectively repairs optimization modeling hallucinations while preserving initially correct artifacts. These results demonstrate effective and controlled repair for LLM-based optimization modeling artifacts.
