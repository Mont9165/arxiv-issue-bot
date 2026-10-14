# Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models

- arXiv ID: `2606.04739v1`
- Authors: Sabrina Kaniewski, Fabian Schmidt, Tobias Heer
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.04739v1) | [pdf](https://arxiv.org/pdf/2606.04739v1)

## Abstract

Large language models (LLMs) have shown strong potential for automated software vulnerability detection, particularly in retrieval-augmented generation (RAG) settings. However, for approaches relying on proprietary models and APIs, reproducibility and replicability remain largely unexplored, raising the question of whether reported results generalize or depend primarily on specific model choices. In this work, we present a reproducibility study of Vul-RAG, a RAG-based framework for source code vulnerability detection that enhances LLMs with high-level vulnerability knowledge. We first replicate the results in a fully local and open-weights setting using the reported open-weight baseline models. We then extend the evaluation to a diverse set of recent open-weight LLMs, including code-specialized, general-purpose, and reasoning models of varying parameter sizes. The results confirm that the findings of Vul-RAG are reproducible under local deployment, but with minor deviations. Across all evaluated models, we observe a performance plateau at approximately 0.30 pairwise accuracy (code pairs for which both the vulnerable and the patched function are correctly classified). Notably, this plateau persists even for more recent and advanced models, indicating that improvements in model capacity alone do not substantially enhance performance. Finally, we discuss practical implications and trade-offs between detection effectiveness, model capabilities, and model scale. Implementation and evaluation artifacts are publicly available at https://github.com/hs-esslingen-it-security/revisiting-Vul-RAG.
