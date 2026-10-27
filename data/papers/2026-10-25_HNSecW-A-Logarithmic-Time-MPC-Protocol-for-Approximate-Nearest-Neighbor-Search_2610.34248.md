# HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search

- arXiv ID: `2610.34248v1`
- Authors: Fahong Zhang, Weijie Jin, Lixu Wang, Ning Luo, Xiao Wang, Wei Dong
- Published: 2026-10-25
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.34248v1) | [pdf](https://arxiv.org/pdf/2610.34248v1)

## Abstract

As a core component of modern RAG systems, approximate nearest neighbor (ANN) search has been extensively studied for decades. In practice, deploying ANN often requires symmetric privacy, where the querier's query and the database owner's data must remain hidden from each other, necessitating a secure multi-party computation (MPC) solution. So far, most MPC-based ANN protocols follow a cluster-based approach: they evaluate distances for the query over a large candidate set and rely on heavyweight primitives such as distributed ORAM to hide access patterns. As a result, each search typically requires $O(\sqrt{N})$ time. We propose HNSecW, a novel MPC protocol for ANN search that achieves the $O(\log N)$ search time for the first time. We first study the single-query setting. Starting from HNSW, the state-of-the-art ANN algorithm, we redesign its control flow and data structures to achieve fully data-independent execution. To further achieve logarithmic search time, we employ offline reshuffling and partial database duplication. Furthermore, we extend our protocol to support multiple sequential queries by introducing a "double visited" caching structure that eliminates redundant cross-query memory accesses, thereby avoiding per-query online shuffling. In addition, we develop a batch-query protocol that exploits higher parallelism to reduce both round complexity and the circuit's critical path. Our experiments show that HNSecW preserves the high accuracy of plaintext HNSW ($\geq 90\%$ recall) and delivers over a $20\times$ efficiency improvement over prior work on million-scale datasets.
