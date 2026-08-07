# SAGE: Selective Attention-Guided Extraction for Token-Efficient

- arXiv ID: `2604.15583v1`
- Authors: Xinzhi Wang, Peter Baile Chen, Gerardo Vitagliano, Matthew Russo, Jun Chen, Michael Cafarella, Samuel Madden, Chunwei Liu
- Published: 2026-04-16
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.15583v1) | [pdf](https://arxiv.org/pdf/2604.15583v1)

## Abstract

Large language models with long context windows can answer complex questions directly from full-length academic, technical, and policy documents, but passing entire documents is often costly, slow, and can degrade answer quality while increasing the risk of unnecessary data leakage. This paper targets the common setting of answering many heterogeneous questions over long document(s), where fixed position heuristics and standard retrieval-augmented generation (RAG) can fail due to document structure variability and weak query-chunk semantic similarity, which often requires task- and domain-specific tuning of embedding retrievers. We propose {Selective Attention-Guided Extraction} (\ourmethod), a training-free, plug-and-play context reduction framework that uses a lightweight local LLM to perform a single prefilling pass and convert language model attention signals into a query-specific relevance heatmap at configurable granularities. \ourmethod\ further introduces \emph{differential attention} strategies to better isolate question-relevant evidence, then selects the top-scoring units under a user-defined token budget and forwards only this reduced context to a downstream LLM for answer generation. \ourmethod\ surpasses traditional reduction techniques across multiple long-document QA benchmarks, notably securing a top-4 rank on QuALITY-hard while constrained to a 10\% context budget. This enables a 90\% reduction in tokens with competitive accuracy, without the need for model fine-tuning or complex calibration.
