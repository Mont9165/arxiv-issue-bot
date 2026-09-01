# Diachronic Hypergraphs for Orchestrated Multi-Agent Multimodal Memory Curation

- arXiv ID: `2608.29678v1`
- Authors: Yichao Feng, Ran Zhang, Haoran Luo, Zhenghong Lin, Carl Yang, Anh Tuan Luu
- Published: 2026-08-30
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.29678v1) | [pdf](https://arxiv.org/pdf/2608.29678v1)

## Abstract

Multi-agent systems solve tasks through collaboration, tool use, multimodal reasoning, and orchestration, but each agent operates within a knowledge boundary defined by its observations, context, and resources. Memory must preserve and transfer evidence, role specific context, decisions, procedures, and experience across interactions, not only outcomes. Vector and graph memories flatten these structures into embeddings or dyadic traces, obscuring events involving agents, tools, documents, errors, and evidence. This limits knowledge sharing, tracing, reuse, revision, and orchestration. We present MAGE, a hypergraph based multimodal database designed as a memory engine for MAS. MAGE stores agents, messages, tools, errors, procedures, documents, entities, decisions, and evidence in a heterogeneous temporal hypergraph, preserving high order collaborative events as reusable memory. It supports decision driven updates, role aware retrieval, validation, lifecycle management, and budget bounded context packing. By delivering knowledge to agents and orchestrators, MAGE expands their knowledge boundaries without modifying the models. Experiments show MAGE outperforms on various memory baselines.
