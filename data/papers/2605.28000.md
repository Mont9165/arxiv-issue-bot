# Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution

- arXiv ID: `2605.28000v1`
- Authors: Swanand Rao
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.28000v1) | [pdf](https://arxiv.org/pdf/2605.28000v1)

## Abstract

Large language model agents are increasingly expected to perform operational work: calling APIs, manipulating files, assembling workflows, and acting inside enterprise systems. Yet the tool layer on which this execution depends is still commonly treated as either a hand-written integration artifact or a static list of schemas exposed to a model. This paper introduces Tool Forge, a validation-carrying toolchain for converting natural-language capability intent into governed, sandbox-verified, cataloged tool artifacts and exposing those artifacts to agents through a token-efficient routing layer.
  Tool Forge treats a tool as a capsule containing intent, capability contract, implementation, dependency policy, tests, documentation, runtime validation evidence, lifecycle state, credential bindings, and routing metadata. It also introduces a Router that exposes intent-scoped tool sessions instead of loading full catalog schemas into the model context. We describe the system architecture, validation pipeline, MCP-facing routing model, governance controls, and initial reproducible benchmarks from the open-source implementation.
  Across 83 Router benchmark cases, Tool Forge Router achieves aggregate micro-F1 of 0.901 while reducing estimated task-flow tool context by 99.2% relative to naive full-catalog schema exposure. In a 25-case end-to-end generation probe over local-tool tasks, Tool Forge generates 25 of 25 tool bundles, reaches micro-F1 of 0.940 against deterministic acceptance checks, and passes 23 of 25 live sandbox validations. These results are presented as an initial systems benchmark, not as a state-of-the-art claim. The paper identifies remaining challenges in adversarial routing, broader API grounding, sandbox isolation, and cross-system evaluation.
