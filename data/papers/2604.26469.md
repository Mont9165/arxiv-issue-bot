# An Empirical Study of Speculative Decoding on Software Engineering Tasks

- arXiv ID: `2604.26469v1`
- Authors: Yijia Li, Junkai Chen, Xing Hu, Xin Xia
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26469v1) | [pdf](https://arxiv.org/pdf/2604.26469v1)

## Abstract

Large Language Models (LLMs) have become widely used for Software Engineering (SE) tasks, spanning from function-level code generation to complex repository-level workflows. However, the high latency of autoregressive inference remains a significant bottleneck, hindering their deployment in interactive environments. While Speculative Decoding (SD) offers a promising technique for lossless acceleration, prior research on long-context repository-level tasks and complex agentic interactions remains limited. To bridge this gap, we present the first systematic empirical study to evaluate the effectiveness of SD in SE tasks. We systematically benchmark a comprehensive spectrum of strategies, encompassing both model-based and model-free methods, across representative generation, editing, and repair scenarios. Our empirical results indicate that SD demonstrates clear potential for accelerating inference, particularly for smaller models that achieve higher speedups than those of their larger counterparts. We find that the effectiveness of SD methods varies across different task scenarios. Model-based approaches are well-suited for code generation, whereas model-free methods are better adapted to repository-level repair and editing scenarios. Furthermore, we observe that the repetitiveness of SE tasks improves the performance of model-free methods. In contrast to natural language tasks, the higher predictability of SE tasks allows for more aggressive hyperparameters. Our findings are summarized as guidelines to help increase inference efficiency for SE scenarios.
