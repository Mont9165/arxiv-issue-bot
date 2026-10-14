# When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary

- arXiv ID: `2609.15397v1`
- Authors: Artem Trofimov, Boris Novikov
- Published: 2026-09-14
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.DC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.15397v1) | [pdf](https://arxiv.org/pdf/2609.15397v1)

## Abstract

AI agents increasingly execute long-running workflows that externalize effects through independently supplied tools. Under retries, speculative execution, concurrency, and partial failures, the resulting external state may be inconsistent with the workflow's intended resolution: required effects may be missing or duplicated, aborted effects may survive, and committed effects may depend on provisional state that is later withdrawn. Advanced transaction models address related failures, but assume that lower-level operations expose the semantics they depend on: whether an effect occurred, whether it can be compensated, staged, or safely reordered. Shared agent-tool interfaces usually do not.
  We contribute an effect-history model that separates events in the external world from the runtime's observations of them, and a catalog of eight recurring external-effect anomalies. From the catalog we derive the boundary capabilities required to exclude each anomaly in general, and four points where black-box tool invocation alone cannot provide a general guarantee. We then ask how much of this is expressible in a widely used shared tool interface, measuring the use of the standard annotation vocabulary across 98,291 tools exposed by registered Model Context Protocol (MCP) servers. The fields are widely emitted but provide only coarse call-level hints, and none of the required capabilities is fully expressible. These results motivate reusable transactional contracts at the tool boundary.
