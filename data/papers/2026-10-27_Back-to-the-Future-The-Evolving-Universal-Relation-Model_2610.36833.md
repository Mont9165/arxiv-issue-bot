# Back to the Future: The Evolving Universal Relation Model

- arXiv ID: `2610.36833v1`
- Authors: Nan Tang, Haixun Wang
- Published: 2026-10-27
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.36833v1) | [pdf](https://arxiv.org/pdf/2610.36833v1)

## Abstract

Document backed analytics need databases that can be built as queries arrive. Enterprises increasingly ask analytical queries over messy document collections such as contracts, invoices, reports, emails, policies, and tickets, where the relevant structure and facts are often not known in advance. RAG can retrieve and summarize supporting evidence, but it does not by itself produce reusable, joinable, governed database state. Schema first construction offers the opposite strength: once a database is built, it supports joins, aggregation, constraints, indexes, optimization, and transactions. Yet for document analytics, fixing the schema and extracting all possible fields upfront is both expensive and brittle, because later queries and new documents often surface concepts that were not modeled before. We propose the Evolving Universal Relation Model (EUR), a query first model for document backed analytics. Users ask natural language queries as if the document corpus exposed one conceptual relation over application concepts. Internally, the DBMS turns each query into controlled database evolution: it updates the logical schema when new concepts are needed, extracts and integrates the facts required to answer the query, and decides what durable database state should remain for future queries. Thus, in EUR, a query is not only evaluated; it also helps construct the database. Document backed analytics becomes query first universal access plus workload-driven database schema and instance evolution.
