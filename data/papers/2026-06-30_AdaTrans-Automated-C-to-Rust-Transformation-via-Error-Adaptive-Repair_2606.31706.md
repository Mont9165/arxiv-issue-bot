# AdaTrans: Automated C to Rust Transformation via Error-Adaptive Repair

- arXiv ID: `2606.31706v1`
- Authors: Xiaofan Liu, Zecan Li, Zhuang Zhao, Ziqi Shuai, Yanming Yang, Qi Xin, Jifeng Xuan
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.31706v1) | [pdf](https://arxiv.org/pdf/2606.31706v1)

## Abstract

The automated transformation of C code to Rust is challenging due to Rust's strict ownership and borrowing semantics. While Large Language Models (LLMs) show promise, they often produce code that violates these rules or relies on unsafe constructs. We propose AdaTrans, a framework that addresses these issues through three core mechanisms: a Strategy-Driven Retrieval-Augmented Generation (RAG) mechanism to map compiler errors to specific repairs, an Error-Stratified Transformation Strategy (ESTS) that adapts its behavior based on error types, and a multi-stage validation pipeline to ensure both compilability and functional equivalence. Evaluating on a dataset of 104 algorithmic problems, AdaTrans achieves a mean compilation pass rate of 95.51% and a mean solve rate of 81.09%, significantly outperforming existing tools while maintaining an unsafe file rate of only 1.19%.
