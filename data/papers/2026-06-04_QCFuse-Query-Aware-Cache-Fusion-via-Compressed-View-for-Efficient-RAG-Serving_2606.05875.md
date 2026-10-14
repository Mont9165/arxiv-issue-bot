# QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving

- arXiv ID: `2606.05875v1`
- Authors: Jianxin Yan, Wangze Ni, Zhenxin Li, Jiabao Jin, Zhitao Shen, Haoyang Li, Jia Zhu, Peng Cheng, Xuemin Lin, Lei Chen, Kui Ren
- Published: 2026-06-04
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.05875v1) | [pdf](https://arxiv.org/pdf/2606.05875v1)

## Abstract

Retrieval-augmented generation (RAG) improves large language model (LLM) answer quality by grounding generation in external evidence, but processing retrieved contexts makes the prefill stage a dominant serving cost. RAG cache fusion reduces this cost by reusing precomputed key-value (KV) caches for retrieved chunks and selectively recomputing tokens under the current prompt. Existing selectors, however, face a dilemma between quality and efficiency: fast query-agnostic or final-layer query-to-context selectors can miss request-relevant evidence, whereas full-view query-aware selectors require broad context and layer visibility before recomputation and therefore stall the layer-wise cache-fusion pipeline. We present QCFuse, a compressed-view query-aware selector for RAG cache fusion. QCFuse uses chunk-anchor query probing to condition user-query states on compact per-chunk anchors and critical-layer profiling to identify recomputation tokens without all-layer inspection. We implement QCFuse in SGLang and evaluate it on four open-weight LLMs across six datasets. QCFuse reaches full-prefill-level quality. At matched quality, QCFuse achieves an average prefill-time speedup of 1.7x over full prefill and 1.5x over ProphetKV, the strongest quality-preserving baseline.
