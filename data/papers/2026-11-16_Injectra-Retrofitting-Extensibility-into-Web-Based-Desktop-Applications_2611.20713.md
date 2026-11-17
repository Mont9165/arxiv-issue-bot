# Injectra: Retrofitting Extensibility into Web-Based Desktop Applications

- arXiv ID: `2611.20713v1`
- Authors: Qin Sun
- Published: 2026-11-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2611.20713v1) | [pdf](https://arxiv.org/pdf/2611.20713v1)

## Abstract

Large language models can generate code based on natural language prompts, opening up new possibilities for users to customize software and extend its functionality. This paper proposes and implements Injectra, a general-purpose code injection and feature enhancement system for existing desktop clients, suitable for applications whose user interfaces are built using embedded browser engines (such as Electron) or system WebViews (such as Tauri). Injectra decouples the host integration logic from the upper-layer enhancement code. Combining both runtime integration and pre-launch bootstrap mechanisms, it injects JavaScript, HTML, and CSS into the application's internal Web runtime environment through a unified execution channel, thereby enabling modifications to interface rendering, adjustments to interactive behaviors, and client-side functionality extensions. The system uses a command-line interface (CLI) as a unified entry point, allowing external tools, AI agents, and MCP integration layers to reuse its injection and enhancement capabilities. We tested 38 desktop applications already installed on our macOS machine; code injection was successfully completed for all of them. We demonstrated the system's capability to extend functionality through various enhanced use cases and also successfully validated the Windows version. Based on Injectra, we further developed an LLM-powered enhancement tool driven by selection and annotation: users select interface objects within the original application and describe their modification requirements; the large language model then generates the enhancement code, which is injected, executed, and rendered by Injectra. The system's source code has now been released as open source: https://github.com/sqmw/injectra.
