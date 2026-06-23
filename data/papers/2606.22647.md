# RAVEN: Agentic RAG for Automated Vulnerability Repair

- arXiv ID: `2606.22647v1`
- Authors: Varun Gadey, Zijie Liu, Alexandra Dmitrienko
- Published: 2026-06-21
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22647v1) | [pdf](https://arxiv.org/pdf/2606.22647v1)

## Abstract

Automated vulnerability repair has emerged as a promising direction to mitigate the growing number of software vulnerabilities. Recent advances in Large Language Models (LLMs) have further accelerated research in automated repair. However, existing frameworks remain largely restricted to memory-related vulnerabilities and locally repairable vulnerability settings, leaving generalization to unseen vulnerability types underexplored. Their evaluations are often limited to a single programming language, and largely rely on proprietary models. In this paper, we propose RAVEN, a scalable, efficient and autonomous framework that integrates an agentic retrieval-augmented generation (RAG) pipeline with controlled iterative repair in a unified framework. The framework utilizes open-source LLMs in a fully locally deployable setting with limited GPU requirements, while building a multi-faceted retrieval pipeline to retrieve historically relevant vulnerability fixes and guide the patch generation. In addition, RAVEN introduces a dedicated Curator Agent that retrieves cross-file dependencies from the target repository, to fix complex vulnerabilities that cannot be addressed using local vulnerable code alone. We evaluate RAVEN on 160 real-world CVE vulnerabilities across diverse vulnerability types, two programming languages, unseen CWE categories, and out-of-distribution settings. RAVEN achieves an overall repair success rate of 83.13%, outperforming all existing state-of-the-art repair frameworks, while also demonstrating strong generalization capabilities and maintaining the repair cost negligible.
