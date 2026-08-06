# From Research Questions to Columns: Operationalization-Aware Data Discovery

- arXiv ID: `2608.04536v1`
- Authors: Houming Chen, H. V. Jagadish
- Published: 2026-08-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.04536v1) | [pdf](https://arxiv.org/pdf/2608.04536v1)

## Abstract

Researchers often approach a data repository with an abstract concept and ask which columns can measure it. Useful columns may not resemble the query; they may matter only as complementary indicators in a defensible measure. This need differs from schema linking and column retrieval, which begin from more explicit needs and reward direct relevance. We define operationalization-aware data discovery (OADD): given a broad question and a database, optionally under a scope constraint, OADD jointly determines how focal concepts can be measured with available data and identifies supporting columns.
  Developing OADD methods requires examples for design and evaluation, but asking researchers to supply conceptual questions and their columns is impractical. We construct OADD-Bench by treating empirical papers as records of schema in use. A question miner extracts and reframes a paper-supported question; a paper-conditioned column miner reconstructs its measurements and grounds them to database identifiers. We admit only mappings supported by the publication and database documentation. OADD-Bench contains 160 questions from 111 papers and 4,682 question-column labels. Each target records a measurement used in published research; the paper supplies the precedent, while the miners extract and ground it.
  We evaluate lexical and neural retrieval, adapted schema-linking systems, and large language model (LLM) OADD agents. Each method receives only a question, permitted years, and dataset metadata; source papers are used only to construct and document benchmark labels. At the largest output limit, direct retrieval reaches at most 0.185 recall. The strongest schema-linking adaptation reaches 0.401 but remains optimized for a different objective; an OADD-directed agent performs best at 0.465. Even this agent covers less than half the target columns, showing that OADD remains an open problem.
