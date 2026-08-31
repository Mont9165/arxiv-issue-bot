# From Architecture to Binary: Ensuring Cross-Domain Consistency in Model-Based Airborne Software Development

- arXiv ID: `2608.28156v1`
- Authors: Nils Schlautmann, Viktor Sinitsyn, Benjamin Engelhard, Florian Holzapfel
- Published: 2026-08-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.28156v1) | [pdf](https://arxiv.org/pdf/2608.28156v1)

## Abstract

This paper presents an airborne software development approach for manned and unmanned aerial vehicles aimed at reducing inconsistencies across system, model-based functional, and embedded software domains. In environments influenced by standards such as ARP-4754B and DO-178C, these inconsistencies typically stem from insufficient enforcement across domain boundaries rather than missing process definitions. Building on a previously proposed toolchain centered on a relational interface database, we identify recurring failure modes and propose a repository-centered implementation to address them, tailored to small, resource-constrained teams operating without heavyweight process overhead. Each domain is assigned a primary repository with cross-repository references and dedicated CI pipelines that generate, update, and validate the exchanged artifacts. Automated interface updates, differential change notifications, and consistency checks propagate changes with minimal manual effort and surface inconsistencies before the time-consuming code-generation and compilation steps. An initial implementation in an ongoing experimental project is described, with qualitative feedback from its early use.
