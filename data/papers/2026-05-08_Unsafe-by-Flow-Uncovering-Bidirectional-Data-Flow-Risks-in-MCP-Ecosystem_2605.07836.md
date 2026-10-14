# Unsafe by Flow: Uncovering Bidirectional Data-Flow Risks in MCP Ecosystem

- arXiv ID: `2605.07836v1`
- Authors: Xinyi Hou, Yanjie Zhao, Haoyu Wang
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07836v1) | [pdf](https://arxiv.org/pdf/2605.07836v1)

## Abstract

Model Context Protocol (MCP) have quickly become the interface layer between LLM agents and external tools, yet they also introduce unsafe data flows that existing analyzers handle poorly. Vulnerabilities manifest in two directions: requester-controlled arguments may propagate to sensitive operations, while untrusted external or sensitive internal data may surface through MCP-visible outputs and subsequently influence host or model behavior. Accurate detection is complicated by the heterogeneous registration and dispatch patterns MCP servers employ, the need for MCP-specific taint semantics, and the fact that bugs often only materialize along complete tool-scoped execution paths. We present MCP-BiFlow, a bidirectional static analysis framework built around MCP-aware entrypoint recovery, protocol-specific taint modeling, and interprocedural propagation analysis. Against a benchmark of 32 confirmed MCP vulnerability cases, MCP-BiFlow identifies 30 (93.8% recall), substantially outperforming CodeQL, Semgrep, Snyk Code, and MCPScan. Across 15,452 real-world MCP server repositories, MCP-BiFlow surfaces 549 overlap-compressed candidate clusters; manual review confirms 118 vulnerability paths in 87 servers, establishing unsafe propagation as a recurring failure mode that resists detection without protocol-aware recovery of both request-side and return-side flows.
