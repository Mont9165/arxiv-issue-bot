# Retrieval-Oriented Code Representations in Agentic Bug Localization

- arXiv ID: `2607.11046v1`
- Authors: Genevieve Caumartin,  Tse-Hsun,  Chen, Diego Elias Costa
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.11046v1) | [pdf](https://arxiv.org/pdf/2607.11046v1)

## Abstract

LLM-based agents are increasingly being used to support software development, yet their performance in repository-level tasks depends on retrieving the right code context. Existing studies have explored file-level localization using traditional information retrieval over file paths and raw source code. However, the role of textual code representations in retrieval and localization remains underexplored.
  We study file-level bug localization as a representation-driven retrieval problem. Across the Long Code Arena (LCA) and SWE-bench Verified (SWE) datasets, we compare five code representations: file paths, raw source code, and three LLM-generated textual representations. Our experiments include lexical, semantic, and LLM-based retrieval, followed by LLM-based post-retrieval ranking. We quantify the cost incurred by a representation through the representation footprint. We find that the choice of code representation affects both localization effectiveness and cost. Role-aware summaries outperform file-path representations by up to 40% Hit@5 while requiring a representation footprint 10.4 to 20.9x smaller than raw source code. Combining complementary representation results and ranking retrieved candidates with an LLM provides further gains of up to 31.9% and 42.0%, respectively. Overall, role-aware summaries provide the best cost-effectiveness trade-off, while raw source code offers effectiveness in some settings at a significantly higher cost. A case study with Agentless reveals the utility of our techniques within a well-known pipeline, reaching 94% Hit@6 on file localization (+4.7% against the baseline). Our findings suggest that code representation should be treated as a first-class design choice in agentic localization pipelines, guided by pipeline stage and cost-accuracy requirements.
