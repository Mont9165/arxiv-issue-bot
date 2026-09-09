# Factorized and Vectorized Execution: Optimizing Analytical and Semantic Queries over Relations

- arXiv ID: `2609.09002v1`
- Authors: Sunny Yasser, Anas Dorbani, Amine Mhedhbi
- Published: 2026-09-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.09002v1) | [pdf](https://arxiv.org/pdf/2609.09002v1)

## Abstract

Many-to-many joins are central to analytical and semantic workloads such as fraud detection, network analysis, and recommendation, where insights arise from relationships between entities. These workloads often suffer from an explosion of intermediate results, sometimes orders of magnitude larger than the inputs. Factorized representations address this problem by exploiting conditional independence among attributes to encode intermediates more compactly. In some cases, they can reduce the output size asymptotically below the worst-case output size. However, adopting factorization in modern vectorized query processors remains challenging: factorized representations are hierarchical, whereas vectorized execution is built around flat, block-oriented processing. Prior approaches either rely on full materialization or support only restricted factorization layouts, sacrificing much of the benefits of both factorization and vectorization.
  We present FFX, a novel engine for Fast Factorized eXecution. FFX is the first pipelined engine to support arbitrary factorization schemes while preserving full vectorization. The engine introduces packed factorized vectors and operators that maintain cache-friendly, contiguous layouts. Beyond analytics, FFX also co-optimizes semantic operators by serializing factorized intermediates into compact prompts for large language models (LLMs), substantially reducing token usage and inference cost while maintaining output quality and, in some cases, improving it. Together, these contributions enable efficient execution of join-heavy analytical queries, including queries augmented with semantic operators.
