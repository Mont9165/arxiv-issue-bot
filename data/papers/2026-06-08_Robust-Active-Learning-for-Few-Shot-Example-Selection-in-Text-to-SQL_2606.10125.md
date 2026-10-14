# Robust Active Learning for Few-Shot Example Selection in Text-to-SQL

- arXiv ID: `2606.10125v1`
- Authors: Arash Pourhabib
- Published: 2026-06-08
- Primary category: `stat.ML`
- Categories: `stat.ML`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.10125v1) | [pdf](https://arxiv.org/pdf/2606.10125v1)

## Abstract

Few-shot example retrieval is the dominant paradigm for grounding large language models (LLMs) in domain-specific text-to-SQL systems. However, the quality of the annotated example bank directly governs system accuracy, and expert annotation is prohibitively expensive. We formalize the active selection of these examples as a constrained experimental design problem over the intrinsic, low-dimensional manifold of semantic query embeddings. Unlike standard active learning frameworks, our setting introduces three critical challenges: varying, query-dependent annotation reliability (heteroscedasticity), strict requirements for spatial diversity across semantic topics (partition matroid constraints), and the inherent reality that the true covariance structure of the embedding space is unknown (misspecification). To address these, we propose a stratified greedy algorithm that maximizes a heteroscedastic mutual information objective. We prove that this objective remains submodular and approximately monotonic on the intrinsic manifold, yielding a theoretical constant-factor approximation guarantee. We establish a spectral bound demonstrating that this approximation guarantee degrades gracefully, rather than catastrophically, when the assumed surrogate kernel diverges from the true underlying data-generating process. Empirical results demonstrate that the proposed strategy significantly reduces labeling effort while maintaining high text-to-SQL retrieval accuracy.
