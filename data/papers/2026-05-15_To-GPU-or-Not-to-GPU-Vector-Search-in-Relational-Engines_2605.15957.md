# To GPU or Not to GPU: Vector Search in Relational Engines

- arXiv ID: `2605.15957v1`
- Authors: Vasilis Mageirakos, Joel André, Marko Kabić, Bowen Wu, Yannis Chronis, Gustavo Alonso
- Published: 2026-05-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.15957v1) | [pdf](https://arxiv.org/pdf/2605.15957v1)

## Abstract

Vector search (VS) is now available in most database engines. However, while vector search is a common feature in AI/ML/LLMs where the dominant computing platforms are GPUs, existing database engines operate on CPUs even when implementing vector search. This raises the question of whether integrating vector processing on GPUs as part of the engine would be a better design. In this paper, we explore this question in detail. First, we extend the TPC-H benchmark with vector data (from text and images) and propose a number of representative SQL+VS queries. Second, we develop a modular execution engine that can run SQL+VS queries across CPU and GPU. Third, we perform extensive experiments on a number of deployments: running the SQL+VS queries across CPU and/or GPU, with data residing in CPU or GPU memory, with existing indices and novel, optimized versions, as well as across different GPUs and interconnects (PCIe, NVLink). The results provide actionable and counter-intuitive insights on how to run such queries over CPUs and GPUs. For instance, the relational components benefit much more from running on the GPU than the vector search part. In addition, when the vector search involves moving data and indexes, using the GPU is not the best option, even with fast interconnects. Thus, we develop an alternative organization of vector index and embeddings that reduces the size of the index, making GPU-based vector search more competitive. With these improvements, the final result is that both the relational and vector search components are faster on the GPU, particularly on fast interconnects, in contrast with the architecture used in existing engines.
