# Directory-Aware Query and Maintenance in Vector Databases

- arXiv ID: `2606.16903v1`
- Authors: Mengzhao Wang, Zheng Gong, Jingpei Hu, Jiajie Fu, Maojia Sheng, Junwen Chen, Yifan Zhu
- Published: 2026-06-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.16903v1) | [pdf](https://arxiv.org/pdf/2606.16903v1)

## Abstract

Vector databases typically manage metadata as flat scalar attributes, which limits their ability to express hierarchical directory semantics commonly used to organize code repositories, enterprise documents, and agent memories. As a result, directory-scoped retrieval and structural updates are often implemented as application-layer workarounds, making recursive scope resolution expensive and directory maintenance difficult to keep consistent. This paper studies native directory semantics as a first-class capability for vector databases. We formalize two core operators: Directory-Semantic Query (DSQ) for hierarchically scoped retrieval, and Directory-Semantic Maintenance (DSM) for structural updates. We then evaluate three implementation strategies: query-time path expansion (PE-Online), ingestion-time path expansion (PE-Offline), and a Trie-based Hierarchical Index (TrieHI). Our analysis exposes the fundamental limitations of expansion-based designs: flattening the hierarchy incurs high recursive-query latency in PE-Online and unscalable write amplification during structural changes in both expansion strategies. In contrast, TrieHI keeps the directory topology as a native prefix tree, enabling efficient recursive retrieval through tree traversal and reducing maintenance cost through topological node manipulation. We benchmark these design points within ByteDance's Viking vector search engine and release two large-scale datasets, WIKI-Dir and ARXIV-Dir, to support future research on directory-semantic vector search. Finally, TrieHI has been integrated into OpenViking, an open-source context database for AI agents, where it supports filesystem-style context organization and directory-recursive retrieval.
