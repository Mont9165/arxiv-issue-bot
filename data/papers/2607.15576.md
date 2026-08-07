# Efficient and Effective In-place Graph-based Vector Index Updates

- arXiv ID: `2607.15576v1`
- Authors: Haotian Liu, Yujun He, Bo Tang
- Published: 2026-07-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2607.15576v1) | [pdf](https://arxiv.org/pdf/2607.15576v1)

## Abstract

In the era of Large Language Models (LLMs), efficient vector updates are critical for capturing real-time information from rapidly evolving data. However, it is not trivial to process frequent vector insert and delete updates and maintain a high recall of the search results simultaneously. Specifically, the cluster-based vector indexing methods have high update throughput but low search result quality. Existing out-of-place graph-based vector indexing update approaches suffer from poor update throughput due to the need to periodically merge update batches into the underlying graph index.
  Building a vector data system that supports efficient and effective in-place updates is inherently challenging. In this work, we propose Yi to achieve it. In particular, Yi supports in-place graph-based vector indexing updates with consistently high update throughput and good search result quality. The key idea of Yi is decomposition facilitates consolidation. In particular, we introduce a vector-level update mechanism and architect Yi with three core components: (i) a tasklet-based execution engine, (ii) an asynchronous buffer manager, and (iii) a vector file system. Experimental results demonstrate that Yi achieves 1.75x higher update throughput and 1.8x higher concurrent search throughput than the state-of-the-art systems on the 800M dataset, while using only 73% of the peak memory and fewer CPU cores.
