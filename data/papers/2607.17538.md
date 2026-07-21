# D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation

- arXiv ID: `2607.17538v1`
- Authors: Chang Eun Song, Sumukh Pinge, Tianqi Zhang, Sung Eun Kim, Tajana S. Rosing, Mingu Kang
- Published: 2026-07-20
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.CL`, `cs.DB`, `cs.ET`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2607.17538v1) | [pdf](https://arxiv.org/pdf/2607.17538v1)

## Abstract

Retrieval-Augmented Generation (RAG) enhances the factual grounding of large language model (LLM) inference by retrieving relevant information from external knowledge bases. However, its dense vector retrieval introduces significant latency and energy overhead, becoming the primary performance bottleneck. Although recent in-storage accelerators aim to reduce data movement, they still rely on host or embedded processors outside the memory, where nearly 70% of the total retrieval time is spent. As a result, they cannot fully overcome the bandwidth limitations, leading to yet another memory bottleneck. To tackle these limitations, we present D-NOVA, a hardware-software co-designed in-storage retrieval accelerator. D-NOVA executes an inverted file (IVF)-based hierarchical retrieval pipeline by deeply embedding the search functionality directly into the NAND memory array. This is achieved by incorporating a new distance metric, Dual-Bound Tight Similarity Sensing (DTS), which is specifically tailored for searching within the NAND string. In addition, we introduce a lightweight contrastive adapter that maps embedding vectors into a DTS-friendly domain, recovering near-software recall while improving performance and energy efficiency. D-NOVA is up to 41.7x faster and 71x more energy-efficient than a CPU baseline, and achieves 12.13x higher throughput while being up to 1.26x more energy-efficient than state-of-the-art in-storage RAG accelerators, demonstrating the potential of fully in-storage vector search for scalable RAG acceleration.
