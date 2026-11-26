# Data Agents Need a Map: Evolving, Demand-Driven Knowledge of Large Collections

- arXiv ID: `2611.33763v1`
- Authors: Christos Koutras, Yurong Liu, Laura Haas, Juliana Freire
- Published: 2026-11-25
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.33763v1) | [pdf](https://arxiv.org/pdf/2611.33763v1)

## Abstract

Most data that could power rich analysis sits unintegrated and uncataloged in open data portals, data lakes, and collections of independently published tables. Data agents now answer analytical questions over such collections with a full workflow per question, including dataset retrieval, join discovery and evaluation, and tailored program synthesis, most of which are discarded when a new task arrives. The knowledge these workflows depend on, such as what each column means, which context a dataset leaves implicit, and how datasets combine, is therefore perpetually rederived and never persisted.
  We argue for persisting this knowledge in an evolving semantic atlas that users and agents can navigate and extend. The atlas describes every dataset offline, through topics, semantic types, and profiles, so that agents can find the datasets that a task requires. Relationships between datasets and integrated views, which require comparing datasets, are instead built on demand for the areas of analysis that users declare. Every item is stored with its provenance and the confidence of the methods that produced it, so that agents can decide how far to trust it or whether to abstain. As datasets change, inconsistencies are detected and corrected automatically, while human users settle what the data leaves inconclusive. We present this vision and its challenges, namely building the atlas over large, multi-domain collections, keeping it correct and up to date, serving it to users and agents, and evaluating whether it improves their answers. A proof of concept on DAB, a benchmark for data agents, shows that with only part of the atlas a coding agent can already read a fifth to a third fewer tokens while achieving the same accuracy as without it.
