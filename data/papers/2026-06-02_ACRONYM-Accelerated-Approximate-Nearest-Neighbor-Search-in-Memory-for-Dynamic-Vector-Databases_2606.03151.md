# ACRONYM: Accelerated Approximate Nearest Neighbor Search in Memory for Dynamic Vector Databases

- arXiv ID: `2606.03151v1`
- Authors: Md Mizanur Rahaman Nayan, Tianqi Zhang, Flavio Ponzina, Tajana Rosing, Azad J Naeemi
- Published: 2026-06-02
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.DB`, `cs.ET`
- Links: [abs](http://arxiv.org/abs/2606.03151v1) | [pdf](https://arxiv.org/pdf/2606.03151v1)

## Abstract

Vector database search with frequent updates is increasingly critical in applications such as retrieval augmented generation, recommendation systems, and large-scale embedding retrieval. Existing solutions, such as graph-based and partition-based approximate nearest neighbor search (ANNS), suffer from frequent index rebuilding due to data distribution-dependent indexing that impacts continuous deployment and causes long rebuilding latency. This paper proposes an algorithm-hardware co-designed platform, ACRONYM, that addresses key problems with state of the art database search. Algorithmically, it leverages efficient encoding independent of data distribution and Hamming-distance based search for efficient hardware acceleration. Architecturally, we propose CAM-based in-memory parallel distance computation followed by time multiplexed approximated top-k selection to enable the exhaustive search. We propose two-stage search that includes coarse search followed by binary refinement to achieve high recall in CAM based search which is heavily limited to small vector dimension due to capacity and wordline parasitic. ACRONYM supports continuous update without stalling and integrates novel XOR-and-Accumulate (XAC) based systolic-array encoder for efficient on chip encoding during search. Across million-scale datasets, while serving dynamic database ACRONYM achieves >90% recall at a throughput of 8e6 queries per second, with a memory footprint of only 32MB and an average energy consumption of 2.56uJ per query, speedup over HNSW (CPU) of about 400x and FAISS-IVF (GPU) of about 80x.
