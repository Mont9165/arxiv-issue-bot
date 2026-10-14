# How Hard is it to Decide if a Fact is Relevant to a Query?

- arXiv ID: `2604.22422v1`
- Authors: Meghyn Bienvenu, Diego Figueira, Pierre Lafourcade
- Published: 2026-04-24
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.22422v1) | [pdf](https://arxiv.org/pdf/2604.22422v1)

## Abstract

We consider the following fundamental problem: given a database D, Boolean conjunctive query (CQ) q, and fact f in D, decide whether f is relevant to q wrt. D, i.e., does f belong to a minimal subset S of D such that S |= q. Despite being of central importance to query answer explanation, the combined complexity of deciding query relevance has not been studied in detail, leaving open what makes this problem hard, and which restrictions can yield lower complexity. Relevance has already been shown to be harder than query evaluation: namely, $Σ^p_2$-complete for CQs, even over a binary signature. We further observe that NP-hardness applies already to (acyclic) chain CQs. Our work identifies self-joins (multiple atoms with the same relation) as the culprit. Indeed, we prove that if we forbid or bound the occurrence of self-joins, then relevance has the same complexity as query evaluation, namely, NP (without structural restrictions) and LogCFL (for bounded hypertreewidth classes). In the ontology setting, we establish an analogous result for ontology-mediated queries consisting of a CQ and DL-Lite_R ontology, namely that relevance is no harder than query answering provided that we bound the interaction width (which generalizes both self-join width and a recently introduced 'interaction-free' condition). Our results thus pinpoint what makes relevance harder than query evaluation and identify natural classes of queries which admit efficient relevance computation.
