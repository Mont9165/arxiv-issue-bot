# From Natural Language Requirements to Graphical User Interfaces: Automated Prototyping and Verification with Pretrained Language Models

- arXiv ID: `2608.24749v1`
- Authors: Kristian Kolthoff
- Published: 2026-08-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24749v1) | [pdf](https://arxiv.org/pdf/2608.24749v1)

## Abstract

Requirements elicitation is essential for developing interactive software systems, as it helps ensure that the resulting product meets stakeholder needs. Since elicitation typically relies on natural language (NL), misunderstandings can arise from its inherent ambiguity. Formal specifications can reduce ambiguity but require technical expertise. GUI prototyping therefore provides a valuable alternative by turning requirements into tangible visual artifacts that support communication, elicitation, and validation. However, creating high-fidelity prototypes remains time-consuming and costly. Similarly, requirements verification, which ensures that implementations conform to specified requirements, is still largely manual, while existing automated approaches are often limited to static, rule-based techniques. This work addresses two challenges: (C1) reducing the effort required to transform NL requirements into GUI prototypes, and (C2) reducing the effort required for requirements verification in GUI applications and prototypes. For C1, we introduce novel NL-based GUI retrieval and reranking methods, new benchmarks, and techniques for efficiently adapting LLMs to GUI generation, including proprietary GUI representations. Their effectiveness is demonstrated on a large benchmark with human annotations. For C2, we propose LLM-based methods for verifying semantically complex NL requirements on static GUI prototypes and introduce a multimodal LLM-based agent for verifying complex functional and non-functional requirements in dynamic GUI applications through automatically generated and evaluated interaction trajectories. Overall, the proposed methods substantially reduce manual effort in GUI prototyping and requirements verification.
