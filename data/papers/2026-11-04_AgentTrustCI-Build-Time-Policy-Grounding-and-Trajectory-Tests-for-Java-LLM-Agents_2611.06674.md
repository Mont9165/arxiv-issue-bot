# AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents

- arXiv ID: `2611.06674v1`
- Authors: Sachin Gupta
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.06674v1) | [pdf](https://arxiv.org/pdf/2611.06674v1)

## Abstract

Infrastructure security does not establish whether an LLM agent selected an allowed tool, grounded its answer in tool output, or followed a required workflow. AgentTrustCI is a Java/JUnit 5 framework that expresses these application-layer expectations as policy, grounding, and trajectory checks over recorded traces. A deterministic replay implementation supports repeatable build-time tests; a judge interface provides an extension point for optional semantic evaluation. On 55 synthetic cases spanning seven enterprise domains, the full pipeline correctly classifies all 30 injected faults and 25 passing controls, including ten non-trivial controls, and misses none of 12 designated critical cases. Each single-layer configuration correctly classifies 35 cases because the corpus deliberately isolates ten faults per layer. A grounded answer obtained through a disallowed sequence illustrates the additional coverage of trajectory checks. Repeated measurements quantify validator execution separately from process startup and reporting. These results establish coverage of the authored regression suite, not production accuracy. We describe a production-trace validation protocol, optional LLM-judge integration, and maintenance of expectations as workflows evolve. The contribution is a practical pattern for expressing behavioral contracts within an existing Java release pipeline.
