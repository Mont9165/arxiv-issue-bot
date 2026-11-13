# Authenticated Approximate Nearest Neighbor Search in Outsourced Vector Databases

- arXiv ID: `2611.16516v1`
- Authors: Yuanhang Zhou, Xinyi Zhang, Cheng Xu, Jianliang Xu
- Published: 2026-11-12
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2611.16516v1) | [pdf](https://arxiv.org/pdf/2611.16516v1)

## Abstract

Approximate Nearest Neighbor (ANN) search has become a fundamental query primitive in modern vector databases for managing large-scale embedding data. To support growing vector collections, organizations increasingly outsource database management and query processing to third-party clouds. However, untrusted service providers may return suboptimal or fabricated results, posing a serious threat to ANN search integrity. Existing authenticated ANN approaches face substantial scalability challenges. They typically require transmitting high-dimensional vectors for distance verification and rely on topology-agnostic authentication structures, resulting in excessive communication and verification overhead. In this paper, we propose VIDA, a novel and efficient scheme for authenticated graph-based ANN search. VIDA replaces raw vector transmission with compact vector commitments and employs an aggregated Inner Product Argument to efficiently verify multiple distance computations. Furthermore, we introduce MeST, a topology-aware authenticated data structure that aligns authentication paths with graph traversal, significantly reducing structural proof overhead. Additionally, we design a quantization-aware authentication strategy that exploits distance bounds for pruning, reducing the number of exact distances requiring cryptographic authentication. Extensive experiments demonstrate that the proposed schemes substantially improve the efficiency of authenticated ANN search, achieving up to a $6.6\times$ speedup in end-to-end latency and reducing data transfer time by up to 99.2% compared with state-of-the-art methods.
