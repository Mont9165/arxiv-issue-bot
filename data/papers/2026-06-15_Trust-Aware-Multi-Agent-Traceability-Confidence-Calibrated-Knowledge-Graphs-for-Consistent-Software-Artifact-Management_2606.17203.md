# Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management

- arXiv ID: `2606.17203v1`
- Authors: Mohamed Essam, Kareem Wael, Azza Hassan, Ahmed Haitham, Mahmoud Soliman, Samer Saber, Ibrahim Habib
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.17203v1) | [pdf](https://arxiv.org/pdf/2606.17203v1)

## Abstract

Multi-agent AI systems are increasingly used to automate software engineering tasks including requirements analysis, architecture design, test generation, and traceability linking. When these agents operate as a sequential pipeline over shared software artifacts, errors and low-confidence decisions made by upstream agents propagate to downstream stages, producing orphaned requirements, contradictory links, and compliance gaps that pose significant risks in safety-critical domains. We propose a trust-aware coordination framework where a shared knowledge graph serves as both centralized semantic memory and a coordination surface through which agents assess and build upon each other's contributions using calibrated confidence scores. Our approach introduces a two-stage traceability link prediction pipeline combining embedding-based retrieval with LLM-based multi-criteria analysis, a traceability seeding mechanism that enables comparison between derivation-time and validation-time confidence, and a consistency protocol governing pipeline interactions through confidence threshold gating, confidence divergence detection, and conflict resolution. We evaluate on an automotive software engineering case study measuring link prediction calibration, protocol effectiveness, threshold sensitivity, and the impact of traceability seeding. Ablation studies confirm that confidence calibration is essential for effective pipeline coordination.
