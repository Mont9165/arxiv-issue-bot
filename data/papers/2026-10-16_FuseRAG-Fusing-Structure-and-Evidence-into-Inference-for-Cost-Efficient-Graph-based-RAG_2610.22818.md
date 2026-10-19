# FuseRAG: Fusing Structure and Evidence into Inference for Cost-Efficient Graph-based RAG

- arXiv ID: `2610.22818v1`
- Authors: Tingqi Wang, Yingshu Li, Zhipeng Cai
- Published: 2026-10-16
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.22818v1) | [pdf](https://arxiv.org/pdf/2610.22818v1)

## Abstract

Graph-based retrieval-augmented generation (RAG) exploits relationships among evidence to support multi-hop question answering. However, conveying retrieved graphs through non-unique linear textual contexts to Large Language Models (LLMs) leads to graph-structure degradation and inefficient KV-cache reuse. Meanwhile, graph-structure order optimization is already NP-hard, and the additional KV-cache reuse objective further complicates the search by introducing potentially conflicting orders. To tackle these issues, we propose FuseRAG, a cost-efficient graph-based RAG framework that shifts most retrieved evidence from explicit textual contexts to latent representations. Our main idea is to separate reusable evidence content from query-aware structural interactions in latent space, while retaining only a few explicit facts as semantic anchors. The resulting latent representations are injected into decoder self-attention, where they reshape attention over evidence and thereby influence hidden states and next-token probabilities. This design preserves graph structure through latent interactions, enables evidence reuse beyond exact token-prefix matching. Experiments on three multi-hop question-answering datasets with Llama-3-8B and Qwen3.5-9B show that FuseRAG improves answer quality while achieving up to 2.7x and 2.2x TTFT speedups over the fastest graph-based baseline, respectively.
