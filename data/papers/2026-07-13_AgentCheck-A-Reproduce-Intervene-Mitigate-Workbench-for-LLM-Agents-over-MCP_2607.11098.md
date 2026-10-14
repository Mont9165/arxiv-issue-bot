# AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP

- arXiv ID: `2607.11098v1`
- Authors: Aritra Mazumder, Nusrat jahan Lia
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.11098v1) | [pdf](https://arxiv.org/pdf/2607.11098v1)

## Abstract

Tool-using LLM agents are mostly evaluated assuming all tools work. When a tool times out, returns a week-stale value, or has its description poisoned in deployment, the developer needs a controlled way to reproduce the failure, test a fix, and confirm the fix worked before deployment. We present AgentCheck, an open-source web workbench that turns an MCP server into an intervention surface. AgentCheck runs an agent against its real tools and records every tool response, then re-runs the agent with the response perturbed by a fault (12 types) injector. Matching tool calls are replayed from cache, and later tool calls go live after the agent diverges. This yields a reproduce-intervene-confirm loop: the developer toggles a mitigation, re-runs against the identical fault, and sees if the failure goes away. Scoring has two parts: deterministic pass/fail rules, plus an LLM judge for interpretive labels, validated against human annotations. Across five agents, the best passes 105/120 scenarios and the weakest only 77. The failures are usually silent, confident use of incorrect tool outputs rather than crashes. On the weakest agent, a retry mitigation raises success on timeout error faults from as few as 30% of cases to 100%, whereas stale-data faults remain near 3-4 of 10 regardless of the mitigation. AgentCheck makes these failure modes reproducible, comparable, and verifiable before deployment.
