# AutoSQL: Extracting SQL Templates from Imperative ORM Code in Large-Scale Repositories

- arXiv ID: `2608.15595v1`
- Authors: Junsong Pu, Yichen Li, Zhuangbin Chen, Zhihan Jiang, Zibin Zheng
- Published: 2026-08-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.15595v1) | [pdf](https://arxiv.org/pdf/2608.15595v1)

## Abstract

Suboptimal SQL queries can significantly degrade the performance of cloud systems, motivating the extraction and auditing of SQL statements before deployment. However, Go ORM frameworks construct SQL imperatively through scattered method-call sequences, making it difficult to statically recover the resulting SQL templates. We present AutoSQL, a system that reconstructs SQL templates from Go ORM code. AutoSQL constructs a Code Index, a directed graph that captures structural dependencies between functions, types, and global variables as navigable edges. It then traces upstream call chains from ORM invocation sites to identify database-interacting functions as entry points. For each entry point, an LLM agent traverses the Code Index to collect code slices that influence SQL generation, switching to pattern-based search when the graph cannot resolve a retrieval goal. We call this strategy Hybrid Context Retrieval. Once sufficient context is collected, the agent synthesizes SQL templates. Evaluation on a benchmark of 579 test-covered entry points and 1,186 runtime-traced SQL statements from five large-scale Go repositories shows that AutoSQL achieves 68.04% to 72.18% recall, exceeding the static reachability baseline by 11.80% to 15.94% and outperforming existing methods by 8.52% to 21.50%.
