# Simulation Code Generation for Fluid Systems using Large Language Models: Benchmarking Models and Prompting Strategies

- arXiv ID: `2607.29389v1`
- Authors: Jan Marius Stürmer, Jascha Knack, Tobias Koch, Andreas Weinmann
- Published: 2026-07-31
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.29389v1) | [pdf](https://arxiv.org/pdf/2607.29389v1)

## Abstract

Large language models (LLMs) have demonstrated a strong ability to generate syntactically correct code from natural-language specifications. In this study, we explore how LLMs can be harnessed to automatically translate a neutral graph representation of fluid system models into executable code for two widely adopted simulation environments: the Python library WNTR and the Modelica Standard Library. We conduct a systematic comparison of ten state-of-the-art LLMs and six prompting strategies that differ in the contextual information supplied (e.g., code or documentation). For each configuration we assess the generated code using a suite of software-quality metrics and we validate the functional fidelity of the resulting simulation models by reproducing benchmark fluid system scenarios. Our findings offer concrete guidance for researchers and engineers seeking to integrate LLM-driven code synthesis into model-based design pipelines. While the best-performing configurations achieve acceptable syntactic quality, we observe substantial gaps remain in simulation fidelity.
