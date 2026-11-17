# CapCover Filter: Semantic Approximate Membership Queries over Embeddings

- arXiv ID: `2611.20132v1`
- Authors: Dvir David Biton, Shay Hahiashvili, Nadav Keren, Gil Einziger, Roy Friedman
- Published: 2026-11-15
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.20132v1) | [pdf](https://arxiv.org/pdf/2611.20132v1)

## Abstract

Determining whether an embedding is sufficiently similar to any vector in a vector store without performing a nearest-neighbor search can substantially improve query throughput in vector-store systems. We study Semantic Approximate Membership Queries (SAMQs), which allow queries to be rejected when no indexed vector meets the requested similarity threshold, while guaranteeing no false negatives.
  We introduce CapCover Filter, a geometric data structure that summarizes a set of embeddings using spherical caps. Its representation is independent of the query threshold, allowing a single filter to support arbitrary thresholds without reconstruction. We evaluate alternative construction and quantization methods, compare CapCover Filter with competing filters, and measure its impact on query throughput.
  Across five real-world datasets, at a cosine similarity threshold of 0.95, CapCover Filter eliminates approximately 20--100\% of index accesses while using only 2\% of the raw (FP32) embedding memory. When placed before a FAISS flat index, it improves query throughput by up to 382\% and by approximately 116\% on average across the five datasets, while returning the same range-search result. We also evaluate lower similarity thresholds. Our results show that CapCover Filter can substantially improve vector-store throughput when similarity thresholds are tight, retrieval is expensive, and indexed embeddings are highly clustered. We release an optimized implementation of CapCover Filter and its evaluation framework.
