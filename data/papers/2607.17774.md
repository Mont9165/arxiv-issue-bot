# Persona-as-Configuration: Generative Stakeholder Reporting for Agricultural Floods

- arXiv ID: `2607.17774v1`
- Authors: Oliver Aleksander Larsen, Tiziano Santilli, Francesco Daghero, Mahyar T. Moghaddam
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2607.17774v1) | [pdf](https://arxiv.org/pdf/2607.17774v1)

## Abstract

Cyber-physical systems built on deterministic edge inference, such as on-vehicle flood detection for agricultural fields, produce structured decision logs that must be interpreted differently by heterogeneous stakeholders. Pairing such systems with large language models (LLMs) to generate stakeholder-specific reports introduces a tension: the generative layer is non-deterministic, while the edge plane must remain replayable and auditable. We propose an architectural pattern resting on two invariants: unidirectional consumption, in which the generative layer is a strict read-only consumer of the deterministic plane and never writes back, and persona-as-configuration, in which stakeholder adaptation is a versioned prompt-template artifact rather than runtime improvisation. We instantiate the pattern as a context-aware dashboard layer over the JSON decision logs of a previously published edge-based standing-water detection system, and analyse how the integration boundary admits standard generative-reliability mitigations as configuration- or middleware-level extension points. A structured expert review rated the pattern favourably across five ISO/IEC 25010-aligned quality dimensions, with strongest agreement on separation of concerns. End-user evaluation with agricultural stakeholders is planned for future work.
