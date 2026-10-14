# Execution-First Synthetic Tool-Use Trace Generation for LLM Agents

- arXiv ID: `2607.29175v1`
- Authors: Hafsa Ouajdi, Francesco Giannuzzo, Alaa Boukhary, Paolo Papotti, Gerard Conangla, Adam Elwood
- Published: 2026-07-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.29175v1) | [pdf](https://arxiv.org/pdf/2607.29175v1)

## Abstract

Agentic software-engineering and industrial systems increasingly operate through executable workflows rather than code genera- tion alone: they search artifacts, invoke tools, inspect structured observations, and query databases. Training these agents requires supervision data that captures valid tool interactions and executable workflows. However, traditional query-first data synthesis can fail because plausible user requests may not correspond to valid tool sequences, compatible parameters, or available data. To address this limitation, we propose SyntheticAgentTraceQA, an execution- first framework for generating scalable supervision data for tool- augmented agents. Our framework first constructs high-level work- flow structures, maps them to available tools through dependency- aware assignment, executes and validates the resulting traces in con- trolled environments, and only then synthesizes natural-language user tasks, teacher-generated reasoning annotations, and reference answers. We evaluate the framework across four tool ecosystems and use the resulting data to fine-tune and evaluate Qwen model variants. The results show that execution-grounded supervision improves tool execution behavior, reference-trace agreement, and answer-generation performance on the evaluated tasks. Further analysis reveals a supervision trade-off: masked supervision, which excludes reasoning annotations from the training objective, im- proves final-answer metrics, whereas full supervision, computing loss over the complete assistant output including reasoning tokens, underperforms on answer quality and does not consistently im- prove reference-trace agreement, particularly at the 9B scale. These findings highlight the importance of designing synthetic supervi- sion according to the desired capabilities of tool-augmented agents.
