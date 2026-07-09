# Mitigating Taint-Style Vulnerabilities in MCP Servers via Security-Aware Tool Descriptions

- arXiv ID: `2607.07461v1`
- Authors: Yang Shi, Jiaheng Fu, Yihe Huang, Ruixiang Wu, Chengyao Sun, Kaifeng Huang
- Published: 2026-07-08
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.07461v1) | [pdf](https://arxiv.org/pdf/2607.07461v1)

## Abstract

Large language models (LLMs) are increasingly deployed as autonomous agents that interact with external tools and services via the Model Context Protocol (MCP), a standardized interface for dynamic tool invocation. While MCP simplifies integration, it also expands the attack surface and enables generic exploits across multiple servers. Despite prior work on malicious MCP servers, the vulnerability landscape of MCP servers remains underexplored. In this work, we systematically analyze MCP server vulnerabilities, focusing on metadata characteristics, vulnerable code patterns, and community responses. Our study reveals that taint-style vulnerabilities constitute a substantial fraction of MCP server vulnerabilities, require significant code modifications to remediate, and are met with slow community responses. Motivated by these findings, we propose SPELLSMITH, presenting a novel textbased avenue for shielding taint-style vulnerabilities in MCP servers. In particular, SPELLSMITH analyzes the high-risk capabilities exposed by an MCP server and combines them with tool descriptions and parameter semantics to identify potential taint-style vulnerability risks, thereby constructing a tool-level risk profile. Then, SPELLSMITH leverages the Description property of the protocol to embed behavioral guidance (Description Enhancement Module) and exploits LLMs' self-reflection capabilities (Self-Reflection Module) to iteratively evaluate and refine outputs. By strengthening LLM internal decision-making, SPELLSMITH provides an active and unified mitigation strategy that generalizes across multiple vulnerabilities, reducing reliance on context-specific code-level fixes. Our experiments demonstrate that SPELLSMITH effectively mitigates taint-style vulnerability exploitation in MCP servers, highlighting its practical applicability and advantages over traditional code-level mitigations.
