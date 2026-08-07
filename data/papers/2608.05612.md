# Keeping Models and Code in Sync: Roundtrip Engineering for Tactical Domain-Driven Design

- arXiv ID: `2608.05612v1`
- Authors: Weixing Zhang, Mario Herb, Wai Chung Dorothy Cheng, Michael Wagner, Bowen Jiang, Tianhai Liu, Anne Koziolek
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.05612v1) | [pdf](https://arxiv.org/pdf/2608.05612v1)

## Abstract

Domain-Driven Design gives teams a shared vocabulary for complex business logic, but that vocabulary only stays useful as long as the model and the code agree with each other. In practice, they drift apart: code changes outpace the model, or model revisions never make it into the codebase. This paper presents JDomInO, a bidirectional synchronization toolchain for tactical DDD that keeps a Java codebase and its domain model connected through a shared metamodel, with the goal of keeping the two in sync as the system evolves. JDomInO generates Java code structure deterministically from a domain model (forward path) and reconstructs a domain model from existing Java code (reverse path). The forward path has been fully validated on a Hotel Management scenario covering all 12 building block types in the metamodel; the reverse path's mapping logic has passed unit testing, with end-to-end validation underway. We also outline how the structured domain model produced by JDomInO could serve as a precision context layer for AI code assistants, helping them respect aggregate boundaries and DDD semantics that raw source code alone does not convey.
