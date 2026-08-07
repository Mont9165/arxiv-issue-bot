# CacheRAG: A Semantic Caching System for Retrieval-Augmented Generation in Knowledge Graph Question Answering

- arXiv ID: `2604.26176v1`
- Authors: Yushi Sun, Lei Chen
- Published: 2026-04-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.26176v1) | [pdf](https://arxiv.org/pdf/2604.26176v1)

## Abstract

The integration of Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) has significantly advanced Knowledge Graph Question Answering (KGQA). However, existing LLM-driven KGQA systems act as stateless planners, generating retrieval plans in isolation without exploiting historical query patterns: analogous to a database system that optimizes every query from scratch without a plan cache. This fundamental design flaw leads to schema hallucinations and limited retrieval coverage. We propose CacheRAG, a systematic cache-augmented architecture for LLM-based KGQA that transforms stateless planners into continual learners. Unlike traditional database plan caching (which optimizes for frequency), CacheRAG introduces three novel design principles tailored for LLM contexts: (1) Schema-agnostic user interface: A two-stage semantic parsing framework via Intermediate Semantic Representation (ISR) enables non-expert users to interact purely in natural language, while a Backend Adapter grounds the LLM with local schema context to compile executable physical queries safely. (2) Diversity-optimized cache retrieval: A two-layer hierarchical index (Domain $\rightarrow$ Aspect) coupled with Maximal Marginal Relevance (MMR) maximizes structural variety in cached examples, effectively mitigating reasoning homogeneity. (3) Bounded heuristic expansion: Deterministic depth and breadth subgraph operators with strict complexity guarantees significantly enhance retrieval recall without risking unbounded API execution. Extensive experiments on multiple benchmarks demonstrate that CacheRAG significantly outperforms state-of-the-art baselines (e.g., +13.2% accuracy and +17.5% truthfulness on the CRAG dataset).
