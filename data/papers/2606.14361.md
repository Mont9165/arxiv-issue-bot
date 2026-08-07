# SemPiper: Interactive Code Synthesis for Semantic Operators in Machine Learning Pipelines

- arXiv ID: `2606.14361v1`
- Authors: Olga Ovcharenko, Luciano Duarte, Sebastian Schelter
- Published: 2026-06-12
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.14361v1) | [pdf](https://arxiv.org/pdf/2606.14361v1)

## Abstract

Machine learning (ML) pipelines require extensive data preparation, feature engineering, and integration across heterogeneous sources, making them tedious and error-prone to develop. While large language models (LLMs) have recently shown promise for assisting programming tasks, chat-based interfaces provide limited control over pipeline behavior and often produce code that is difficult to optimize or integrate into production systems. We demonstrate SemPipes, a novel programming model that extends ML pipelines with declarative, LLM-powered semantic data operators. SemPipes allows developers to specify high-level natural language instructions for data-centric operations, while seamlessly combining these operators with arbitrary Python code from standard data science libraries. For the semantic operators, it synthesizes specialized implementations at pipeline training time, conditioned on dataset characteristics and pipeline context, enabling the flexible yet controlled integration of LLM capabilities. We demonstrate SemPipes through SemPiper, an interactive interface that visualizes computational graphs of the pipelines, synthesized operator implementations, and optimization trajectories produced by an evolutionary search procedure. Attendees can explore three end-to-end scenarios, modify pipelines, inspect generated code, and observe how semantic operators are synthesized and iteratively optimized. The demonstration highlights how declarative semantic operators enable controllable, optimizable, and practical integration of LLMs into ML pipeline development.
