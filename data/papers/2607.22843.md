# Queryable Self-Organizing Maps: A Database Abstraction for Topology-Driven Data Exploration

- arXiv ID: `2607.22843v1`
- Authors: Denis Mayr Lima Martins, Gottfried Vossen
- Published: 2026-07-24
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.22843v1) | [pdf](https://arxiv.org/pdf/2607.22843v1)

## Abstract

Self-Organizing Maps (SOMs) have long been used as exploratory tools for high-dimensional data: they organize objects into a two-dimensional topology that reveals clusters, gradients, sparse regions, dense regions, and boundaries. Yet, in modern data systems, SOMs are typically trained and visualized outside the DBMS, disconnected from the relational data they summarize. We introduce the abstraction of a queryable data map: a learned topological artifact consisting of representatives, neighborhood relations, object assignments, and derived summaries. We instantiate this idea with MapDB, a lightweight prototype that makes SOM artifacts queryable so users can explore data topology without leaving the database. Experimental study shows that SOM training is feasible at moderate analytical scale, that map queries are interactive after materialization, and that SOM regions provide meaningful targets for exploratory SQL.
