# Pragmos: A Process Agentic Modeling System

- arXiv ID: `2604.27311v1`
- Authors: Pedro-Aarón Hernández-Ávalos, Luciano García-Bañuelos
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.27311v1) | [pdf](https://arxiv.org/pdf/2604.27311v1)

## Abstract

The advent of Large Language Models (LLMs) has significantly transformed tasks across Software Engineering. In the context of Business Process Management, LLMs are now being explored as tools to derive process models directly from textual descriptions. Existing approaches range from chatbot-driven systems that assist with iterative, text-based modeling to fully automated end-to-end modeling assistants. However, we argue that process modeling is inherently complex and cannot be effectively addressed through black-box solutions. Instead, we envision modeling as an open-ended conversational activity, best supported by an interactive, iterative process involving both humans and LLM. In our approach, the modeling task is decomposed into smaller, manageable steps. Each step results in intermediate artifacts and explicitly documents the rationale behind each modeling decision. During this process, we incrementally uncover simple behavioral relations that guide the construction of the model. Given the current limitations of LLMs in reasoning about complex dependencies, we complement them with specialized tools developed in the field to structure process models based on behavioral relations. This hybrid approach enables the generation of sound, yet comprehensible models that evolve through transparent and explainable steps. In this paper, we present our research agenda and introduce Pragmos, a prototype system that operationalizes this vision. Pragmos demonstrates how LLMs can collaborate with human users as both domain and modeling experts to co-create evolving process models through a structured and explainable workflow.
