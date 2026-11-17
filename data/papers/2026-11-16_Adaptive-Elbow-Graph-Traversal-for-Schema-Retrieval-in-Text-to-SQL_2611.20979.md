# Adaptive-Elbow Graph Traversal for Schema Retrieval in Text-to-SQL

- arXiv ID: `2611.20979v1`
- Authors: Fabio Picariello, Salvatore Cipolla, Susanna Bonura, Vito Morreale
- Published: 2026-11-16
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.20979v1) | [pdf](https://arxiv.org/pdf/2611.20979v1)

## Abstract

LLM-based natural-language interfaces to relational databases are gated by a schema-retrieval step: the generator can only be as good as the slice of schema it is shown. On a database with hundreds of tables, that slice must be selected and the selection is two-sided---omit a needed table and the query becomes unrecoverable, include too many and the irrelevant ones act as noise that degrades the model's output. When an agentic retriever that lets the model inspect the schema can be too costly or too slow, the fallback is an embedder that ranks tables by cosine similarity and keeps a top-k. This fallback has two weaknesses: a fixed budget is suboptimal question by question, and embedding similarity overlooks foreign-key-linked tables that are necessary for joins. We present Adaptive-Elbow Graph Traversal (AEGT, ElbowHop for short), a property-graph table retriever that addresses both: an adaptive elbow cutoff replaces the fixed budget with a per-question one under a single aggressiveness parameter, and bidirectional foreign-key traversal deterministically recovers the bridge tables embedding similarity misses. We evaluate the retriever on 3 corpora of increasing candidate-pool size (BIRD Mini-Dev queried per database, 3--13 tables; its eleven schemas merged, 74; and a merged Spider-train graph, 546) and isolate the two mechanisms under a per-question budget-matched protocol. Across these settings the adaptive elbow emerges as the dominant mechanism---at matched recall it roughly doubles precision over a fixed budget on the larger pools, the margin widening as the pool grows---while the foreign-key traversal pays off on the join-critical bridge tables dense retrieval cannot reach, in the single-hop tight-budget case. We characterize the method as a low-cost, recall-robust first stage for schema retrieval on which a downstream selection or generation step can build.
