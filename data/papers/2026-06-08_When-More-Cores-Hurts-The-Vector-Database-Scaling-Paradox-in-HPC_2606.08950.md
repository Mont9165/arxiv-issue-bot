# When More Cores Hurts: The Vector Database Scaling Paradox in HPC

- arXiv ID: `2606.08950v1`
- Authors: Seth Ockerman, Song Young Oh, Amal Gueroudji, Rochana Chaturvedi, Philip Carns, Nicholas Chia, Matthieu Dorier, Robert Latham, Tanwi Mallick, Swan Perarnau, Robert Underwood, Kyle Chard, Ian Foster, Robert Ross, Shivaram Venkataraman
- Published: 2026-06-08
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.08950v1) | [pdf](https://arxiv.org/pdf/2606.08950v1)

## Abstract

Vector databases have been designed and optimized for cloud environments; however, emerging scientific AI workloads (e.g., molecular search, meteorological trajectory detection, and literature-driven hypothesis generation) demand efficient, scalable execution on HPC systems. We present a large-scale evaluation of three state-of-the-art vector databases -- Qdrant, Milvus, and Weaviate -- on two production supercomputers, scaling to 256 distributed workers across 64 compute nodes. We evaluate representative workload patterns -- mixed read/write and write-then-read -- using popular benchmarks, multimodal embeddings, and a novel real-world scientific dataset. Our results reveal that workload characteristics can limit latency reduction, additional cores can reduce query throughput by up to 30.67%, and scaling from 16 to 256 workers (16x) only yields a 5.46x improvement. This scaling paradox exposes the fundamental mismatch between cloud-oriented designs and HPC systems, highlighting the need for new, HPC-aware vector database designs.
