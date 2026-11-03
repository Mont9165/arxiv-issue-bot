# Mixed-Type Relational Database Synthesis with Graph-Prompted Language Model

- arXiv ID: `2611.02373v1`
- Authors: Yuxiang Sun, Mengshi Chen, Jianwei Wang, Wenjie Zhang, Kai Wang
- Published: 2026-11-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.02373v1) | [pdf](https://arxiv.org/pdf/2611.02373v1)

## Abstract

Data access is often limited by privacy or proprietary restrictions, motivating relational database synthesis, which synthesizes realistic contents across related tables. Relational databases couple multi-table structure with mixed-type attributes and intricate semantic dependencies among values, making realistic synthesis challenging. In this paper, we propose REMIX, a unified framework for realistic relational database synthesis with mixed-type attributes. REMIX integrates a small language model (SLM) and a large language model (LLM) through two key phases: Graph-to-Prompt Tuning and Collaborative SLM-LLM Decoding. To capture attribute dependencies within and across tables, Graph-to-Prompt Tuning represents the database as an attributed heterogeneous graph. We project mixed-type record embeddings and aggregated relational context into soft prompts that serve as continuous vectors for an SLM. We jointly optimize the graph-to-prompt mapping and SLM through autoregressive attribute reconstruction. Furthermore, to reduce semantic inconsistencies, Collaborative SLM-LLM Decoding combines SLM-based record generation with repair programs induced by an LLM. The LLM discovers semantic dependencies, iteratively refines them through independent validation with a statistical bound on the overall probability of false acceptance, and translates validated dependencies into tested programs that repair generated values. Extensive experiments on seven real-world relational databases demonstrate the effectiveness of REMIX in generating high-fidelity data with improved semantic consistency and downstream utility.
