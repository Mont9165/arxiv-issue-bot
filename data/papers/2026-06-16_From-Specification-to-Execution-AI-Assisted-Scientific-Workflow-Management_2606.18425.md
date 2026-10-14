# From Specification to Execution: AI Assisted Scientific Workflow Management

- arXiv ID: `2606.18425v1`
- Authors: Komal Thareja, Hamza Safri, Rajiv Mayani, Anirban Mandal, Ewa Deelman
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2606.18425v1) | [pdf](https://arxiv.org/pdf/2606.18425v1)

## Abstract

Scientific workflow management systems (WMS) support scalable and reproducible execution of complex pipelines, but workflow design, implementation, and debugging remain largely manual and require significant expertise. Recent approaches using large language models (LLMs) show promise for workflow generation from natural language, but often rely on direct code synthesis, which limits transparency, reproducibility, and integration with workflow systems. We present an AI-assisted approach to scientific workflow management that combines specification-driven workflow generation, automated debugging, and distributed execution. The method introduces a structured specification phase that separates workflow intent, design, and implementation, allowing validation prior to code generation. We also develop an LLM-based debugging agent that diagnoses and resolves failures across multiple system layers. To support distributed execution and user interaction, we integrate Pegasus, a widely used WMS, with a Model Context Protocol (MCP) layer, providing a unified interface for workflow submission, monitoring, and control. We evaluate the approach using a federated learning workflow for medical imaging, chosen for its parallel, iterative, and dependency-intensive structure. The system generated and executed large-scale workflows with thousands of jobs, reduced debugging effort, and allowed non-expert users to construct workflows with expert-level design patterns. These results indicate that end-to-end AI-assisted workflow generation and execution is feasible, and point toward AI-driven platforms for managing the scientific workflow lifecycle.
