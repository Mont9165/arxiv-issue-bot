# AptMQL-Bench: From Text-to-SQL to Text-to-MQL via Access-Pattern Schema Design and Data-Preserving Migration

- arXiv ID: `2610.02770v1`
- Authors: Hy Nguyen, Nabi Rezvani, Robin Vujanic
- Published: 2026-10-02
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.02770v1) | [pdf](https://arxiv.org/pdf/2610.02770v1)

## Abstract

Document databases such as MongoDB are core infrastructure for modern applications, and natural-language interfaces to them---text-to-MQL---would let non-experts query complex, semi-structured data without mastering the query language. Progress on this task depends on high-quality benchmarks, which are most practically obtained by converting an existing text-to-SQL benchmark to the document setting. Unfortunately, existing efforts rely on heuristics for mechanical conversion: the document schema mirrors the relational foreign-key graph, and each query mirrors its source SQL. As a result in our experiments, these approaches fail to migrate 6 of 21 BIRD databases outright, silently drop up to 25.9\% of rows on others, and yield schemas whose ground-truth queries run over an order of magnitude slower as the data scales. We instead propose a conversion pipeline, driven by coding agents with human-in-the-loop verification, that designs each document schema from expected access patterns and rewrites queries to be MongoDB-native. Applying it to BIRD, we build an access-pattern-based text-to-MQL benchmark (AptMQL-Bench). It includes 21 document-oriented databases, 3,186 natural-language requests, and their associated MQL queries---whose databases are migrated from SQLite without data loss and scale efficiently. The strongest model, Claude Opus 4.5, achieves only 57.38\% accuracy without external knowledge evidence and 70.34\% with it. This indicates that realistic text-to-MQL generation remains challenging.
