# Agent-Native by Design: A Programming Language for Agentic Applications

- arXiv ID: `2611.21298v1`
- Authors: Jayanaka Dantanarayana, Savini Kashmira, Xiaoyu Ma,  Malitha, Malitha Prabhashana, Lingjia Tang, Jason Mars
- Published: 2026-11-16
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.21298v1) | [pdf](https://arxiv.org/pdf/2611.21298v1)

## Abstract

Building agentic applications requires combining large language model (LLM) operations, workflow structure and application state, and model-guided routing. With SDKs and agent frameworks, developers connect these components through supporting code that prepares model inputs, propagates state, and dispatches model-selected steps. Workflow changes can require coordinated updates to this code, increasing development and testing effort. Splitting execution logic between application code and framework internals also limits compiler visibility into control flow and state dependencies, hindering automatic optimization. We introduce Agent-Native Programming, which unifies these three components with shared execution semantics. We realize this approach in Jac, a Python-superset language, through "by llm()" for typed model operations and tool use, Object-Spatial Programming for workflow structure and state, and "visit ... by llm()" for model-guided routing. The routing construct derives the model's choices from executable workflow steps and schedules the selected steps. This explicit connection between model decisions and program execution gives the compiler and runtime a common basis for dependency analysis and automatic optimization. Across five benchmarks and five baselines, Jac achieves a 1.8-8.7x reduction in AI-integration code relative to the OpenAI SDK, with competitive observed task quality and lower coding-agent development effort. Two case studies demonstrate speculative execution and service partitioning through configuration alone, using program analysis and runtime checks to preserve workflow behavior under stated conditions.
