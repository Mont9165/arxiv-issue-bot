# Grid-Orch: An LLM-Powered Orchestrator for Distribution Grid Simulation and Analytics

- arXiv ID: `2605.12728v1`
- Authors: Boming Liu, Jin Dong, Jamie Lian
- Published: 2026-05-12
- Primary category: `eess.SY`
- Categories: `eess.SY`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.12728v1) | [pdf](https://arxiv.org/pdf/2605.12728v1)

## Abstract

The power distribution engineering workforce faces a projected shortage of up to 1.5 million engineers by 2030, creating urgent demand for more accessible analysis tools. This paper introduces Grid-Orch, a framework that bridges Large Language Models (LLMs) and power system simulation through the Model Context Protocol (MCP), enabling engineers to perform complex distribution analyses via natural language. Using OpenDSS as the reference implementation, Grid-Orch provides 36 domain-specific tools across eleven categories, covering power flow, voltage analysis, quasi-static time series (QSTS) simulation, and automated optimization. A provider-agnostic LLM layer supports both cloud-hosted (Gemini, Claude) and locally deployed (Ollama, llama-cpp) models, enabling air-gapped operation for security-sensitive utility environments. Three optimization skills, capacitor placement, voltage violation analysis, and overvoltage mitigation, extend the platform beyond single-tool queries to multi-step engineering workflows. Grid-Orch is delivered as an interactive web platform with chat-based interaction, a QSTS dashboard, and feeder topology visualization, and renders simulation results inline. Workflow demonstrations show that distribution analyses formerly requiring hours of scripting, such as distributed energy resource (DER) interconnection screening, complete in under two minutes through natural language, producing numerically identical results to direct OpenDSS scripting.
