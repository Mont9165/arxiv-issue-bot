# Cluster-Aware Dual-Level Test Specification Generation for Large-Scale Automotive Software Requirements

- arXiv ID: `2606.17197v1`
- Authors: Hazem Ayman, Menna Sedik, Kareem Mostafa, Mahmoud Soliman, Samer Saber, Ibrahim Habib
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.17197v1) | [pdf](https://arxiv.org/pdf/2606.17197v1)

## Abstract

Generating test specifications that satisfy Automotive SPICE SWE.6 requirements becomes increasingly challenging and time-consuming as projects scale to thousands of requirements. Because this manual process often consumes weeks of engineering effort, automation becomes a critical necessity. However, standard Large Language Model (LLM) approaches struggle at scale: processing requirements individually discards vital inter-requirement dependencies, while feeding entire corpora at once exceeds context-window limits, leading to incomplete integration coverage and redundant test cases. This paper presents a novel "Cluster-then-Summarize" pipeline that addresses these limitations through three-stages. Requirements are embedded using sentence transformers and grouped using UMAP dimensionality reduction followed by HDBSCAN density-based clustering. This grouping utilizes an automatic minimum cluster size selection driven by a quality criterion combining normalized Silhouette and Calinski-Harabasz scores. A multi-level map-reduce summarization algorithm then distills each cluster into concise, domain-conformant descriptions while preserving quantitative thresholds and safety integrity levels. The pipeline exploits the derived cluster topology to generate test specifications at two levels: individual requirement verification and cluster-level integration tests that verify cross-requirement feature behavior. A nearby-cluster context mechanism provides bounded cross-feature awareness during each LLM call, and Retrieval-Augmented Generation grounds all outputs in ISO 26262 and ASPICE standards. Evaluation on automotive requirement datasets of varying scale demonstrates that the cluster-aware approach improves integration test coverage and maintains summarization fidelity compared to baseline methods while scaling efficiently to thousands of requirements.
