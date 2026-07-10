# DocMaster: A Hierarchical Structure-Aware System for Document Analysis

- arXiv ID: `2607.08539v1`
- Authors: Ziqi Chen, Yingli Zhou, Fangyuan Zhang, Quanqing Xu, Chuanhui Yang, Yixiang Fang
- Published: 2026-07-09
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.08539v1) | [pdf](https://arxiv.org/pdf/2607.08539v1)

## Abstract

Leveraging large language models (LLMs) to analyze complex documents -- such as academic papers, technical manuals, and financial reports -- has emerged as a mainstream and critical task in both research and industry. In practice, users must first filter relevant documents from large collections and then conduct in-depth analysis (e.g. question answering) over the selected subset, yet existing systems flatten documents into plain-text chunks, discarding the rich hierarchical structures (sections, tables, figures, equations) and degrading downstream performance. We present DocMaster, a hierarchical structure-aware document analysis system. DocMaster parses documents into hierarchical document trees preserving original layouts and constructs a structure-aware semantic index that enables accurate document filtering and in-depth analysis. We demonstrate DocMaster through an interactive web interface that enables users to upload document collections, construct tree-based and multi-view semantic indices, filter relevant documents via natural-language conditions, and perform follow-up question answering over the filtered results. The source code, data, and demo are available at https://doc-master.github.io/.
