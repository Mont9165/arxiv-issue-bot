# Automated Semantic Fault Localization in SysML v2: A Human-in-the-Loop Framework Using Knowledge-Graph Augmented LLMs

- arXiv ID: `2606.23395v1`
- Authors: Haitham Al-Shami, Rohail Malik, Riku Ala-Laurinaho, Jari Vepsäläinen, Raine Viitala
- Published: 2026-06-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.23395v1) | [pdf](https://arxiv.org/pdf/2606.23395v1)

## Abstract

SysML v2's textual syntax enables compiler-based validation of model structure and language conformance. However, semantic mistakes that preserve syntactic validity but violate domain rules cannot be detected through compilers. These errors can propagate through the design process and surface late as costly integration failures. This paper presents a human-in-the-loop framework for identifying and repairing such errors automatically. It combines a fine-tuned Small Language Model (SLM) with a domain knowledge graph encoding physical compatibility rules between system elements. The knowledge graph also guides the generation of synthetic training data by systematically introducing plausible domain violations, and augments the model at inference time to ground repair suggestions in valid engineering constraints. We demonstrate the framework using the vehicle systems domain, where the knowledge graph captures the relationships between the mechanical, electrical, fluid, and signal interfaces. Two SLMs, Qwen2.5-Coder-1.5B and DeepSeek-Coder-6.7B, are fine-tuned to output unified diff patches that localize faults and present candidate repairs for engineer review, preserving human judgment in the design process. Evaluation of 1,184 test samples shows that fine-tuning improves semantic fault repair from less than 3% to more than 91%, with patch-based output reducing token length by over 60%. The framework offers a practical path toward AI-assisted model verification that complements existing MBSE tools.
