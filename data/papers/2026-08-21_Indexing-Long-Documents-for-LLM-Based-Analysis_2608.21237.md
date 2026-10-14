# Indexing Long Documents for LLM-Based Analysis

- arXiv ID: `2608.21237v1`
- Authors: Donna Pham
- Published: 2026-08-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.21237v1) | [pdf](https://arxiv.org/pdf/2608.21237v1)

## Abstract

Long documents such as clinical records, legal contracts, and scientific papers are increasingly analyzed with large language models (LLMs). Naturally, feeding the full document to the model for every question can eventually become slow, expensive, prone to hallucination, and it reuses no work across questions. We explore an indexing-based solution for document analysis and propose a hierarchical plain-text index that is built once per document and consulted by subsequent queries. Inspired by the classic B+ tree, the index organizes a document into pages arranged from general summaries at the root to specific ones at the leaves, but it departs from the B+ tree in three ways suited to LLM access: content lives at every level, the index is plain text rather than attribute values, and navigation follows relevance between page summaries rather than comparing a search key. Its structure is discovered per document by the LLM rather than being hand-designed. In a preliminary evaluation on the NarrativeQA dataset, the index reaches accuracy comparable to DocETL, the strongest baseline, while being 40\% cheaper to answer questions.
