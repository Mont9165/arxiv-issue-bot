# RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation

- arXiv ID: `2608.20845v1`
- Authors: Kyle Wild, Yusuke Takahashi, Asako Uraki
- Published: 2026-08-21
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.20845v1) | [pdf](https://arxiv.org/pdf/2608.20845v1)

## Abstract

Nearly every retrieval-augmented question-answering system in production ships with a hidden interpreter: on each query a language model re-derives the meaning of raw corpus text and then throws that work away. Cheaper models do not close the gap: per-token prices have fallen by orders of magnitude while inference spend has risen, because context volume grows faster than prices fall. This is the modern equivalent of the full-table scan, and the remedy is the one databases found fifty years ago: do the expensive work once, at write time, into a maintained structure that makes reads cheap. A corpus whose read pattern is known before it ever meets a user can and should be indexed too.
  We call the paradigm ingest-time semantic compilation (ISC): compile a corpus's meaning into a queryable substrate with two coupled layers - incrementally maintained embeddings, and atomic claims whose provenance is validated at compile time - and treat that substrate as a first-class database object with its own DDL, maintenance contract, migration contract, and cost model.
  Two existence proofs support it. Substrate upkeep scales with change rather than corpus size: incremental updates run 33.7x cheaper than reconstruction while tracking it to floating-point precision. And on a held-out sample of 500 broadcast-interview transcripts, compiled claims as the retrieval payload win all 32 budget-by-model cells: 85.2% correct from roughly 2.2k reader tokens against 72.5% from 16.3k for the best chunk configuration anywhere. The only baseline that keeps pace is a contextualized-chunk pipeline with hybrid retrieval and reranking, statistically indistinguishable from compiled claims at roughly twenty-one times the query-path tokens - and it reaches that parity, we argue, precisely because it has itself begun to compile. We close with the systems agenda this opens, from compilation planners to read planning.
