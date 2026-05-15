# Not All RAGs Are Created Equal: A Component-Wise Empirical Study for Software Engineering Tasks

- arXiv ID: `2605.14503v1`
- Authors: Qiang Ke, Yanjie Zhao, Hongjin Leng, Shengming Zhao, Haoyu Wang
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.14503v1) | [pdf](https://arxiv.org/pdf/2605.14503v1)

## Abstract

While Retrieval-Augmented Generation (RAG) is increasingly adopted to ground Large Language Models (LLMs) in software artifacts, the optimal configuration of its components remains an open question for software engineering (SE) tasks. The lack of systematic guidance forces practitioners into costly, ad-hoc experimentation. This paper presents a comprehensive, component-wise empirical study that dissects the RAG pipeline, evaluating over 21 distinct models and methods. Our study systematically isolates and evaluates 4 query processing techniques, 7 retrieval models spanning sparse, dense, and hybrid paradigms, 4 context refinement methods, and 6 distinct generators. We test these components on a suite of 3 core SE tasks: code generation, summarization, and repair. Our empirical findings reveal a crucial insight: the retriever-side components, particularly the choice of the retrieval algorithm, often exert a more significant influence on final system performance than the selection of the generator model. Strikingly, the classic lexical retriever BM25 demonstrates exceptionally robust performance across diverse tasks. Our analysis provides a practical, data-driven roadmap for researchers and practitioners, offering clear guidance on prioritizing optimization efforts when constructing effective RAG systems for software engineering contexts.
