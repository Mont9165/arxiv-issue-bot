# A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models

- arXiv ID: `2608.14370v1`
- Authors: Md Kamrul Islam, Tiphaine Henry, Mattia Salnitri, Julius Köpke, Sami Souihi
- Published: 2026-08-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.14370v1) | [pdf](https://arxiv.org/pdf/2608.14370v1)

## Abstract

The modelling and analysis of secure business processes require the incorporation of security annotations into process models. Although BPMN extensions, including SecBPMN2, exist for this purpose, the derivation of accurate and complete security annotations from natural-language specifications remains a manual, expert-intensive, and error-prone task. This paper presents a hybrid framework that takes a BPMN process model and a security requirements document as input and automatically generates security annotations adhering to the SecBPMN2 specification. The approach combines Large Language Model (LLM)--based semantic extraction with schema-constrained mapping, rule-based normalization, and deterministic validation. The framework is evaluated comprehensively on a curated dataset of 27 process models from various domains. The results indicate that it consistently produces structurally valid SecBPMN2 annotations with high schema completeness. Compared to human security analysts, the system achieves substantially higher precision (0.58 vs. 0.29) while maintaining comparable recall (0.52 vs. 0.50) and reduces erroneous or misplaced annotations by nearly 50%. In addition, annotation generation is significantly faster than manual annotation. These findings demonstrate that hybrid LLM- and rule-based automation can reduce modeling effort while improving consistency and reliability, thereby providing a scalable foundation for security-by-design BPM.
