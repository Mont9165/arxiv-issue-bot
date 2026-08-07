# MAS-Algorithm: A Workflow for Solving Algorithmic Programming Problems with a Multi-Agent System

- arXiv ID: `2605.05949v1`
- Authors: Yuliang Xu, Xiang Xu, Yao Wan, Hu Wei, Tong Jia
- Published: 2026-05-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.05949v1) | [pdf](https://arxiv.org/pdf/2605.05949v1)

## Abstract

Algorithmic problem solving serves as a rigorous testbed for evaluating structured reasoning in AI coding systems, as it directly reflects a model's ability to perform structured reasoning in complex scenarios.Existing approaches predominantly rely on model-centric strategies, such as architectural modifications and data scaling, which are costly and offer limited interpretability. Alternative methods leveraging external tools or prompting techniques (e.g., chain-of-thought) are often fragmented and lack a unified framework. In this paper, we propose MAS-Algorithm, a systematic multi-agent workflow for algorithmic problem solving inspired by the practices of competitive programmers and algorithm engineers. Our framework decomposes the end-to-end solving process into modular stages, enabling structured reasoning, tool integration, and flexible coordination among agents. The design emphasizes both rigor and extensibility, allowing it to generalize across diverse problem types.Experimental results on a self-constructed benchmark demonstrate consistent improvements across multiple Qwen series models, achieving an average gain of 6.48% in acceptance rate. In contrast, parameter-efficient fine-tuning on the same data yields only a marginal improvement of 0.89%. We further observe a 4.72% gain on LiveCodeBench-Pro, along with consistent improvements across additional accuracy and efficiency metrics.Beyond performance gains, we conduct comprehensive analyses to better understand the reasoning process within the workflow, including error patterns and cross-scenario behaviors. We further perform customized replacement and ablation studies to explore the upper bound of the framework, showing that individual agents can contribute improvements of up to 27.7%. These results highlight the strong potential of MAS-Algorithm for advancing AI-driven algorithmic reasoning.
