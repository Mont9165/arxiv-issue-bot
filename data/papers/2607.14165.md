# Towards Reliable AI-Assisted Analog Design: Template-Constrained LLM Agents for SAR ADC Generation

- arXiv ID: `2607.14165v1`
- Authors: Dimple Vijay Kochar, Hae-Seung Lee, Anantha P. Chandrakasan
- Published: 2026-07-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.AR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.14165v1) | [pdf](https://arxiv.org/pdf/2607.14165v1)

## Abstract

While Large Language Models (LLMs) have demonstrated significant capability in software code generation, their application to analog Electronic Design Automation (EDA) is bottlenecked. Owing to limited circuit topology understanding and data, directly prompting LLMs and multimodal models leads to hallucinations and failure to produce schematics capable of passing rigorous SPICE simulations, as we show in our work. Instead, we propose an end-to-end, multi-step LLM agentic framework ATLAS, capable of generating a functional Successive Approximation Register (SAR) Analog-to-Digital Converter (ADC) that successfully passes simulation validation. To adhere to the rigid constraints of analog design, we utilize expert knowledge to ground the LLM in its planning, selection, parameterization, and iterative modification. As part of ATLAS, we introduce Template-Constrained Generation - which unlike other template-based works - builds towards a more generalized SAR ADC generation flow. We demonstrate a strong proof-of-concept of our framework by developing SAR ADCs across technology nodes and input specs. Overall, our expert-knowledge grounded multi-step agentic ATLAS establishes a pragmatic foundation for integrating LLMs into reliable analog design methodologies.
