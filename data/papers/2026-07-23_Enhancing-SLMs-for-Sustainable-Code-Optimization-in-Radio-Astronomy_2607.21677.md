# Enhancing SLMs for Sustainable Code Optimization in Radio-Astronomy

- arXiv ID: `2607.21677v1`
- Authors: Elisa Chiarotto, Jingbo Li, P. Chris Broekema, Rob V. van Nieuwpoort
- Published: 2026-07-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.21677v1) | [pdf](https://arxiv.org/pdf/2607.21677v1)

## Abstract

Recent Large Language Models (LLMs) can produce and optimize complex code. We investigate the use of LLMs to generate and optimize code for large-scale sciences, focusing on radio astronomy and sustainability. The LOFAR telescope is currently being upgraded, significantly increasing the sky area observed, while simultaneously processing more data faster. However, this is expected to increase the computational requirements 40-fold. This upgrade thus critically depends on rigorous performance optimization of existing software and widespread adoption of accelerators. The code base is very large, making this a daunting task. We therefore investigate and demonstrate an AI-driven approach meant to assist developers in evaluating and optimizing their code, including porting to hardware accelerators. The LOFAR community is committed to sustainable solutions, and needs to achieve these improvements without increasing the energy budget. We thus need to optimize existing codes or port them to accelerators, while making sure that the optimization process itself is also energy efficient. This poses a challenge, since LLMs are energy-intensive. We therefore propose to use Small Language Models (SLMs) instead to limit environmental impact. In this paper, we show how to enhance SLMs through the use of agentic AI. We extend the SLMs in two ways to improve code generation quality and performance: first with a multi-sampling generation strategy and second with incorporating compiler feedback. We demonstrate that multi-sampling SLMs can match or surpass larger single-generation models with fewer computational resources and that feeding compiler output back into the SLMs leads to consistent improvements across all tested models. Our approach is generic, and can also use Retrieval Augmented Generation (RAG) as well as static and dynamic analysis tools in the code generation pipeline.
