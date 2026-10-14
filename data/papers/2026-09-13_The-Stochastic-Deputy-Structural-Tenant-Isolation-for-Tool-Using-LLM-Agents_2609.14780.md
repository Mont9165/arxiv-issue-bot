# The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents

- arXiv ID: `2609.14780v1`
- Authors: Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Asher Ali, Muhammad Hamzah Siddiqui
- Published: 2026-09-13
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.14780v1) | [pdf](https://arxiv.org/pdf/2609.14780v1)

## Abstract

Multi-tenant tools commonly accept a tenant identifier and validate it against the caller's entitlement. For a large language model (LLM) agent, that pattern delegates resource selection to a process whose context may contain attacker controlled instructions. We formalize this stochastic deputy problem and present a structural defense: remove tenant identity from the Model Context Protocol (MCP) tool schema, bind scope to a verified credential, and enforce it below the agent. In a 373-trial ablation across eight model configurations and two transports, a correctly validated tenant parameter served every out-of-scope attempt: 26 of 26, or 26 of 41 plausible-pretext trials overall. With the parameter removed, no tool signature could express the read. Twelve of 56 trials instead escaped the interface by forging writable scope, showing that interface invariance requires cryptographically protected context. On a production dataset containing multiple GBs of data, set-valued scope caused a measured $57\times$ latency ratio under function-wrapped membership predicates; a JSON_TABLE lateral join recovered index access where the tenant key was indexed. The evaluation also exposes deployment limits, including an entitlement-size query-planner cliff and incomplete index coverage. The result is a tenant-isolation argument that depends on enforceable interfaces and credentials rather than model compliance.
