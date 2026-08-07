# Maintaining Queries under Updates Using Heavy-Light Partitioning of the Input Relations

- arXiv ID: `2605.08397v1`
- Authors: Mahmoud Abo-Khamis, Eden Chmielewski, Andrei Draghici, Ahmet Kara, Dan Olteanu
- Published: 2026-05-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.08397v1) | [pdf](https://arxiv.org/pdf/2605.08397v1)

## Abstract

We study the classical incremental view maintenance problem: Given a query and a database, maintain the query output under single-tuple updates (inserts or deletes) to the database such that the tuples in the query output can be enumerated with constant delay after any update.
  We introduce a maintenance approach whose update time matches or improves the best update time reported in prior work. Whereas prior approaches are manually tailored to each of a handful of queries, our approach generalizes to arbitrary join queries. It combines three techniques: delta queries, trees of materialized views, and heavy-light data partitioning. The overall update time incurred by our approach for a given join query is characterized by the maintenance width, a new measure that is parameterized by the heavy-light threshold for data partitioning. We show how to find the threshold that minimizes the maintenance width.
