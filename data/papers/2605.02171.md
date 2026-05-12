# QuIVer: Rethinking ANN Graph Topology via Training-Free Binary Quantization

- arXiv ID: `2605.02171v2`
- Authors: Wenxuan Xiao, Zhiyou Wang, Chengcheng Li
- Published: 2026-05-04
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.02171v2) | [pdf](https://arxiv.org/pdf/2605.02171v2)

## Abstract

Approximate nearest neighbor (ANN) graph indices such as HNSW and Vamana construct graph topology in full-precision or high-fidelity quantized metric spaces, using binary quantization (BQ) only as a post-hoc search-time distance estimator. We ask whether BQ can build the graph itself.
  We present QuIVer (Quantized Index for Vector Retrieval), a training-free ANN graph index that performs edge selection, pruning, and graph navigation entirely in a 2-bit Sign-Magnitude BQ metric space. QuIVer combines: (i) a 2-bit encoding that preserves sign and magnitude strength at 1/12 the memory of float32 vectors; (ii) Vamana alpha-diversity pruning directly on BQ distances; and (iii) symmetric BQ beam search using XOR/AND/Popcount, followed by float32 reranking over a small candidate set.
  On six embedding datasets spanning 384--3072 dimensions, QuIVer achieves at least 88% Recall@10 at 13--41K multi-threaded QPS with 58--262-second construction and less than 1.3 GB hot memory. At matched recall on Cohere-1M, it outperforms the official DiskANN Rust implementation by 2.5--3.3x, hnswlib by 3.6--4.7x, and FAISS HNSW by 3.8--4.9x in multi-threaded throughput. Controlled experiments on additional datasets, including word vectors, CV features, uniform random vectors, multimodal CLIP embeddings, and low-rank synthetic data, delineate QuIVer's applicability boundary: high recall requires cosine-native distributions with low effective dimensionality, while monotonic recall gains with increasing ef suggest that BQ noise mainly affects navigation efficiency in the tested regimes.
