# Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion

- arXiv ID: `2609.01187v1`
- Authors: Phong Trinh Duy, Trang Dang Yen, Hung Nguyen-Huu, Bach Le, Quyet-Thang Huynh, Dieu Hoang Vu, David Lo, Thanh Le-Cong
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.01187v1) | [pdf](https://arxiv.org/pdf/2609.01187v1)

## Abstract

A single vulnerability in a widely used library can cascade through millions of dependent applications, yet more than half of vulnerability database entries contain missing or incorrect affected-library information. Existing automated approaches neglect the relational structure of vulnerability databases, treating identification as an isolated text retrieval problem. In this paper, we propose Athena, the first graph-based approach for vulnerability affected library identification. Athena models vulnerability databases as a knowledge graph and reformulates the identification problem as knowledge graph completion (KGC). It comprises three key modules: a Modeling module that constructs a security knowledge graph integrating CVEs, libraries, CWE weakness types, CPE products, and software ecosystems; a Completion module that applies a modular KGC backbone to predict missing affected libraries for a given CVE via link prediction; and a Re-ranking module that retrieves KGC candidates and rescores them using a fine-tuned LLM augmented with knowledge graph embeddings, jointly leveraging structural and textual information. Our experiments on VulLib demonstrate that Athena significantly outperforms four state-of-the-art baselines, achieving a 32% improvement in Avg. F1 over the best baseline (i.e., VulLibGen). Notably, our KGC backbone with only 110M parameters already surpasses VulLibGen's best configuration at 7B parameters, demonstrating the effectiveness of graph-based modeling; the re-ranking module then provides substantial further gains, consistently outperforming the best baseline across all evaluated LLM backbones.
