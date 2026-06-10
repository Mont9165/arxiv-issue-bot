# RECON: An LLM-Enhanced Backward Constraint Analysis Framework

- arXiv ID: `2606.10264v1`
- Authors: Babangida Bappah, Lamine Noureddine, Umar Farooq, Aisha Ali-Gombe
- Published: 2026-06-09
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10264v1) | [pdf](https://arxiv.org/pdf/2606.10264v1)

## Abstract

While traditional techniques, such as symbolic execution, provide a principled foundation for precise constraint reasoning in program analysis, they struggle to scale to modern software systems mainly due to path explosion, the need for function modeling, and the loss of semantic intent at low-level program representations. In complex execution environments such as Android, characterized by extensive framework interactions and event-driven behavior, these limitations are even more amplified. Thus, in this paper, we present a novel large language model (LLM)-enhanced backward constraint analysis framework that combines the precision of static program analysis with LLM's semantic understanding to extract precise execution constraints from Android bytecode. Our approach, titled RECON, performs backward path discovery from target method(s) to the application entry point(s), discovers method-level control-flow constraints, and leverages LLM reasoning to transform bytecode conditions into interpretable specifications. We evaluated RECON using five LLMs across 78 Android constraint-extraction scenarios and compared it with traditional symbolic execution on real-world applications. Results demonstrate that our approach operates 5.8X faster than traditional symbolic execution, with a 100% success rate, while maintaining logical equivalence and providing significantly more precise and interpretable output. We further evaluated RECON for malware analysis on 100 samples. The results indicate an 84% success rate in generating semantic constraints that lead to the execution of dangerous API behaviors and in detecting complex constraints across multiple execution paths.
