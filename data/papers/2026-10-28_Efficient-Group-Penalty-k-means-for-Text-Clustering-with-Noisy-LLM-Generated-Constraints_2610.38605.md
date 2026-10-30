# Efficient Group-Penalty k-means for Text Clustering with Noisy LLM-Generated Constraints

- arXiv ID: `2610.38605v1`
- Authors: Feiteng Nie, Yuan Sun, Shengkun Zhu, Sheng Wang, Zhiyong Peng
- Published: 2026-10-28
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.38605v1) | [pdf](https://arxiv.org/pdf/2610.38605v1)

## Abstract

k-means provides a simple and efficient foundation for text clustering, but embedding alone can miss task-specific semantic boundaries. Must-link (ML) and cannot-link (CL) constraints can correct such errors, yet conventional constrained clustering assumes that these relations are already supplied. LLMs can generate them without task-specific labels, but exhaustive querying is costly and their judgments can be incorrect. We present GPKmeans, an efficient Group-Penalty k-means method for text clustering with noisy LLM-generated constraints. GPKmeans uses LLM as an offline local pairwise annotator, querying selected anchor-candidate pairs for sparse ML links and constructing set-valued CL evidence without all-pairs queries. It converts connected components of the ML-link graph and the generated CL sets into groups with normalized, bounded soft penalties, limiting each group's influence independently of its size. Cached coordinate descent is proposed to efficiently solve the constraints clustering problem. We prove finite-step convergence and derive deterministic and probabilistic oracle-referenced bounds that relate objective distortion to the penalty coefficients and to the group-level error probabilities of the generated constraints. Across nine datasets, GPKmeans uses fewer LLM calls and yields more accurate constraints. It achieves the best average ACC, NMI, and ARI while running approximately 30 times faster than state-of-the-art constrained clustering methods.
